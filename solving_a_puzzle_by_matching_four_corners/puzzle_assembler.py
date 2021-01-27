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


class PuzzleAssembler:

    @classmethod
    def assemble(cls, pieces, width, height):
        raise NotImplementedError


puzzle_solver = PuzzleAssembler.assemble  # for Codewars
