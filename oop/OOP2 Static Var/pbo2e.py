class Toko_Buah:
    # static variabel
    no_buah = 0
    total_harga = 0 # class variabel

    def __init__(self, 
        inputNama, 
        inputJumlah,
        inputPotongan,
        inputHarga
        ):
        
        self.nama       = inputNama
        self.jumlah     = inputJumlah # instance variabel / objek
        self.potongan   = inputPotongan
        self.harga      = inputHarga

        Toko_Buah.no_buah += 1 # belum bisa jalan
        Toko_Buah.tampil(self)
        Toko_Buah.total_harga += inputJumlah*inputHarga

    def tampil(self): # Method Tanpa Return Argumen
        print(30*"=")
        print("Buah Nomor       : ", Toko_Buah.no_buah)
        print("Nama Buah        : ", self.nama)
        print("Jumlah Buah      : ", self.jumlah)
        print("Harga Buah       : ", self.harga)
        # Total Harga per Judul Buku
        print("Total Harg@      : ", Toko_Buah.total_harga)
        
    def diskon(self, diskon_harga): # Method dengan argumen
        Toko_Buku.total_harga -= diskon_harga
        print(30*"=")
        print("Diskon           : ", diskon_harga)

    def hargaTotal(self):
        return Toko_Buku.total_harga    


buku1 = Toko_Buku("Laskar Pelangi", 2, 50000)
buku2 = Toko_Buku("Harry Potter", 4, 25000)
buku3 = Toko_Buku("Mewarnai", 5, 10000)
buku4 = Toko_Buku("Menggambar", 15, 5000)

print(30*"=")
print("Sebelum Diskon   : ", Toko_Buku.total_harga) 
# total harga semua setelah dikurangi diskon

buku1.diskon(50000)

print(30*"=")
print("Total Harga      : ", Toko_Buku.total_harga) 
# total harga semua setelah dikurangi diskon