# This is the main file where you control your bot's strategy

#Chickens - These mean get everything
from util.objects import *
from util.routines import *

# Hi! Corbin here. Note the line below says GoslingUtils in the videos.
# DO NOT change the line below. It's no longer compatible with GoslingUtils so we renamed it.
# There are a few places like this where the code that you started with (the code you downloaded) might
# look different than the videos. THAT'S OK! Don't change it. We've made it better over time.
# Just follow along with the videos and it will all work the same.
class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        #This will be true or false
        if self.kickoff_flag:
            # set_intent tells the bot what it's trying to do
            self.set_intent(kickoff())
            return
        #if in front of ball, retreat
        self.set_intent(short_shot(self.foe_goal.location))
        self.set_intent(atba())


#In Progress
"""class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.kickoff_flag:  #Determines whether is actually kickoff time
            self.set_intent(Ekickoff())
            return"""