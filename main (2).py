


a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)



a = int(input())
b = int(input())
if a < b:
 for i in range(a, b + 1):
    print(i)
else:
  for i in range(a, b - 1, -1):
    print(i)



n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)



res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)



n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
     print(j, sep='', end='')
print()


n = int(input())
i = 1
while i ** 2 <= n:
     print(i ** 2)
i += 1


n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)


n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)


len = 0
while int(input()) != 0:
    len += 1
print(len)


prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)


first_max = int(input())
second_max = int(input())
if first_max < second_max:
    (first_max, second_max) = (second_max,first_max)
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)


n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)


n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)


a = input().split()
print(a[::2])


n = [int(asd) for asd in input().split()]
for asd in range(1, int(n)):
    if a[asd] > a[asd - 1]:
        print(a, [asd])


index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, int(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)




a = [int(i) for i in input().split()]
x = int(input())
pos = 0
while pos < int(a) and a[pos] >= x:
    pos += 1
print(pos + 1)


a = [int(i) for i in input().split()]
for i in range(1, int(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))


a = [int(i) for i in input().split()]
for i in range(1, int(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))


a = [int(s) for s in input().split()]
k = int(input())
for i in range(k + 1, int(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))


a = [int(s) for s in input().split()]
k, C = [int(s) for s in input().split()]
a.append(0)
for i in range(int(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))


n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
if correct:
    print('NO')
else:
    print('YES')

