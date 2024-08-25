
from internal.repo.repository import Repo

class User:
    def __init__(self, repo:Repo) -> None:
        self.repo = repo
    
    async def start (self, user_id:int) -> None:
        return await self.repo.user.add_user_id(user_id)