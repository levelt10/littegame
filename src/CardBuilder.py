
from Card import *;
import random;


class CardBuilder:
    def __init__(self):
        return;

    def buildCards(self, totalNum, cardCount, playerCount):
        cardss = [];
        rlist = [];
        for pi in range(playerCount):
            cards = [];
            for ci in range(cardCount):
                p = random.randint(0, 50);

                i = 0;
                while ((p in rlist) and i < 50):
                    p = random.randint(0, 50);
                    ++i;

                c = Card(p)
                cards.append(c)
            cardss.append(cards);

        return cardss;


if __name__ == "__main__":
    testCase = CardBuilder();
    lstCardList = testCase.buildCards(100, 3, 2);