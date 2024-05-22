def tampildata (listdata):
  for x, y in listdata.items():
    print("NPM : " +str(x)+ " nama : "+y['nama']+" angkatan : "+str(y['angkatan'])) 
    
mahasiswa = {
  1 :{ 
    "nama" : "jihan",
    "angkatan" : 2023
  },
  2 :{ 
    "nama" : "devina",
    "angkatan" : 2023
},
  3 :{ 
    "nama" : "rosy",
    "angkatan" : 2023
}
}
tampildata (mahasiswa)


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
        npm = input("inputkan NPM: ")
        nama = input("inputkan nama: ")
        angkatan = input("angkatan: ")
        mahasiswa[npm] = {"nama" : nama, "angkatan" : angkatan}
        print('\n')
        tampildata (mahasiswa)

# Area hapus data
    elif pilihan == 2:
       npm = input("hapus data by NPM  : ")

       mahasiswa.pop(int(npm))
       tampildata(mahasiswa)

# Area update data
    elif pilihan == 3:
       npm = input("masukkan npm yang ingin di update:  ")
       if npm in mahasiswa:
        nama = input("masukkan nama baru: ")
        angkatan = input("masukkan angkatan baru: ")
        mahasiswa[npm] = {"nama: ": nama, "angkatan: ": int(angkatan)}
      
        print("data berhasil di update.")