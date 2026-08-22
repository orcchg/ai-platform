from app.repository import TaskRepository
from app.dto import TaskDTO
from app.exceptions import TaskNotFound

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def get_task(self, task_id: int) -> TaskDTO:
        task = await self.task_repository.get(task_id)
        if task is None:
            raise TaskNotFound(task_id)
        return TaskDTO.model_validate(task)
