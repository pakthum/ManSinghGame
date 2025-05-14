class Room:
    def __init__(self, name, description, exits=None, puzzles=None, items=None, locked=False):
        self.name = name
        self.description = description
        self.exits = exits if exits else {}
        self.puzzles = puzzles if puzzles else []
        self.items = items if items else []
        self.locked = locked

    def describe(self):
        print(f"You find yourself in {self.name}. {self.description}")
        if self.exits:
            print("Exits:", ", ".join(self.exits.keys()))
        if self.items:
            print("You see the following items:", ", ".join(item.name for item in self.items))
        if any(not p.solved for p in self.puzzles):
            print("There's a puzzle here waiting to be solved.")

    def add_exit(self, direction, room):
        self.exits[direction] = room
    
    def add_puzzle(self, puzzle):
        self.puzzles.append(puzzle)

    def add_item(self, item):
        self.items.append(item)

    def unlock(self, key):
        if key.opens_location == self.name:
            self.locked = False
            print(f"The {self.name} is now unlocked! You may proceed.")
        else:
            print("That key doesn't fit here!")


class Puzzle:
    def __init__(self, description, solution, reward):
        self.description = description
        self.solution = solution
        self.reward = reward
        self.solved = False

    def attempt(self, answer, player):
        if answer.strip().lower() == self.solution.lower():
            self.solved = True
            player.add_item(self.reward)
            print(f"Congragulations! You recieved: {self.reward.name}.")
        else:
            print("That's not right! Try again!")

class Key:
    def __init__(self, name, opens_location):
        self.name = name
        self.opens_location = opens_location 


class Character:
    def _init_(self, name, starting_room):
        self.name = name
        self.inventory = []
        self.current_room = starting_room

    def move(self, direction):
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]
            if next_room.locked:
                print("This door is locked. Find a key to get in!")
            else:
                self.current_room = next_room
                self.current_room.describe()
        else:
            print("You can't go that way!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} added to your inventory!")

    def show_inventory(self):
        print("\nInventory:")
        if not self.inventory:
            print(" (empty)")
        for item in self.inventory:
            print(f"-{item.name}")

if __name__ == "__main__":
    pass


