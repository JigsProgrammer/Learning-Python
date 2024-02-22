temperature = 25

if temperature > 30:
    print("It's a hot day") #"" used bc. there is ' in sentence
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else: #this is used as the last option if none of the ^ are true
    print("It's cold")
print("Done")