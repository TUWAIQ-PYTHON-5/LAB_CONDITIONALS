#for if statment 

''' Ex 1   
The date June 10, 1960, is special because when it is written in the following format, the month times the day equals the year:  
6/10/60  Design a program that asks the user to enter a month (in numeric form), a day, and a two digit year. The program should then determine whether the month times the day equals the year. If so, it should display a message saying the date is magic. Otherwise, it should display a message saying the date is not magic. 
'''
month=int(input("enter the month:" ))
if month >= 1 and month<=3 :
    print("1st quarter")
elif month >= 4 and month <=6 :
    print("2nd quarter")
elif month >= 7 and month <=9 :
    print("3rd quarter")
elif month >= 10 and month <=12 :
    print("4th quarter")
else :
    print("not quarter")








# Ex 2
'''
Write a program that asks the user for a month as a number between 1 and 12. The program should display a message indicating whether the month is in the first quarter, the second quarter, the third quarter, or the fourth quarter of the year.  
Following are the guidelines: 
If the user enters either 1, 2, or 3, the month is in the first quarter. 
If the user enters a number between 4 and 6, the month is in the second quarter. 
If the number is either 7, 8, or 9, the month is in the third quarter. 
If the month is between 10 and 12, the month is in the fourth quarter.  If the number is not between 1 and 12, the program should display an error 


'''
mon=int(input("your moth :" ))
day=int(input("your day :" ))
year=int(input("your year :" ))
if mon * day == year :
    print("magical date")
else :
    print("not magical")

