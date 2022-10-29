r=int(input())
t=r%10

o=r%100//10
h=r//100
k=h+o+t
l=h*o*t
print("Сумма цифер =",k)
print("Произведение цифер =",l)
