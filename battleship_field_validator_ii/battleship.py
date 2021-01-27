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
from typing import List, Tuple
from enum import Enum, auto
import numpy as np
from itertools import combinations, groupby, product


class Battleship(ABC):
    """
    Utilitary functions for the game Battleship (Soviet/Russian version).

    Battleship (also Battleships or Sea Battle) is a guessing game for two
    players. Each player has a 10x10 grid containing several "ships" and their
    objective is to destroy the enemy's forces by targetting individual cells
    on the opposing field. Each ship occupies one or more cells in the grid.
    """

    MAX_SHIP_SIZE = 4

    class Ship:
        class Orientation(Enum):
            VERTICAL = auto()
            HORIZONTAL = auto()

        ORIENTATION_TRANSPOSE_DICT = {
            'HORIZONTAL': Orientation.VERTICAL,
            'VERTICAL': Orientation.HORIZONTAL,
        }

        def __init__(self, starting_pos: Tuple[int, int], length: int,
                     orientation: Orientation = None):
            if not orientation and length > 1:
                raise ValueError()
            self.starting_pos = starting_pos
            self.orientation = orientation
            self.length = length

        def transpose(self):
            self.starting_pos = self.starting_pos[::-1]
            if self.orientation:
                self.orientation = \
                    self.ORIENTATION_TRANSPOSE_DICT[self.orientation.name]
            return self

        def __repr__(self):
            w = self.orientation.name.lower() if self.orientation else '1-wide'
            return '{} ship starting at {} with length {}'.format(
                w, self.starting_pos, self.length
            )

        def __eq__(self, other):
            if isinstance(other, type(self)):
                return self.starting_pos == other.starting_pos and \
                       self.orientation == other.orientation and \
                       self.length == other.length

        def __hash__(self):
            return hash((self.starting_pos, self.orientation, self.length))

    @classmethod
    def _extract_possible_ships(cls, field: List[List[int]]) -> List[Ship]:

        def extract_possible_horizontal_ships(field: np.array):
            possible_horizontal_ships = []
            # compute consecutive ship cells at the cell and to it's right
            cons_ship_cells = np.zeros((10, 10), dtype=int)
            for y in range(10):
                acc_cons_ship_cells = 0
                for x in range(9, -1, -1):
                    if field[y][x] == 1:
                        acc_cons_ship_cells += 1
                        cons_ship_cells[y][x] = acc_cons_ship_cells
                    else:
                        acc_cons_ship_cells = 0
            for y, x in np.argwhere(cons_ship_cells > 0):
                possible_horizontal_ships.extend(
                    [cls.Ship(
                        (y, x), length,
                        cls.Ship.Orientation.HORIZONTAL if length > 1 else None
                     )
                     for length in
                     range(1, min(cons_ship_cells[y][x], cls.MAX_SHIP_SIZE)+1)]
                )
            return set(possible_horizontal_ships)

        def flip_ship_orientation(ship):
            flip_dict = {
                'HORIZONTAL': cls.Ship.Orientation.VERTICAL,
                'VERTICAL': cls.Ship.Orientation.HORIZONTAL,
            }
            if ship.orientation:
                ship.orientation = flip_dict[ship.orientation.name]
                ship.starting_pos = ship.starting_pos[::-1]
            return ship

        np_field = np.array(field)
        return extract_possible_horizontal_ships(np_field).union(
            {ship.transpose() for ship in
             extract_possible_horizontal_ships(np.transpose(np_field))})

    @classmethod
    def validate_field(cls, field: List[List[int]]) -> bool:
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
        VALID_AMOUNT_OF_SHIPS = {1: 4, 2: 3, 3: 2, 4: 1}  # by length
        if sum([sum(line) for line in field]) != \
                sum([n*length for length, n in VALID_AMOUNT_OF_SHIPS.items()]):
            return False
        possible_ships = cls._extract_possible_ships(field)
        # print('\n'.join([str(ship) for ship in possible_ships]))
        length_grouped_possible_ships = {
            length: set(ships)
            for length, ships in groupby(
                sorted(list(possible_ships), key=lambda ship: ship.length),
                lambda ship: ship.length
            )
        }
        # print('\n'+'\n'.join(
        #     [f"Length {length}\n"+'\n'.join([str(ship) for ship in group])+'\n'
        #      for length, group in length_grouped_possible_ships.items()])
        # )
        for length, amount in VALID_AMOUNT_OF_SHIPS.items():
            if len(length_grouped_possible_ships[length]) < amount:
                return False
        len_group_poss_ship_combinations = {
            length: combinations(group, VALID_AMOUNT_OF_SHIPS[length])
            for length, group in length_grouped_possible_ships.items()
        }
        # print('\n'.join(
        #     [f'{len(list(cs))} combinations with length {length}'
        #      for length, cs in len_group_poss_ship_combinations.items()]
        # ))
        possible_ship_combinations = product(
            *[combinations for _, combinations in
              len_group_poss_ship_combinations.items()]
        )
        print(len(list(possible_ship_combinations)))
        raise NotImplementedError


validate_battlefield = Battleship.validate_field  # for Codewars
