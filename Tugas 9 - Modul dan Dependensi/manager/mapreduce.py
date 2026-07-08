from manager.database_manager import load_history
def map_reduce_mood():
    history = load_history()
    if not history:
        print("\nBelum ada data mood untuk dianalisis.")
        return

    # Map
    mapped =[]
    for item in history:
        mapped.append((item["mood"], 1))

    # Reduce
    hasil = {}
    for mood, jumlah in mapped:
        if mood in hasil:
            hasil[mood] += jumlah
        else:
            hasil[mood] = jumlah
    
    print("\n" + "=" * 50)
    print("           HASIL MAP REDUCE MOOD")
    for mood, jumlah in hasil.items():
        print(f"{mood}: {jumlah}")