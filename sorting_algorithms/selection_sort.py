# Algorithm for arranging a list in ascending or descending order

# If you do not need user input, then comment out line 5 and replace line 7 with your own list.

numbers = input('List some numbers separated by commas ')

l = [float(n) for n in numbers.split(',') ]

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
