def main():
    #
    print("MTG Breaker for Rough Drafts")
    print("Enter file name (without file extension):")
    file_name = input("--> ")
    try:
        with open(file_name + ".txt") as f:
            for line in f:
                process(line)
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Something went wrong.")

def process(line):
    # name: 2, name: 1
    x = line.split(", ")

class Player:
    def __init__(self, name):
        self.name = name
        self.opponents = []


main()
