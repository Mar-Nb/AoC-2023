inputFile = open('./input.txt', 'r')

values = []

for line in inputFile:
  numbers = [int(letter) for letter in line if letter.isdigit()]
  value = ''.join([str(numbers[0]), str(numbers[len(numbers) - 1])])
  values.append(int(value))

print(sum(values))