Movie = "Venom"
Rating = 3 #out of 5
Popularity = 72.65 #out of 100

if Rating >= 4 and Popularity > 80.0:
    print("Highly recommended")
elif Rating >= 3 and Popularity > 70.0:
    print("I recommended it . It is good")
elif Rating <= 2 and Popularity > 60.0:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")
