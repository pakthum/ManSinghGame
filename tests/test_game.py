import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))


import pytest
from rooms import initialize_rooms, instantiate_puzzles
from skeleton import Character, Room, Puzzle, Key

@pytest.fixture
def world():
    rooms = initialize_rooms()
    instantiate_puzzles(rooms)
    return rooms

def test_room_exits(world):
    gh = world["great_hall"]
    assert "north" in gh.exits, "Great Hall should have 'NORTH' in it's exits"
    assert isinstance(gh.exits["north"], Room)

def test_initial_player_position(world):
    player = Character("TESTER", world["great_hall"])
    assert player.current_room is world["great_hall"]

def test_puzzle_attached_to_north_room(world):
    north_room = world["great_hall_north"]
    puzzles = [p for p in north_room.puzzles if isinstance(p, Puzzle)]
    assert len(puzzles) == 1
    assert puzzles[0].solution == "reflection"

def test_solving_puzzle_gives_reward(world):
    player = Character("Tester", world["great_hall_north"])
    puzzle = world["great_hall_north"].puzzles[0]

    puzzle.attempt(puzzle.solution, player)

    assert puzzle.solved, "Puzzle should be marked as solved"
    assert any(isinstance(item, Key) for item in player.inventory), "Player should have recieved a Key"
    bronze_key = next(item for item in player.inventory if isinstance(item, Key))
    assert bronze_key.opens_location == "The Great Hall - West"

def test_unlocking_west_room(world):
    player = Character("Tester", world["great_hall_north"])
    puzzle = world["great_hall_north"].puzzles[0]
    puzzle.attempt(puzzle.solution, player)

    west_room = world["great_hall_west"]
    assert west_room.locked, "West room should start locked"

    bronze_key = next(item for item in player.inventory if isinstance(item, Key))
    west_room.unlock(bronze_key)
    assert not west_room.locked, "West room should be unlocked after using the Bronze Key"