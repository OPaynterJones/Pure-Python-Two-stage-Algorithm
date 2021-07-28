# There are 2187 possible ways to orientate the corners on a Rubik's Cube (3^7).
# NOTE: The first 7 corners determine the orientation of the last, hence 3^7 (sum(orientations)%3 = 0).
# The orientation of all the corners can be encoded using the ternary number system.
# Each corner has a rotation o, o ∈ {0, 1, 2}.
# EXAMPLE: The corner orientation 0012100(2) -> 144.
# The inverse can be applied to obtain the orientation of all the corners given it's index number.


class C:
    """Abstract Corner class."""

    Cparity: dict[int, int] = {
        0: 0,
        1: 2,
        2: 1
    }

    @staticmethod
    def get_index(orientation: int) -> int:
        """
        Return index number of an corner orientation.

        timeit("C.get_index(20011002)", setup="from corner_ternary_encoding import C")
        0.3369964999999979
        """

        return int(str(orientation)[:-1], 3)

    @staticmethod
    def get_orientation_numpy(index: int) -> int:
        """
        Return the orientation of all corners of an index, using numpy.

        timeit("C.get_orientation_numpy(1494)", setup="from corner_ternary_encoding import C")
        1.5535832999999997
        """
        from numpy import base_repr

        n = base_repr(index, base=3)
        parity = int(n) % 3

        return int(f"{n}{C.Cparity[parity]}")

    @staticmethod
    def get_orientation_builtins(index: int) -> int:
        """
        Return the orientation of all corners of an index, using builtins.

        timeit("C.get_orientation_builtins(1494)", setup="from corner_ternary_encoding import C")
        2.039908699999998
        """

        if index == 0:
            return 0
        nums = []
        while index:
            index, r = divmod(index, 3)
            nums.append(str(r))
        n = ''.join(nums[::-1])
        parity = int(n) % 3

        return int(f"{n}{C.Cparity[parity]}")


# There are 2048 possible ways to orientate the corners on a Rubik's Cube (2^11).
# NOTE: The first 12 corners determine the orientation of the last, hence 2^11 (sum(orientations)%2 = 0).
# The orientation of all the corners can be encoded using the binary number system.
# Each corner has a rotation o, o ∈ {0, 1}.
# EXAMPLE: The corner orientation 10000111100(1) -> 1084.
# The inverse can be applied to obtain the orientation of all the edges given it's index number.


class E:
    """Abstract Edge class."""

    Eparity: dict[int, int] = {
        0: 0,
        1: 1
    }

    @staticmethod
    def get_index(orientation: int) -> int:
        """
        Return index number of an edge orientation.

        # TODO time this function

        """

        return int(str(orientation)[:-1], 2)

    @staticmethod
    def get_orientation_builtins(index: int) -> int:
        """
        Return the orientation of all edges of an index, using builtins.

        # TODO time this function

        """
        # TODO write this function
        pass

    @staticmethod
    def get_orientation_numpy(index: int) -> int:
        """
        Return the orientation of all edges of an index, using numpy.

        timeit("E.get_orientation_numpy(2047)", setup="from corner_ternary_encoding import E")
        3.05947119999999
        """
        from numpy import binary_repr
        n = binary_repr(index)

        parity = sum([int(char) for char in str(n)]) % 2
        return int(f"{n}{E.Eparity[parity]}")