from termcolor import cprint

def is_special_character(char):
  # return not char.isalnum() and char in string.punctuation and char != "."
  return not char.isdigit() and char != "."


def search_above_or_below(line):
  # traverse the line, find character
  # print(line)
  for char in line:
    if is_special_character(char):
      return True
    
  return False

invalid = {}

with open("data.txt", "r") as data:
  
  total = 0
  lines = data.readlines()
  
  
  # for all lines, find digits, and detemrine the length.
  
  for l, line in enumerate(lines):
    # if l != 113: continue
    digit = ""
    digit_found = False
    for i, char in enumerate(line):
      neg = False
      if char.isdigit() and not digit_found:
        digit_found = True
        digit += char
      
      elif char.isdigit() and digit_found:
        digit += char
      
      if not char.isdigit() and digit_found:
        digit_found = False
        # we have found the entire digit. lets search its adjent characters.
        n = len(digit)
        # lets check left and right, easy.
        
        if is_special_character(line[i]):
          # print(f"{digit} is valid, right is special.")
          total += int(digit)
          digit = ""
          continue
        
        if is_special_character(line[i-n-1]):
          # print(f"{digit} is valid, left is special.")
          if line[i-n-1] == "-":
            neg = True
          else:
            total += int(digit)
            digit = ""
            continue
        
        if l > 0 and not neg and search_above_or_below(lines[l-1][i-n-1:i+1]):
          # print(f"{digit} is valid, above is special.")
          total += int(digit)
          digit = ""
          continue
        
        if l < len(lines)-1 and not neg and search_above_or_below(lines[l+1][i-n-1:i+1]):
          # print(f"{digit} is valid, below is special.")
          total += int(digit)
          digit = ""
          continue
          
        if l > 0 and neg and search_above_or_below(lines[l-1][i-n-2:i+1]):
          total += int(digit)
          digit = ""
          continue
          
        if l < len(lines)-1 neg and search_above_or_below(lines[l+1][i-n-2:i+1]):
          total += int(digit)
          digit = ""
          continue
        
        
        # print(lines[l-1] if l > 0 else None)
        # n = len(digit)
        # cprint(lines[l][:i-n], 'white', end='', flush=True)
        # cprint(lines[l][i-n:i], 'green', end='', flush=True)
        # cprint(lines[l][i:], 'white', flush=True)
        # print(lines[l+1])
        # print('\n')
        # print(f"{colored(digit, 'green', attrs=['bold'])} is not valid.\n")
        digit = ""
    
  print(total)