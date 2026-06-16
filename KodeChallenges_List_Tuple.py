#challenge 1
data=[4,7,2,9,1]
print(f"Jumlah elemen = {len(data)}")
angka=0
for i in data:
	angka+=i
print(f"Jumlah angka = {angka}")
data.sort()
print(f"terbesar = {data[-1]}")
print(f"terkecil = {data[0]}")

#challenge 2
#membalik list
angka=[3,4,5,2,1]
temp1=angka[0]
angka[0]=angka[4]
angka[4]=temp1
temp2=angka[1]
angka[1]=angka[3]
angka[3]=temp2
print(angka)
#more high
for i in range(2):
	temp=angka[i]
	angka[i]=angka[4-i]
	angka[4-i]=temp
print(angka)

#challenge 3
#menghapus duplikat
angka=[1,2,7,4,4,6,8,7,8,8,9]
new_angka=[]
for i in angka:
	if i not in new_angka:
		new_angka.append(i)
print(new_angka)

#challenge 4
#memisahkan genap dan ganjil
angka=[3,8,1,10,5,6,7,12]
ganjil=[]
genap=[]
for i in angka:
	if i%2!=0:
		ganjil.append(i)
	else:
		genap.append(i)
print(ganjil)
print(genap)

#challenge 5
#frekuensi elemen muncul
data=[1,2,1,3,2,1,4]
new_data=[]
for i in data:
	if i not in new_data:
		new_data.append(i)
for j in new_data:
	count=0
	for k in data:
		if k==j:
			count+=1
print(f"{j} -> {count} kali")

#challenge 6
#rotasi list
data=[1,2,3,4,5]
#manually
temp=data[-1]
data[4]=data[3]
data[3]=data[2]
data[2]=data[1]
data[1]=data[0]
data[0]=temp
print(data)
#auto
temp=data[-1]
for i in range(len(data)-1):
	data[len(data)-i-1]=data[len(data)-i-2]
data[0]=temp
print(data)

#challenge 7
#menjumlahkan isi tuple
data=10,20,30,40
sum=0
i=0
while i<len(data):
	sum+=data[i]
	i+=1
print(sum)

#challenge 8
#tukar isi tuple
#packing
a=1,2
b=3,4
a,b=b,a
print(f"a = {a}")
print(f"b = {b}")

#challenge 9
#mencari nilai terbesar dalam nested tuple
data=((10,5),(7,30),(4,9))
temp=0
for i in data:
	for j in i:
		temp=max(j,temp)
print(temp)

#challenge 10
siswa=[("Andi",80),("Budi",75),("Citra",90),("Dina",60)]
#nilai tertinggi dan terendah
maks=0
minn=100
siswa_nilai_tertinggi=""
siswa_nilai_terendah=""
for i in siswa:
	maks=max(maks,i[1])
	minn=min(minn,i[1])
print(minn)
for j in range(len(siswa)):
	if maks in siswa[j]:
		index_lokasi=j
		siswa_nilai_tertinggi=siswa[j][0]
	if minn in siswa[j]:
		index_lokasi=j
		siswa_nilai_terendah=siswa[j][0]
print(f"Nilai tertinggi = {maks} oleh {siswa_nilai_tertinggi}")
print(f"Nilai terendah = {minn} oleh {siswa_nilai_terendah}")
#rata-rata
nilai=[siswa[i][1] for i in range(len(siswa))]
print(nilai)
sum=0
for i in nilai:
	sum+=i
av=sum/len(siswa)
print(f"Rata-rata nilai = {av}")
#siswa yang nilainya di atas dan di bawah rata-rata
high=[]
low=[]
for i in range(len(siswa)):
	if siswa[i][1]>av:
		high.append(siswa[i][0])
	elif siswa[i][1]<av:
		low.append(siswa[i][0])
print(f"Siswa yang di atas rata-rata:")
for x in high:
	print(x)
print(f"Siswa yang di bawah rata-rata:")
for y in low:
	print(y)
#ranking siswa
nilai.sort()
nilai.reverse()
print(nilai[0])
for i in nilai:
	for j in siswa:
		if i in j:
			print(f"{j[0]} - {i}")


#challenge 12
#matriks dengan list bersarang
matriks=[[1,2,3],[4,5,6],[7,8,9]]
#jumlah semua angka
sum=0
for i in range(len(matriks)):
	for j in matriks[i]:
		sum+=j
print(f"Jumlah semua angka = {sum}")
#jumlah setiap baris
for i in range(len(matriks)):
	sum=0
	for j in range(len(matriks[i])):
		sum+=matriks[i][j]
	print(f"Jumlah baris {i+1} = {sum}")
#jumlah setiap kolom
x=len(matriks[0])
for i in range(x):
	sum=0
	for j in range(len(matriks)):
		sum+=matriks[j][i]
	print(f"Jumlah kolom {i+1} = {sum}")
#menampilkan diagonal utama
diag_utama=[]
for i in range(len(matriks)):
	for j in range(len(matriks[i])):
		if i==j:
			diag_utama.append(matriks[i][j])
print(f"Diagonal Utama = {diag_utama}")


#challenge BONUS
buku=[("Laskar Pelangi","Andrea Hirata"),("Bumi","Tere Liye")]
menu=[
	"Tambah buku",
	"Hapus buku",
	"Cari buku",
	"Tampilkan semua buku",
	"Keluar"
]
#fungsi
def display():
	for i in range(len(buku)):
		print(f"{i+1}. {buku[i][0]} - {buku[i][1]}")
def delete(n):
	buku.pop(n-1)
def search(arg):
	for i in range(len(buku)):
		if arg in buku[i]:
			print(buku[i])

print("PROGRAM MANAJEMEN BUKU")
while True:
	for i in range(len(menu)):
		print(f"{i+1}. {menu[i]}")
	pilih=int(input("Pilihan (1-5): "))
	if pilih==1:
		print("++ Tambah Buku ++")
		judul=input("Masukkan judul buku: ")
		penulis=input("Masukkan nama penulis: ")
		buku.append((judul,penulis))
	elif pilih==2:
		print("++ Hapus Buku ++")
		display()
		indeks=int(input("Buku mana yang ingin dihapus (angka): "))
		delete(indeks)
	elif pilih==3:
		print("++ Cari Buku ++")
		hint=input("Masukkan petunjuk (judul/pengarang): ")
		search(hint)
	elif pilih==4:
		display()
	elif pilih==5:
		break

	print("====================================================")
