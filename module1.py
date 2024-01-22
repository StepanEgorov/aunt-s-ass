count=0
with open ('Perepis.txt' , 'r') as file:
    for line in file:
        L = line.split()
        data=L[3]
        year=data[6:]
        if int(year) <= 1978:
            print(L[0])
            count+=1
print('всего =', count)
print('Введите диапазон ')
diapazon1=int(input())
diapazon2=int(input())
print('От ',diapazon1," До",diapazon2)
with open ('Perepis.txt' , 'r') as file:
    for line in file:
        L = line.split()
        data=L[3]
        year=data[6:]
        if diapazon1 <= int(year) <= diapazon2:
            print(L[0],L[1],L[2],L[3])


