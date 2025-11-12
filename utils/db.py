# app/utils/db.py
import os
from typing import Generator
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def get_cursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(
        DATABASE_URL,
        row_factory=dict_row,
        sslmode="require"
    )
    cur = conn.cursor()
    try:
        yield cur
        conn.commit()
    finally:
        cur.close()
        conn.close()
