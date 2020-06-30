from skpy import Skype
import config as cfg

# Group id (extracted from skype web)
ml = '19%3A4ed8966c8b2c4b248a8b2194440dd06f%40thread.skype'
arena = '19%3Aa426a4a9ffca4189924b1ee2980b53e1%40thread.skype'

sk = Skype(cfg.username, cfg.password) # connect to Skype

channel = sk.chats.chat(ml)
channel.sendMsg('Hello! This is my second automatic message.')

# contacts = sk.contacts
# for contact in contacts:
#     print(contact.id, contact.name)
    
# content = 'Hello'
# ch = sk.contacts["shivazibiswas22"].chat # 1-to-1 conversation
# ch.sendMsg(content) # plain-text message


"""
    Reference:
        1. https://qxf2.com/blog/posting-messages-on-a-skype-group-channel-using-python/
        2. https://skpy.t.allofti.me/index.html
"""