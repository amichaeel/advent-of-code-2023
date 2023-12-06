import time

digits_forward = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits_backwards = ["", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
total = 0
start = time.time()
with open("data.txt", "r") as data:
  lines = data.readlines()
  first = last = 0
  
  for line in lines:
    first_digit_found = last_digit_found = False
    for index, char in enumerate(line):
      if char.isdigit():
        first_digit_found = True
        first = int(char)
        line_cut = line[0:index]
        prev = index
        for digit_index in range(1, len(digits_forward)):
          digit = digits_forward[digit_index]
          spelled_index = line_cut.index(digit) if digit in line_cut else prev
          if digit in line_cut and spelled_index < prev:
            prev = spelled_index
            first = digit_index
        break
      
    if first_digit_found == False:
      prev = len(line) + 1
      for digit_index in range(1, len(digits_forward)):
        digit = digits_forward[digit_index]
        spelled_index = line.index(digit) if digit in line else prev
        
        if digit in line and spelled_index < prev:
          prev = spelled_index
          first = digit_index
    
      
    line_reverse = line[::-1]
    for index, char in enumerate(line_reverse):
      if char.isdigit():
        last_digit_found = True
        last = int(char)
        line_cut = line_reverse[0:index]
        prev = len(line) + 1
        
        for digit_index in range(1, len(digits_backwards)):
          digit = digits_backwards[digit_index]
          spelled_index = line_cut.index(digit) if digit in line_cut else prev
          if digit in line_cut and spelled_index < prev:
            prev = spelled_index
            last = digit_index
        break
    
    if last_digit_found == False:
      prev = len(line) + 1
      for digit_index in range(1, len(digits_backwards)):
        digit = digits_backwards[digit_index]
        spelled_index = line_reverse.index(digit) if digit in line_reverse else prev
        
        if digit in line_reverse and spelled_index < prev:
          prev = spelled_index
          last = digit_index
      
    str_num = str(first) + str(last)
    total =  total + int(str_num)

end = time.time()
elapsed = end - start
print(f"{total}, took {round(elapsed, 5)} seconds to comlpete.")