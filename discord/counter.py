channel_id = "" # what channel to start in
token = "" # user token

import discum
import time
import random

bot = discum.Client(token=token, log=False)

@bot.gateway.command
def main(msg):
    # ready
    if msg.event.ready_supplemental:
        num = 1720

        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))

        while(True):
            num = num + 1
            bot.sendMessage(channel_id, str(num))
            time.sleep(random.uniform(1, 1.5))

bot.gateway.run(auto_reconnect=True)