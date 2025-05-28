import os
import re
import io
import time
import json
import socket
import zipfile
import shutil
import hashlib
import threading
import datetime
import subprocess
import webbrowser
from pathlib import Path
from urllib.parse import urlparse


import socket
import platform
import nbformat
import requests
import unidecode
from typing import Optional
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Local Config
from lib.source.config.MachineLearning_config import PROJECT_ROOT, PROBLEM_CATEGORY_INFO_MAP, PROBLEM_CATEGORY_MAP, LABEL_MAP


ML_router = APIRouter()
PROJECT_PROGRESS = {}

# ====================
# Utilities: Conda Operations
# ====================

def find_conda_sh():
    """Locate conda.sh from common installation paths."""
    candidate_paths = [
        Path("/opt/miniconda3/etc/profile.d/conda.sh"),
        Path.home() / "miniconda3/etc/profile.d/conda.sh",
        Path.home() / "anaconda3/etc/profile.d/conda.sh",
        Path("/usr/local/miniconda3/etc/profile.d/conda.sh"),
        Path("/usr/local/anaconda3/etc/profile.d/conda.sh"),
    ]
    for path in candidate_paths:
        if path.exists():
            return str(path)
    raise RuntimeError("Cannot find conda.sh in any known location.")

def run_in_conda(command: str, cwd: Path = None, activate_env: str = "lmmllava"):
    """Run a shell command after sourcing conda.sh and activating an environment."""
    conda_sh_path = find_conda_sh()
    full_command = f"source {conda_sh_path} && conda activate {activate_env} && {command}" #其主要目的是「啟動（initialize）Conda 的 shell 整合機制」，讓你之後可以直接使用 conda activate、conda deactivate、conda env list 等指令
    return subprocess.run(["bash", "-c", full_command], capture_output=True, text=True, cwd=cwd)


def popen_in_conda(command: str, cwd: Path = None, activate_env: str = "lmmllava"):
    """Launch a non-blocking subprocess after sourcing conda.sh and activating an environment."""
    conda_sh_path = find_conda_sh()
    full_command = f"source {conda_sh_path} && conda activate {activate_env} && {command}"
    return subprocess.Popen(["bash", "-c", full_command], cwd=cwd)


# ====================
# Utilities: Standard Helpers
# ====================

def standard_response(success=True, message="", data=None, status_code=200):
    """Standard JSON response wrapper."""
    return JSONResponse(status_code=status_code, content={"success": success, "message": message, "data": data})

class ProjectInfo(BaseModel):
    project_name: str
    problem_category: int
    package_name: str
    algorithm_name: str

class ProjectNameRequest(BaseModel):
    project_name: str

class ProblemCategoryRequestest(BaseModel):
    problem_category: int

def set_progress_by_project(project_name, step, msg):
    """Track project creation progress."""
    PROJECT_PROGRESS[project_name] = {
        "step": step,
        "message": msg,
        "timestamp": datetime.datetime.now().isoformat()
    }

def slugify(value: str) -> str:
    """Convert string into slug format."""
    value = unidecode.unidecode(value)
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)

def gen_env_name(project_name: str):
    """Generate environment name based on project name and timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base = f"{project_name}_{timestamp}"
    hash_part = hashlib.sha1(base.encode()).hexdigest()[:6]
    slug = slugify(project_name)[:12]
    return f"{slug}_{timestamp}_{hash_part}"

def get_metadata_path(env_hash: str):
    """Get the metadata.json path for a given environment."""
    return PROJECT_ROOT / env_hash / "metadata.json"

def get_env_hash_by_folder(folder_name: str) -> str:
    """Retrieve env_hash from a project's metadata.json."""
    project_path = PROJECT_ROOT / folder_name
    metadata_path = project_path / "metadata.json"
    if not metadata_path.exists():
        raise FileNotFoundError(f"metadata.json not found in folder: {project_path}")
    with open(metadata_path, "r") as f:
        data = json.load(f)
    env_hash = data.get("env_hash")
    if not env_hash:
        raise ValueError(f"'env_hash' not found in metadata.json of {folder_name}")
    return env_hash, project_path

