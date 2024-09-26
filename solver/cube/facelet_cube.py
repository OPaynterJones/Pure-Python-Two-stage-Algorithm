# Import all the default pieces.
from .definitions import *


class FaceletCube:
    """
    Lowest level of data structure involved in Two-Phase Algorithm. It deals primarily in colours and operates on the
    basis of stickers or "facelets".
    """

    def __init__(self, string_definition: str = None):
        """
        Constructor for FaceletCube.

        :param string_definition: definition of a cube in facelet string form.
        """

        self.f: list[int] = [0] * 54

        if string_definition:
            for i, c in enumerate(string_definition):
                self.f[i] = Axes[c]

        else:
            self.f = [-1] * 54

    def verify(self) -> int:
        """
        Function to determine the validity of a cube defined as a string.

        :return: -1 if not a valid string; 1 if a valid string.
        """

        # Count the frequency of each value.
        count: list[0] = [0] * len(Axes)
        for i, c in enumerate(Axes):
            count[i] = self.f.count(c)

        for c in count:
            # If there are not 9 colours of each facelet.
            if c != 9:
                return -1

        return 1

    @property
    def corners(self) -> list[tuple[int, int, int]]:
        """
        Getter method for the corners of the string definition of a cube.

        :return: A list of corners pulled from positions in the string definition of a cube.
        """

        s = self.f
        corner_facelets = [0] * len(Corner_Indices)
        # Loop through the corners.
        for i in range(len(corner_facelets)):
            corner_facelets[i] = tuple(s[f] for f in corner_facelet_indices[i])

        return corner_facelets

    @property
    def edges(self) -> list[tuple[int, int, int]]:
        """
        Getter method for the edges of the string definition of a cube.

        :return: A list of edges pulled from positions in the string definition of a cube.
        """

        s = self.f
        edges = [0] * len(Edge_Indices)
        # Loop through the edges.
        for i in range(len(edges)):
            edges[i] = tuple(s[f] for f in edge_facelet_indices[i])

        return edges
