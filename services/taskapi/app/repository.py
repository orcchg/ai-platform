from app.models import Task

class TaskRepository:
    def __init__(self, session):
        self.session = session

    async def get(self, task_id: int) -> Task | None:
        return await self.session.get(Task, task_id)

    async def add(self, task: Task) -> Task:
        return await self.session.add(task)