def get_kernel_path(env_hash: str) -> str:
    """Get the jupyter kernel path associated with a given environment."""
    try:
        result = run_in_conda("jupyter kernelspec list --json")
        if result.returncode != 0:
            raise RuntimeError(f"Failed to list kernelspecs: {result.stderr}")
        data = json.loads(result.stdout)
        return data.get("kernelspecs", {}).get(env_hash, {}).get("resource_dir", "")
    except Exception as e:
        print(f"Failed to get kernel path: {e}")
        return ""

def check_disk_space_for_url(local_path: Path, url: str):
    """Check if local disk space is sufficient for downloading a given URL."""
    total, used, free_space = shutil.disk_usage(local_path)
    resp = requests.head(url, allow_redirects=True)
    size = resp.headers.get("Content-Length")
    if not size:
        raise HTTPException(status_code=400, detail="Unable to retrieve remote file size")
    zip_size = int(size)
    if free_space < zip_size * 1.1:
        raise HTTPException(status_code=507, detail=f"Insufficient disk space. Available: {free_space // (1024**2)} MB, Required: {zip_size // (1024**2)} MB")

def fetch_file(source: str, destination: Path, unzip: bool = False, extract_to: Optional[Path] = None):
    """Fetch a file from a local or remote source."""
    parsed = urlparse(source)
    is_remote = parsed.scheme in ["http", "https"]
    if unzip and extract_to is None:
        raise ValueError("extract_to must be specified if unzip is True")
    if is_remote:
        response = requests.get(source)
        response.raise_for_status()
        if unzip:
            # response.content 是你用 requests.get()（或類似方式）從網路上抓回來的「原始二進制資料」（bytes），也就是整個 .zip 的檔案內容。
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref: #io.BytesIO(...) 把這段二進制資料包裝成一個「類檔案物件」（file-like object），讓後面可以像操作真實檔案一樣讀取它。
                zip_ref.extractall(extract_to)
        else:
            with open(destination, "wb") as f:
                f.write(response.content)
    else:
        src = Path(source).expanduser().resolve() #把路徑「解析」成絕對路徑，並且
        if not src.exists():
            raise FileNotFoundError(f"File not found at {src}")
        if unzip:
            temp_zip = extract_to / "temp.zip"
            shutil.copy(src, temp_zip)
            with zipfile.ZipFile(temp_zip) as zip_ref:
                zip_ref.extractall(extract_to)
            temp_zip.unlink()
        else:
            shutil.copy(src, destination)
    if not unzip:
        os.chmod(destination, 0o755)

# ====================
# Utilities: Additional Helpers
# ====================

def get_project_info_by_name(project_name: str):
    """Retrieve project info by project name."""
    for project_dir in PROJECT_ROOT.iterdir():
        if project_dir.is_dir():
            metadata_path = project_dir / "metadata.json"
            if metadata_path.exists():
                try:
                    with open(metadata_path, "r") as f:
                        metadata = json.load(f)
                    if metadata.get("project_name") == project_name:
                        return {
                            "metadata": metadata,
                            "path": project_dir,
                            "env_hash": metadata.get("env_hash")
                        }
                except Exception as e:
                    print(f"Failed to read {metadata_path}: {e}")
    return None

def delete_project_folder(path: Path):
    """Delete the entire project folder."""
    shutil.rmtree(path)

def delete_conda_env(env_name: str):
    """Delete a conda environment by name."""
    try:
        run_in_conda(f"conda env remove --name {env_name} -y")
    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to delete conda env {env_name}: {e}")

def delete_kernel_spec_from_metadata(metadata_path: Path):
    """Delete the Jupyter kernel spec associated with a project."""
    if not metadata_path.exists():
        print("metadata.json not found")
        return
    with open(metadata_path, "r") as f:
        meta = json.load(f)
        kernel_path = Path(meta.get("kernel_path", ""))
        if kernel_path.exists():
            shutil.rmtree(kernel_path)
            print(f"Kernel deleted: {kernel_path}")
        else:
            print(f"Kernel path not found: {kernel_path}")

def fix_all_notebook_kernelspecs(project_dir, env_hash):
    """Fix all notebook files' kernelspec to bind to the created environment."""
    for root, _, files in os.walk(project_dir):
        for fname in files:
            if fname.endswith(".ipynb"):
                nb_path = os.path.join(root, fname)
                nb = nbformat.read(open(nb_path, "r", encoding="utf-8"), as_version=4)
                nb["metadata"]["kernelspec"] = {
                    "display_name": f"Python ({env_hash})",
                    "language": "python",
                    "name": env_hash
                }
                nbformat.write(nb, open(nb_path, "w", encoding="utf-8"))
                print(f"Fixed kernelspec for: {nb_path}")

