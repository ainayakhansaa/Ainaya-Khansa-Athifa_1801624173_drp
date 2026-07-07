"""
database_manager.py

Mengelola database SQLite untuk aplikasi PsyMood.
"""

import sqlite3
from datetime import datetime

DATABASE = "database/psymood.db"


def create_database():
    """Membuat database dan tabel jika belum ada."""

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mood_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mood TEXT NOT NULL,
            skor INTEGER NOT NULL,
            tanggal TEXT NOT NULL,
            waktu TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def tambah_entry(mood, skor):
    

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    sekarang = datetime.now()

    tanggal = sekarang.strftime("%d-%m-%Y")
    waktu = sekarang.strftime("%H:%M")

    cursor.execute("""
        INSERT INTO mood_history (mood, skor, tanggal, waktu)
        VALUES (?, ?, ?, ?)
    """, (mood, skor, tanggal, waktu))

    conn.commit()

    data = {
        "id": cursor.lastrowid,
        "mood": mood,
        "skor": skor,
        "tanggal": tanggal,
        "waktu": waktu
    }

    conn.close()

    return data


def load_history():
    """
    Mengambil seluruh data mood dari database.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, mood, skor, tanggal, waktu
        FROM mood_history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    history = []

    for row in rows:
        history.append({
            "id": row[0],
            "mood": row[1],
            "skor": row[2],
            "tanggal": row[3],
            "waktu": row[4]
        })

    return history


def update_entry(id, mood, skor):
    """
    Mengubah data mood berdasarkan ID.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE mood_history
        SET mood = ?, skor = ?
        WHERE id = ?
    """, (mood, skor, id))

    conn.commit()
    conn.close()

def delete_entry(id):
    """
    Menghapus data mood berdasarkan ID.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM mood_history
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()