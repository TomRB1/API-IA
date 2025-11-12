# app/managers/pedido_manager.py
from psycopg import Cursor
from typing import List, Optional

class PedidoManager:
    def get_all(self, cursor: Cursor) -> List[dict]:
        res = cursor.execute(
            """
            SELECT p.id, p.id_cliente, c.nombre || ' ' || c.apellido AS cliente_nombre,
                   p.id_componente, comp.nombre AS componente_nombre,
                   p.cantidad, p.precio_unitario, p.total, p.fecha
            FROM Pedido p
            LEFT JOIN Cliente c ON p.id_cliente = c.id
            LEFT JOIN Componente comp ON p.id_componente = comp.id
            ORDER BY p.fecha DESC
            """
        ).fetchall()
        return [r for r in res]

    def get_by_id(self, pedido_id: int, cursor: Cursor) -> Optional[dict]:
        cursor.execute(
            """
            SELECT p.id, p.id_cliente, c.nombre || ' ' || c.apellido AS cliente_nombre,
                   p.id_componente, comp.nombre AS componente_nombre,
                   p.cantidad, p.precio_unitario, p.total, p.fecha
            FROM Pedido p
            LEFT JOIN Cliente c ON p.id_cliente = c.id
            LEFT JOIN Componente comp ON p.id_componente = comp.id
            WHERE p.id = %s
            """,
            (pedido_id,)
        )
        return cursor.fetchone()

    def create(self, data: dict, cursor: Cursor) -> dict:
        cursor.execute(
            'INSERT INTO Pedido (id_cliente, id_componente, cantidad, precio_unitario) VALUES (%s,%s,%s,%s) RETURNING id, fecha, (cantidad * precio_unitario) AS total',
            (data["id_cliente"], data["id_componente"], data.get("cantidad", 1), data["precio_unitario"])
        )
        row = cursor.fetchone()
        return {
            "id": row["id"],
            "fecha": row["fecha"],
            "total": float(row["total"]),
            **data
        }

    def update(self, pedido_id: int, data: dict, cursor: Cursor) -> dict:
        for k, v in data.items():
            cursor.execute(f'UPDATE Pedido SET "{k}" = %s WHERE id = %s', (v, pedido_id))
        return self.get_by_id(pedido_id, cursor)

    def delete(self, pedido_id: int, cursor: Cursor) -> dict:
        cursor.execute('DELETE FROM Pedido WHERE id = %s', (pedido_id,))
        return {"mensaje": "Pedido eliminado con éxito!"}
