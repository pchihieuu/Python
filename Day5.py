##1

def sumOfFloat(param):
    a = 0.0
    for i in range(1, param + 1):
        print(i)
        a = a + (1/i)
    print("Result:", a)


n = (int)(input("Nhập số n :"))
sumOfFloat(n)


##2

def sumList(list1):
  sum = 0
  for number in list1:
    if number % 2 == 0:
      sum = sum + number
  return sum
 
list1 = [int(item) for item in input("Nhập vào các giá trị : ").split()] 
sumList(list1)


##3

def perfectNum(x):
  sum = 0
  for i in range(1, x):
    if x % i == 0:
      sum = sum + i
  return sum == x

x = int(input("Nhập x: "))

if perfectNum(x):
  print(x, "là số hoàn hảo")
else:
  print(x, "không phải là số hoàn hảo")


