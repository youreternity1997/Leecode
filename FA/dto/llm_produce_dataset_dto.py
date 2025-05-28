from pydantic import BaseModel
from typing import List, Optional

class LlmProductDatasetDTO(BaseModel):
    FileFolder: str = '~/LLaMA-Factory/data'
    UploadFile: List[str] = ['~/LLaMA-Factory/data/Files/美利堅合眾國憲法.json']
    Name: str = '美利堅合眾國憲法'
    Chosen_Model: Optional[str] = ""
    num_QandA: int = 30
    NoLimit_QandA: bool = False
