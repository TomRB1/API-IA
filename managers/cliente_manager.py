# app/managers/cliente_manager.py
from typing import List, Optional
from psycopg import Cursor

class ClienteManager:
    def get_all(self, cursor: Cursor) -> List[dict]:
        res = cursor.execute('SELECT id, nombre, apellido, telefono, email FROM Cliente').fetchall()
        return [row for row in res]

    def get_by_id(self, cliente_id: int, cursor: Cursor) -> Optional[dict]:
        cursor.execute('SELECT id, nombre, apellido, telefono, email FROM Cliente WHERE id = %s', (cliente_id,))
        return cursor.fetchone()

    def create(self, cliente: dict, cursor: Cursor) -> dict:
        cursor.execute(
            'INSERT INTO Cliente (nombre, apellido, telefono, email) VALUES (%s, %s, %s, %s) RETURNING id',
            (cliente["nombre"], cliente.get("apellido"), cliente.get("telefono"), cliente.get("email"))
        )
        new_id = cursor.fetchone()["id"]
        return { "id": new_id, **cliente }

    def update(self, cliente_id: int, data: dict, cursor: Cursor) -> dict:
        # only update fields present
        for k, v in data.items():
            cursor.execute(f'UPDATE Cliente SET "{k}" = %s WHERE id = %s', (v, cliente_id))
        cursor.execute('SELECT id, nombre, apellido, telefono, email FROM Cliente WHERE id = %s', (cliente_id,))
        return cursor.fetchone()

    def delete(self, cliente_id: int, cursor: Cursor) -> dict:
        cursor.execute('DELETE FROM Cliente WHERE id = %s', (cliente_id,))
        return {"mensaje": "Cliente eliminado con éxito!"}
