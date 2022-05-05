from template import Agent
import random


class myAgent(Agent):
    def __init__(self,_id):
        super().__init__(_id)
    
    def SelectAction(self,actions,game_state):
        print("lkalalal1111111111")
        return random.choice(actions)
