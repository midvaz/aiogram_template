
from internal.repo.repository import Repo
from internal.resources.messages.base import START

class Base:
    def __init__(self, repo:Repo) -> None:
        self.repo = repo
        
    async def start(self) -> str:
        return START