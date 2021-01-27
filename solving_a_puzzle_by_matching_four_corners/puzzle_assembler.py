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
    def _get_pieces_border(cls, piece, border_name: str) -> tuple:
        if border_name == 'upper':
            return piece[0]
        elif border_name == 'lower':
            return piece[1]
        elif border_name == 'left':
            return (piece[0][0], piece[1][0])
        elif border_name == 'right':
            return (piece[0][1], piece[1][1])
        else:
            raise ValueError('Invalid border_name: {}'.format(border_name))

    @classmethod
    def _sorted_by_border(cls, pieces: list, border_name: str) -> list:
        return sorted(
            pieces,
            key=lambda p: cls._get_pieces_border(p, border_name).__hash__()
        )

    @classmethod
    def _find_left_upper_corner_piece(cls, pieces: list):
        return [piece for piece in pieces if piece[0][0] is None and
                piece[0][1] is None and piece[1][0] is None][0]

    @classmethod
    def assemble(cls, pieces: list, width: int, height: int) -> list:
        # since pieces borders are unique, compute attachments by finding
        # matching opposing borders through sorting
        horizontal_attachments = {
            p1[2]: p2[2] for p1, p2 in
            zip(cls._sorted_by_border(pieces, 'right'),
                cls._sorted_by_border(pieces, 'left'))
        }  # attachments to the right
        vertical_attachments = {
            p1[2]: p2[2] for p1, p2 in
            zip(cls._sorted_by_border(pieces, 'lower'),
                cls._sorted_by_border(pieces, 'upper'))
        }  # attachments bellow
        # build assembled puzzle id matrix by iterating through attachments
        top_row_piece_ids = [cls._find_left_upper_corner_piece(pieces)[2]]
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
