channel_id = "" # what channel to start in
route = 3 # 1, 2, 3, 4
auto_evolve = True # auto evolve your pokemon
token = "" # user token

#######################################
import discum
import time
import random

bot = discum.Client(token=token, log=True)

@bot.gateway.command
def main(msg):
    # ready
    if msg.event.ready_supplemental:
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    
    # on message
    if msg.event.message:
        m = msg.parsed.auto()
        if (m['channel_id'] != channel_id): return

        
        #content = m['content']

bot.gateway.run(auto_reconnect=True)