import random
import time
import os

name1 = str(input("joueur1 entrez votre pseudo: "))
name2 = str(input("joueur2 entrez votre pseudo: "))

if name2 == name1:
    print("Choissisez un autre nom !")
while name2 == name1:
    name2 = str(input("joueur2 entrez votre pseudo: "))

turns = 4
os.system("color b")
os.system("cls")

log = []


class Joueur:
    global turns

    def __init__(self, name):
        self.tentative = None
        self.vie = 250
        self.attackd = 0
        self.attack_number = turns / 2
        self.player_name = name

    def attack(self, target):
        self.attackd = random.randint(0, 100)
        self.roll()
        if self.tentative == 1:
            target.vie -= self.attackd
            print(target.player_name + " has now " + str(target.vie) + " health")
            log.append(target.player_name + " has now " + str(target.vie) + " health")
            self.attack_number -= 1

    def roll(self):

        self.tentative = random.randint(0, 1)
        if self.tentative == 0:
            print(f" {self.player_name} missed")
            log.append(f" {self.player_name} missed")
        if self.tentative == 1:
            print(f" {self.player_name} attack with {self.attackd} pts")
            log.append(f" {self.player_name} attack with {self.attackd} pts")
            time.sleep(0.600)


# on cree les instances
joueur2 = Joueur(name2)
joueur1 = Joueur(name1)

# log stat player 1
log.append("{stats joueur1}")
log.append("nom=" + joueur1.player_name)
log.append("vie=" + str(joueur1.vie))
log.append("nombre de tour = " + str(joueur1.attack_number))

# log stat player 2
log.append("{stats joueur2}")
log.append("nom=" + joueur2.player_name)
log.append("vie=" + str(joueur2.vie))
log.append("nombre de tour = " + str(joueur2.attack_number))


def play():
    global turns
    player1_turn = True
    while turns != 0:
        if player1_turn:
            joueur1.attack(joueur2)
            time.sleep(3)
            os.system("cls")
            player1_turn = False
            turns -= 1
        if not player1_turn:
            joueur2.attack(joueur1)
            time.sleep(3)
            os.system("cls")
            player1_turn = True
            turns -= 1

        if joueur1.vie > joueur2.vie:
            winner_message = f"the player {name1} won"

        elif joueur1.vie == joueur2.vie:
            winner_message = "It's draw"

        elif joueur1.vie <= 0:
            winner_message = f"the player {name2} won"

        elif joueur2.vie <= 0:
            winner_message = f"the player {name1} won"

        else:
            winner_message = f"the player {name2} won"

        if joueur2.attack_number <= 0:
            print(winner_message)
            log.append(">>>>>" + winner_message + "<<<<<")
            time.sleep(3)
            os.system("start game_log.txt")


play()
log = "\n\n".join(log)
with open("game_log.txt", "w") as f:
    f.write(str(log))

