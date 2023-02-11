print("Welcome to calculator")
print("Made by @Kirito071008")
import math
while True:
    print("If you want to stop the calculator type (stop)")
    e1 = input("Do you want to do:\n 1)math\n 2)physics?")
    if e1 == "math" or e1 == "1":        
         i1 = input("Do you want to do:\n 1)raise a number by a power\n 2)the square root of a number\n 3)the round of a number\n 4)how further is a number from zero\n 5) simple math function?")
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
         elif i1 == "How further is a number from zero" or i1 == "4":
            n1 = float(input("What's the number? "))
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
            #combinations yet to be tested
    elif e1 == "2":
        i1 = input("Do you want to:\n 1)Convert\n 2) Use formulas")
        if i1 == "Convert" or i1 == "convert" or i1 == "CONVERT" or i1 == "1":
             q2 = input("1)convert km/h to m/s or 2)m/s to km/h?")
             if q2 == "convert km/h to m/s" or q2 == "1":
              n2 = float(input("What's the number you want to convert?"))
              n3 = float("3.6")
              s1 = n2 / n3
              print(s1)
             elif q2 == "m/s to km/h?" or q2 == "2":
              n2 = float(input("What's the number you want to convert?"))
              n3 = float("3.6")
              s1 = n2 * n3
              print(s1)

    elif e1 == "stop" or e1 == "Stop" or e1 == "STOP" or i1 == "stop" or i1 == "Stop" or i1 == "STOP":  
        break
