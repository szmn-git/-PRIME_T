
def prime(n):
    if n <= 1:
        return (True)

    for i in range(2, n):
        if n % i == 0:
            print("NIE")
            return (False)
    print("TAK")
    return (True)


# czytanie z pliku

filename = "prime.txt"

with open(filename) as f:
    content = f.readlines()

for line in content:
  splitted_line = line.split()
  for values in splitted_line:
    value_as_int = int(values)
    prime(value_as_int)