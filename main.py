if(input("test? (confirm by typing \"1\", \"t\" or \"y\")\n") in ["1", "t", "y"]):
    lines = open("input_test.txt", "r")
else:
    lines = open("input.txt", "r")

def check_number(line, reverse = False):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    iteration = reversed(range(len(line))) if reverse else range(len(line))
    
    for i in iteration:
        if(line[i] in numbers):
            return (i, line[i])

def check_spelling(line, reverse = False):
    spellings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    iteration = reversed(range(len(line))) if reverse else range(len(line))
        
    for i in iteration:
        for spelling in spellings:
            if(len(line) >= i + len(spelling)):
                the_same = True
                for j in range(len(spelling)):
                    if(line[i+j] != spelling[j]):
                        the_same = False
                if(the_same):
                    return (i, spellings.index(spelling) + 1)
    

part1_sum = 0
part2_sum = 0
part_1_can_be_done = True

for line in lines:
    line = line.strip()
    
    #gets first and last number as well as first and last spelled out number
    first = [check_number(line), check_spelling(line)]
    last = [check_number(line, True), check_spelling(line, True)]
    
    
    if((first[0] is None or last[0] is None) and part_1_can_be_done):
        print("\n\033[91m----------EXCEPTION---------")
        print("part1 can't be done. this line doesn't contain a digit:\n" + line + "\033[0m")
        part_1_can_be_done = False
    
    if(None in first):
        first.remove(None)
    if(None in last):
        last.remove(None)
    
    if(part_1_can_be_done):
        part1_sum += int(str(first[0][1]) + str(last[0][1]))

    # add the smaller index number from first and bigger index number from last
    part2_sum += int(str(min(first, key = lambda k: k[0])[1]) + str(max(last, key = lambda k: k[0])[1]))
   
print("\n\033[94m==========SOLUTIONS=========\033[0m")
if(part_1_can_be_done):
    print("part 1 solution: " + str(part1_sum))
print("part 2 solution: " + str(part2_sum))

lines.close()