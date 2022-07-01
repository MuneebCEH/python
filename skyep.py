from email.mime import image
from tokenize import group
from skpy import Skype
import os.path
slogin = Skype("demo@gmail.com","passwordenet")


#ch = slogin.contacts()
contact = slogin.contacts["live:.cid.2443ff3qfqe"]
with open("E:/ enter your path","rb") as f:
    contact.chat.sendFile(f,"skp.png",image=True)

# group = slogin.chats.create(["live:.cid.2443ff3qfqe","live:.cid.2443ff3qfqe"])

# contact = slogin.contacts["live:.cid.2443ff3qfqe"]
# contact.chat.sendMsg("welcome mfx mentor . ")

# for i in contact :
#     print(i)