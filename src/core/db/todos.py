import sqlite3
from typing import Any


class Todos_manager:
    def __init__(self):
        self.__conn = sqlite3.connect("todos.db")
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                text TEXT NOT NULL,
                created TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.__conn.commit()

    def read_all(self) -> list[Any] | None:
        try:
            res = self.__cursor.execute("SELECT * FROM todos ORDER BY id DESC")
        except Exception as e:
            print(f"Ha ocurrido un error al leer todos los todos: {e}")
        else:
            return res.fetchall()

    def create(self, title: str, text: str) -> bool:
        try:
            self.__cursor.execute(
                "INSERT INTO todos (title, text) VALUES (?, ?)",
                (title, text),
            )
            self.__conn.commit()
        except Exception as e:
            print(f"Ha ocurrido un error al crear el todo: {e}")
            return False
        else:
            return True

    def update(self, id: int, title: str, text: str) -> bool:
        try:
            self.__cursor.execute(
                "UPDATE todos SET title = ?, text = ? WHERE id = ?",
                (title, text, id),
            )
            self.__conn.commit()
        except Exception as e:
            print(f"Ha ocurrido un error al actualizar el todo: {e}")
            return False
        else:
            return True

    def delete(self, id: int):
        try:
            self.__cursor.execute("DELETE FROM todos WHERE id = ?", (id,))
            self.__conn.commit()
        except Exception as e:
            print(f"Ha ocurrido un error al eliminar el todo: {e}")
            return False
        else:
            return True

    def close_db(self):
        self.__conn.close()
