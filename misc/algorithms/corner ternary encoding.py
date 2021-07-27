from numpy import base_repr


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
        """Return index number of a corner orientation."""

        return int(str(orientation)[:-1], 3)

    @staticmethod
    def get_orientation_numpy(index: int) -> int:
        """Return the orientation of all corners of an index, using numpy."""

        # timeit("base_repr(1494, base=3)", setup="from numpy import base_repr")
        # 1.1511318999999958

        n = base_repr(index, base=3)
        parity = int(n) % 3

        return int(f"{n}{C.Cparity[parity]}")

    @staticmethod
    def get_orientation_builtins(index: int) -> int:
        """Return the orientation of all corners of an index, using builtins."""

        # timeit(stmt=s, setup = "index = 1494")
        # 0.026654500000006465

        if index == 0:
            return 0
        nums = []
        while index:
            index, r = divmod(index, 3)
            nums.append(str(r))
        n = ''.join(nums[::-1])
        parity = int(n) % 3

        return int(f"{n}{C.Cparity[parity]}")