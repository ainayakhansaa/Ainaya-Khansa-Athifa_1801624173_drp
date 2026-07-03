"""
database_manager.py

Mengelola database SQLite untuk aplikasi PsyMood.
"""

import os
import sqlite3
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATABASE = os.path.join(PROJECT_ROOT, "database", "psymood.db")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
JSON_FILE = os.path.join(DATA_DIR, "mood_history.json")


def create_database():
    """Membuat database dan tabel jika belum ada."""

    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

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


def export_json():
    """
    Mengekspor seluruh data mood ke file JSON.
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    history = load_history()
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)

    print(f"✅ Data berhasil diekspor ke {JSON_FILE}")


def import_json(filename=None):
    if filename is None:
        filename = JSON_FILE

    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' tidak ditemukan.")

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    imported_count = 0
    for item in data:
        cursor.execute("""
            INSERT INTO mood_history (mood, skor, tanggal, waktu)
            VALUES (?, ?, ?, ?)
        """, (
            item["mood"],
            item["skor"],
            item["tanggal"],
            item["waktu"]
        ))
        imported_count += 1

    conn.commit()
    conn.close()

    print(f"✅ Berhasil mengimpor {imported_count} data dari {filename}")
    return imported_count