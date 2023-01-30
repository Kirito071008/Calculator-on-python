print("Welcome to calculator")
print("Made by @Kirito071008")
import math
while True:
    print("If you want to stop the calculator digit (stop)")
    i1 = input("Do you want to do: 1)raise a number by a power 2)the square root of a number 3)the round of a number 4)how further is a number from zero 5) simple math function?")
    if i1 == "raise a number by a power" or i1 == "1":
        n1 = int(input("What's the number you want to raise? "))
        p1 = int(input("What's the value of the power? "))
        s1 = pow(n1,p1)
        print(s1)
    elif i1 == "the square root of a number" or i1 == "2":
        n1 = int(input("Of what number? "))
        s1 = (math.sqrt(n1))
        print(s1)
    elif i1 == "the round of a number" or i1 == "3":
        n1 = float(input("What number do you want to round? "))
        q1 = str(input("Do you want to round for excess or for defect? "))
        if q1 == "excess" or q1 == "Excess":
            s1 = (math.ceil(n1))
            print(s1)
        elif q1 == "Defect" or q1 == "defect":
            s2 = (math.floor(n1))
            print(s2)
    elif i1 == "How far is a number from zero" or i1 == "4":
        n1 = int(input("What's the number? "))
        s1 = (abs(n1))
        print(s1)
    elif i1 == "simple math function" or i1 == "5":
        q1 = input("Of how many numbers? (max 4) ")
        if q1 == "2":
            n1 = int(input("What's the first number? "))
            n2 = input("What math operation do you want to use?")
            n3 = int(input("What's the third second number?"))
            if n2 == "+":
                s1 = n1 + n3
                print(s1)
            if n2 == "-":
                s1 = n1 - n3
                print(s1)
            if n2 == "*":
                s1 = n1 * n3
                print(s1)
            if n2 == "/":
                s1 = n1 / n3
                print(s1)
        elif q1 == "3":
            n1 = int(input("What's the first number? "))
            n2 = input("What math operation do you want to use?")
            n3 = int(input("What's the second number? "))
            n4 = input("What's the second math operation do you want to use?")
            n5 = int(input("What's the third number?"))
            if n2 == "+" and n4 == "+":
                s1 = n1 + n3 + n4
                print(s1)
            if n2 == "+" and n4 == "-":
                s1 = n1 + n3 - n5
                print(s1)
            if n2 == "+" and n4 == "*":
                s1 = n1 + n3 * n5
                print(s1)
            if n2 == "+" and n2 == "/":
                s1 = n1 + n3 / n5
                print(s1)
            if n2 == "-" and n4 == "+":
                s1 = n1 - n3 + n5
                print(s1)
            if n2 == "-" and n4 == "-":
                s1 = n1 - n3 - n5
                print(s1)
            if n2 == "-" and n4 == "*":
                s1 = n1 - n3 * n5
                print(s1)
            if n2 == "-" and n4 == "/":
                s1 = n1 - n3 / n5
                print(s1)
            if n2 == "*" and n4 == "-":
                s1 = n1 * n3 - n5
                print(s1)
            if n2 == "*" and n4 == "+":
                s1 = n1 * n3 + n5
                print(s1)
            if n2 == "*" and n4 == "*":
                s1 = n1 * n3 * n5
                print(s1)
            if n2 == "*" and n4 == "/":
                s1 = n1 * n3 / n5
                print(s1)
            if n2 == "/" and n4 == "-":
                s1 = n1 / n3 - n5
                print(s1)
            if n2 == "/" and n4 == "+":
                s1 = n1 / n3 + n5
                print(s1)
            if n2 == "/" and n4 == "*":
                s1 = n1 / n3 * n5
                print(s1)
            if n2 == "/" and n4 == "/":
                s1 = n1 / n3 / n5
                print(s1)
        elif q1 == "4":
            print("Disclaimer, i have not yet write all the possibility, if you find one that didn't work please report to me and i will add it to the code")
            n1 = int(input("What's the first number?"))
            n2 = input("What math operation do you want to use?")
            n3 = int(input("What's the second number?"))
            n4 = input("What's the second math operation do you want to use?")
            n5 = int(input("What's the third number?"))
            n6 = input("What's the third math operationd do you want to use?")
            n7 = int(input("What's the fourth number?"))
            if n2 == "+" and n4 == "+" and n6 == "+":
                s1 = n1 + n3 + n5 + n7
                print(s1)
            if n2 == "+" and n4 == "+" and n6 == "-":
                s1 = n1 + n3 + n5 - n7
                print(s1)
            if n2 == "+" and n4 == "+" and n6 == "*":
                s1 = n1 + n3 + n5 * n7
                print(s1)
            if n2 == "+" and n4 == "+" and n6 == "/":
                s1 = n1 + n3 + n5 / n7
                print(s1)
            if n2 == "+" and n4 == "-" and n6 == "+":
                s1 = n1 + n3 - n5 + n7
                print(s1)
            if n2 == "+" and n4 == "*" and n6 == "+":
                s1 = n1 + n3 * n5 + n7
                print(s1)
            if n2 == "+" and n4 == "/" and n6 == "+":
                s1 = n1 + n3 / n5 + n7
                print(s1)
            if n2 == "-" and n4 == "+" and n6 == "+":
                s1 = n1 - n3 + n5 + n7
                print(s1)
            if n2 == "*" and n4 == "-" and n6 == "+":
                s1 = n1 * n3 - n5 + n7
                print(s1)
            if n2 == "/" and n4 == "-" and n6 == "+":
                s1 = n1 / n3 + n5 + n7
                print(s1)
            if n2 == "+" and n4 == "-" and n6 == "-":
                s1 = n1 + n3 - n5 - n7
                print(s1)
            if n2 == "+" and n4 == "*" and n6 == "*":
                s1 = n1 + n3 * n5 * n7
                print(s1)
            if n2 == "+" and n4 == "/" and n6 == "/":
                s1 = n1 + n3 / n5 / n7
                print(s1)
            if n2 == "-" and n4 == "-" and n6 == "-":
                s1 = n1 - n3 - n5 - n7
                print(s1)
            if n2 == "*" and n4 == "*" and n6 == "*":
                s1 = n1 * n3 * n5 * n7
                print(s1)
            if n2 == "/" and n4 == "/" and n6 == "/":
                s1 = n1 / n3 / n5 / n7
                print(s1)
            if n2 == "+" and n4 == "*" and n6 == "/":
                s1 = n1 + n3 * n5 / n7
                print(s1)
            if n2 == "-" and n4 == "*" and n6 == "/":
                s1 = n1 - n3 * n5 / n7
                print(s1)
            if n2 == "/" and n4 == "+" and n6 == "*":
                s1 = n1 / n3 + n5 * n7
                print(s1)
            if n2 == "*" and n4 == "/" and n6 == "*":
                s1 = n1 * n3 / n5 * n7
                print(s1)
            if n2 == "/" and n4 == "+" and n6 == "-":
                s1 = n1 / n3 + n5 - n7
                print(s1)
            if n2 == "*" and n4 == "/" and n6 == "/":
                s1 = n1 * n3 / n5 / n7
                print(s1)
            if n2 == "*" and n4 == "*" and n6 == "/":
                s1 = n1 * n3 * n5 / n7
                print(s1)
            if n2 == "*" and n4 == "+" and n6 == "-":
                s1 = n1 * n3 - n5 - n7
                print(s1)
            if n2 == "*" and n4 == "-" and n6 == "-":
                s1 = n1 * n3 - n5 - n7
                print(s1)
            #combinazioni ancora da testare
    elif i1 == "stop" or i1 == "Stop" or i1 == "STOP":  
        break
        
