import re

if(input("test?\n") in ["1", "t", "y"]):
    lines = open("input_test.txt", "r")
else:
    lines = open("input.txt", "r")
    
output = open("output.txt", "w")
output2 = open("output2.txt", "w")

regex = "\d+"
output_lines = []

for line in lines:
    line = line.strip()
    line = re.findall(regex, line)
    output_lines.append(line)
    #line = [int(i) for i in line]

lista1 = [line[0] for line in output_lines]
lista2 = [line[1] for line in output_lines]
output.write("\n".join(lista1))
output2.write("\n".join(lista2))

lista1.sort()
lista2.sort()
suma = 0
for i in range(len(lista1)):
    suma += abs(int(lista1[i]) - int(lista2[i]))
    
print(suma)

output.close()
output2.close()
    