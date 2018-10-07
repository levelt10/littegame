
from Game import *;

def sayHello():
    str="helloyour"
    print(str)

if __name__ == "__main__":
    sayHello();
    game = Game();
    game.build();
    game.startGame();
    game.printResult();
