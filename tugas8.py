print("---LAYOUT PAPAN CATUR---")
for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("🔲", end="")
        else:
            print("🔳", end="")
    print()