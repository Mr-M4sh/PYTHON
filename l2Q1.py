# Total program 
User =int(input("Enter your purchase amount: "))
final = 0
if User >= 10000:
    final = User - (User * 0.20)
    discount = User * 0.20
    print(f"Your Total is {final} and discount is{discount}")
elif User >= 5000 and User < 10000:
    final = User - (User * 0.10)
    discount = User * 0.10
    print(f"Your Total is {final} and discount is {discount}")
elif User < 5000:
    print(f"Your Total is No Discount {User} ")
else:
    print("Invalid input")