# app/managers/marca_manager.py
from typing import List, Optional
from psycopg import Cursor

class MarcaManager:
    def get_all(self, cursor: Cursor):
        res = cursor.execute('SELECT id, nombre, pais_origen FROM Marca').fetchall()
        return [r for r in res]

    def get_by_id(self, marca_id: int, cursor: Cursor):
        cursor.execute('SELECT id, nombre, pais_origen FROM Marca WHERE id = %s', (marca_id,))
        return cursor.fetchone()

    def create(self, data: dict, cursor: Cursor):
        cursor.execute('INSERT INTO Marca (nombre, pais_origen) VALUES (%s, %s) RETURNING id',
                       (data["nombre"], data.get("pais_origen")))
        nid = cursor.fetchone()["id"]
        return {"id": nid, **data}

    def update(self, marca_id: int, data: dict, cursor: Cursor):
        for k, v in data.items():
            cursor.execute(f'UPDATE Marca SET "{k}" = %s WHERE id = %s', (v, marca_id))
        cursor.execute('SELECT id, nombre, pais_origen FROM Marca WHERE id = %s', (marca_id,))
        return cursor.fetchone()

    def delete(self, marca_id: int, cursor: Cursor):
        cursor.execute('DELETE FROM Marca WHERE id = %s', (marca_id,))
        return {"mensaje": "Marca eliminada con éxito!"}
