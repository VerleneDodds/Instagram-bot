from instadm import InstaDM
import instaloader
import os

#Gather followers
L = instaloader.Instaloader()

username = "verlenedodds"
password = "BashNShell!!$LinuxVarechO@!"
L.login(username, password)  # (login)

profileusers = "mountainviewhighschool"

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, profileusers)

# Print list of followees
follow_list = []
count = 0
for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open("prada_followers.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count = count + 1
    
os.system('cls' if os.name == 'nt' else 'clear')
    
# Message Followers
# Auto login

insta = InstaDM(username='verlenedodds', password='BashNShell!!$LinuxVarechO@!', headless=False)


for user in follow_list:	
    # Send message
    insta.sendMessage(user, message='This is a message to verify that the bot works!')
	
# Send message
#insta.sendGroupMessage(users=['user1', 'user2'], message='Hey !')