#JUDUL
print("TUGAS 2")
print("Algoritma dan Logika Informatika")

print() #agar ada spasi antara judul dengan data diri

#DATA DIRI
#mencetaka nama
print("DATA DIRI")
print("Nama : I Wayan Wahyudi")
#mencetak NIM
print("Nim  : 2401010425")
#mencetak Prodi(Kelas)
print("Prodi: IF-KAB(K)")

print() #agar ada spasi antara data diri dengan tugas

#JUDUL TUGAS
print("KONVERSI SATUAN m -> cm")
print()
print("Masukan Jumlah yang mau anda coba konversi")

#INPUT
#meminta pengguna memasukkan nilai dalam meter
meter = float(input("Masukkan nilai dalam meter: "))

#PROSES
#mengonversi meter ke sentimeter (1 meter = 100 sentimeter)
centimeter = meter * 100

#OUTPUT
#menampilkan hasil konversi
print(f"{meter} meter sama dengan {centimeter} sentimeter.")
