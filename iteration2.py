from random import randint

class Player:
    def __init__(self):
        self._counter = 10
        
    def set_counter(self, win, lose):
        if win:
            self._counter += 1
        elif lose:
            self._counter -= 1
        return self._counter

class Die:
    def __init__(self):
        self._value = None

    def set_value(self): # roll / toss
        self._value = randint(1,6)
        return  self._value
        
class DiceGame:
    def __init__(self):
        self.human = human
        self.computer = computer

    def start(self):
        print("Let the game begin!")
    
    def play(self):
        print("Round one, GO!")
        
    def quit(self):
        print(f"Game over. The winner is {winner}")



