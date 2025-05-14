# rooms.py

from skeleton import Room, Puzzle, Key

def initialize_rooms():
    # 1) Instantiate all rooms (descriptions empty for now)
    great_hall        = Room(name="The Great Hall",         description="Called 'Dungar Darwaza'(which roughly translates to 'Hill Gate') the main Great Hall served as the primary accsess point to Jaigarh Fort.", locked_exits={"east","west","south"})
    great_hall_north  = Room(name="The Great Hall - North", description="North side of the Great Hall")
    great_hall_west   = Room(name="The Great Hall - West",  description="West side of the Great Hall", locked=True)
    great_hall_east   = Room(name="The Great Hall - East",  description="East side of the Great Hall")
    office            = Room(name="The Office",             description="A general planning area within the Fort.")
    dining_complex    = Room(name="The Dining Complex",     description="Not much is known about this area of the fort, but it's believed to have been a designated area for royal banquets and such.", locked_exits={"north"})
    kal_bhairav_temple= Room(name="Kal Bhairav Temple",     description="Built by Kankal Dev in 1036 A.D, this temple worships the deity Kaal Bhairav, who is considered the protector of Jaigarh Fort.")
    garden            = Room(name="The Charbagh Garden",    description="Located within Jaigarh Fort, this garden is filled with lush greenery, and was said to be one of the Maharaja's favorite places.")
    observation_deck  = Room(name="The Observation Deck",   description="Located on the moutainside, this observation deck provided ample views of the surrouding area, most notably to warn of forthcoming enemies.")
    armory            = Room(name="The Armory",             description="While also being apart of the Cannon Foundry, the armory in Jaigarh Fort was famous for it's housing of different swords, spears, shields, and even early firearms which were imported and locally modified.")
    laxmi_villas      = Room(name="The Laxmi Villas",       description="This intricatly designed area was historically used for cermonial gatherings, and as an area for drawing for members of the royal family", locked_exits = {"north"})
    canon_foundry     = Room(name="The Cannon Foundry",      description="One of the biggest areas for artillery production, the Canon Foundry in Jaigarh also houses the Jaivaan Cannon, which at the time, was the world's largest canon on wheels.")
    shiv_temple       = Room(name="The Shiv Temple",        description="A temple dedicated to Lord Shiva, praying here was said to bring strength, courage, and protection tto the soilders.")
    ramharihar_temple = Room(name="The Ramharihar Temple",  description="This temple is dedicated to Lord Ram, a incarnation of Vishnu, and Harihar, constructed mostly in a Rajasthani style. It likely served as a place for prayer and worship before battles.", locked=True)

    # 2) Wire up exits once every variable exists
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

    office.exits = {
        "north": None,
        "south": None,
        "east":  None,
        "west":  great_hall_east
    }

    dining_complex.exits = {
        "north": laxmi_villas,
        "south": great_hall_west,
        "east":  great_hall_north,
        "west":  kal_bhairav_temple
    }

    kal_bhairav_temple.exits = {
        "north": None,
        "south": None,
        "east":  dining_complex,
        "west":  None
    }

    garden.exits = {
        "north": armory,
        "south": great_hall_north,
        "east":  canon_foundry,
        "west":  dining_complex
    }

    observation_deck.exits = {
        "north": canon_foundry,
        "south": great_hall,
        "east":  None,
        "west":  great_hall_north
    }

    armory.exits = {
        "north": None,
        "south": garden,
        "east":  canon_foundry,
        "west":  laxmi_villas
    }

    laxmi_villas.exits = {
        "north": ramharihar_temple,
        "south": dining_complex,
        "east":  armory,
        "west":  None
    }

    canon_foundry.exits = {
        "north": None,
        "south": observation_deck,
        "east":  shiv_temple,
        "west":  garden
    }

    shiv_temple.exits = {
        "north": None,
        "south": None,
        "east":  None,
        "west":  canon_foundry
    }

    ramharihar_temple.exits = {
        "north": None,
        "south": laxmi_villas,
        "east":  None,
        "west":  laxmi_villas  # or whichever room borders it
    }

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
###PUZZLES####

def instantiate_puzzles(rooms):
    bronze_key = Key("Bronze Key", opens_location="The Great Hall - West")
    mirror_riddle = Puzzle(
        description="Mirror Riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        solution="reflection",
        reward=bronze_key
    )
    rooms["great_hall_north"].add_puzzle(mirror_riddle)


    silver_key = Key("Silver Key", opens_location="The Laxmi Villas")
    banquet_puzzle = Puzzle(
        description="Banquet Seating: Unscramble the letters 'AJAR' to find the word the grants you entry.",
        solution="raja",
        reward=silver_key
    )
    rooms["dining_complex"].add_puzzle(banquet_puzzle)

    gold_key = Key("Gold Key", opens_location="The Ramharihar Temple")
    tile_puzzle = Puzzle(
        description="Ceremonial Tiles: Among these tiles, one bears the lotus: name it to earn your prize.",
        solution="lotus",
        reward=gold_key
    )
    rooms["laxmi_villas"].add_puzzle(tile_puzzle)