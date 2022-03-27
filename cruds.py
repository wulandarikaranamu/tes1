    #ONLINE SHOP
barang = []
pilihan = 0
while pilihan != 7 :
    print(''' menu :
    1. menambah barang
    2. menghapus barang
    3. mengedit barang
    4. menampilkan semua barang
    5. mencari barang
    6. mencari index di barang tertentu
    7. exit''')
    print("\t========SELAMAT BERBELANJA========")
    
    pilihan = int(input("silahkan meimilih menu :"))
    if pilihan == 1 :
        while True :
            goods = input("pilih barang anda :")
            print(goods,barang.append(goods),"barang berhasil ditambahkan!")

            berhenti = input("masukkan perintah t selain itu silahkan lanjut memilih barang :")
            if berhenti == "t" :
                break
            
    elif pilihan == 2 :
        while True :
            goods = input("pilih barang yang ingin dihapus :")
            print(goods,barang.remove(goods),"berang berhasil dihapus!")
            
            
            berhenti = input("masukkan perintah t selain itu silahkan lanjut menghapus barang :")
            if berhenti == "t" :
                break
            
    elif pilihan == 3 :
        while True :
            edit = int(input("silahkan edit barang anda :"))
            if edit > len(barang):
                print("index barang tidak tersedia!")
                
            else:
                barang [edit] = input("masukkan barang yang ingin diganti :")
                berhenti = input("masukkan perintah t selain itu lanjut mengedit barang :")
                if berhenti == "t" :
                    break
                
    elif pilihan == 4 :
        for key in range(len(barang)):
            print(key)
            
    elif pilihan == 5 :
        cari = input("silahkan masukkan nama barang yang dicari :")
        for key in range(len(barang)):
            if [key] == cari :
                print("nama barang yang anda cari ada dalam daftar barang")
            else:
                print("nama barang yang anda cari tidak ada dalam daftar barang")
                
    elif pilihan == 6 :
        brg = input("silahkan pilih barang yang indexnya ingin ditampilkan :")
        if brg in barang :
            print(f"{brg} berada pada index ke-{brg.index(brg)}")
        else:
            print("index barang tidak ditemukan!")

            
print(barang)        