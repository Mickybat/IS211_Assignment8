import random
import time
import datetime
correct = 0
start = datetime.datetime.now()


def throw_die(sides=6):
    """
    Function to simulate a throw of a die
    """
    return random.randint(1, sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.turn_total = 0
        self.roll_hold = 'r'

    def __str__(self):
        return f"{self.name}'s Total = {self.total}"

    def play(self):
        """Represents a player's turn"""
        self.turn_total = 0
        self.roll_hold = 'r'
        while self.roll_hold != 'h':
            die = throw_die()
            print(self.name + " Rolled a " + str(die))
            if die == 1:
                break
            self.turn_total += die
            print(
                f"{self.name} Turn Total = {self.turn_total}, "
                f"{self.name} Total = {self.total}, "
                f"Possible {self.name} Total = {self.total + self.turn_total}"
            )
            # automatically finish the game when it reaches 100
            if self.total + self.turn_total >= 100:
                self.roll_hold = 'h'
                break

            self.roll_hold = input("Roll(r) or Hold(h)?").lower()

        if self.roll_hold == 'h':
            self.total += self.turn_total

        print(f"{self.name} Total = {self.total}")


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        """Represents computer's turn"""
        self.turn_total = 0
        self.roll_hold = 'r'
        while self.roll_hold != 'h':
            die = throw_die()
            print(self.name + " Rolled a " + str(die))
            if die == 1:
                break
            self.turn_total += die
            print(
                f"{self.name} Turn Total = {self.turn_total}, "
                f"{self.name} Total = {self.total}, "
                f"Possible {self.name} Total = {self.total + self.turn_total}"
            )

            if self.total + self.turn_total >= 100:
                self.roll_hold = 'h'
                break

            if self.turn_total > 25 or (100 - self.total) < 25:
                self.roll_hold = 'h'
            else:
                self.roll_hold = 'r'

        if self.roll_hold == 'h':
            self.total += self.turn_total

        print(f"{self.name} Total = {self.total}")


class PlayerFactory:

    def __init__(self):
        self.num_players = 0

    def get_player(player_type):
        if player_type == "computer":
            return ComputerPlayer("CPU")

        elif player_type == "human":
            return Player(input("What is the name for this player?: "))


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None

    def check_winner(self):
        """
        Returns true if there is a winner and set the winner
        :return:
        """

        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True

    def play_game(self):

        current_player = self.players[0]

        while not self.check_winner():
            # play the game
            current_player.play()

            # find out how to switch players
            if current_player == self.players[0]:
               current_player = self.players[1]
            else:
                current_player = self.players[0]

        print(self.winner.name + " wins")


class TimedGameProxy(Game):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)

    def check_winner(self):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S")
        print(current_time)

        for player in self.players:
            while player.total >= 100:
                self.winner = player
                return True

    def play_game(self):
        total = 0
        current_player = self.players[0]

        while not self.check_winner():
            # play the game
            current_player.play()

            # find out how to switch players

            if current_player == self.players[0]:
               current_player = self.players[1]
            else:
                current_player = self.players[0]
            if (datetime.datetime.now() - start).seconds > 60:
                print("The scores are:" + str(self.players[0].total) + " " + str(self.players[1].total))
                if self.players[0].total > self.players[1].total:
                    print(str(self.players[0].name) + "" + " is the winner!")
                else:
                    print(str(self.players[1].name) + "" + " is the winner!")
                return print("GAME OVER!!!")

        print(self.winner.name + " wins")


if __name__ == "__main__":
    computer = PlayerFactory.get_player("computer")
    human = PlayerFactory.get_player("human")
    pig_game = TimedGameProxy(human, computer)
    pig_game.play_game()