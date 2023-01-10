MovieName : str = "The sky"
MovieRating : int = 2
MoviePopularity : float = 40


if MovieRating >= 4 and MoviePopularity > 80:
    print("Highly recommended")
elif MovieRating >= 3 and MoviePopularity> 70:
    print("I recommended it . It is good")
elif MovieRating <= 2 and MoviePopularity > 60:
    print("You should check it out!")
elif MovieRating <= 2 and MoviePopularity < 50:
    print("Don't watch it. It is a waste of time") 
else:
    print("please Check a real movie")    
