# Tugas PBO 1
# Membuat Fungsi untuk merubah dan menambah
# Nama  : Andhi Prasetyo
# NIM   : C20010004
# Prodi : Teknik Informatika
# UNIVERSITAS BOYOLALI (UBY)

class Tugassatu:
    
    #construktor
    def __init__(self, InputNama, InputNim, 
    InputNilai, InputProdi, InputAlamat):
        self.nama   = InputNama
        self.NIM    = InputNim
        self.nilai  = InputNilai
        self.prodi  = InputProdi
        self.alamat = InputAlamat     

    #ini untuk menampilkan function
    def tampilkanawal(self): 
        print("\n")
        print("========================================")
        print("DATA SEBELUM DIUBAH")
        print("========================================")
        print("Nama Mahasiswa\t: " + self.nama)
        print("NIM Mahasiswa\t: " + self.NIM)
        print("Nilai Mahasiswa\t: " + str(self.nilai))
        print("Prodi Mahasiswa\t: " + self.prodi)
        print("Alamat\t\t: " + self.alamat)
        print("========================================")
        print("\n")

    def tampilkanperubahanmanual(self):
        #print("\n")
        print("========================================")
        print("DATA SETELAH DIUBAH MANUAL")
        print("========================================")
        print("Nama Mahasiswa\t: " + self.nama)
        print("NIM Mahasiswa\t: " + self.NIM)
        print("Nilai Mahasiswa\t: " + str(self.nilai))
        print("Prodi Mahasiswa\t: " + self.prodi)
        print("Alamat\t\t: " + self.alamat)
        print("========================================")
        print("\n")

    def tampilkanperubahanlangsung(self):
        #print("\n")
        print("========================================")
        print("DATA SETELAH DIUBAH DI FUNCTION")
        print("========================================")
        print("Nama Mahasiswa\t: " + self.nama[:0] + "Epsilon")
        print("NIM Mahasiswa\t: " + self.NIM[:0] + "C11111")
        print("Nilai Mahasiswa\t: " + str(self.nilai+15))
        print("Prodi Mahasiswa\t: " + self.prodi[:0] + "Peternakan")
        print("Alamat\t\t: " + self.alamat[:0] + "Kartasura")
        print("========================================")
        print("\n")

mahasiswa1 = Tugassatu("Alpha", "C12345", 90, "Komunikasi", "Boyolali") 
mahasiswa2 = Tugassatu("Beta", "C12346", 91, "Ekonomi", "Klaten") 
mahasiswa3 = Tugassatu("Gamma", "C12347", 95, "Pertanian", "Ampel")

mahasiswa1.tampilkanawal()

mahasiswa1 = Tugassatu("Delta", "C54321", 80, "Manajemen", "Surakarta") 
mahasiswa1.tampilkanperubahanmanual()

mahasiswa1.tampilkanperubahanlangsung()



