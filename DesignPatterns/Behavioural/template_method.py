"""
    Purpose: Define the skeleton of an algorithm and let subclasses fill in the blanks.
"""

class Game:
    def play(self):
        self.start()
        self.play_turn()
        self.end()

    def start(self): pass
    def play_turn(self): pass
    def end(self): pass

class Chess(Game):
    def start(self): print("Chess started")
    def play_turn(self): print("Move piece")
    def end(self): print("Chess ended")

if __name__ == '__main__':
    game = Chess()
    game.play()

"""
    Pros : 
    - Code reuse.
    - Enforces algorithm structure.

    Cons:
    - Inflexible due to inheritance.
"""