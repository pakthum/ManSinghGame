from rooms import initialize_rooms, instantiate_puzzles
from skeleton import Character

def print_help():
    print("""
Commands:
    go <north\south\east\west>
    solve <your answer>
    use <key name>
    inventory
    look
    help
    quit
""")




def main():
    rooms = initialize_rooms()
    instantiate_puzzles(rooms)

    name = input("Enter your name: ").strip() or "Adventurer"
    player = Character(name=name, starting_room=rooms["great_hall"])

    print(f"Welcome, {player.name}! Type 'help' for a list of commands.")
    player.current_room.describe()

    while True:
        cmd = input("\n> ").strip().lower()
        if cmd in ("quit", "exit"):
            print("Thanks for playing!")
            break

        if cmd.startswith("go "):
            direction = cmd.split()[1]
            player.move(direction)

        elif cmd.startswith("solve "):
            puzzles = [p for p in player.current_room.puzzles if not p.solved]
            if puzzles:
                answer = cmd[len("solve "):].strip()
                puzzles[0].attempt(answer, player)
            else:
                print("There's nothing here to solve!")

        elif cmd.startswith("use "):
            key_name = cmd[len("use "):].strip().title()
            key = next((k for k in player.inventory
                        if k.name.lower() == key_name.lower()), None)
            if key:
                unlocked = False
                for room in player.current_room.exits.values():
                    if room and room.name.lower() == key.opens_location.lower():
                        room.unlock(key)
                        unlocked = True
                        break
                if not unlocked:
                    print("That key doesn't fit any door here.")
            else:
                print("You don't have that key.")

        elif cmd == "inventory":
            player.show_inventory()

        elif cmd == "look":
            player.current_room.describe()

        elif cmd in ("help", "?"):
            print_help()

        else:
            print("I’m sorry, that command is invalid. Type 'help' to see valid commands.")

        # Check victory
        if (player.current_room.name == "The Ramharihar Temple"
            and all(p.solved for p in player.current_room.puzzles)):
            print(
                "\nYou see an ancient chest gleaming in the center—"
                "Man Singh's lost treasure is finally yours!\n\n"
                "Congratulations!"
            )
            break

if __name__ == "__main__":
    main()