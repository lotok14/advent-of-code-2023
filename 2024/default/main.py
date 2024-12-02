import re

if(input("test?\n") in ["1", "t", "y"]):
    lines = open("input_test.txt", "r")
else:
    lines = open("input.txt", "r")

regex = "\d+"
output_lines = []

for line in lines:
    line = line.strip()
    line = re.findall(regex, line)
    output_lines.append(line)
    #line = [int(i) for i in line]