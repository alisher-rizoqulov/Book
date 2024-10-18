class BOOK:
    def __init__(self, id, name, author, count, price):
        self.id = id
        self.name = name
        self.author = author
        self.count = count
        self.price = price

    def writee(self, ptr):
        ptr.write(f"{self.id},{self.name},{self.author},{self.count},{self.price}\n")

  
    def read():
        print("Mavjud kitoblar:")
        with open("yozish.txt", "r") as ptr:
            print(ptr.read())

    def countt(self, idd):
        with open("yozish.txt", "r") as ptr:
            lines = ptr.readlines()

        updated_lines = []
        lampochka = False
        for line in lines:
            data = line.strip().split(',')
            if int(data[0]) == idd:
                data[3] = str(int(data[3]) - 1)  
                print(f"Kitob ID {idd} uchun miqdor 1 donaga kamaytirildi!")
                lampochka = True
            updated_lines.append(','.join(data) + '\n')

        if lampochka:
            with open("yozish.txt", "w") as ptr:
                ptr.writelines(updated_lines)
                
        else:
            print("Kitob topilmadi.")

    def ochirish(self, idd):
        with open("yozish.txt", "r") as ptr:
            lines = ptr.readlines()

        updated_lines = []
        lampochka = False
        for line in lines:
            data = line.strip().split(',')
            if int(data[0]) != idd:
                updated_lines.append(line) 
            else:
                lampochka = True

        if lampochka:
            with open("yozish.txt", "w") as ptr:
                ptr.writelines(updated_lines)
            print(f"Kitob ID {idd} o'chirildi!")
        else:
            print("Kitob topilmadi.")
with open("yozish.txt", "a") as ptr:
    for i in range(1, int(input("Filega nechta malumot kiritasiz: ")) + 1):
        print(f"{i} - Kitob:")
        x = BOOK(int(input("ID: ")), input("Nomi: "), input("Muallif: "), int(input("Nechta: ")), int(input("Narxi: ")))
        x.writee(ptr)
BOOK.read()
print("Filedagi kitob sonini ID bo'yicha [0] --> ochirish || [1] --> Countini 1 taga kamaytirish")
x = BOOK(0, "", "", 0, 0)  
if int(input(":")):
    a_id = int(input("Qaysi ID bo'yicha countini kamaytiramiz? "))
    x.countt(a_id)
else:
    b_id = int(input("Qaysi ID bo'yicha o'chiramiz? "))
    x.ochirish(b_id)
