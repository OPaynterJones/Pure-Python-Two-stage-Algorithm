# Permutations can use index numbers and algorithms to encode each state.
# The corner permutation is given by a state index from 0-40319 (8! - 1).
# A natural order of corners is used. URF<UFL<ULB<UBR<DFR<DLF<DBL<DRB.


class C:
    """
    Abstract corner class.
    :cvar corners: corners  "hierarchy".
    """

    # The corners on a cube have a "hierarchy" through which they are defined.
    # This system is used to represent the states of permutations on a cube.
    corners: dict[str, int] = {
        "URF": 0,
        "UFL": 1,
        "UBL": 2,
        "UBR": 3,
        "DRF": 4,
        "DLF": 5,
        "DLB": 6,
        "DRB": 7,
    }

    @staticmethod
    def get_permutation_index(perm_state: str) -> int:
        """
        :param perm_state: the order of corners in  permutation.
        :return: returns index number of given permutation.
        """
        # TODO write this function regarding permutations and research variable base representation/encoding.