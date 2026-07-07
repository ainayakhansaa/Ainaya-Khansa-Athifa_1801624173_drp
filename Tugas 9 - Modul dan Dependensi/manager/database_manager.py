"""
database_manager.py

Mengelola penyimpanan dan pembacaan data mood pengguna
menggunakan file JSON.
"""

import json
import os
from datetime import datetime

# Lokasi file database
DATA_FILE = "data/mood_history.json"


def load_history():
    """
    Membaca seluruh riwayat mood.
    Mengembalikan list.
    """

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_history(data):
    """
    Menyimpan seluruh data ke file JSON.
    """

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def tambah_entry(mood, skor):
    """
    Menambahkan satu data mood baru.
    """

    history = load_history()

    sekarang = datetime.now()

    entry = {
        "tanggal": sekarang.strftime("%d-%m-%Y"),
        "waktu": sekarang.strftime("%H:%M"),
        "mood": mood,
        "skor": skor
    }

    history.append(entry)

    save_history(history)

    return entry