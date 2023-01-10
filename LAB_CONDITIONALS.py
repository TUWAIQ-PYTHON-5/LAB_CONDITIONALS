far_movie = "BATMAN"

evaluation : int= 3.5
evaluation2 : float = 72.65


if evaluation >= 4 and evaluation2 < 80:
    print("Highly recommend!")
elif evaluation >= 3 and evaluation2 > 70:
    print("l recommend it")
elif evaluation <= 2 and evaluation2 > 60:
    print("You should check it out!")
elif evaluation <= 2 and evaluation2 < 50:
    print("Don't watch it")
else:
    print("find a new movie")
