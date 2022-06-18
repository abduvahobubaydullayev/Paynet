
# 1 - mustaqil talim 1-ish 10-varyant
# a
import math

a = eval(input('a := '))
b = eval(input('b := '))
x = eval(input('x := '))

l = math.tan(4.5 * x) + (pow(x, -10) + b) / (math.sin(0.5 * x) + a)

t = (math.exp(a + b) + pow(x * x + 3, 1 / 2)) / a
print('l := ', l)
print('t := ', t)

# b

if pow(math.fabs(a - b), 1 / 2) > x:
    z = math.atan(5 * x) / (b * math.cos(x) + math.log(a) * x)
else:
    z = pow(a+math.sin(2*x), 1/2)+a*x*x*x + b *math.log(math.fabs(2*x))
print('z := ', z)

# 2 - ish 10-varyant
# a
def item(n):
    j = 1
    for i in range(1, n+1):
        j = j * i
    return j
n = eval(input('n := '))
c = 0
k = 1
for i in range(1, 6):
    c = c + (-1 + a)

for i in range(1, n + 1):
    k = k * (i*i*i - 1)/item(i)

S = c + k

print('S := ', S)

# b

a = eval(input('a := '))
b = eval(input('b := '))
c = eval(input('c := '))

def EKUB(a, b, c):
    e = 1
    for i in range(2, min(a, b, c)+1):
        if a%i==0 and b % i == 0 and c % i == 0:
            e = e * i
    print('EKUB(a, b, c) := ', e)
EKUB(a, b, c)

# c

S = 1
k = 0

for i in range(1, 5):
    for j in range(1, 11):
        k = (item(i)+item(j))/(a+b)
    S = S * k
print('S := ', S)

# 3 - ish 10- varyant

n = eval(input('Massiv o`lchamini kiriting := '))
x = []
z = []
u = []
for i in range(n):
    x.append(input(f'x[{i}] := '))
for i in x:
    if x.index(i)%2 == 0:
        z.append(i)
    else:
        u.append(i)
print('x := ', x)
print('z := ', z)
print('u := ', u)


