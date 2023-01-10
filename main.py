Movie_Name: str = "breaking bad"
Movie_Rating: int = 4
Movie_popularity: float = 72.65
if Movie_Rating >=4 and Movie_popularity > 80:
    print ("Highly recommended")
elif Movie_Rating >=3 and Movie_popularity > 70:
    print ("I recommended it . It is good")
elif Movie_Rating >=2 and Movie_popularity > 60:
    print ("You should check it out!")
else :
    print ("Don't watch it. It is a waste of time")

