
import math
"1"


def countNumber(number):
    for i in range(1, number + 1):
        print(i, end='  ')


number = (int)(input("Nhập số nguyên :"))
countNumber(number)

"2"


def countAndCalculate(number):
    for i in range(1, 11):
        print("{} * {} = {}".format(number, i, number * i))


number = (int)(input("Nhập số nguyên :"))
countAndCalculate(number)
print("Bye.")

"3"


def countDownNumber(number):
    for i in range(1, number + 1):
        for j in range(i, number + 1):
            print(j, end=' ')
        print("")


number = int(input("Nhập số nguyên: "))
countDownNumber(number)

"4"


def isPrimeNum(n):
    if n < 2:
        return False
    tg = int(math.sqrt(n))
    for i in range(2, tg + 1):
        if(n % i) == 0:
            return False
    return True


n = int(input('Nhập số nguyên n: '))
print('Các số nguyên tố không được bé hơn hoặc bằng', n, 'là: ')
if n >= 2:
    print(2)
    for i in range(3, n + 1):
        if isPrimeNum(i):
            print(i)
        i = i + 2


"5"


def arrayMethod(param):
    list = ['a', 'b', 'c']
    if param == 1:
        print(list)
    elif param == 2:
        value = (input("Nhập giá trị:"))
        list.append(value)
        print(list)
    elif param == 3:
        list.pop(-1)
        print(list)
    elif param == 4:
        value = (input("Nhập giá trị:"))
        count = list.count(value)
        print("Số lần xuất hiện của `${value}`:", count)
    elif param == 5:
        list.reverse()
        print(list)
    elif param == 6:
        list.sort()
        print(list)
    elif param == 7:
        newmylist = sorted(list, reverse=True)
        print(newmylist)


print("1. Xem mảng \n 2.Thêm phần tử \n 3.Xóa phần tử cuối cùng ở mảng \n 4.Đếm số lần xuất hiện của phần tử x \n 5.Đảo mảng \n 6.Sắp xếp mảng tăng dần \n 7.Sắp xếp mảng giảm dần")
param = int(input('Nhập vào lựa chọn: '))
arrayMethod(param)


"7"


def showResult(a, b):
    difference_A_B = a - b
    difference_B_A = b - a
    intersection_A_B = a.intersection(b)
    union_A_B = a.union(b)

    print("Tập A - B:", difference_A_B)
    print("Tập B - A:", difference_B_A)
    print("Tập A ∩ B:", intersection_A_B)
    print("Tập A ∪ B:", union_A_B)


a = set(input("Nhập các phần tử của tập A: ").split())
b = set(input("Nhập các phần tử của tập B: ").split())
showResult(a, b)

"8"


def factorial(param):
    fact = 1
    if param < 0:
        print("Khong co gia tri")
    elif param == 0:
        print("Giai thua cua 0 la 1")
    else:
        for i in range(1, param + 1):
            fact = fact * i
        print("Giai thua cua", param, "la", fact)


n = (int)(input("Nhập số n :"))
factorial(n)

"9"


def fibonacci(param):
    a = 0
    b = 1
    count = 0
    print("Day fibonacci")
    while count < param:
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
        count += 1
    print(" ")


n = (int)(input("Nhập số n :"))
fibonacci(n)


"10"


def sumOfFloat(param):
    a = 0.0
    for i in range(1, param + 1):
        print(i)
        a = a + (1/i)
    print("Result:", a)


n = (int)(input("Nhập số n :"))
sumOfFloat(n)

"11"


def USCLN(a, b):
    while (a != b):
        if (a > b):
            a = a-b
        else:
            b = b - a
    print("USCLN(a,b) = ", a)


a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
USCLN(a, b)


"12"


def getProfit(wallet, dream):
    month = 0
    while (wallet < dream):
        wallet += wallet*0.03
        month += 1
    print("Bạn phải gửi trong", month, " tháng, lúc đó bạn sẽ được ", wallet)


wallet = float(input("Số tiền hiện có: "))
dream = float(input("Số tiền mơ ước: "))
getProfit(wallet, dream)
