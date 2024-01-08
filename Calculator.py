import math
from fractions import Fraction
print("Welcome to calculator")
print("Made by @Kirito071008")
def menu():
    x = input("Do you want to do:\n1) Math\n2) Physics\n")
    if x.lower() == "math" or x == "1":
        mat()
    elif x.lower() == "physics" or x == "2":
        physics()
    elif KeyboardInterrupt:
        print("Bye!")
    else:
        print("Invalid input")
def mat():
    x = input("Do you want to do:\n1)1 Normal calculator\n2) Quadratic equations\n")
    if x.lower() == "normal calculator" or x == "1":
        while True:
            try:
                x = (input("Write your equation:\n"))
                y = eval(x, {"__builtins__": None}, {"sqrt": math.sqrt})
                print((y))
            except (SyntaxError,ValueError,) as e:
                print(f"Error: {e}")
                menu()
    elif x.lower() == "quadratic equations" or x == "2":
        while True:
              a1 = int(input("First number:\t"))
              b1 = int(input("Second:\t"))
              c1 = int(input("Third:\t"))
              x = int("4")
              y = int(b1)*int(b1)
              s = int(x)*int(a1)*int(c1)
              ss = int(y)-int(s)
              if ss < int(0):
                  print("Δ<0, sorry but i can't solve this :(")
                  menu()
                  break
              elif ss == int(0):
                       a = 2*int(a1)
                       b = -1*b1
                       print(f"X = {Fraction(int(b),int(a))}")
                       if c.lower() == "yes" or c.lower() == "y":
                            continue
                       else:
                            menu()
                            break
              elif ss > 0:
                       a = 2*a1
                       b = -b1+math.sqrt(ss)
                       a2 = 2*a1
                       b2 = -b1-math.sqrt(ss)
                       print(f"X1 = {Fraction(int(b),int(a))}")
                       print(f"X2 = {Fraction(int(b2),int(a2))}")
                       c = input("Continue?")
                       if c.lower() == "yes" or c.lower() == "y":
                            continue
                       else:
                            menu()
                            break
def physics():
        while True:
            i1 = input("Do you want to:\n1) Convert\n2) Use formulas")
            if i1.lower() == "convert" or i1 == "1":
             q2 = input("Convert\n1) km/h to m/s\n2) m/s to km/h?\n")
             if q2.lower() == "convert km/h to m/s" or q2 == "1":
              n2 = float(input("What's the number you want to convert?:\t"))
              n3 = float("3.6")
              s1 = n2 / n3
              print(s1)
             elif q2.lower() == "m/s to km/h?" or q2 == "2":
              n2 = float(input("What's the number you want to convert?:\t"))
              n3 = float("3.6")
              s1 = n2 * n3
              print(s1)
            else:
                menu()
                break
menu()
