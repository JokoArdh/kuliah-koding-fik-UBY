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
        Toko_Buku.sebelumDiskon = inputJumlah*inputHarga
        Toko_Buku.tampil(self)
        
        #print("Harga Total      : ", Toko_Buku.hargaTotal(self))

    def tampil(self): # Method Tanpa Return Argumen
        print(30*"=")
        print("Buku Nomor       : ", Toko_Buku.no_buku)
        print("Judul Buku       : ", self.judul)
        print("Jumlah Buku      : ", self.jumlah)
        print("Harga Buku       : ", self.harga)
        print("Sebelum Diskon   : ", self.sebelumDiskon)
        
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