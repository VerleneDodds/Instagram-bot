# Get instance
import instaloader
import os

L = instaloader.Instaloader()

# Login or load session
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
# (likewise with profile.get_followers())

os.system('cls' if os.name == 'nt' else 'clear')

print(follow_list)

