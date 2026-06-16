# readline() -> satu baris
# readlines() -> semua baris dalam bentuk list
# read() -> seluruh isi file menjadi satu string

# membaca file (seluruh isi)
with open("test.py","r") as f:
	isi=f.read()
	print(isi)

# membaca file (perbaris)
with open("test.py","r") as f1:
	while True:
		baris=f1.readline()
		if baris=="":
			break
		print(baris)

# membaca file
with open("test.py","r") as f2:
	print(f2.readlines())


# menulis file
with open("test.py","w") as f3:
	f3.write("Nulis apa ya?")

# menulis di bagian akhir
with open("test.py","a") as f4:
	f4.write("\nCerita senja mungkin cocok!")

# membuat file baru
# with open("create.py","x") as f5:
#	f5.write("Mau diisi apa ini?")

# r+
with open("create.py","r+") as f6:
	print(f6.read())
	f6.write("Helo")

# w+
with open("test.py", "w+") as f7:
	f7.write("Isinya tak ganti") # isian lama hilang, diganti ini
	f7.seek(0) # kembali ke awal baris
	print(f7.read())


# a+
with open("create.py", "a+") as f8:
	f8.write("Tambahan di akhir\n")
	f8.seek(0)
	print(f8.read())



# MODE

# w -> write (overwrite)
# x -> create file baru (error jika sudah ada)
# r+ -> read + write
# w+ -> write + read (overwrite)
# a+ -> append + read

# overwrite (w, w+) : isian lama hilang total dan diganti yang baru
# r+ isi lama tidak akan hilang total

