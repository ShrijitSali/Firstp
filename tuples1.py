welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])

#metallica[0]="Master of puppets" # error: immutable
#tuples use less memory than list
#preserve intigrity of data

'''
Tuple Unpacking
'''
data=(1,2,76)
x,y,z=data
print(x)
print(y)
print(z)
'''
#list of tuples:
("More Mayhem","Imelda May", 2011,
 [#list of tuples     ::: use () instead of [] for tuple of tuples
     (1,"Pulling the Rug"),
     (2,"Psycho"),
     (3,"Mayhem"),
     (4,"Kentish Town Waltz"),
 ]

)
#use list if we dont know where data is coming from or user input data
# converting list to tuple n vice-versa is easy in python so as to change the code

'''