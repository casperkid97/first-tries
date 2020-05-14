a=input("username")

if a=="marc":
    for x in range(3):
        z=input("enter password")
        if z=="ugly":
         print("holy shit this works")
         break

if a=="austin":
    for x in range(3):
        z=input("enter password")
        if z=="ugly":
         print("I hate you")
         break

if a=="zach":
    for x in range(3):
        z=input("enter password")
        if z=="ugly":
         print("CHUFF")
         break

if a!="marc" or "zach" or "austin":
    print("retry password")