from pydantic import BaseModel

class TaskDTO(BaseModel):
    model_config = {"from_attributes":True}