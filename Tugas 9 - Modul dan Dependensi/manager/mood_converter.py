"""
mood_converter.py

Mengubah mood menjadi skor numerik.
"""

def get_mood_options():
    return {
        "1": "Senang",
        "2": "Tenang",
        "3": "Sedih",
        "4": "Stres",
        "5": "Marah"
    }


def konversi_mood_ke_skor(mood):

    skor = {
        "Senang": 5,
        "Tenang": 4,
        "Sedih": 3,
        "Stres": 2,
        "Marah": 1
    }

    return skor.get(mood, 0)