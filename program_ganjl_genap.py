print ("=======PROGRAM GENAP=======")
awal = int(input("Ketik nilai awal anda = "))
selisih =  int(input("Ketik nilai selisihnya = "))
akhir =  int(input("Ketik nilai akhir anda = "))

while awal <= akhir:
    if awal % 2 == 0:
        print (awal)
    awal += selisih 
