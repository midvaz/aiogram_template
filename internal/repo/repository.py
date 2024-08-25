import asyncpg

from internal.service.repo.user import UserRepo

class Repo:
    """Db abstract level"""

    def __init__(self, conn: asyncpg.pool.PoolAcquireContext):
        self.conn = conn

    def user(self) -> UserRepo:
        "return UserRepo class"
        return UserRepo(conn=self.conn)