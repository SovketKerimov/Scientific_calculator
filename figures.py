import math

numbers=[]
#1- Triangle / Cone
def triangle_cone():
    try:
        while True:
            print("1-Triangle")
            print("2-cone")
            main_choice0=input("Choose one(1-2) :")
            #triangle
            if main_choice0=="1":
                print("1-Area")
                print("2-Perimeter")
                print("3-Hypotenuse (for right triangle)")
                print("4-Type of triangle")
                print("5-Altitudes")
                print("6-Medians")
                print("7-Radius of the inscribed circle")
                print("8-Radius of the circumscribed circle")
                print("9-Angles in degrees")
                choice0=input("Enter your choice(1-9) :")

                if choice0 == "1":

                    a_t0=float(input("Enter the first side of a triangle :"))
                    a_t1=float(input("Enter the second side of a triangle :"))
                    a_t2=float(input("Enter the third side of a triangle :"))

                    halfp_t=(a_t0+a_t1+a_t2)/2
                    area_t= round(math.sqrt(halfp_t*(halfp_t-a_t0)*(halfp_t-a_t1)*(halfp_t-a_t2)),2)

                    print(f"The area of a triangle is : {area_t}")

                elif choice0 == "2":

                    a_ta=float(input("Enter the first side of a triangle :"))
                    a_tb=float(input("Enter the second side of a triangle :"))
                    a_tc=float(input("Enter the third side of a triangle :"))

                    perimeter_t=round((a_ta+a_tb+a_tc),2)

                    print(f"The perimeter of a triangle is : {perimeter_t}")

                elif choice0 == "3":

                    rs_t0=float(input("Enter the first right side of a triangle :"))
                    rs_t1=float(input("Enter the second right side of a triangle :"))

                    hyp_t=round(math.sqrt(rs_t0**2+rs_t1**2),2)

                    print(f"The hypotenuse of a triangle is : {hyp_t}")

                elif choice0 == "4":

                    a_tl=float(input("Enter the first side of a triangle :"))
                    a_tk=float(input("Enter the second side of a triangle :"))
                    a_tm=float(input("Enter the third side of a triangle :"))

                    if a_tl==a_tk==a_tm:
                        print("Your triangle is : Equilateral")
                    elif a_tl==a_tk or a_tl==a_tm or a_tk==a_tl:
                        print("Your triangle is : Isosceles")
                    else:
                        print("Your triangle is : Scalene")

                elif choice0 == "5":

                    a_td=float(input("Enter the first side of a triangle :"))
                    a_te=float(input("Enter the second side of a triangle :"))
                    a_tf=float(input("Enter the third side of a triangle :"))

                    halfp_t=(a_td+a_te+a_tf)/2
                    area_t=math.sqrt(halfp_t*(halfp_t-a_td)*(halfp_t-a_tf)*(halfp_t-a_te))
                    hight_t0=(2*area_t)/a_td
                    hight_t1=(2*area_t)/a_te
                    hight_t2=(2*area_t)/a_tf

                    print(f"The altitude to the first side : {hight_t0} ")
                    print(f"The altitude to the second side : {hight_t1} ")
                    print(f"The altitude to the third side : {hight_t2}")

                elif choice0== "6":

                    a_t5=float(input("Enter the first side of a triangle :"))
                    a_t6=float(input("Enter the second side of a triangle :"))
                    a_t7=float(input("Enter the third side of a triangle :"))

                    median_t0=0.5*math.sqrt(2*(a_t6**2+a_t7**2)-a_t5**2)
                    median_t1=0.5*math.sqrt(2*(a_t5**2+a_t7**2)-a_t6**2)
                    median_t2=0.5*math.sqrt(2*(a_t5**2+a_t6**2)-a_t7**2)

                    print(f"The median to the first side is : {median_t0} ")
                    print(f"The median to the second side is : {median_t1} ")
                    print(f"The median to the third side is : {median_t2}")

                elif choice0== "7":

                    a_t0=float(input("Enter the first side of a triangle :"))
                    a_t1=float(input("Enter the second side of a triangle :"))
                    a_t2=float(input("Enter the third side of a triangle :"))

                    half_p=(a_t0+a_t1+a_t2)/2
                    area_t=math.sqrt(half_p*(half_p-a_t0)*(half_p-a_t1)*(half_p-a_t2))
                    radius_in=round(area_t/half_p,2)

                    print(f"The radius of the inscribed circle is : {radius_in}")

                elif choice0== "8":

                    a_t0=float(input("Enter the first side of a triangle :"))
                    a_t1=float(input("Enter the second side of a triangle :"))
                    a_t2=float(input("Enter the third side of a triangle :"))

                    half_p=(a_t0+a_t1+a_t2)/2
                    area_t=math.sqrt(half_p*(half_p-a_t0)*(half_p-a_t1)*(half_p-a_t2))
                    radius_out=round((a_t0*a_t1*a_t2)/(4*area_t),2)

                    print(f"The radius of the circumcircle is : {radius_out}")

                elif choice0== "9":

                    a_t0=float(input("Enter the first side of a triangle :"))
                    a_t1=float(input("Enter the second side of a triangle :"))
                    a_t2=float(input("Enter the third side of a triangle :"))

                    a_d0=round(math.degrees(math.acos((pow(a_t1,2) + pow(a_t2,2) - pow(a_t0,2))/(2*a_t1*a_t2))),2)
                    a_d1=round(math.degrees(math.acos((pow(a_t0,2 + pow(a_t2,2)-pow(a_t1,2))/(2*a_t0*a_t2)))),2)
                    a_d2=round(180-a_d0-a_d1,2)

                    print(f"The degrees of the triangle is : \n")
                    print(f"First one :{a_d0} ")
                    print(f"Second one :{a_d1} ")
                    print(f"Third one :{a_d2} ")

            elif main_choice0== "2":

                print("1-Volume")
                print("2-Lateral surface area")
                print("3-Base area")
                print("4-Total surface area")
                print("5-Slant height")
                choice1=input("Enet your choice(1-5) :")

                if choice1== "1":

                    height_0=float(input("Enter the height of the cone :"))
                    radius_0=float(input("Enter the radius of the base"))
                    volume_0=round(1/3*math.pi*height_0*radius_0,2)

                    print(f"The volume of the cone is : {volume_0}")
                elif choice1=="2":

                    radius_1=float(input("Enter the radius of the cone : "))
                    slant_0=float(input("Enter the length of the slant :"))
                    lat_s0=round(math.pi*radius_1*slant_0,2)

                    print(f"The value of the lateral surface area is : {lat_s0} ")

                elif choice1== "3":

                    radius_2=float(input("Enter the radius of the cone: "))

                    base_a0=round(math.pi*pow(radius_2,2),2)

                    print(f"The are of the base is : {base_a0} ")

                elif choice1== "4":

                    radius_2=float(input("Enter the radius of the cone :"))
                    slant_2=float(input("Enter the slant of the cone :"))

                    total_area=round((math.pi*pow(radius_2,2)+math.pi*radius_2*slant_2),2)

                    print(f"The total area of the cone is : {total_area} ")
                elif choice1== "5":

                    radius_3=float(input("Enter the radius of the cone :"))
                    height_3=float(input("Enter the height of the cone :"))

                    slant_a=round(math.sqrt(pow(radius_3,2)+pow(height_3,2)),2)

                    print(f"The length of the slant is : {slant_a}")
    except ValueError:
        print("Invalid input")
        pass
