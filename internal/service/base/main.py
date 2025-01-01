
from internal.repositories.repository import Repo
from internal.app.messages.base import START

class Base:
    def __init__(self, repo:Repo) -> None:
        self.repo = repo
        
    async def start(self) -> str:
        return START