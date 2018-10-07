
class Turn:
    def __init__(self):
        self.players = [];
        return

    def addPlayer(self, player):
        self.players.append(player)

    def start(self):
        trunRecord = {};
        winer = None;
        winerCard = None;
        for i in range(len(self.players)):
            player = self.players[i];
            card = player.putCard();
            trunRecord[player] = card;
            if winer is None:
                winer = player;
                winerCard = card;
            else:
                if card.point > winerCard.point:
                    winer = player;
                    winerCard = card;

        return winer