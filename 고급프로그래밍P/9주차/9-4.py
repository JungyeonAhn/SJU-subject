fw = open("menu.txt", "w")
print("<메뉴 입력>")
num = int(input("# of menus = "))

for i in range (0,num):
    name=input("메뉴 이름 : ")
    price=input("메뉴 가격 : ")
    fw.write(name+' '+price+'\n')

fw = open("menu.txt", "r")

while True:
    line= fw.readline()
    if not line: break
    print(line,end='')

fw.close()
