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

print('\n')
npm = input("inputkan NPM: ")
nama = input("inputkan nama: ")
angkatan = input("angkatan: ")

dataupdate = {
      npm:{
        "nama" : nama,
        "angkatan" : angkatan
      }
}
mahasiswa.update(dataupdate)

tampildata (mahasiswa)

print('\n')
idnpm = input("hapus data by NPM: ")

mahasiswa.pop(int(idnpm))
tampildata (mahasiswa)