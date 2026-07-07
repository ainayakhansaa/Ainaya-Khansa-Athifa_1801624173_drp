from tools import *

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
            print("\nPilihan tidak valid. Silakan coba lagi.")


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
    print("7. 🚪 Keluar")
    print("=" * 55)


def main():

    welcome()

    while True:

        tampilkan_menu()

        pilihan = input("Pilih menu (1-7): ")

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
            print("\nTerima kasih telah menggunakan PsyMood 😊")
            print("Semoga harimu menyenangkan!")
            break

        else:
            print("\n❌ Pilihan tidak valid.")

        input("\nTekan Enter untuk kembali ke menu...")


if __name__ == "__main__":
    main()