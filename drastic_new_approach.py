from random import randint


class Die:
    def __init__(self):
        self.value = None

    def roll(self):
        value = randint(1,6)
        return value
    

class Player:
    def __init__(self, Dice):
        self.die_inst = Dice
        self.computer = computer
        self.human = human
        self.counter = 10

    def set_win(self):
        self.counter -= 1
        return self.counter
    
    def set_lose(self):
        self.counter += 1
        return self.counter
    
    def get_roll(self, Die):
        return Die.roll

def play():
    print("Welcome to the OOP dice game!")
    while Player.counter != 0:
        self.start_round()
        continue
    print("Game Over!")


def start_round(self):
    
    print("Let this round begin.")

    dice_roll1 = Player.get_roll
    dice_roll2 = Player.get_roll
    
    while self.human:
        
        print(f"Current score \n 
                - human: {self.human.counter} and computer: {self.computer.counter}")
        
        if dice_roll1 > dice_roll2:
            self.human.set_win
            print(f"Round winner is {self.human}")
            
        elif dice_roll1 < dice_roll2:
            self.computer.set_win
            print(f"Round winner is {self.computer}")
        
        elif dice_roll1 == dice_roll2:
            print("Tie. Play another round.")

        continue

dice_game = play()