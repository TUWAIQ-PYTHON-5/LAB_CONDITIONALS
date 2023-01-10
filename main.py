movie:str="Interstellar"
rating:int=3
popularScore:float=72.65

if rating >= 4 and popularScore > 80:
    print ("Highly recommended")
elif rating >= 3 and popularScore > 70:
    print ("I recommended it . It is good")
elif rating <= 2 and popularScore > 60:
    print ("You should check it out!")
elif rating <= 2 and popularScore < 50:
    print ("Don't watch it. It is a waste of time")

