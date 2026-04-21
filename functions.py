import math

ededler=[]
#1- Triangle / Cone
def triangle_cone():
    try:
        print("1-Triangle")
        print("2-cone")
        main_choice0=int(input("Choose one(1 or 2) :"))
        #triangle
        if main_choice0 == 1:
            print("1-Area")
            print("2-Perimeter")
            print("3-Hypotenuse (for right triangle)")
            print("4-Type of triangle")
            print("5-Altitudes")
            print("6-Medians")
            print("7-Radius of the inscribed circle")
            print("8-Radius of the circumscribed circle")
            print("9-Angles in degrees")
            choice0=input("Choose one(1 or 2) :")
    except ValueError:
        print("Invalid input")
        triangle_cone()