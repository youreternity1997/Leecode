from fastapi import FastAPI, Request, Body
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from transformers import TextIteratorStreamer
import torch
import asyncio
import re
import threading
from datetime import datetime   # <─ 新增
import psutil
import platform
import shutil
from typing import List, Dict, Any         # <─ 新增
from enum import Enum

description = """
ChatbotAPP API helps you do awesome stuff. 🚀

## Items
You can **read items**.

## Users
You will be able to:
* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "load",
        "description": "Load with LLM model. The **load** logic is also here.",
        "externalDocs": {
            "description": "Model list website",
            "url": "https://huggingface.co/models",
        },
    },
    {
        "name": "chat",
        "description": "Chat with LLM model. Begin your LLM model",
    },
]


app = FastAPI(title="GIGABYTE Chat bot",
              description=description,
              summary="chat bot app",
              version="3.2.3",
              terms_of_service="https://fastapi.tiangolo.com/zh-hant/tutorial/metadata/#metadata-for-api",
              contact={
                  "name": "GIGABYTE Utility",
                  "url": "https://www.gigabyte.com/tw/Support/Utility",
                  "email": "youreternity1997@gmail.com",
                  },
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                  },
              openapi_tags=tags_metadata,
            ) 
            # docs_url="/documentation",
            # redoc_url=None,

from routers.llm_produce_dataset_router import llm_produce_dataset_router
app.include_router(llm_produce_dataset_router, prefix="/dataset", tags=["dataset"])

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

api_logs = []
# 開啟 FastAPI Log 中介層 (可以在 console 上看到 Electron 或瀏覽器是否真的有 request 被送進來。)
@app.middleware("http")
async def capture_logs(request: Request, call_next):
    client_host, client_port = request.client if request.client else ("<unknown>", -1)
    body = await request.body()
    log_item = {
        "timestamp"     : datetime.utcnow().isoformat(),
        "path"          : request.url.path,
        "client"        : f"{client_host}:{client_port}",
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "body": body.decode('utf-8'),
        "query_params"  : dict(request.query_params),
    }
    api_logs.append(log_item)
    return await call_next(request)

@app.get("/logs")
def get_logs():
    return api_logs[-10:]  # 回傳最新的 10 筆互動

#@app.post("/load_model", tags=["load"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)