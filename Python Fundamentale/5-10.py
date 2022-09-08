current_users = ['Tom', 'Ewa', 'Steve', 'Garreth', 'Joe', 'Curd']

new_users = ['Jake', 'Michael', 'Jim', 'Ewa', 'Margreth', 'Steve']

for new_users in new_users:
    if new_users in current_users:
        print(new_users + ": " + "Brugernavnet er allerede i brug. Vælg et andet")
    else:
        print(new_users + ": " + "Brugernavnet er tilgængeligt")
