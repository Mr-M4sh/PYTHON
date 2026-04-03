#working weekends 
Day = input("Enter the day of the week: ").lower()
if Day in ["saturday", "sunday"]:
    print("You are  on the weekend.")
elif Day in [ "tuesday", "wednesday", "thursday"]:
    print("midweek")
elif Day == "firday":
    print("Almost Weekend")
elif Day =="monday":
    print("start of weekend ")
else:
    print("invalid")