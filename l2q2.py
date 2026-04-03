#if a given year leap year
Year =int(input("Enter a year: "))
if Year % 4 == 0 :
    if Year % 100 != 0:
        print(f"{Year} is a leap year")
else:
    print(f"{Year} is not a leap year")
