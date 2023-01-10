monvieName:  str   = "Reach the Rock"
movieRating: int   = 2
moviePop:    float = 52.65

if movieRating >= 4 and moviePop >= 80.0:
    print("Highly recommended")
elif movieRating >=3 and moviePop >= 70.0:
    print("It is good")
elif movieRating <=2 and moviePop >= 60.0:
    print("You should check it out")
elif movieRating <=2 and moviePop <= 50:
    print("Don't watch it. It is waste of time")

