movie_name :str = "Taken "
movie_rate : int = 3
popularity_score :float = 72.75
if 4<= movie_rate and popularity_score > 80 :
    print("Highly recommended")

elif 3<= movie_rate  and   popularity_score >70 :
    print("It is good")

elif 2>= movie_rate and popularity_score >60 :
    print("You should check it out!")

else: 
  print("Don't watch it It is a waste of time")