#10/08/23 22 lines
i = 1
while i < 6:
    print(i)
    i += 1

a = 1
while a < 6:
  print(a)
  if (a == 3):
    break
  a += 1

b = 0
while b < 6:
  b += 1
  if b == 3:
    continue
  print(b)

j = 1
while j < 6:
  print(j)
  j += 1
else:
  print("j is no longer less than 6")

  '''
  1
2
3
4
5
1
2
3
1
2
4
5
6
1
2
3
4
5
j is no longer less than 6
'''