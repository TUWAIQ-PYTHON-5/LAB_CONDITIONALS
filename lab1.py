movie = "سطّار"
rate = 5
IMDB = 3
popularity_score = 72.65
if IMDB >=4 and popularity_score >= 80:
    print("Highly recommended")
elif IMDB >=3 and popularity_score >=70:
    print("I recommended it . It is good")
elif IMDB >=2 and popularity_score >=60:
    print("You should check it out!")
elif IMDB <2 and popularity_score <50:
    print("Don't watch it. It is a waste of time")
