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

        Toko_Buku.no_buku += 1 # Sudah bisa jalan
        Toko_Buku.tampil(self)
        Toko_Buku.total_harga += inputJumlah*inputHarga
        print("Harga Total = ", Toko_Buku.hargaTotal(self))

    def tampil(self): # Method Tanpa Return Argumen
        print(30*"=")
        print("Buku Nomor       : ", Toko_Buku.no_buku)
        print("Judul Buku       : ", self.judul)
        print("Jumlah Buku      : ", self.jumlah)
        print("Harga Buku       : ", self.harga)
        # Total Harga per Judul Buku
        print("Total Harg@      : ", Toko_Buku.total_harga)
        
    def diskon(self, diskon_harga): # Method dengan argumen
        self.harga -= diskon_harga
        Toko_Buku.total_harga -= diskon_harga
        print(30*"=")
        print("Diskon           : ", diskon_harga)

    def hargaTotal(self): 
        # Method tanpa argumen dengan return
        return Toko_Buku.total_harga    


buku1 = Toko_Buku("Laskar Pelangi", 2, 55000)
buku2 = Toko_Buku("Harry Potter", 4, 35000)
buku3 = Toko_Buku("Angkasa Biru", 5, 15000)
buku4 = Toko_Buku("Laut Hitam", 15, 20000)

print(30*"=")
print("Sebelum Diskon   : ", Toko_Buku.total_harga) 
# total harga semua setelah dikurangi diskon

#buku1.diskon(5555)

print(30*"=")
print("Total Harga      : ", Toko_Buku.total_harga) 
# total harga semua setelah dikurangi diskon