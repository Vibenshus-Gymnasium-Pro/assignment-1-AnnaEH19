sandwich_orders = ['Ham sandwich', 'Tuna sandwich', 'Egg and bacon sandwich']
finished_sandwiches = []

while sandwich_orders:
        sandwiches = sandwich_orders.pop()

        print("Your " + sandwiches.title() + " has been made.")
        finished_sandwiches.append(sandwiches)

print("\nThe following sandwiches has been made:")
for finished_sandwiches in finished_sandwiches:
        print(finished_sandwiches.title())