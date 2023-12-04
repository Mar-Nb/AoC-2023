inputFile = open('./test.txt', 'r')

values = []

for line in inputFile:
  counter = { 'blue': 0, 'green': 0, 'red': 0 }
  gameSets = line.strip().split(':')[1].split(';')

  for gameSet in gameSets:
    colors = gameSet.split(',')

    for color in colors:
      result = color.split()
      if result[1] == 'green': counter['green'] = max(int(result[0]), counter['green'])
      if result[1] == 'blue': counter['blue'] = max(int(result[0]), counter['blue'])
      if result[1] == 'red': counter['red'] = max(int(result[0]), counter['red'])
  
  values.append(counter['green'] * counter['blue'] * counter['red'])

print(sum(values))