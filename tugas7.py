from datetime import datetime
pilihan = input("Mau ngapain hari ini?(sarapan/kerja):").strip().lower()
if pilihan == "sarapan":
    kulkas = ["telur","ikan","nugget"]
    menu = input("Mau masak apa untuk sarapan?:").strip().lower()
    if menu in kulkas:
        print("Bahan makanan harus dimasak terlebih dahulu")
    else:
        print("Kamu harus membeli bahannya terlebih dahulu")
elif pilihan == "kerja":
    waktu_sekarang = datetime.now()
    jam = waktu_sekarang.hour
    if jam>= 8:
        print("Notifikasi: Anda TERLAMBAT masuk kerja!")
    else:
        print("Notifikasi: Anda BELUM terlambat masuk kerja. Selamat beraktivitas!")
        
