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

insta = InstaDM(username='verlenedodds', password='BashNShell!!$LinuxVarechO@!', headless=True)

x = 1

for user in follow_list:
    if x<= 191:
        print("Finished already.")
        x = x + 1
    # Send message
    else:
        insta.sendMessage(user, message='Hello, my name is Verlene, I am sorry to bug you, but my friend Quinn has dissapered from social medias, and I have not been able to reach out to her, and it is important that I talk to her, due to an event with another person, if you know Quinn Carter, and have a way to contact her, please let me know, it would be extremely helpful and appreciated')
	
