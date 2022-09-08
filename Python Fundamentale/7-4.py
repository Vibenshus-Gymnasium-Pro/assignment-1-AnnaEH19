print("What would you like on your pizza")
print("Write which toppings you would like.")
print("When you are done write 'quit' and the press ENTER.")
prompt = "\nWrite your toppings here: "

toppings = ""
while toppings != 'quit':
        toppings = input(prompt)
        print(toppings + " is added to your pizza")



