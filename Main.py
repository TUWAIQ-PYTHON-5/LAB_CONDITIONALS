MovieName : str = "The sky"
MovieRating : int = 3
MoviePopularity : float = 72.56


if MovieRating >= 4 and MoviePopularity > 80:
    print("Highly recommended")
elif MovieRating >= 3 and MoviePopularity> 70:
    print("I recommended it . It is good")
elif MovieRating <= 2 and MoviePopularity > 60:
    print("You should check it out!")

else:
    print("Don't watch it. It is a waste of time")    