#2-Square,Rombus,Trapezoid
def square_rombus_trapezoid():
    print("1-Square")
    print("2-Rombus")
    print("3-Trapezoid")
    main_cs=input("Choose one(1-3)")
    try:
      if main_cs==1:

          print("1-Area")
          print('2-Perimeter')
          print('3-Diagonal')
          print('4-Radius of inscribed circle')
          print('5-Radius of circumscribed circle')
          square_c=input("Enter your choice(1-5) :")

          if square_c==1:

            s_s0=float(input('Enter the side of a square :'))
            a_s0=round(pow(s_s0,2),2)

            print(f"The area of the square is : {a_s0}")
          elif square_c==2:

              s_s1=float(input('Enter the side of a square :'))
              p_s0=round((s_s1*4),2)

              print(f'The perimeter of a square is : {p_s0}')
          elif square_c==3:

              s_s2=float(input('Enter the side of a square :'))
              d_s0=round(math.sqrt(pow(s_s2,2)+pow(s_s2,2)),2)

              print(f'The diagonal of a square is : {d_s0}')
          elif square_c==4:

              s_s3=float(input('Enter the side of a square :'))
              r_s0=s_s3/2

              print(f'The radius of an inscribed circle is : {r_s0}')

          elif square_c==5:

              s_s4=float(input('Enter the side of a square :'))
              d_s1=round(math.sqrt(pow(s_s4,2)+pow(s_s4,2)),2)/2

              print(f'The radius of an circumscribed circle is  : {d_s1}')

      elif main_cs==2:
          print('1-Area')
          print('2-Perimeter')
          print('3-Acute Angel')
          print('4-Obtuse Angel')
          print('5-Altitude')
          print('6-Radius of inscribed circle')
          print('7-Diagonals')
          rombus_c=input('Choose one(1-7) :')
          if rombus_c==1:

              romb_s=float(input('Enter the side of a rombus :'))
#finish elif main_cs==2



    except ValueError:
        print("Invalid input")
        pass
#3-Circle,Cylinder,Sphere
def circle_cylinder_sphere():
    print("1-Circle")
    print("2-Cylinder")
    print("3-Sphere")
    main_cc=input("Choose one(1-3)")
    pass
def menyu():
    print("\n-MENU-")
    print("1-Triangle / Cone")
    print("2-Square / Rombus / Trapezoid")
    print("3-Circle / Cylinder / Sphere")
def daire_silindr_kure():
    print("1-Dairə\n2-Silindr\n3-Küre")
    sec=int(input("Secim: "))
    r=float(input("Radius: "))
    if sec==1:
        print("Sahə:",math.pi*r**2,"Uzunluq:",2*math.pi*r)
    elif sec==2:
        h=float(input("Hündürlük: "))
        print("Həcmi:",math.pi*r**2*h)
    elif sec==3:
        print("Həcmi:",(4/3)*math.pi*r**3)