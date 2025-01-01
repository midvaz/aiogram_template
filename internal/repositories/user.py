import asyncpg

class UserRepo():
    __table_name = "users"
    def __init__(self, conn: asyncpg.Connection):
        self.conn = conn

    async def add_user_id (self, user_id:int)->int:
        """
        Add user telegram id at database if not exist
        Returning new user id
        """
        new_user_id = await self.conn.fetch(
            f"""INSERT INTO {self.__table_name} (telegram_id)
            SELECT $1
            WHERE NOT EXISTS (
                SELECT telegram_id FROM {self.__table_name} WHERE telegram_id = $1
            )
            RETURNING id;""",
            user_id
        )
        return new_user_id
        

    async def read_user_by_id(self, user_id:int):
        """
        Read one user
        """
        
        row = await self.conn.fetchrow(
            f"""SELECT * FROM {self.__table_name}
            WHERE telegram_id = $1
            """, user_id
        )
        return row