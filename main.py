# mtg breaker v0.0.1

def main():
    #
    print("MTG Breaker for Rough Drafts")
    players = get_players()
    print(players)

def get_players():
    # get a list of all players
    print("Please enter the names of all players attending as a comma separated list.")
    players = input("--> ")
    return players.split(", ")

def tiebreakers(player_list):
    # calculate tiebreakers for all players
    pass

def pmw(match_points, rounds_played):
    # calculate player match win percentage
    return match_points / (rounds_played * 3)

def omw(arg):
    # calculate opponent match win percentage
    # omw% is the average of the pmw% of each of their opponents
    pass

def pgw(games_won, games_played):
    # calculate player game win percentage
    return games_won / games_played

def ogw(arg):
    # calculate opponent game win percentage
    # ogw% is the average of the pgw% of each of their opponents
    pass

main()
