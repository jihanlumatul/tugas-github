def tampildata(listdata):
    for x, y in listdata.items():
        print("NPM : " + str(x) + " nama : " + y['nama'] + " angkatan : " + str(y['angkatan']))

mahasiswa = {
    "1": {
        "nama": "jihan",
        "angkatan": 2023
    },
    "2": {
        "nama": "devina",
        "angkatan": 2023
    },
    "3": {
        "nama": "rosy",
        "angkatan": 2023
    }
}

tampildata(mahasiswa)

while True:
    print('\n')
    print("==============================")
    print("1. Tambah data baru")
    print("2. Hapus data By NPM")
    print("3. Update data by NPM")
    print("4. Exit")
    print("===============================")
    pilihan = int(input("Masukkan pilihan anda (1-4): "))

    # Area penambahan data
    if pilihan == 1:
        npm = input("Inputkan NPM: ")
        nama = input("Inputkan nama: ")
        angkatan = input("Angkatan: ")
        mahasiswa[npm] = {"nama": nama, "angkatan": int(angkatan)}
        print('\n')
        tampildata(mahasiswa)

    # Area hapus data
    elif pilihan == 2:
        npm = input("Hapus data by NPM: ")
        if npm in mahasiswa:
            mahasiswa.pop(npm)
            print("\nData berhasil dihapus.")
        else:
            print("\nNPM tidak ditemukan.")
        tampildata(mahasiswa)

    # Area update data
    elif pilihan == 3:
        npm = input("Masukkan NPM yang ingin diupdate: ")
        if npm in mahasiswa:
            nama = input("Masukkan nama baru: ")
            angkatan = input("Masukkan angkatan baru: ")
            mahasiswa[npm] = {"nama": nama, "angkatan": int(angkatan)}
            print("\nData berhasil diupdate.")
        else:
            print("\nNPM tidak ditemukan.")
        tampildata(mahasiswa)

    # Exit
    elif pilihan == 4:
        break
