from typing import List, Tuple, Dict, Union, NewType
from bisect import bisect

bits = NewType('bits', str)
char = NewType('char', str)


class HuffmanEncoder:

    class Node:
        id_counter = 0

        def __init__(self, left: Union['HuffmanEncoder.Node', str],
                     right: Union['HuffmanEncoder.Node', str]):
            self.left = left
            self.right = right
            self.id = HuffmanEncoder.Node.id_counter
            HuffmanEncoder.Node.id_counter += 1

        def get_recursive_repr(self) -> str:
            return self.__repr__() + \
                ('\n' + self.left.get_recursive_repr()
                 if isinstance(self.left, HuffmanEncoder.Node) else '') + \
                ('\n' + self.right.get_recursive_repr()
                 if isinstance(self.right, HuffmanEncoder.Node) else '')

        def __repr__(self) -> str:
            return '({}) <-- ({}) --> ({})'.format(
                'Node ' + str(self.left.id) if
                isinstance(self.left, HuffmanEncoder.Node) else self.left,
                'Node ' + str(self.id),
                'Node ' + str(self.right.id) if
                isinstance(self.right, HuffmanEncoder.Node) else self.right
            )

    @staticmethod
    def _build_tree(char_freqs: List[Tuple[char, int]]) -> 'Node':
        # start with each char as an individual tree and iterativelly
        # put the 2 more frequent trees under a new node
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
    def _compute_encoding_dict_rec(cls, node: Union[Node, char],
                                   acc_bits: bits = '') -> None:
        if acc_bits == '':
            cls.encoding_dict = {}
        if isinstance(node, str):  # leaf
            cls.encoding_dict[node] = acc_bits
        else:  # recursive steps
            cls._compute_encoding_dict_rec(node.left, acc_bits + '0')
            cls._compute_encoding_dict_rec(node.right, acc_bits + '1')

    @classmethod
    def _compute_encoding_dict(
        cls, char_freqs: List[Tuple[char, int]]
    ) -> Tuple[Dict[char, bits], Dict[bits, char]]:
        cls._compute_encoding_dict_rec(cls._build_tree(char_freqs))
        return cls.encoding_dict

    @staticmethod
    def extract_char_freqs(str_: str) -> List[Tuple[char, int]]:
        freqs_dict = {}
        for char_ in str_:
            freqs_dict[char_] = freqs_dict[char_] + 1 \
                if char_ in freqs_dict else 1
        return freqs_dict.items()

    @classmethod
    def encode(cls, char_freqs: List[Tuple[char, int]], str_: str) -> bits:
        if len(char_freqs) <= 1:
            return None
        encoding_dict = cls._compute_encoding_dict(char_freqs)
        return ''.join([encoding_dict[char_] for char_ in str_] + [''])

    @classmethod
    def decode(cls, char_freqs: List[Tuple[char, int]], bits_: bits) -> str:
        if len(char_freqs) <= 1:
            return None
        node = root = cls._build_tree(char_freqs)
        decoded_str = ''
        for bit_ in bits_:
            node = node.left if bit_ == '0' else node.right
            if isinstance(node, str):
                decoded_str += node
                node = root
        return decoded_str


# define aliases for Codewars
frequencies = HuffmanEncoder.extract_char_freqs
encode = HuffmanEncoder.encode
decode = HuffmanEncoder.decode
