# 使用 NVIDIA 官方的 CUDA 映像
#FROM nvidia/cuda:11.6.2-devel-ubuntu20.04
FROM nvidia/cuda:11.6.1-runtime-ubuntu20.04

# 安裝 Python 3.10 + 基本工具
RUN apt-get update && apt-get install -y python3.10 python3-pip git && rm -rf /var/lib/apt/lists/*

# 設定 python 與 pip alias
#RUN ln -s /usr/bin/python3.10 /usr/bin/python && ln -s /usr/bin/pip3 /usr/bin/pip
RUN python3.10 -m pip install --upgrade pip

# 設定工作目錄
WORKDIR /app

# 複製需求檔案
COPY requirements.txt .

# 安裝 python 套件 (CUDA 版 PyTorch)
#RUN pip install --upgrade pip && pip install --no-cache-dir torch==2.0.0+cu118 torchvision --index-url https://download.pytorch.org/whl/cu118
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


# 複製你的應用程式
COPY app/ ./app/

# 啟動服務
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "8"]
