MovieName = ("Inolla hlomes")
MovieRating :int = 3
PopularityScore : float = 72.65


if MovieRating >=4 and PopularityScore > 80 :
    print("Highly recommended !!! ")
elif MovieRating >=3 and PopularityScore > 70 :
    print(" recommended it . It is good ")
elif MovieRating <=2 and PopularityScore > 60 :
    print(" You should check it out!")
else :
    print(" Don't watch it. It is a waste of time ")



