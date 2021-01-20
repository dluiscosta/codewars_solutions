"""
Solution to the problem Battleship field validator II (3kyu) of Code Wars.
Description:
    Write a method that takes a field for well-known board game "Battleship" as
    an argument and returns true if it has a valid disposition of ships, false
    otherwise. The argument is guaranteed to be 10*10 two-dimension array.
    Elements in the array are numbers, 0 if the cell is free and 1 if occupied
    by a ship.
    Before the game begins, players set up the board and place the ships
    according to the following rules:
        - There must be a single battleship (size of 4 cells), 2 cruisers
        (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any
        additional ships are not allowed, as well as missing ships.
        - Each ship must be a straight line, except for submarines, which are
        just single cells.
        - The ships cannot overlap, but can be in contact with any other ship.
"""

from abc import ABC
from typing import List


class Battleship(ABC):
    """
    Utilitary functions for the game Battleship (Soviet/Russian version).

    Battleship (also Battleships or Sea Battle) is a guessing game for two
    players. Each player has a 10x10 grid containing several "ships" and their
    objective is to destroy the enemy's forces by targetting individual cells
    on the opposing field. Each ship occupies one or more cells in the grid.
    """

    @staticmethod
    def validate_field(field: List[List[int]]) -> bool:
        """
        Validate the disposition of ships in a given field.

        Validate the disposition of ships in a given field, where each ship is
        formed by consecutive (vertically or horizontally) "ship cells".
        A valid field contains exactly 1 4-wide, 2 3-wide, 3 2-wide and
        4 1-wide ships, which can't overlap.

        Parameters
        ----------
            field: 10x10 list of lists containing integers, where 1 represents
                   a "ship cell" and 0 represents water.
        """
        if sum([sum(line) for line in field]) != 20:
            return False
        raise NotImplementedError


validate_battlefield = Battleship.validate_field  # for Codewars
