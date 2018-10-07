from Turn import *;
from Player import *;
from CardBuilder import *;
from Card import *;


class Game:
    def __init__(self):
        self.record = {};
        self.turns = [];
        return;

    def build(self):
        cardBuilder = CardBuilder();
        player1 = Player("dy");
        player2 = Player("dw");
        self.record[player1] = 0;
        self.record[player2] = 0;

        cardss = cardBuilder.buildCards(200, 3, 2);
        player1.setCards(cardss[0]);
        player2.setCards(cardss[1]);

        nTurnCount = 3;
        for i in range(nTurnCount):
            oneTurn = Turn();
            oneTurn.addPlayer(player1);
            oneTurn.addPlayer(player2);
            self.turns.append(oneTurn);

    def startGame(self):
        for i in range(len(self.turns)):
            turn = self.turns[i];
            winner = turn.start();
            n = self.record[winner];
            self.record[winner] = n + 1;

    def printResult(self):
        for player in self.record.keys():
            sc = self.record[player];
            print(player.id + " get " + str(sc))


