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

                a_t0=float(input("Enter the first side of a triangle :"))
                a_t1=float(input("Enter the second side of a triangle :"))
                a_t2=float(input("Enter the third side of a triangle :"))

                if a_t0==a_t1==a_t2:
                    print("Your triangle is : Equilateral")
                elif a_t0==a_t1 or a_t1==a_t2 or a_t2==a_t0:
                    print("Your triangle is : Isosceles")
                else:
                    print("Your triangle is : Scalene")

            elif choice0 == 5:

                a_t0=float(input("Enter the first side of a triangle :"))
                a_t1=float(input("Enter the second side of a triangle :"))
                a_t2=float(input("Enter the third side of a triangle :"))

                halfp_t=(a_t0+a_t1+a_t2)/2
                area_t=math.sqrt(halfp_t*(halfp_t-a_t0)*(halfp_t-a_t1)*(halfp_t-a_t2))
                hight_t0=2*area_t/a_t0
                hight_t1=2*area_t/a_t1
                hight_t2=2*area_t/a_t2

                print(f"The altitude to the first side : {hight_t0} ")
                print(f"The altitude to the second side : {hight_t1} ")
                print(f"The altitude to the third side : {hight_t2}")

            elif choice0== 6:

                a_t0=float(input("Enter the first side of a triangle :"))
                a_t1=float(input("Enter the second side of a triangle :"))
                a_t2=float(input("Enter the third side of a triangle :"))

                median_t0=0.5*math.sqrt(2*(a_t2**2+a_t1**2)-a_t0**2)
                median_t1=0.5*math.sqrt(2*(a_t0**2+a_t0**2)-a_t1**2)
                median_t2=0.5*math.sqrt(2*(a_t1**2+a_t2**2)-a_t2**2)

                print(f"The median to the first side is : {median_t0} ")
                print(f"The median to the second side is : {median_t1} ")
                print(f"The median to the third side is : {median_t2}")
            elif choice0==7:
                a_t0=float(input("Enter the first side of a triangle :"))
                a_t1=float(input("Enter the second side of a triangle :"))
                a_t2=float(input("Enter the third side of a triangle :"))
                half_p=(a_t0+a_t1+a_t2)/2
                area_t=math.sqrt(half_p*(half_p-a_t0)*(half_p-a_t1)*(half_p-a_t2))
                radius_in=round(area_t/half_p,2)
                print(f"The radius of the inscribed circle is : {radius_in}")
            elif choice0==8:
                a_t0=float(input("Enter the first side of a triangle :"))
                a_t1=float(input("Enter the second side of a triangle :"))
                a_t2=float(input("Enter the third side of a triangle :"))
                half_p=(a_t0+a_t1+a_t2)/2
                area_t=math.sqrt(half_p*(half_p-a_t0)*(half_p-a_t1)*(half_p-a_t2))
                radius_out=round((a_t0*a_t1*a_t2)/(4*area_t),2)
                print(f"The radius of the circumcircle is : {radius_out}")




    except ValueError:
        print("Invalid input")
        triangle_cone()
