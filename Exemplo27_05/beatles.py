import time
# 1

beatles = []

# 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)

# 3

for i in range(2):
    beatlesSTR = str(input("Adicione os outros membros da banda 'Stu Sutcliffe e Pete Best' à lista: "))
    beatles.append(beatlesSTR)
    
print(beatles)

# 4

del(beatles[-1])
del(beatles[-1])

print(beatles)
#5

beatles.insert(0, "Ringo Starr")
print(beatles)

time.sleep(3)