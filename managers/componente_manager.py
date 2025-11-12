# app/managers/componente_manager.py
from psycopg import Cursor
from typing import List, Optional

class ComponenteManager:
    def get_all(self, cursor: Cursor) -> List[dict]:
        # join to include marca and categoria names
        res = cursor.execute(
            """
            SELECT comp.id, comp.nombre, comp.id_marca, m.nombre AS marca_nombre,
                   comp.id_categoria, c.nombre AS categoria_nombre,
                   comp.precio, comp.stock, comp.descripcion
            FROM Componente comp
            LEFT JOIN Marca m ON comp.id_marca = m.id
            LEFT JOIN Categoria c ON comp.id_categoria = c.id
            ORDER BY comp.id DESC
            """
        ).fetchall()
        return [r for r in res]

    def get_by_id(self, comp_id: int, cursor: Cursor) -> Optional[dict]:
        cursor.execute(
            """
            SELECT comp.id, comp.nombre, comp.id_marca, m.nombre AS marca_nombre,
                   comp.id_categoria, c.nombre AS categoria_nombre,
                   comp.precio, comp.stock, comp.descripcion
            FROM Componente comp
            LEFT JOIN Marca m ON comp.id_marca = m.id
            LEFT JOIN Categoria c ON comp.id_categoria = c.id
            WHERE comp.id = %s
            """,
            (comp_id,)
        )
        return cursor.fetchone()

    def create(self, data: dict, cursor: Cursor) -> dict:
        cursor.execute(
            'INSERT INTO Componente (nombre, id_marca, id_categoria, precio, stock, descripcion) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id',
            (data["nombre"], data.get("id_marca"), data.get("id_categoria"), data["precio"], data.get("stock", 0), data.get("descripcion"))
        )
        nid = cursor.fetchone()["id"]
        return { "id": nid, **data }

    def update(self, comp_id: int, data: dict, cursor: Cursor) -> dict:
        for k, v in data.items():
            cursor.execute(f'UPDATE Componente SET "{k}" = %s WHERE id = %s', (v, comp_id))
        return self.get_by_id(comp_id, cursor)

    def delete(self, comp_id: int, cursor: Cursor) -> dict:
        cursor.execute('DELETE FROM Componente WHERE id = %s', (comp_id,))
        return {"mensaje": "Componente eliminado con éxito!"}
