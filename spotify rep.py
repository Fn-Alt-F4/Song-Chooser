

#Spotify replicate
#Goal is to create a login
#Then create multiple playlists with a random song selecter / song randomizer
#Then create multiple playlists and randomize which playlist is on
#Also create the ability to log out
#Allow user to select songs specifically out of the playlist

#Step 1 create the login

username = "evan22"

password = "edogg586"

while True:
    typed_username = input("username:")
    typed_password = input("password:")

    if typed_username == username and typed_password == password :
        print("Correct!")
        break
    else :
        print("Incorrect!")

###########################################

#Create playlist number 1

playlist_1 = ["Thriller" , "Sympathy for the devil" , "Horse with no name" , "Beat it" "We are the people"]

#Now we want random songs selected

import random

print(playlist_1 = random)

############################################

#Create playlist 2

playlist_2 = ["First day out" , "from the D to the A" , "Pressure" , "Nervous" , "In and out" , "Losing my mind" , "Goyard"]

#Now we want to randomize songs

print(playlist_2 = random)

############################################

#Create playlist 3

playlist_3 = ["Finish the fight" , "Covenant dance" , "The pillar of autumn" , "Winter contingencey" , "Overture" , "The great journey" , "New Alexandria"]

#Now we want to randomize songs

print(playlist_3 = random)

############################################

random_playlist = (playlist_1 + playlist_2 + playlist_3 [random])

user_select = (random_playlist)

if user_select == input(random_playlist) :
    print("nice playlist choice!")
else :
    print("Thats not a song on the playlist")

#############################################

#Now we want the user to be able to select a song from a playlist

random_playlist_diff = ("playlist_1 , playlist_2 playlist_3")

userselect1 = playlist_1

userselect2 = playlist_2

userselect3 = playlist_3

if userselect1 == playlist_1[0 : 3] :
    print("Great song choice!")
else :
    print("Other playlist was selected.")

if userselect2 == playlist_2[0 : 6] :
    print("Great song choice!")
else : 
    print("User chose other playlist")

if userselect3 == playlist_3[0 : 7] :
    print("Great song choice!")
else : 
    print("Other playlist was chosen")

#############################################

#Now we want the user to be able to log out

logout = "user has selected to logout"

input_logout = input(logout)

if input_logout == logout :
    print("user has logged out.")
else:
    print("not logged out")
