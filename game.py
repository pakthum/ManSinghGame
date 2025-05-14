from rooms import initialize_rooms, instantiate_puzzles
from skeleton import Character

def main():
    rooms = initialize_rooms()
    instantiate_puzzles(rooms)


    player = Character(name="Your Name", starting_room=rooms["grat_hall"])




    if __name__ == "__main__":
        main()
