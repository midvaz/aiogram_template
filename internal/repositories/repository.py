import asyncpg

from internal.repositories.user import UserRepo

class Repo:
    """Db abstract level"""

    def __init__(self, conn: asyncpg.pool.PoolAcquireContext):
        self.conn = conn
        self.user:UserRepo = self.__user()

    def __user(self) -> UserRepo:
        "return UserRepo class"
        return UserRepo(conn=self.conn)