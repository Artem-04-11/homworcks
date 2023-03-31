def printNumber(n, k = '\n'):
  if n > 0:
    printNumber(n - 1, k = ',')
    print(n, end = k)

n = int(input())
printNumber(n)