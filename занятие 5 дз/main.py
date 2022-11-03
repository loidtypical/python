# a=int(input())
# # 123
# b=a%10
# c=(a//10)%10
# d=a//100
# print(a)
# print(d,b,c,sep="")
# print(c,d,b,sep="")
# print(c,b,d,sep="")
# print(b,d,c,sep="")
# print(b,c,d,sep="")

p=int(input())
a=p//1000
b=(p//100)%10
c=(p//10)%10
d=p%10
print("Цифра в позиции тысяч равна",a)
print("Цифра в позиции сотен равна",b)
print("Цифра в позиции десятков равна",c)
print("Цифра в позиции единиц равна",d)
