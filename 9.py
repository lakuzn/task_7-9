print("Введите Х")
x = int(input())
while (x<10000) or (x>99999):
    print("Ошибка, введите пятизначное положительное число.")
    x = int(input())
def cifra(x):
    return x%10
def umensh(x):
    return x//10
e = cifra(x)
x = umensh(x)
d = cifra(x)
x = umensh(x)
c = cifra(x)
x = umensh(x)
b = cifra(x)
x = umensh(x)
a = cifra(x)
if  (a==e) and (b==d):
    print("Число является палиндромом.")
else:
    print("Число не является палиндромом.")


