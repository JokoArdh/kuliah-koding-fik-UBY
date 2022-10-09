class Toko_Buku:
    # static variabel
    no_buku = 0
    total_harga = 0 # class variabel

    def __init__(self, 
        inputJudul, 
        inputJumlah,
        inputHarga
        ):
        
        self.judul  = inputJudul
        self.jumlah = inputJumlah # instance variabel / objek
        self.harga  = inputHarga

        Toko_Buku.no_buku += 1 # belum bisa jalan
        Toko_Buku.total_harga += inputJumlah*inputHarga

    def tampil(self): # Method Tanpa Return Argumen
        print(30*"=")
        print("Buku Nomor   : ", Toko_Buku.no_buku)
        print("Jumlah Buku  : ", self.judul)
        print("Harga Buku   : ", self.jumlah)
        print("Harga Buku   : ", self.harga)
        print("Total Harg@  : ", Toko_Buku.total_harga)
        # Total Harga per Judul Buku

    def diskon(self, diskon_harga): # Method dengan argumen
        Toko_Buku.total_harga -= diskon_harga
        print(30*"=")
        print("Diskon       : ", diskon_harga)

    


buku1 = Toko_Buku("Laskar Pelangi", 2, 50000)
buku2 = Toko_Buku("Harry Potter", 4, 25000)
buku3 = Toko_Buku("Mewarnai", 5, 10000)
buku4 = Toko_Buku("Menggambar", 15, 5000)

buku1.tampil()
buku2.tampil()
buku3.tampil()
buku4.tampil()

buku1.diskon(50000)

print(30*"=")
print("Total Harga  : ", Toko_Buku.total_harga) # total harga semua