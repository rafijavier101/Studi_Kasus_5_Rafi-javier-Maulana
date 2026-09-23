def parkir(jenken, durpar):
    jenis = jenken.lower()
    if jenis == "mobil":
        tj = 5000
    elif jenis == "motor":
        tj = 3000
    else:
        return None
    return tj * durpar
mm = input("Masukkan jenis kendaraan (Mobil/Motor): ")
jm = int(input("Masukkan jam masuk (0-24): "))
jk = int(input("Masukkan jam keluar (0-24): "))
if jk >= jm:
    lama = jk - jm
else:
    lama = (24 - jm) + jk
u = parkir(mm, lama)
print("RINCIAN PARKIR")
print(f"Jenis Kendaraan : {mm}")
print(f"Jam Masuk       : {jm}.00")
print(f"Jam Keluar      : {jk}.00")
print(f"Lama Parkir     : {lama} jam")
print(f"Total Biaya     : Rp{u}")