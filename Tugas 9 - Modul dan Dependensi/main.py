import os

from manager.database_manager import create_database, tambah_entry, load_history, update_entry, delete_entry, export_json, import_json

def welcome():
    while True:
        print("\n" + "=" * 50)
        print("           SELAMAT DATANG DI PSYMOOD")
        print("=" * 50)
        print("Pantau mood harianmu,")
        print("kenali tingkat stresmu,")
        print("dan dapatkan dukungan positif setiap hari.")
        print("\n1. Lanjutkan")
        print("2. Keluar")
        print("=" * 50)

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            return True

        elif pilihan == "2":
            print("\nTerima kasih telah menggunakan PsyMood 😊")
            print("Semoga harimu menyenangkan dan tetap menjaga kesehatan mentalmu.")
            return False

        else:
            print("\n❌ Pilihan tidak valid. Silakan coba lagi.")



def tampilkan_menu():
    print("\n" + "=" * 55)
    print("                 MENU UTAMA PSYMOOD")
    print("=" * 55)
    print("1. 😊 Input Mood Harian")
    print("2. 📜 Lihat Riwayat Mood")
    print("3. 📊 Analisis Mood")
    print("4. 😟 Cek Level Stres")
    print("5. 🌿 Stress Relief Guide")
    print("6. 💬 Motivasi Hari Ini")
    print("7. ✏️ Edit Mood")
    print("8. 🗑️ Hapus Mood")
    print("9. Export JSON")
    print("10. Import JSON")
    print("11. 🚪 Keluar")
    print("=" * 55)



# ==========================
# INPUT MOOD
# ==========================

def input_mood():

    print("\n=== INPUT MOOD HARIAN ===")

    mood = input("Bagaimana mood kamu hari ini? ")

    skor = int(input("Masukkan skor mood (1-10): "))

    tambah_entry(mood, skor)

    print("\n✅ Mood berhasil disimpan!")



# ==========================
# LIHAT HISTORY
# ==========================

def lihat_riwayat():

    print("\n=== RIWAYAT MOOD ===")

    history = load_history()

    if len(history) == 0:
        print("Belum ada data mood.")

    else:
        for data in history:
            print("--------------------------------")
            print(f"ID      : {data['id']}")
            print(f"Mood    : {data['mood']}")
            print(f"Skor    : {data['skor']}")
            print(f"Tanggal : {data['tanggal']}")


# ==========================
# ANALISIS MOOD
# ==========================

def analisis_mood():

    print("\n=== ANALISIS MOOD ===")

    history = load_history()

    if len(history) == 0:
        print("Belum ada data mood untuk dianalisis.")

    else:
        total_data = len(history)

        total_skor = 0
        skor_tertinggi = history[0]
        skor_terendah = history[0]

        for data in history:
            total_skor += data["skor"]

            if data["skor"] > skor_tertinggi["skor"]:
                skor_tertinggi = data

            if data["skor"] < skor_terendah["skor"]:
                skor_terendah = data


        rata_rata = total_skor / total_data

        print("--------------------------------")
        print(f"Jumlah catatan mood : {total_data}")
        print(f"Rata-rata skor      : {rata_rata:.2f}")
        print("--------------------------------")

        print(f"Mood terbaik        : {skor_tertinggi['mood']} ({skor_tertinggi['skor']})")
        print(f"Mood terendah       : {skor_terendah['mood']} ({skor_terendah['skor']})")

        print("\nKesimpulan:")

        if rata_rata >= 8:
            print("😊 Kondisi mood kamu sangat positif!")

        elif rata_rata >= 5:
            print("🙂 Kondisi mood kamu cukup stabil.")

        else:
            print("😟 Kondisi mood kamu sedang kurang baik.")


# ==========================
# CEK LEVEL STRES
# ==========================

def cek_stres():

    print("\n=== CEK LEVEL STRES ===")

    skor = int(input("Masukkan skor stres kamu (1-10): "))

    print("\nHasil Analisis:")

    if skor <= 3:
        print("😊 Level stres: Rendah")
        print("Kondisimu terlihat cukup tenang. Tetap jaga keseimbangan aktivitas.")

    elif skor <= 7:
        print("😐 Level stres: Sedang")
        print("Coba luangkan waktu untuk istirahat dan lakukan aktivitas yang membuat rileks.")

    else:
        print("😟 Level stres: Tinggi")
        print("Disarankan untuk mengambil waktu istirahat dan mencari dukungan jika diperlukan.")


# ==========================
# STRESS RELIEF GUIDE
# ==========================

