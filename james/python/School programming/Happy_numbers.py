
def happy_numbers(n):
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = sum(int(i) ** 2 for i in str(n))    
        return n == 1

happy_numbers_list = []
i = 1

while len(happy_numbers_list) < 8:
    if happy_numbers(i):
          happy_numbers_list.append(i)
    i += 1

print(happy_numbers_list)