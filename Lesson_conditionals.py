movie_name = "Breath"
movie_rating : int = 3
popularity_score : float = 72.65

#Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if movie_rating >= 4 and popularity_score >= 80 :
    print(movie_name,"Highly recommended")

#else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
elif movie_rating >= 3 and popularity_score > 70 :
    print(movie_name,"I recommended it . It is good")
    
#else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
elif movie_rating <= 2 and popularity_score > 60 :
    print(movie_name,"You should check it out!")

 #else  the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
else :
    print(movie_name,"Don't watch it. It is a waste of time")