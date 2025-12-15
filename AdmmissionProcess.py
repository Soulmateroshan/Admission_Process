age = int(input("Enter your Age: "))

if age>=18 and age<25:
    print("You are elligiable for admission")
    
    marks = float(input("Enter Your Marks: "))
    if marks>=90:
        print("You admmission successfuly confirm....!")
    elif marks>=70 and marks<90:
        print("You need to pay 1lakh rs donation for admmission")
    elif marks>=50 and marks<70:
        print("You need to pay 2 lakh rs donation for admmission")
    elif marks>=35 and marks<50:
        print("You need to pay 4 lakh rs donation for admmission")
    else:
        print("Sorry...! Your score is very low you can't eligiable  for admmission")
else:
    print("Sorry....! you can't eligiable for admmission")