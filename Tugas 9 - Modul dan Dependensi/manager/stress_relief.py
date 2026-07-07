"""
stress_relief.py

Memberikan rekomendasi aktivitas untuk membantu mengurangi stres.
"""

from manager.stress_checker import cek_stres


def tampilkan_relief():
    """Menampilkan rekomendasi berdasarkan level stres."""

    hasil = cek_stres()

    if hasil is None:
        return

    level = hasil["level"]

    print("\n" + "=" * 50)
    print("         STRESS RELIEF GUIDE")
    print("=" * 50)

    if "Rendah" in level:
        print("Rekomendasi:")
        print("- Pertahankan pola hidup sehat.")
        print("- Tetap luangkan waktu untuk hobi.")
        print("- Istirahat yang cukup.")
        print("- Lakukan olahraga ringan secara rutin.")

    elif "Sedang" in level:
        print("Rekomendasi:")
        print("- Lakukan latihan pernapasan 5-10 menit.")
        print("- Dengarkan musik yang menenangkan.")
        print("- Jalan santai di luar ruangan.")
        print("- Ceritakan perasaanmu kepada orang terdekat.")

    else:
        print("Rekomendasi:")
        print("- Coba teknik meditasi atau mindfulness.")
        print("- Tuliskan perasaanmu di jurnal.")
        print("- Kurangi aktivitas yang membuat stres.")
        print("- Jangan ragu mencari bantuan profesional jika diperlukan.")

    print("=" * 50)