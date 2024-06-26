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
        self.player_type = True # True = human (default) or False = computer
        self.counter = 10

    def set_win(self):
        self.counter -= 1
        return self.counter
    
    def set_lose(self):
        self.counter += 1
        return self.counter
    
    def get_roll(self, Die):
        return Die.roll

class DiceGame(Die,Player):

    def __init__(self,player_type):
        self.human = Player.player_type # True
        self.computer = Player.player_type # False


    def play(self):
        print("Welcome to the OOP dice game!")
        while self.counter != 0:
            self.start_round()
            continue
        print(f"Game Over! The winner is {self.Player.counter==0}")


    def start_round(self):
        input("Press any key to begin the (next) round.")

        dice_roll1 = Player.get_roll
        dice_roll2 = Player.get_roll
        
        while self.human:
            
            print(f"Current score \n 
                  - human: {self.human.counter} and computer: {self.computer.counter}")
            
            if dice_roll1 > dice_roll2:
                self.human.set_win
                self.computer.set_lose
                print(f"Round winner is {self.human}")
                
            elif dice_roll1 < dice_roll2:
                self.computer.set_win
                self.human.set_lose
                print(f"Round winner is {self.computer}")
            
            elif dice_roll1 == dice_roll2:
                print("Tie. Play another round.")

            continue




        