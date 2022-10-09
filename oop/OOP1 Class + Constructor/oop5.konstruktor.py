#nama class diawali huruf besar dan tanpa karakter
class Mahasiswa:
    
    def __init__(self, InputNama, InputNim, InputNilai):
        #construktor
        self.nama = InputNama
        self.NIM = InputNim
        self.nilai = InputNilai

    def tampilkan(self): #ini untuk menampilkan function
        print("\n")
        print("Nama Mahasiswa\t: " + self.nama)
        print("NIM Mahasiswa\t: " + self.NIM)
        print("Nilai Mahasiswa\t: " + str(self.nilai))
        print("\n")

    def tampilkansemua(self):
        print("")

mahasiswa1 = Mahasiswa("Alpha", "C12345", 90) 
mahasiswa2 = Mahasiswa("Beta", "C12346", 91) 
mahasiswa3 = Mahasiswa("Gamma", "C12347", 95)

mahasiswa1.tampilkan()

#properti yang dimiliki class = class variabel => statis
#fungsi = perintah yang dapat dimiliki objek
