"""
Solution to the problem Fabergè Easter Eggs crush test (3kyu) of Code Wars.
Description:
    One man (lets call him Eulampy) has a collection of some almost identical
    Fabergè eggs. One day his friend Tempter said to him:
        - Do you see that skyscraper? And can you tell me a maximal floor that
        if you drop your egg from will not crack it?
        - No, - said Eulampy.
        - But if you give me N eggs, - says Tempter - I'l tell you an answer.
        - Deal - said Eulampy. But I have one requirement before we start this:
        if I will see more than M falls of egg, my heart will be crushed
        instead of egg. So you have only M trys to throw eggs. Would you tell
        me an exact floor with this limitation?
    Your task is to help Tempter - write a function that takes 2 arguments -
    the number of eggs n and the number of trys m - you should calculate
    maximum scyscrapper height (in floors), in which it is guaranteed to find
    an exactly maximal floor from which that an egg won't crack it.
    Which means,
        1. You can throw an egg from a specific floor every try;
        2. Every egg has the same, certain durability - if they're thrown from
        a certain floor or below, they won't crack. Otherwise they crack;
        3. You have n eggs and m tries;
        4. What is the maxmimum height, such that you can always determine
        which floor the target floor is when the target floor can be any floor
        between 1 to this maximum height?
"""


from abc import ABC


class FabergEasterEggsCrushUtilitary(ABC):
    """
    When throwing a Faberg Easter Egg from a skycrappers floor, it might or
    not crush depending on it's durability, which is unknown. Since all eggs
    have the same durability, they would always break if thrown from a certain
    floor or any above it, but never when thrown from the floors bellow. This
    particular floor is called the target floor.
    """

    @staticmethod
    def max_skyscrapper_height_with_determinable_target_floor(
            eggs: int, tries: int) -> int:
        """
        Determines the maximum height, in floors, of a skycrapper to which the
        target floor can always be determined, regardless of the eggs
        durability, but given limited numbers of eggs to throw and throwing
        tries (unbroken eggs can be thrown again).
        """
        #  dynamic programming table where msh(0,x) = msh(x,0) = 0
        msh = [[0]*(tries+1)] + [[0]+[None]*tries for i in range(eggs)]
        for eggs_ in range(1, eggs+1):
            for tries_ in range(1, tries+1):
                msh[eggs_][tries_] = sum(
                    [msh[eggs_-1][tries__] + 1 for tries__ in range(tries_)]
                )
        return msh[eggs][tries]
