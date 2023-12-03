inputFile = open('./input.txt', 'r')

values = []
numberSpelledOut = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in inputFile:
  posToReplace = []
  trueLine = line

  for number in numberSpelledOut[1:]:
    count = line.count(number)
    if count > 0:
      start = 0
      for i in range(count):
        pos = line.find(number, start)
        start = pos + 1
        posToReplace.append([number, pos])

    posToReplace = sorted(posToReplace, key=lambda x: x[1])
  
  overlapped = False
  i = 0
  for ptr in posToReplace:
    if not overlapped:
      risky = [number for number in numberSpelledOut[1:] if number[0] == ptr[0][-1]]
      
      for r in risky:
        if overlapped: break
        overlapped = trueLine.find(r) == (ptr[1] + len(ptr[0]) - 1)

      trueLine = trueLine.replace(ptr[0], str(numberSpelledOut.index(ptr[0])) + ' ' * (len(ptr[0]) - 1), 1)
    else:
      trueLine = trueLine[:posToReplace[i-1][1] + 1] + str(numberSpelledOut.index(ptr[0])) + trueLine[posToReplace[i-1][1] + 1:]
      overlapped = False
    i += 1
  
  # print(trueLine)

  numbers = [int(letter) for letter in trueLine if letter.isdigit()]
  value = ''.join([str(numbers[0]), str(numbers[len(numbers) - 1])])
  values.append(int(value))

print(sum(values))
