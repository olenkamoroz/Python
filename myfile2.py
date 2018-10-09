file_a = open('E:\\Python\\a.txt')
lines = file_a.readlines()
file_a.close()

i = 0
file_a = open('E:\\Python\\a.txt')
file_b1 = open('E:\\Python\\b1.txt', 'w')
file_b2 = open('E:\\Python\\b2.txt', 'w')
for line in lines:
    i += 1
    if i % 2 == 0:
        line = line.upper()
        file_b1.write(line)
    elif (i - 1) % 2 == 0:
        line = line.lower()
        file_b2.write(line)

file_a.close()
file_b1.close()
file_b2.close()

file_b1 = open('E:\\Python\\b1.txt')
print(file_b1.read())
file_b2 = open('E:\\Python\\b2.txt')
print(file_b2.read())

