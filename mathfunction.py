def factorial(n):
    result= 1
    for i in range (2,n + 1):
        result *= i
        print(result)
        
factorial(6)
factorial(11)
factorial(15)
factorial(22)


def reminder(a,b):
    print("The result is")
    print(a -((a//b)*b))
 
reminder(3,2)
reminder(21,4)
reminder(131,19)
reminder(81,9)

3 % 2
21 % 4
131 % 19
81 % 9