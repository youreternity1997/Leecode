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


chatbot = None  # global placeholder

request_logs: List[Dict[str, Any]] = []

class LoadRequest(BaseModel):
    modelDir: str = Field(..., example=r"C:\Users\User\Downloads\Llama-3.2-1B-Instruct")
    prompt: str = Field(default="", example="你是AI助理，請回答問題。")

class ChatRequest(BaseModel):
    input_text: str = Field(..., example="請解釋量子物理是什麼？")

class TransformerChat:
    def __init__(self, Chosen_Model, prompt="", top_p=0.9, temperature=0.8, maximum_tokens=512):
        self.optional_prompt = prompt
        self.text_qa_template_str = (
            "---------------------\n"
            "Please answer the following question.\n"
            "---------------------\n"
        )
        self.top_p = top_p
        self.temperature = temperature
        self.maximum_tokens = maximum_tokens
        self.prompt_len = len(prompt)
        self.tokenizer = AutoTokenizer.from_pretrained(
            Chosen_Model,
            model_max_length=maximum_tokens,
            add_eos_token=True,
            add_bos_token=True,
            padding_side='left',
            trust_remote_code=True
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(
            Chosen_Model,
            torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"
        )

    def format_prompt(self, input_text):
        return f"{self.optional_prompt}{self.text_qa_template_str}{input_text}"


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


@app.post("/load_model", tags=["load"])
async def load_model(req: LoadRequest):
    global chatbot
    try:
        chatbot = TransformerChat(req.modelDir, prompt=req.prompt)
        return JSONResponse({"status": "success", "message": f"Model {req.modelDir} loaded."}, status_code=200)
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)


@app.post("/chat", tags=["chat"])
async def chat(req: ChatRequest):
    if chatbot is None:
        return JSONResponse({"error": "Model not loaded yet. Call /load_model first."}, status_code=400)

    def generate_stream():
        # 格式化 prompt
        prompt = chatbot.format_prompt(req.input_text)

        # 編碼成 input_ids
        inputs = chatbot.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
        input_ids = inputs["input_ids"].to(chatbot.model.device)
        attention_mask = inputs["attention_mask"].to(chatbot.model.device)

        # 使用 HuggingFace 官方 streamer（會 yield 字串）
        streamer = TextIteratorStreamer(
            tokenizer=chatbot.tokenizer,
            skip_special_tokens=True,
            skip_prompt=True
        )

        # 建立一個執行 generate() 的執行緒
        generation_kwargs = dict(
            input_ids=input_ids,
            attention_mask=attention_mask,
            streamer=streamer,
            do_sample=True,
            temperature=chatbot.temperature,
            top_p=chatbot.top_p,
            top_k=40,
            repetition_penalty=1.15,
            max_new_tokens=chatbot.maximum_tokens,
        )

        thread = threading.Thread(target=chatbot.model.generate, kwargs=generation_kwargs)
        thread.start()

        # 回傳字串 stream
        for token in streamer:
            yield token  # 確保是 string，不會出錯

    return StreamingResponse(generate_stream(), media_type="text/plain")


class DeviceType(str, Enum):
    cpu = "cpu"
    ssd = "ssd"
    dram = "dram"
    gpu = "gpu"

@app.get("/device_info/{Type}", tags=["show device info"])
async def get_device_info(Type: DeviceType = None):
    #Type = Type.lower()
    info = {}

    if Type is DeviceType.cpu: # if Type.value == "cpu"
        info = {
            "physical_cores": psutil.cpu_count(logical=False),
            "total_cores": psutil.cpu_count(logical=True),
            "cpu_freq": psutil.cpu_freq()._asdict(),
            "cpu_usage_percent": psutil.cpu_percent(interval=1),
            "processor": platform.processor()
        }

    elif Type is DeviceType.dram:
        virtual_mem = psutil.virtual_memory()
        info = {
            "total_MB": virtual_mem.total // 1024 // 1024,
            "available_MB": virtual_mem.available // 1024 // 1024,
            "used_MB": virtual_mem.used // 1024 // 1024,
            "percent_used": virtual_mem.percent
        }

    elif Type == DeviceType.ssd:
        disk = shutil.disk_usage("/")
        info = {
            "total_GB": round(disk.total / (1024 ** 3), 2),
            "used_GB": round(disk.used / (1024 ** 3), 2),
            "free_GB": round(disk.free / (1024 ** 3), 2),
            "percent_used": round(disk.used / disk.total * 100, 2)
        }

    elif Type == DeviceType.gpu:
        if torch.cuda.is_available():
            info = {
                f"gpu_{i}": {
                    "name": torch.cuda.get_device_name(i),
                    "total_memory_MB": torch.cuda.get_device_properties(i).total_memory // 1024 // 1024,
                    "memory_allocated_MB": torch.cuda.memory_allocated(i) // 1024 // 1024,
                    "memory_reserved_MB": torch.cuda.memory_reserved(i) // 1024 // 1024,
                    "device_capability": torch.cuda.get_device_properties(i).major,
                }
                for i in range(torch.cuda.device_count())
            }
        else:
            info = {"message": "CUDA GPU not available"}
    else:
        return JSONResponse({"error": "Unsupported type. Use cpu/gpu/dram/ssd"}, status_code=400)
    return JSONResponse({"Type": Type, "info": info}, status_code=200) #傳回枚舉成員，甚至嵌套在 JSON 主體中（例如dict) 它們將被轉換為對應的值（在本例中為字串），然後傳回給客戶端：


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)