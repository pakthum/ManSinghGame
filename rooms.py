from skeleton import Room, Puzzle, Key

def initialize_rooms():
    """
    Create every Room, set locked flags, and wire up exits.
    Returns a dict mapping room identifiers to Room instances.
    """
    # 1) Instantiate rooms (name, description, locked state)
    great_hall         = Room(
        name="The Great Hall",
        description=(
            "Called 'Dungar Darwaza' (which roughly translates to 'Hill Gate'), "
            "the main Great Hall served as the primary access point to Jaigarh Fort."
        ),
        locked=False
    )
    great_hall_north   = Room(
        name="The Great Hall - North",
        description="The north side of the Great Hall, its walls lined with faded murals.",
        locked=False
    )
    great_hall_west    = Room(
        name="The Great Hall - West",
        description="The west wing of the Great Hall, once used by royal guards.",
        locked=True    # locked until Bronze Key is used
    )
    great_hall_east    = Room(
        name="The Great Hall - East",
        description="The east wing of the Great Hall, overlooking the valley below.",
        locked=False
    )
    office             = Room(
        name="The Office",
        description="A planning room where Man Singh and his commanders once met.",
        locked=False
    )
    dining_complex     = Room(
        name="The Dining Complex",
        description=(
            "Believed to have hosted royal banquets, now dusty tables "
            "and broken chairs litter the floor."
        ),
        locked=False
    )
    kal_bhairav_temple = Room(
        name="Kal Bhairav Temple",
        description=(
            "Built in 1036 A.D., this temple honors Kaal Bhairav, "
            "protector deity of the fort."
        ),
        locked=False
    )
    garden             = Room(
        name="The Charbagh Garden",
        description=(
            "A sunken garden of symmetrical flower beds, once the Maharaja's "
            "private retreat."
        ),
        locked=False
    )
    observation_deck   = Room(
        name="The Observation Deck",
        description=(
            "Perched on the mountainside, offering panoramic views of the plains "
            "below."
        ),
        locked=False
    )
    armory             = Room(
        name="The Armory",
        description=(
            "Filled with racks of swords, spears, shields, and even early firearms "
            "that were locally modified."
        ),
        locked=False
    )
    laxmi_villas       = Room(
        name="The Laxmi Villas",
        description=(
            "An ornate pavilion used for ceremonies and scholarly gatherings."
        ),
        locked=True    # locked until Silver Key is used
    )
    canon_foundry      = Room(
        name="The Cannon Foundry",
        description=(
            "The heart of artillery production — home to the mighty Jaivaan Cannon."
        ),
        locked=False
    )
    shiv_temple        = Room(
        name="The Shiv Temple",
        description=(
            "Dedicated to Lord Shiva, soldiers came here seeking strength "
            "and protection."
        ),
        locked=False
    )
    ramharihar_temple  = Room(
        name="The Ramharihar Temple",
        description=(
            "A Rajasthani-style shrine to Lord Ram and Harihar — "
            "your final destination for Man Singh’s lost treasure."
        ),
        locked=True    # locked until Gold Key is used
    )

    # 2) Wire up exits
    great_hall.exits = {
        "north": great_hall_north,
        "south": None,
        "east":  great_hall_east,
        "west":  great_hall_west
    }
    great_hall_north.exits = {
        "north": garden,
        "south": great_hall,
        "east":  observation_deck,
        "west":  dining_complex
    }
    great_hall_west.exits = {
        "north": dining_complex,
        "south": None,
        "east":  great_hall,
        "west":  None
    }
    great_hall_east.exits = {
        "north": observation_deck,
        "south": None,
        "west":  great_hall,
        "east":  office
    }
    office.exits = {"north": None, "south": None, "east": None, "west": great_hall_east}
    dining_complex.exits = {
        "north": laxmi_villas,
        "south": great_hall_west,
        "east":  great_hall_north,
        "west":  kal_bhairav_temple
    }
    kal_bhairav_temple.exits = {"north": None, "south": None, "east": dining_complex, "west": None}
    garden.exits = {"north": armory, "south": great_hall_north, "east": canon_foundry, "west": dining_complex}
    observation_deck.exits = {"north": canon_foundry, "south": great_hall, "east": None, "west": great_hall_north}
    armory.exits = {"north": None, "south": garden, "east": canon_foundry, "west": laxmi_villas}
    laxmi_villas.exits = {"north": ramharihar_temple, "south": dining_complex, "east": armory, "west": None}
    canon_foundry.exits = {"north": None, "south": observation_deck, "east": shiv_temple, "west": garden}
    shiv_temple.exits = {"north": None, "south": None, "east": None, "west": canon_foundry}
    ramharihar_temple.exits = {"north": None, "south": laxmi_villas, "east": None, "west": None}

    # 3) Return the room map
    return {
        "great_hall": great_hall,
        "great_hall_north": great_hall_north,
        "great_hall_west": great_hall_west,
        "great_hall_east": great_hall_east,
        "office": office,
        "dining_complex": dining_complex,
        "kal_bhairav_temple": kal_bhairav_temple,
        "garden": garden,
        "observation_deck": observation_deck,
        "armory": armory,
        "laxmi_villas": laxmi_villas,
        "canon_foundry": canon_foundry,
        "shiv_temple": shiv_temple,
        "ramharihar_temple": ramharihar_temple
    }


def instantiate_puzzles(rooms):
    """
    Attach main-quest puzzles (and their keys) to the appropriate rooms.
    """
    # Puzzle 1 (mirror riddle → Bronze Key)
    bronze_key   = Key("Bronze Key", opens_location="The Great Hall - West")
    mirror_riddle = Puzzle(
        description=(
            "\nMirror Riddle: I speak without a mouth and hear without ears. "
            "I have no body, but I come alive with wind. What am I?"
        ),
        solution="reflection",
        reward=bronze_key
    )
    rooms["great_hall_north"].add_puzzle(mirror_riddle)

    # Puzzle 2 (banquet seating → Silver Key)
    silver_key     = Key("Silver Key", opens_location="The Laxmi Villas")
    banquet_puzzle = Puzzle(
        description="Banquet Seating: Unscramble the letters 'AJAR' to find the word that grants you entry.",
        solution="raja",
        reward=silver_key
    )
    rooms["dining_complex"].add_puzzle(banquet_puzzle)

    # Puzzle 3 (tile pattern → Gold Key)
    gold_key    = Key("Gold Key", opens_location="The Ramharihar Temple")
    tile_puzzle = Puzzle(
        description="Ceremonial Tiles: Among these tiles, one bears the lotus—name it to earn your prize.",
        solution="lotus",
        reward=gold_key
    )
    rooms["laxmi_villas"].add_puzzle(tile_puzzle)