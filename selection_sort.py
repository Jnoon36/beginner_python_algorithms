# Selection sort algorithm for arranging a list in a certain order

numbers = input('List some numbers separated by commas ')

l = [int(n) for n in numbers.split(',') ]

for i in range(len(l)):
    for j in range(len(l) - 1):
        if l[j] >= l[j + 1]:  # Ascending order
            l[j], l[j + 1] = l[j + 1], l[j]

print('Rearranged list in ascending order: ', l)

for i in range(len(l)):
    for j in range(len(l) - 1):
        if l[j] <= l[j + 1]:  # Descending order
            l[j], l[j + 1] = l[j + 1], l[j]


print('Rearranged list in descending order: ', l)
