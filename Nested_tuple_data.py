albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

for name, artist,year,songs in albums:
    print(f"Album: {name}, Artist:{artist},Year:{year},Songs:{songs}")
print()
album=albums[2]
print(album)

 #   for s in songs:
  #      print(s)
print("bellow are list of songs")
songs=album[3]
print(songs)
print("bellow is 2nd tuple in list")
song=songs[1]
print(song)
print("\n try to use for loop in songs to show songs")
i=1
for s in songs:
   # print(s)
    a,b=s
    print(f"The song number {i} is: {b}")
    i+=1

