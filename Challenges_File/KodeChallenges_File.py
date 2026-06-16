# Manajemen Buku

def display():
	print("\nList of books:")
	with open("buku.txt","r",encoding="utf-8") as b:
		if b.read()=="":
			print("[ kosong ]")
			print("# Format: Title - Author")
		else:
			b.seek(0)
			content=b.readlines()
			for i in range(len(content)):
				print(f"{i+1}. {content[i]}")

def Add():
	print("\nFormat -> Title - Author")
	n1=input("Title: ")
	n2=input("Author: ")
	with open("buku.txt","a+",encoding="utf-8") as b:
		b.write(f"{n1}, {n2}\n")
		b.seek(0)
		print(b.read())

def edit(arg1,arg2):
	with open("buku.txt","r",encoding="utf-8") as b:
		text=b.read()
	new_text=text.replace(arg1,arg2)
	with open("buku.txt","w",encoding="utf-8") as b:
		b.write(new_text)

def search(arg):
	with open("buku.txt","r") as b:
		for line in b:
			if arg.lower() in line.lower():
				print(line,end="")
			

def delete(x):
	if isinstance(x,int):
		with open("buku.txt","r") as b:
			content=b.readlines()
			content.pop(x-1)
		with open("buku.txt","w") as b:
			b.write(" ".join(content))
	else:
		edit(x,"")



print("\n=======================================")
print("*** WELCOME TO THE BOOK MANAGEMENT ***")
print("=======================================\n")

display()

menu={
	1:"Display",
	2:"Add",
	3:"Edit",
	4:"Search",
	5:"Delete",
	6:"Quit"
}

print("\nAction:")
for i in range(len(menu)):
	print(f"{i+1}. {menu[i+1]}")
	

while True:
	print("---------------------")
	n=int(input("So, what's your act (1-4): "))
	if n==1:
		display()
	elif n==2:
		Add()
	elif n==3:
		display()
		n1=input("++ which words you want to change: ")
		n2=input("++ change with: ")
		edit(n1,n2)
		print("-> Data edited!\n")
		display()
		print("\n")
	elif n==4:
		n1=input("++ What words you want to find: ")
		search(n1)
	elif n==5:
		display()
		n1=input("++ Delete list (l) or words (w): ")
		if n1=='l' or n1=='L':
			n2=int(input("- Enter index of the list: "))
			delete(n2)
			display()
		elif n1=='w' or n1=='W':
			n2=input("- Which words you want to delete: ")
			delete(n2)
			display()
	elif n==6:
		break
