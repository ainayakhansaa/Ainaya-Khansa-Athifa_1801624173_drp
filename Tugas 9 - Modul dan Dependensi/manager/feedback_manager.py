"""
feedback_manager.py

Memberikan motivasi berdasarkan level stres pengguna.
"""

from manager.stress_checker import cek_stres


def tampilkan_feedback():
    """Menampilkan motivasi kepada pengguna."""

    hasil = cek_stres()

    if hasil is None:
        return

    level = hasil["level"]

    print("\n" + "=" * 50)
    print("          MOTIVASI HARI INI")
    print("=" * 50)

    if "Rendah" in level:
        print("😊 Luar biasa! Terus pertahankan energi positifmu.")
        print("Setiap langkah kecil yang kamu lakukan sangat berarti.")

    elif "Sedang" in level:
        print("💛 Tidak apa-apa jika hari ini terasa melelahkan.")
        print("Istirahat sejenak bukan berarti menyerah.")

    else:
        print("🌿 Kamu sudah berusaha sejauh ini, itu patut dihargai.")
        print("Tidak apa-apa meminta bantuan ketika merasa kewalahan.")
        print("Besok adalah kesempatan baru untuk memulai lagi.")

    print("=" * 50)