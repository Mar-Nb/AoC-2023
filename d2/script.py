inputFile = open('./input.txt', 'r')

RED = 12
GREEN = 13
BLUE = 14

game = 1
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

  if counter['red'] <= RED and counter['green'] <= GREEN and counter['blue'] <= BLUE: values.append(game)
  # Game suivante
  game += 1

print(sum(values))