def tampilkan_relief():

    print("\n" + "=" * 50)
    print("         STRESS RELIEF GUIDE")
    print("=" * 50)

    history = load_history()

    if len(history) == 0:
        print("Belum ada data mood.")
        print("Silakan input mood terlebih dahulu.")
        print("=" * 50)
        return


    mood_terakhir = history[0]["mood"].capitalize()
    skor_terakhir = history[0]["skor"]


    print(f"\nBerdasarkan catatan mood terakhir kamu:")
    print(f"Mood terakhir : {mood_terakhir}")
    print(f"Skor mood     : {skor_terakhir}")

    print("\nRekomendasi untuk kamu:")


    if mood_terakhir in ["Cemas", "Takut"]:

        print("Saat ini kamu mungkin sedang merasa khawatir atau tidak tenang.")
        print("Tidak apa-apa untuk memberi waktu bagi diri sendiri agar lebih rileks.")
        print()
        print("- 🧘 Lakukan latihan pernapasan sederhana.")
        print("- 📝 Tuliskan hal-hal yang sedang memenuhi pikiranmu.")
        print("- 🌿 Lakukan aktivitas yang membuat tubuh lebih tenang.")


    elif mood_terakhir in ["Stres", "Kewalahan"]:

        print("Kamu mungkin sedang menghadapi banyak tekanan atau beban pikiran.")
        print("Cobalah menyelesaikan sesuatu secara perlahan dan bertahap.")
        print()
        print("- 📌 Pecah tugas besar menjadi langkah kecil.")
        print("- 😴 Luangkan waktu untuk beristirahat.")
        print("- 💬 Ceritakan perasaanmu kepada orang yang dipercaya.")


    elif mood_terakhir in ["Sedih", "Kecewa", "Kesepian"]:

        print("Terlihat bahwa kamu sedang mengalami emosi yang cukup berat.")
        print("Berikan waktu untuk memahami perasaanmu dan jangan terlalu keras pada diri sendiri.")
        print()
        print("- 💙 Lakukan aktivitas yang kamu sukai.")
        print("- 🎵 Dengarkan musik atau lakukan kegiatan yang membuat nyaman.")
        print("- 🤝 Cari dukungan dari orang terdekat jika diperlukan.")


    elif mood_terakhir == "Marah":

        print("Kamu mungkin sedang merasakan emosi yang kuat.")
        print("Cobalah memberi jeda sebelum mengambil keputusan atau bereaksi.")
        print()
        print("- 🌬️ Tarik napas dalam secara perlahan.")
        print("- 🚶 Lakukan aktivitas fisik ringan.")
        print("- 🧘 Berikan waktu untuk menenangkan diri.")


    elif mood_terakhir in ["Lelah", "Bosan"]:

        print("Kamu mungkin sedang membutuhkan waktu untuk memulihkan energi.")
        print("Istirahat juga merupakan bagian penting dari menjaga kesehatan mental.")
        print()
        print("- 😴 Tidur dan istirahat yang cukup.")
        print("- 🚶 Lakukan peregangan atau jalan santai.")
        print("- 🎨 Luangkan waktu untuk hobi.")


    elif mood_terakhir in ["Senang", "Bahagia", "Sangat Bahagia"]:

        print("Kondisi emosimu terlihat positif.")
        print("Pertahankan kebiasaan baik yang membantu menjaga suasana hatimu.")
        print()
        print("- 😊 Nikmati aktivitas yang membuatmu bahagia.")
        print("- 🌱 Tetap jaga keseimbangan aktivitas dan istirahat.")
        print("- ⭐ Hargai hal-hal positif dalam keseharianmu.")


    else:

        print("Tetap perhatikan kondisi emosimu hari ini.")
        print("Kenali apa yang kamu rasakan dan lakukan hal yang membuatmu nyaman.")
        print()
        print("- 🌿 Luangkan waktu untuk diri sendiri.")
        print("- 💪 Pertahankan kebiasaan positif.")
        print("- 😊 Jangan lupa menjaga kesehatan fisik dan mental.")


    print("=" * 50)


# ==========================
# MOTIVASI HARI INI
# ==========================

def tampilkan_feedback():

    import random

    motivasi = [
        "✨ Kamu sudah melakukan yang terbaik hari ini. Tetap hargai prosesmu.",
        "🌱 Tidak apa-apa berjalan perlahan, yang penting kamu terus bergerak.",
        "💙 Setiap hari adalah kesempatan baru untuk menjadi lebih baik.",
        "😊 Jangan lupa memberi waktu untuk dirimu sendiri.",
        "🌻 Hal kecil yang kamu lakukan hari ini tetap memiliki arti."
    ]

    print("\n" + "=" * 50)
    print("          MOTIVASI HARI INI")
    print("=" * 50)

    print(random.choice(motivasi))

    print("=" * 50)


def edit_mood():

    print("\n=== EDIT MOOD ===")

    id = int(input("Masukkan ID mood yang ingin diedit: "))

    mood = input("Mood baru: ")
    skor = int(input("Skor baru (1-10): "))

    update_entry(id, mood, skor)

    print("✅ Data mood berhasil diperbarui!")



def hapus_mood():

    print("\n=== HAPUS MOOD ===")

    id = int(input("Masukkan ID mood yang ingin dihapus: "))

    delete_entry(id)

    print("🗑️ Data mood berhasil dihapus!")


def impor_json_ke_db():

    print("\n=== IMPORT JSON ===")

    nama_file = input("Masukkan nama file JSON (tekan Enter untuk data/mood_history.json): ").strip()

    if not nama_file:
        nama_file = "data/mood_history.json"

    if not os.path.exists(nama_file):
        print(f"❌ File '{nama_file}' tidak ditemukan.")
        return

    import_json(nama_file)
    print("✅ Data berhasil diimpor ke database!")


def main():

    # Membuat database SQLite jika belum ada
    create_database()

    # Menampilkan halaman awal
    if not welcome():
        return

    while True:

        tampilkan_menu()

        pilihan = input("Pilih menu (1-11): ")

        if pilihan == "1":
            input_mood()

        elif pilihan == "2":
            lihat_riwayat()

        elif pilihan == "3":
            analisis_mood()

        elif pilihan == "4":
            cek_stres()

        elif pilihan == "5":
            tampilkan_relief()

        elif pilihan == "6":
            tampilkan_feedback()

        elif pilihan == "7":
            edit_mood()

        elif pilihan == "8":
            hapus_mood()

        elif pilihan == "9":
            export_json()

        elif pilihan == "10":
            impor_json_ke_db()

        elif pilihan == "11":
            print("\nTerima kasih telah menggunakan PsyMood 😊")
            print("Semoga harimu menyenangkan!")
            break

        else:
            print("\n❌ Pilihan tidak valid.")

        input("\nTekan Enter untuk kembali ke menu...")


if __name__ == "__main__":
    main()