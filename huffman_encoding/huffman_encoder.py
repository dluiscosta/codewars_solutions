from typing import List, Tuple, Dict, Union, NewType
from bisect import bisect


class HuffmanEncoder:

    class Node:
        def __init__(self, left: Union['HuffmanEncoder.Node', str],
                     right: Union['HuffmanEncoder.Node', str]):
            self.left = left
            self.right = right

    bits = NewType('bits', str)
    char = NewType('char', str)

    @staticmethod
    # O(nlogn) time and O(n) space, n = len(char_freqs)
    def _build_tree(char_freqs: List[Tuple[char, int]]) -> Node:
        # start with each char as an individual tree and iterativelly
        # put the 2 less frequent trees under a new node
        trees, freqs = [list(t) for t in
                        zip(*sorted(char_freqs, key=lambda t: t[1]))]
        while(len(trees) > 1):
            new_tree = HuffmanEncoder.Node(trees.pop(0), trees.pop(0))
            new_tree_freq = freqs.pop(0) + freqs.pop(0)
            new_tree_pos = bisect(freqs, new_tree_freq)
            trees.insert(new_tree_pos, new_tree)
            freqs.insert(new_tree_pos, new_tree_freq)
        return trees[0]

    @classmethod
    # O(nlogn) time and O(n) space, n = len(char_freqs)
    def _compute_encoding_dict(cls, char_freqs: List[Tuple[char, int]]
                               ) -> Tuple[Dict[char, bits], Dict[bits, char]]:

        def _compute_encoding_dict_rec(node: Union['cls.Node', 'cls.char'],
                                       acc_bits: 'cls.bits' = '') -> None:
            if isinstance(node, str):  # leaf
                encoding_dict[node] = acc_bits
            else:  # recursive step
                _compute_encoding_dict_rec(node.left, acc_bits + '0')
                _compute_encoding_dict_rec(node.right, acc_bits + '1')

        encoding_dict = {}
        _compute_encoding_dict_rec(cls._build_tree(char_freqs))
        return encoding_dict

    @staticmethod
    # O(nlogn) time and O(n) space, n = len(str_)
    def extract_char_freqs(str_: str) -> List[Tuple[char, int]]:
        freqs_dict = {}
        for char_ in str_:
            freqs_dict[char_] = freqs_dict[char_] + 1 \
                if char_ in freqs_dict else 1
        return freqs_dict.items()

    @classmethod
    # O(nlogn) time and O(n) space, n = len(str_)
    def encode(cls, char_freqs: List[Tuple[char, int]], str_: str) -> bits:
        if len(char_freqs) <= 1:
            return None
        encoding_dict = cls._compute_encoding_dict(char_freqs)
        return ''.join([encoding_dict[char_] for char_ in str_] + [''])

    @classmethod
    # O(nlogn) time and O(n) space, n = len(bits_)
    def decode(cls, char_freqs: List[Tuple[char, int]], bits_: bits) -> str:
        if len(char_freqs) <= 1:
            return None
        node = root = cls._build_tree(char_freqs)
        # travel down the tree following bits_ directions
        decoded_str = ''
        for bit_ in bits_:
            node = node.left if bit_ == '0' else node.right
            if isinstance(node, str):  # reached leaf
                decoded_str += node  # decoded char
                node = root  # go back to root
        return decoded_str


# define aliases for Codewars
frequencies = HuffmanEncoder.extract_char_freqs
encode = HuffmanEncoder.encode
decode = HuffmanEncoder.decode
