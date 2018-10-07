import string;
class Player:
    def __init__(self, id):
        self.id = id;
        self.cards = [];
        return;

    def addCard(self, card):
        self.cards.append(card);

    def setCards(self, cards):
        self.cards = cards;

    def removeCard(self, card):
        for c in self.cards:
            if c.point == card.point:
                self.cards.remove(c);
                return;

    def printCards(self):
        print (self.id);
        for c in self.cards:
            print(c.point);

    def findCard(self, point):
        for c in self.cards:
            if c.point == point:
                return c;
        return None;

    def putCard(self):
        self.printCards();
        str = raw_input("select card:");
        nPoint = string.atoi(str)
        card = self.findCard(nPoint);
        while card is None :
            self.printCards();
            str = raw_input("select card:");
            nPoint = string.atoi(str)
            bFind = self.findCard(nPoint);
        self.removeCard(card);
        return card
