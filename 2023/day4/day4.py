if(input("test?\n") in ["1", "t", "y"]):
    file = "input_test.txt"
    beginning_parsing = 8
else:
    file = "input.txt"
    beginning_parsing = 10

with open(file, "r") as lines:
    for i, line in enumerate(lines):
        pass
    file_length = i + 1

lines = open(file, "r")

def find_repeating_numbers(list1, list2):
    result = []
    for elem in list1:
        if(elem in list2 and elem not in result):
            result.append(elem)
    return result

suma = 0
card_amounts = [1] * file_length
for card_id, line in enumerate(lines):
    # parsing input
    line = line.strip()[beginning_parsing:].split("|")
    for i in range(2):
        line[i] = line[i].split(" ")
        while("" in line[i]):
            line[i].remove("")
        for j in range(len(line[i])):
            line[i][j] = int(line[i][j])
    
    repeating_numbers = find_repeating_numbers(line[0], line[1])
    amount_repeating = len(repeating_numbers)
    
    if(amount_repeating > 0):
        suma += 2 ** (amount_repeating - 1)
    
    for i in range(amount_repeating):
        card_amounts[card_id + i + 1] += card_amounts[card_id]
    
print(sum(card_amounts))
print(card_amounts)