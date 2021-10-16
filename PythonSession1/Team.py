from Player import Player

player1 = Player("Shardul", "26", 45.12, 21.21)
player2 = Player("Virat", "26", 45.12, 21.21)
player3 = Player("Dhoni", "26", 45.12, 21.21)

listOfPlayers = [player1, player2, player3]

for player in listOfPlayers:
    player.myfunc()