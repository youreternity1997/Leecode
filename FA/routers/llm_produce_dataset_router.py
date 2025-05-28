from fastapi import APIRouter, HTTPException, Depends
from fastapi import BackgroundTasks

from lib.source.finetune_options import (
    get_visible_devices, get_model_path, get_learning_rate,
    get_num_train_epochs, get_per_device_train_batch_size, get_lr_scheduler_type,
    get_save_strategy, get_save_steps, get_model_config,
    get_precision, get_finetuning_type, get_lora_targets, get_dataset,
    get_deepspeed_config, get_flash_attn, get_max_length, get_num_layer_trainable,
    get_name_module_trainable, get_lora_r, get_lora_alpha, get_lora_dropout,
    get_quantization_bit, get_checkpoint_folder, get_output_folder
)
#from lib.source.finetune_schedule import ScheduleManager
from lib.source.llm_produce_dataset import run, stop
from lib.source.core.llm_produce_dataset.recommend import recommend_fun
from lib.source.core.llm_produce_dataset.saving import saving_fun
from lib.source.core.llm_produce_dataset.showing import showing_fun

from dto.llm_produce_dataset_dto import LlmProductDatasetDTO
from dto.save_produce_dataset_dto import ReturnDatasetDTO
from dto.recommend_language_model_dto import Recommend_Language_Model_DTO


import asyncio
import os
import sys
from typing import Optional

llm_produce_dataset_router = APIRouter()
#from lib.source.log import get_training_parameters, get_resume_training_parameters
from dto.produce_dataset_state_manager import LLMProduceDatasetStateManager 


@llm_produce_dataset_router.post("/llm_produce_dataset_start")
async def start(llm_pro_data_config_dto: LlmProductDatasetDTO):
    LLMProduceDatasetStateManager.set_producing_running(True)

    task = asyncio.create_task(run_async(**llm_pro_data_config_dto.dict())) # 創建並調度異步任務
    #BackgroundTasks.add_task(task)

    try:
        Json_content = await task
        await asyncio.sleep(0.2)
        return {"Result": Json_content}
    
    except Exception as e:
        print("start llm_produce_dataset Exception......", str(e))
        return {"ErrorMessage": str(e)}

async def run_async(**kwargs):
    try:
        await asyncio.sleep(0.1)
        Json_content = await run(**kwargs) # from lib.source.finetune import run
        return Json_content 
    finally:
        LLMProduceDatasetStateManager.set_producing_running(False)


@llm_produce_dataset_router.get("/llm_produce_dataset_end")
async def end():
    print("Stop-------------------------------------------")
    LLMProduceDatasetStateManager.set_producing_running(False)

    global task
    if task and not task.done():
        task.cancel()   

    stop_producing_event = LLMProduceDatasetStateManager.get_stop_producing_event()
    if stop_producing_event is not None:
        stop(stop_producing_event)
    
    return {"message": "LLM produce dataset process has been stopped"}




if __name__ == '__main__':
    pass
