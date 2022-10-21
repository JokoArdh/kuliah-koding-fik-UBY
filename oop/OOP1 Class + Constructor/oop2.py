#nama class diawali huruf besar dan tanpa karakter
class Mahasiswa:
    #pass #belum digunakan pakai pass
    def tampil(self): #ini untuk menampilkan function
        print("Nama Mahasiswa 1\t: " + mahasiswa1.nama)
        print("NIM Mahasiswa 1\t\t: " + mahasiswa1.NIM)
        print("Nilai Mahasiswa 1\t: " + str(mahasiswa1.nilai))

mahasiswa1 = Mahasiswa() #objek1
mahasiswa2 = Mahasiswa() #objek2

mahasiswa1.nama = "Alpha" #artribut / property
mahasiswa1.NIM = "C0012022"
mahasiswa1.nilai = 70

mahasiswa2.nama = "Beta" #artribut
mahasiswa2.NIM = "C0022022"
mahasiswa2.nilai = 85

mahasiswa1.tampil()

#properti yang dimiliki class = class variabel => statis
#fungsi = perintah yang dapat dimiliki objek
