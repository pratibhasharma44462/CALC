sum = 0
while True:
    user_input = (input("ENTER THE ITEM VALUE =  "))
    if user_input != "q" and user_input !="Q":
        sum = sum  + int(user_input)

    else:
        print(f"THANKS FOR USING IT = {sum}")
        break
