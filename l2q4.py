#program to give instruction on traffic light
Light = input("Enter the traffic light color (red, yellow, green): ").lower()
if Light == "red":
    print("Stop")
elif Light == "yellow":
    print("Slow down")
elif Light == "green":
    print("Go")