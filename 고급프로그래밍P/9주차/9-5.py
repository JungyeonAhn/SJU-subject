m = input("문자열 입력 : ")
fw = open("python.txt", "w")
fw.write(m)
n=int(input("n 입력 : "))

fw = open("python.txt", "r")
fw.seek(n)
s=fw.read(1)
print(n,'bytes 떨어진 위치에 있는 문자 :',s)
