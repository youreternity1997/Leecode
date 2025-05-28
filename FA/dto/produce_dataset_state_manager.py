import asyncio

class LLMProduceDatasetStateManager:
    producing_running = False
    stop_producing_event: asyncio.Event = None

    @classmethod
    def set_producing_running(cls, status: bool):
        cls.producing_running = status

    @classmethod
    def is_producing_running(cls) -> bool:
        return cls.producing_running

    @classmethod
    def set_stop_producing_event(cls, event: asyncio.Event):
        cls.stop_producing_event = event

    @classmethod
    def get_stop_producing_event(cls) -> asyncio.Event:
        return cls.stop_producing_event
