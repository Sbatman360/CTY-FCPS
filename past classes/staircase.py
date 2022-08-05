height = int(input('Height: '))

for i in range(1, height + 1):
  for m in range(0, height - i):
    print(" ", end="")
  for j in range(0, i):
    print("#", end="")
  print("\n")
  