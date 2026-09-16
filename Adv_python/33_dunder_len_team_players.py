"""
Q33. Magic Method __len__()

Create a class Team containing a list of players.
Implement:
    __len__()
so that:
    len(team)
returns the number of players.
"""


class Team:
    def __init__(self, players=None):
        if players is None:
            players = []
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def __len__(self):
        return len(self.players)


if __name__ == "__main__":
    team = Team(["Aditya", "Ravi", "Sneha"])
    print("Number of players:", len(team))

    team.add_player("Kiran")
    print("Number of players:", len(team))