def get_free_port(start: int = 8888, end: int = 8999) -> int:
    """Scan for an available TCP port within the given range."""
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                continue
    raise RuntimeError("No available port found")

def wait_for_port(port, host="127.0.0.1", timeout=30.0):
    """Wait until a TCP port is open."""
    start_time = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=1):
                return
        except (OSError, ConnectionRefusedError):
            if time.time() - start_time > timeout:
                raise TimeoutError(f"⏳ Timed out waiting for {host}:{port}")
            time.sleep(0.5)

import subprocess

def force_open_browser(url):
    try:
       
        subprocess.Popen(["chromium-browser", "--no-sandbox", url])
    except FileNotFoundError:
        try:
            subprocess.Popen(["google-chrome", "--no-sandbox", url])
        except FileNotFoundError:
            import webbrowser
            
            webbrowser.open_new_tab(url)



def start_jupyter(path: Path, port: int, activate_env: str = "base", kernel_dirs: list = None):
    """
    Start a JupyterLab server in the specified working directory using the given port.
    Automatically detect if 'jupyter' is available; if not, source conda.sh and activate environment first.
    Automatically open a browser tab after the server is ready.
    
    Parameters:
        path (Path): The directory where JupyterLab should be launched.
        port (int): The port number on which JupyterLab will run.
        activate_env (str): Conda environment name to activate if jupyter is not globally available.
        kernel_dirs (list): List of paths to search for kernelspecs. (Optional)
    """
    time.sleep(1)

    # Build the jupyter command
    jupyter_command = (
        f"jupyter lab --port={port} "
        f"--port-retries=0 "
        f"--NotebookApp.allow_root=True "
        f"--NotebookApp.token='' "
        f"--NotebookApp.password='' "
        f"--ip=127.0.0.1 "
        f"--no-browser "
    )

    if kernel_dirs:
        kernel_dirs_argument = ",".join([f"'{d}'" for d in kernel_dirs])
        jupyter_command += (
            f"--NotebookApp.kernel_spec_manager_class='jupyter_client.kernelspec.KernelSpecManager' "
            f"--KernelSpecManager.kernel_dirs=[{kernel_dirs_argument}] "
        )

    check = subprocess.run(["which", "jupyter"], capture_output=True, text=True)

    if check.returncode == 0:
        subprocess.Popen(jupyter_command.split(), cwd=path, env=os.environ)
        print("Directly launched Jupyter without activating env.")
    else:
        conda_sh_path = find_conda_sh()
        full_command = f"source {conda_sh_path} && conda activate {activate_env} && {jupyter_command}"
        subprocess.Popen(["bash", "--login", "-c", full_command], cwd=path)
        print(f"Jupyter not found globally, sourced conda.sh and activated {activate_env} before launch.")

    # Wait for server to be ready
    print(f"Waiting for JupyterLab server to be ready at port {port}...")
    try:
        wait_for_port(port)
    except TimeoutError as e:
        print(str(e))
        print("JupyterLab may have failed to start properly. Please check manually.")
        return

    url = f"http://127.0.0.1:{port}/lab"
    print(f"Please open the following URL manually if browser does not open automatically:")
    print(url)

    try:
        force_open_browser(url)
    except Exception as e:
        print(f"Failed to open browser automatically: {e}")


def get_example_path(problem_category, package_name, algorithm_name):
    """Fetch example path based on problem category, package and algorithm."""
    category_info = PROBLEM_CATEGORY_MAP.get(problem_category)
    if not category_info:
        return 0
    package_info = category_info.get(package_name)
    if not package_info:
        return None
    algorithm_info = package_info.get("algorithms", {}).get(algorithm_name)
    if not algorithm_info:
        return None
    return algorithm_info.get("example_path")

# ====================
# API Routes
# ====================



