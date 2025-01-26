import random
import os
from datetime import datetime

# Ensure GitPython is installed
try:
    import git
except ImportError:
    os.system('pip install gitpython')
    from git import Repo

from git import Repo


def random_edit(file_path):
    """Randomly edits a line in the specified file."""
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        if not lines:
            print("File is empty. Nothing to edit.")
            return

        # Pick a random line to edit
        line_to_edit = random.randint(0, len(lines) - 1)
        random_comment = f"# Edited on {datetime.now().strftime('%Y-%m-%d %H:%M:%S edit')}\n"

        # Replace the chosen line with a comment or add a random modification
        lines[line_to_edit] = random_comment

        # Write the modified lines back to the file
        with open(file_path, "w") as file:
            file.writelines(lines)

        print(f"Edited line {line_to_edit + 1} in {file_path}")
    except Exception as e:
        print(f"Error editing file: {e}")

def push_to_github(repo_path, commit_message, remote_name, branch_name):
    """Commits and pushes changes to the GitHub repository."""
    try:
        repo = Repo(repo_path)

        if repo.is_dirty():
            # Stage all changes
            repo.git.add(A=True)

            # Commit changes
            repo.index.commit(commit_message)
            print("Changes committed.")

            # Push changes to the remote repository
            origin = repo.remote(name=remote_name)
            origin.push(refspec=f"{branch_name}:{branch_name}")
            print("Changes pushed to GitHub.")
        else:
            print("No changes to commit.")
    except Exception as e:
        print(f"Error pushing to GitHub: {e}")



# Set up your configuration
REPO_PATH = "../"  # Replace with your local repository path
FILE_TO_EDIT = "../Fibonacci numbers.py"  # Replace with the file to randomly edit
COMMIT_MESSAGE = datetime.now().strftime('%Y-%m-%d-%H-%M edit')
GITHUB_REMOTE = "origin"  # Default remote name is 'origin'
BRANCH_NAME = "master"  # Replace with your branch name


def main():
    random_edit(FILE_TO_EDIT)
    push_to_github(REPO_PATH, COMMIT_MESSAGE, GITHUB_REMOTE, BRANCH_NAME)

if __name__ == "__main__":
    main()
