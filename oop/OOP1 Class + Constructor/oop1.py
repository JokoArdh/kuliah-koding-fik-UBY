#nama class diawali huruf besar dan tanpa karakter
class Mahasiswa:
    pass #belum digunakan pakai pass

mahasiswa1 = Mahasiswa() #objek1
mahasiswa2 = Mahasiswa() #objek2

mahasiswa1.nama = "Alpha" #artribut
mahasiswa1.NIM = "C0012022"
mahasiswa1.nilai = 70

mahasiswa2.nama = "Beta" #artribut
mahasiswa2.NIM = "C0022022"
mahasiswa2.nilai = 85

print("Nama Mahasiswa 1\t: " + mahasiswa1.nama)
print("NIM Mahasiswa 1\t\t: " + mahasiswa1.NIM)
print("Nilai Mahasiswa 1\t: " + str(mahasiswa1.nilai))