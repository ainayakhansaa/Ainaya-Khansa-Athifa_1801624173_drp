"""
mood_tracker.py

Mengelola fitur:
1. Input mood harian
2. Menampilkan riwayat mood
"""

from manager.mood_converter import get_mood_options, konversi_mood_ke_skor
from manager import database_manager as db


def input_mood():
    """Mencatat mood harian pengguna."""

    print("\n" + "=" * 50)
    print("             INPUT MOOD HARIAN")
    print("=" * 50)
    print("Bagaimana perasaanmu hari ini?\n")

    opsi = get_mood_options()

    for kode, mood in opsi.items():
        print(f"{kode}. {mood}")

    print("-" * 50)

    while True:

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan in opsi:
            break

        print("❌ Pilihan tidak valid. Silakan pilih kembali.")

    mood = opsi[pilihan]

    skor = konversi_mood_ke_skor(mood)

    data = db.tambah_entry(mood, skor)

    print("\n✅ Mood berhasil disimpan!")
    print(f"Mood      : {data['mood']}")
    print(f"Skor      : {data['skor']}")
    print(f"Tanggal   : {data['tanggal']}")
    print(f"Waktu     : {data['waktu']}")

    return data


def lihat_riwayat():
    """Menampilkan seluruh riwayat mood."""

    print("\n" + "=" * 50)
    print("             RIWAYAT MOOD")
    print("=" * 50)

    history = db.load_history()

    if len(history) == 0:
        print("Belum ada riwayat mood.")
        print("Silakan input mood terlebih dahulu.")
        return

    for nomor, item in enumerate(history, start=1):

        print(f"\nData ke-{nomor}")
        print("-" * 30)
        print(f"Tanggal : {item['tanggal']}")
        print(f"Waktu   : {item['waktu']}")
        print(f"Mood    : {item['mood']}")
        print(f"Skor    : {item['skor']}")

    print("\n" + "=" * 50)
    print(f"Total riwayat mood : {len(history)}")