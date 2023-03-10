user = [
    {'nama': 'arsene lupin', 'nik': '1234', 'jenis_kelamin': 'male', 'tanggal_lahir': '1902-03-23'},
    {'nama': 'sherlock holmes', 'nik': '4321', 'jenis_kelamin': 'male', 'tanggal_lahir': '1876-08-16'},
    {'nama': 'irene adler', 'nik': '6789', 'jenis_kelamin': 'female', 'tanggal_lahir': '1884-10-07'}
]
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
jenis_kelamin = input("Masukkan Jenis Kelamin:(ex : Pria/Wanita) ")
tanggal_lahir = input("Masukkan tanggal lahir (ex : 2020-01-02): ")

CariNama = input("Masukkan nama yang ingin dicari: ")

found = False

for data in user:
    if data['nama'] == CariNama:
        print("Nama :", data['nama'])
        print("NIK :", data['nik'])
        print("Jenis Kelamin :", data['jenis_kelamin'])
        print("Tanggal Lahir :", data['tanggal_lahir'])
        found = True
        break

if not found:
    print("Data tidak ada")
