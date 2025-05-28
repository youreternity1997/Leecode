import time
from lib.source.producing import ProducingProcess
import asyncio
import traceback

from dto.produce_dataset_state_manager import LLMProduceDatasetStateManager  # ~/dto/produce_dataset_state_manager.py

stop_producing = False

global producing

async def run(
        FileFolder = '~/LLaMA-Factory/data',
        UploadFile = ['~/LLaMA-Factory/data/Files/美利堅合眾國憲法.json'], # '~/LLaMA-Factory/data/alpaca_data_en_52k.json', # '~/LLaMA-Factory/data/美利堅合眾國憲法.json',
        Name = '美利堅合眾國憲法', # 'alpaca_data_en_52k',
        Chosen_Model = "",
        num_QandA = 30,
        NoLimit_QandA = False,
):
    LLMProduceDatasetStateManager.set_producing_running(True)
    stop_producing_event = asyncio.Event()  # asyncio.Event 是協調協程之間同步的有力工具。通過設置和等待事件，協程可以高效地協同工作而不會阻塞主線程。
    LLMProduceDatasetStateManager.set_stop_producing_event(stop_producing_event)  # Set the event in the StateManager
    stop_producing_event = LLMProduceDatasetStateManager.get_stop_producing_event()  # Retrieve the event
    if stop_producing_event is None:
        raise Exception("stop_producing_event is not set before producing starts")
    
    global producing
    producing = None
    try:
        producing = ProducingProcess(
            FileFolder = FileFolder,
            UploadFile = UploadFile,
            Name = Name,
            Chosen_Model = Chosen_Model,
            num_QandA = num_QandA,
            NoLimit_QandA = NoLimit_QandA,
        )
        #producing.write_script()
        check_task = asyncio.create_task(check_condition(stop_producing_event, producing)) # producing = ProducingProcess
        await asyncio.sleep(0.1)
        dataset_data = await producing.start() 
        #print('llm_produce_dataset.py dataset_data= ', dataset_data)
        
        # 等待停止事件被触发
        #await stop_producing.wait() # stop_producing = False

        return dataset_data
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if producing is not None:
            await producing.stop()
        LLMProduceDatasetStateManager.set_producing_running(False)


async def check_condition(stop_producing_event, producing):
    while not stop_producing_event.is_set():
        await asyncio.sleep(1)  # 使用异步sleep等待
    # 当stop_producing_event被设置时，停止训练进程
    await producing.stop()


async def stop(stop_producing_event): # stop_producing_event = asyncio.Event()
    print('------------------------------0')
    if stop_producing_event is not None:
        print("stop producing function is called")  # 添加日誌輸出
        stop_producing_event.set()  # trigger stop event # asyncio.Event().set() 方法是將事件狀態設置為已設置，從而喚醒所有等待該事件的協程。這在需要多個協程協同工作的異步編程中非常有用。
    
    print('------------------------------1')
    print('producing====================', producing)
    if producing is not None:
        await producing.stop()


if __name__ == '__main__':
    pass