@ML_router.post("/create_projects")
def create_project(info: ProjectInfo):
    """API to create a new ML project."""
    project_dir = None  
    try:
        existing = get_project_info_by_name(info.project_name)
        if existing:
            return standard_response(success=False, message="Project name already exists", status_code=400)

        env_hash = gen_env_name(info.project_name)
        project_dir = PROJECT_ROOT / env_hash
        if project_dir.exists():
            return standard_response(success=False, message="Project already exists", status_code=400)

        # Create project directory
        project_dir.mkdir(parents=True)
        set_progress_by_project(info.project_name, 1, "Creating project directory...")

        # Lookup ZIP path based on problem_category, package_name, and algorithm_name
        zip_url = get_example_path(info.problem_category, info.package_name, info.algorithm_name)
        if not zip_url:
            raise Exception("No matching example found for the given problem_category, package_name, and algorithm_name.")

        # Check disk space and download the ZIP file
        set_progress_by_project(info.project_name, 2, "Downloading ZIP...")
        check_disk_space_for_url(project_dir, zip_url)
        fetch_file(zip_url, destination=None, unzip=True, extract_to=project_dir)

        set_progress_by_project(info.project_name, 3, "Extracting ZIP...")

        # Locate install.sh script
        install_script_path = next(project_dir.glob("*/install.sh"), None)
        if not install_script_path or not install_script_path.exists():
            raise Exception("install.sh not found in extracted ZIP")

        # Make install.sh executable and run it to set up the environment
        os.chmod(install_script_path, 0o755)
        set_progress_by_project(info.project_name, 4, "Running install.sh to create environment...")
        run_in_conda(f"bash {install_script_path} {env_hash}", cwd=project_dir)

        # Get kernel path after environment creation
        kernel_path = get_kernel_path(env_hash)

        # Start Jupyter Lab in a new thread
        set_progress_by_project(info.project_name, 5, "Starting Jupyter Lab...")
        port = get_free_port()
        threading.Thread(target=start_jupyter, args=(project_dir, port)).start()

        # Determine annotation automatically
        if info.problem_category == 3:
            annotation = 2
        elif info.problem_category == 1:
            annotation = 0
        else:
            annotation = 1

        # Prepare metadata information
        data = {
            "env_hash": env_hash,
            "project_name": info.project_name,
            "problem_category": info.problem_category,
            "package_name": info.package_name,
            "algorithm_name": info.algorithm_name,
            "annotation": annotation,
            "create_time": datetime.datetime.now().isoformat(),
            "kernel_path": kernel_path
        }

        # Save metadata
        with open(get_metadata_path(env_hash), "w") as f:
            json.dump(data, f, indent=2)

        # Fix all notebook kernelspecs
        fix_all_notebook_kernelspecs(project_dir, env_hash)
        set_progress_by_project(info.project_name, 6, f"Project created successfully, Notebook initialized and bound to kernel '{env_hash}'")

        return standard_response(success=True, message=f"Project '{info.project_name}' created.", data={"env_hash": env_hash})

    except Exception as e:
        # Clean up project directory if error happens
        if project_dir and project_dir.exists():
            try:
                shutil.rmtree(project_dir)
            except Exception as cleanup_error:
                print(f"Warning: Failed to clean up project directory after error: {cleanup_error}")

        return standard_response(success=False, message=f"Error creating project: {str(e)}", status_code=500)



@ML_router.post("/project_status")
def get_progress_by_name(info: ProjectNameRequest):
    """API to get project creation progress by project name."""
    try:
        progress = PROJECT_PROGRESS.get(info.project_name, {"step": 0, "message": "Not started yet"})
        return standard_response(success=True, message="Project status retrieved", data=progress)
    except Exception as e:
        return standard_response(success=False, message=f"Error retrieving project status: {str(e)}", status_code=500)

@ML_router.get("/get_all_projects")
def get_all_projects():
    """API to retrieve all created projects."""
    try:
        projects = []
        if not PROJECT_ROOT.exists():
            return standard_response(success=True, message="No project directory", data=[])

        for project_dir in PROJECT_ROOT.iterdir():
            if project_dir.is_dir():
                metadata_path = project_dir / "metadata.json"
                if metadata_path.exists():
                    try:
                        with open(metadata_path, "r") as f:
                            meta = json.load(f)
                        latest_mtime = max((f.stat().st_mtime for f in project_dir.rglob("*") if f.is_file()), default=None)
                        modify_time = datetime.datetime.utcfromtimestamp(latest_mtime).isoformat() + "Z" if latest_mtime else None
                        projects.append({
                            "no": len(projects) + 1,
                            "project_name": meta.get("project_name", ""),
                            "env_hash": meta.get("env_hash", ""),
                            "problem_category": meta.get("problem_category", -1),
                            "annotation": meta.get("annotation", False),
                            "modify_time": modify_time
                        })
                    except Exception as e:
                        print(f"Error reading {metadata_path}: {e}")
                        continue

        return standard_response(success=True, message="All projects retrieved", data=projects)
    except Exception as e:
        return standard_response(success=False, message=f"Error retrieving projects: {str(e)}", status_code=500)

