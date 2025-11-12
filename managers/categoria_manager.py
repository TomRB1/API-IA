# app/managers/categoria_manager.py
from psycopg import Cursor

class CategoriaManager:
    def get_all(self, cursor: Cursor):
        res = cursor.execute('SELECT id, nombre, descripcion FROM Categoria').fetchall()
        return [r for r in res]

    def get_by_id(self, categoria_id: int, cursor: Cursor):
        cursor.execute('SELECT id, nombre, descripcion FROM Categoria WHERE id = %s', (categoria_id,))
        return cursor.fetchone()

    def create(self, data: dict, cursor: Cursor):
        cursor.execute('INSERT INTO Categoria (nombre, descripcion) VALUES (%s, %s) RETURNING id',
                       (data["nombre"], data.get("descripcion")))
        nid = cursor.fetchone()["id"]
        return {"id": nid, **data}

    def update(self, categoria_id: int, data: dict, cursor: Cursor):
        for k, v in data.items():
            cursor.execute(f'UPDATE Categoria SET "{k}" = %s WHERE id = %s', (v, categoria_id))
        cursor.execute('SELECT id, nombre, descripcion FROM Categoria WHERE id = %s', (categoria_id,))
        return cursor.fetchone()

    def delete(self, categoria_id: int, cursor: Cursor):
        cursor.execute('DELETE FROM Categoria WHERE id = %s', (categoria_id,))
        return {"mensaje": "Categoria eliminada con éxito!"}
