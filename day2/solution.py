def get_game_id(line):
  index = 5
  id = ""
  while line[index].isdigit():
    id += line[index]
    index += 1
    
  return int(id)

def get_draw_count(line, color):
  count = ""
  index = draw.index(color)-2
  while line[index].isdigit():
    count += line[index]
    index -= 1
  
  count = ''.join(reversed(count))
  return int(count) 

def get_game_start(line):
  index = line.index(":")
  while not line[index].isdigit():
    index += 1
  
  return index
  

with open("data.txt", "r") as data:
  total = 0
  for line in data.readlines():
    successful = True
    game_id = get_game_id(line)
    draws = line[get_game_start(line):].split("; ")
    greens = reds = blues = 0
    for draw in draws:
      if "green" in draw: greens = max(greens, get_draw_count(draw, "green"))
      if "blue" in draw: blues = max(blues, get_draw_count(draw, "blue"))
      if "red" in draw: reds = max(reds, get_draw_count(draw, "red"))
    
    total = total + (greens * blues * reds)
  
  print(total)