"""
Solution to the problem Next bigger number with the same digits (4kyu) of
Code Wars.
Description:
    reate a function that takes a positive integer and returns the next bigger
    number that can be formed by rearranging its digits.
"""


def get_smallest_bigger_int_with_same_digits(int_: int) -> int:
    digits = [int(digit) for digit in str(int_)]
    # look for a break in a monotonically increasing sequence, right to left
    current_biggest_digit = 0
    for backwards_idx, digit in enumerate(reversed(digits)):
        if digit >= current_biggest_digit:  # sequence continues
            current_biggest_digit = digit
        else:  # found a break, one of the digits to be swapped
            idx = len(digits) - backwards_idx - 1
            # look for the smallest digit bigger than the break digit
            # inside the monotonically increasing sequence
            replacement_idx, replacement = min(
                [(i, d) for i, d in enumerate(digits[idx+1:], start=idx+1)
                 if d > digit], key=(lambda i_d: i_d[1])
            )
            # swap both digits, ensuring the resulting integer is bigger
            digits[idx], digits[replacement_idx] = replacement, digit  # swap
            # sort the monotonically increasing sequence, getting the lowest
            # integer value possible for that section
            digits[idx+1:] = sorted(digits[idx+1:])
            return int(''.join((str(d) for d in digits)))  # list->int convers.
    return -1


next_bigger = get_smallest_bigger_int_with_same_digits  # for Codewars
