mahasiswa_list = [
    {
        'NPM': 1,
        'Nama': 'Emil',
        'Angkatan': 2004,
        'Alamat': 'Lampung'
    },
    {
        'NPM': 2,
        'Nama': 'Tobias',
        'Angkatan': 2007,
        'Alamat': 'Jakarta'
    },
    {
        'NPM': 3,
        'Nama': 'Linus',
        'Angkatan': 2011,
        'Alamat': 'Palembang'
    }
]

def tampil_data_mahasiswa():
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
    else:
        for mhs in mahasiswa_list:
            print(f"NPM: {mhs['NPM']}, Nama: {mhs['Nama']}, Angkatan: {mhs['Angkatan']}, Alamat: {mhs['Alamat']}")

def tambah_data_mahasiswa():
    npm = int(input("Masukkan NPM baru: "))
    nama = input("Masukkan Nama: ")
    angkatan = int(input("Masukkan Angkatan: "))
    alamat = input("Masukkan Alamat: ")

    mahasiswa_list.append({
        'NPM': npm,
        'Nama': nama,
        'Angkatan': angkatan,
        'Alamat': alamat
    })

    print("Data mahasiswa berhasil ditambahkan.")

def hapus_data_mahasiswa():
    npm = int(input("Masukkan NPM yang ingin dihapus: "))

    for i, mhs in enumerate(mahasiswa_list):
        if mhs['NPM'] == npm:
            del mahasiswa_list[i]
            print("Data mahasiswa berhasil dihapus.")
            return
        
    print("Data mahasiswa dengan NPM tersebut tidak ditemukan.")

def update_data_mahasiswa():
    npm = int(input("Masukkan NPM yang ingin diupdate: "))

    for mhs in mahasiswa_list:
        if mhs['NPM'] == npm:
            nama = input("Masukkan Nama baru (kosongkan jika tidak diubah): ")
            angkatan = input("Masukkan Angkatan baru (kosongkan jika tidak diubah): ")
            alamat = input("Masukkan Alamat baru (kosongkan jika tidak diubah): ")

            if nama:
                mhs['Nama'] = nama
            if angkatan:
                mhs['Angkatan'] = int(angkatan)
            if alamat:
                mhs['Alamat'] = alamat

            print("Data mahasiswa berhasil diupdate.")
            return

    print("Data mahasiswa dengan NPM tersebut tidak ditemukan.")

print("Data Mahasiswa:")
tampil_data_mahasiswa()

while True:
    print("\nPilih Menu:")
    print("1. Tambah Data Baru")
    print("2. Hapus Data by NPM")
    print("3. Update Data by NPM")
    print("4. Exit")

    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        tambah_data_mahasiswa()
        tampil_data_mahasiswa()  
    elif pilihan == 2:
        hapus_data_mahasiswa()
        tampil_data_mahasiswa()  
    elif pilihan == 3:
        update_data_mahasiswa()
        tampil_data_mahasiswa() 
    elif pilihan == 4:
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")