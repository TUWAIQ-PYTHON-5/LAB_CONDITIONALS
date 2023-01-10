movie = "friends"
ratmovie = 3
popularscor = 72.65
if ratmovie >= 4 and popularscor > 80:
    print(movie,"Highly recommended")
elif ratmovie >= 3 and popularscor > 70:
    print(movie, "I recommended it . It is good") 
elif ratmovie <= 2 and popularscor > 60:
    print(movie,"You should check it out!")
else : 
    print(movie,"Don't watch it. It is a waste of time")
