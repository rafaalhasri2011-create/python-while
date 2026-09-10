print ("=======PROGRAM GANJIL=======")
awal = int(input("Ketik nilai awal anda = "))
selisih =  int(input("Ketik nilai selisihnya = "))
akhir =  int(input("Ketik nilai akhir anda = "))

while awal <= akhir:
    if awal % 2 == 1:
        print (awal)
    awal += selisih 
