movie = "split"
rate : int = 3
popularity : float = 72.65

if rate >= 4 and popularity > 80 :
    print (movie," Highly recommended")
elif rate >= 3 and popularity > 70 :
        print (movie," I recommended it . It is good")
elif rate <= 2 and popularity > 60 :
        print (movie," You should check it out!")
elif rate <= 2 and popularity < 50 :
        print (movie," Don't watch it. It is a waste of time")
else:
    print ("find a new movie")
    

