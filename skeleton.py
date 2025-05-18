class Room:
    def __init__(self, name, description, exits=None, puzzles=None, items=None, locked=False):
        self.name = name
        self.description = description
        self.exits = exits if exits else {}      # dict: direction -> Room
        self.puzzles = puzzles if puzzles else []  # list of Puzzle objects
        self.items = items if items else []      # list of Key objects
        self.locked = locked                     # bool

    def describe(self):
        if self.name == "The Great Hall":
            print(f"\nYou start in {self.name}. {self.description}")
        else:
            print(f"\nYou are in {self.name}. {self.description}")
        if self.exits:
            print("Exits:", ", ".join(self.exits.keys()))
        if self.items:
            print("You see the following items:", ", ".join(item.name for item in self.items))
        unsolved = [p for p in self.puzzles if not p.solved]
        if unsolved:
            print("There's a puzzle here waiting to be solved.")
            for p in unsolved:
                print(" •", p.description)

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_puzzle(self, puzzle):
        self.puzzles.append(puzzle)

    def add_item(self, item):
        self.items.append(item)

    def unlock(self, key):
        if key.opens_location == self.name:
            self.locked = False
            print(f"\n\nThe {self.name} is now unlocked.")
        else:
            print("\n\nThat key doesn't fit here.")


class Puzzle:
    def __init__(self, description, solution, reward):
        self.description = description
        self.solution = solution
        self.reward = reward    # Key object to give upon solving
        self.solved = False

    def attempt(self, answer, player):
        if answer.strip().lower() == self.solution.lower():
            self.solved = True
            player.add_item(self.reward)
            print(f"Congratulations! You received: {self.reward.name}.")
        else:
            print("That's not correct. Try again.")


class Key:
    def __init__(self, name, opens_location):
        self.name = name
        self.opens_location = opens_location  # Room name this key unlocks


class Character:
    def __init__(self, name, starting_room):
        self.name = name
        self.inventory = []  # list of Key objects
        self.current_room = starting_room

    def move(self, direction):
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]
            if next_room is None:
                print("You can't go that way.")
            elif next_room.locked:
                print("The door is locked. You need a key to enter.")
            else:
                self.current_room = next_room
                self.current_room.describe()
        else:
            print("You can't go that way.")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} added to your inventory.")

    def show_inventory(self):
        print("\nInventory:")
        if not self.inventory:
            print("  (empty)")
        for item in self.inventory:
            print(f"- {item.name}")