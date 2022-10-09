class Toko_Mobil:
    # static variabel
    no_mobil = 0
    total_harga = 0 # class variabel

    def __init__(self, 
        namaMobil, 
        inputJumlah,
        inputHarga,
        #inputDiskon
        ):
        
        self.judul  = namaMobil
        self.jumlah = inputJumlah # instance variabel / objek
        self.harga  = inputHarga
        #self.potongan = inputDiskon

        Toko_Mobil.no_mobil += 1 
        Toko_Mobil.tampil(self)
        Toko_Mobil.total_harga += inputJumlah*inputHarga
        print("Harga Total      : ", Toko_Mobil.hargaTotal(self))

    def tampil(self): # Method tanpa return tanpa argumen
        print(30*"=")
        print("Mobil ke         : ", Toko_Mobil.no_mobil)
        print("Nama Mobil       : ", self.judul)
        print("Jumlah Mobil     : ", self.jumlah)
        print("Harga Mobil      : ", self.harga)
        #print("Nilai Diskon     : ", 
        #self.potongan*(self.jumlah*self.harga))

    def diskon(self, diskon_harga): # Method dengan argumen
        Toko_Mobil.total_harga -= diskon_harga
        print(30*"=")
        print("Diskon Total     : ", diskon_harga)

    def hargaTotal(self): 
        # Method tanpa argumen dengan return
        return Toko_Mobil.total_harga    


mobil1 = Toko_Mobil("Ferari", 2, 50000)
mobil2 = Toko_Mobil("Lamborghini", 4, 25000)

mobil1.diskon(5000)
mobil2.diskon(2500)

print("Harga Mobil (All): ", Toko_Mobil.total_harga)
print(30*"=")