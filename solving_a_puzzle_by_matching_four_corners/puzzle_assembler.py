"""
Solution to the problem Solving a puzzle by matching four corners (4kyu)
of Codewars.
Description:
    The goal here is to solve a puzzle (the "pieces of paper" kind of puzzle).
    You will receive different pieces of that puzzle as input, and you will
    have to find in what order you have to rearrange them so that the "picture"
    of the puzzle is complete.
    All the pieces of the puzzle will be represented in the following way:
        - 4 numbers, grouped in 2 tuples, which are representing the "picture"
          on the piece. Every piece has a 2x2 size.
        - 1 id number. All id numbers are unique in a puzzle, but their value
          may be random.
        - Note that all numbers will be non-negative integers.
    Solving the puzzle
        - You'll get an array of pieces as well as the size of the puzzle
          (width and height).
        - Two pieces can be assembled if they share the same pattern on the
          border where they are in contact (see example below).
        - Puzzle pieces being unique, you'll never encounter two different
          pieces that could be assembled with the same third one. So to say:
          borders are unique.
        - Once you found the proper arrangment for all the pieces, return the
          solved puzzle as a list of tuples (height * width) of the id number
          of the piece at its correct position.
"""

from typing import Tuple
from enum import Enum, auto


class PuzzleAssembler:

    class Border(Enum):
        LEFT = auto()
        RIGHT = auto()
        LOWER = auto()
        UPPER = auto()

    Piece = list[tuple[tuple[int, int], tuple[int, int]]]

    @classmethod
    def _sorted_by_border(pieces: list[Piece],
                          border: Border) -> list[Piece]:
        raise NotImplementedError

    @classmethod
    def assemble(cls, pieces: list[Piece], width: int,
                 height: int) -> list[Tuple[int, ...]]:
        horizontal_attachments = {
            p1_id: p2_id for p1_id, p2_id in
            zip(cls._sorted_by_border(pieces, cls.Border.RIGHT)[height:],
                cls._sorted_by_border(pieces, cls.Border.LEFT)[height:])
        }
        vertical_attachments = {
            p1_id: p2_id for p1_id, p2_id in
            zip(cls._sorted_by_border(pieces, cls.Border.LOWER)[height:],
                cls._sorted_by_border(pieces, cls.Border.UPPER)[height:])
        }
        left_upper_piece_id = [
            piece[2] for piece in pieces if piece[0][0] is None and
            piece[0][1] is None and piece[1][0] is None
        ][0]
        top_row_piece_ids = [left_upper_piece_id]
        for _ in range(width-1):
            top_row_piece_ids.append(
                horizontal_attachments[top_row_piece_ids[-1]]
            )
        assembled_puzzle_piece_ids = [top_row_piece_ids]
        for _ in range(height-1):
            assembled_puzzle_piece_ids.append(
                [vertical_attachments[p_id] for p_id
                 in assembled_puzzle_piece_ids[-1]]
            )
        return [tuple(row) for row in assembled_puzzle_piece_ids]


puzzle_solver = PuzzleAssembler.assemble  # for Codewars
