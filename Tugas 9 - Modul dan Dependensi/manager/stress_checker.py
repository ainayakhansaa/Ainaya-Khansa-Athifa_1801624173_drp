"""
stress_checker.py

Menentukan tingkat stres berdasarkan hasil analisis mood.
"""

from manager.mood_analysis import analisis_mood


def cek_stres():
    """Menentukan level stres pengguna."""

    hasil = analisis_mood()

    if hasil is None:
        return None

    rata_skor = hasil["rata_skor"]

    if rata_skor >= 4:
        level = "Rendah 😊"
        keterangan = "Kondisi emosimu cukup stabil. Pertahankan kebiasaan baikmu."

    elif rata_skor >= 2.5:
        level = "Sedang 😐"
        keterangan = "Mulai perhatikan kondisi emosimu dan luangkan waktu untuk beristirahat."

    else:
        level = "Tinggi 😔"
        keterangan = "Kamu menunjukkan tanda-tanda stres yang cukup tinggi. Cobalah melakukan relaksasi atau berbicara dengan orang yang kamu percaya."

    print("\n" + "=" * 50)
    print("          HASIL CEK LEVEL STRES")
    print("=" * 50)
    print(f"Level Stres : {level}")
    print(f"Keterangan  : {keterangan}")
    print("=" * 50)

    return {
        "level": level,
        "keterangan": keterangan
    }