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

            if choice0 == 1:
                a_t0=float(input("Enter the first side of a triangle :"))
                a_t1=float(input("Enter the second side of a triangle :"))
                a_t2=float(input("Enter the third side of a triangle :"))
                halfp_t=(a_t0+a_t1+a_t2)/2
                area_t= round(math.sqrt(halfp_t*(halfp_t-a_t0)*(halfp_t-a_t1)*(halfp_t-a_t2)),2)
                print(f"The area of a triangle is : {area_t}")
            elif choice0 == 2:
                a_t0=float(input("Enter the first side of a triangle :"))
                a_t1=float(input("Enter the second side of a triangle :"))
                a_t2=float(input("Enter the third side of a triangle :"))
                perimeter_t=round((a_t0+a_t1+a_t2),2)
                print(f"The perimeter of a triangle is : {perimeter_t}")
            elif choice0 == 3:
                rs_t0=float(input("Enter the first right side of a triangle :"))
                rs_t1=float(input("Enter the second right side of a triangle :"))
                hyp_t=round(math.sqrt(rs_t0**2+rs_t1**2),2)
                print(f"The hypotenuse of a triangle is : {hyp_t}")
            elif choice0 == 4:
                pass

    except ValueError:
        print("Invalid input")
        triangle_cone()
