#main.py
temp = int(input("What is the temperature?"))
if(temp > 120):
    print("\nOh boy it is HOT!!!")

elif(temp > 70):
    print("\nStill too hot for my liking, but livable")
    print("\nWear shorts")

elif(temp > 35):
    print("\nJust how I like it.")
    print("\nLight Jacket and Pants weather.")

elif(temp <= 35):
    print("\nIt is getting colder.")
    print("\nBetter consider wearing heavier and warmer clothing")

else:
    print("\nWhy are you outside and not near the fire")