@ML_router.post("/open_project")
def open_project(info: ProjectNameRequest):
    """API to open an existing project."""
    try:
        project_info = get_project_info_by_name(info.project_name)
        if not project_info:
            return standard_response(success=False, message="Project not found", status_code=404)

        port = get_free_port()
        jupyter_work_dir = project_info['path']
        threading.Thread(target=start_jupyter, args=(jupyter_work_dir, port)).start()

        return standard_response(success=True, message=f"{info.project_name} opened successfully")
    except Exception as e:
        return standard_response(success=False, message=f"Error opening project: {str(e)}", status_code=500)

@ML_router.post("/delete_project")
def delete_project(info: ProjectNameRequest):
    """API to delete a project along with its environment and kernel."""
    try:
        project_info = get_project_info_by_name(info.project_name)
        if not project_info:
            return standard_response(success=False, message="Project not found", status_code=404)

        delete_conda_env(project_info["env_hash"])
        delete_kernel_spec_from_metadata(project_info["path"] / "metadata.json")
        delete_project_folder(project_info["path"])

        return standard_response(success=True, message=f"Project '{info.project_name}' deleted successfully.")
    except Exception as e:
        return standard_response(success=False, message=f"Error deleting project: {str(e)}", status_code=500)


@ML_router.post("/modify_project")
def modify_project(info: ProjectNameRequest, new_name: str):
    project_info = get_project_info_by_name(info.project_name)
    if not project_info:
        return standard_response(success=False, message="Project not found", status_code=404)

    metadata_path = project_info["path"] / "metadata.json"
    with open(metadata_path, "r+") as f:
        data = json.load(f)
        data["project_name"] = new_name
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    return standard_response(success=True, message=f"{info.project_name} renamed to {new_name}")


@ML_router.post("/check_or_install_label_env")
def check_or_install_label_env(info: ProblemCategoryRequestest):
    """Check or install the appropriate label environment based on the problem category."""
    try:
        problem_category = info.problem_category

        # Determine environment and script keys
        if problem_category in [2, 4]:
            env_name = "labelImg"
            run_script_key = "run_labelImg"
            install_script_key = "install_labelImg"
        elif problem_category == 3:
            env_name = "labelme"
            run_script_key = "run_labelme"
            install_script_key = "install_labelme"
        else:
            return standard_response(success=False, message="Invalid problem_category", status_code=400)

        
        # Paths
        run_script_path = PROJECT_ROOT / f"{run_script_key}.sh"
        install_script_path = PROJECT_ROOT / f"{install_script_key}.sh"

        # Fetch run script
        fetch_file(LABEL_MAP[run_script_key], run_script_path)

        # Check if environment exists
        result = run_in_conda("conda env list")
        if result.returncode != 0:
            raise RuntimeError(f"Failed to list conda environments: {result.stderr}")

        if env_name in result.stdout:
            # If env exists, run the label tool
            popen_in_conda(f"bash {run_script_path}")
            return standard_response(success=True, message=f"{env_name} environment found and started.")
        else:
            # If env does not exist, fetch and run install script
            fetch_file(LABEL_MAP[install_script_key], install_script_path)
            run_in_conda(f"bash {install_script_path}", cwd=PROJECT_ROOT)
            popen_in_conda(f"bash {run_script_path}")
            return standard_response(success=True, message=f"{env_name} installed and started.")

    except Exception as e:
        return standard_response(success=False, message=f"Error: {str(e)}", status_code=500)


#PROBLEMS

@ML_router.get("/get_all_problems")
def get_all_problems():
    data = []
    for category_id, info in PROBLEM_CATEGORY_INFO_MAP.items():
        data.append({
            "problem_name": info["problem_name"],
            "problem_category": category_id,
            "description": info["description"],
            "badge": info["badge"],
            "annotation": info["annotation"],
            "icon_url": info["icon_url"]
        })
    return standard_response(success=True, message="All problems retrieved", data=data)
 

if __name__ == '__main__':
    pass