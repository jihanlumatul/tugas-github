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

for x, y in mahasiswa.items():
  print("NPM : " +str(x)+ " nama : "+y['nama']+" angkatan : "+str(y['angkatan'])) 
