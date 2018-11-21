all_players = []

def main():
    #


    print("MTG Breaker for Rough Drafts")
    print("Enter file name:")
    file_name = input("--> ")
    with open(file_name) as f:
        for line in f:
            process(line.strip())

    print(all_players)

def process(line):
    # line -> "name: 2, name: 1"
    get_players(line)

def get_players(line):
    player_and_score = line.split(", ")
    for i in player_and_score:
        player_name = i[:-3]
        if player_name not in all_players:
            all_players.append(player_name)


class Player(object):
    def __init__(self, name):
        self.name = name
        self.opponents = []


main()
