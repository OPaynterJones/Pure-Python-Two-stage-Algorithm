from .cubie_cube import CubieCube, MOVES
from .facelet_cube import FaceletCube
from .definitions import *

def to_cubie_cube(fc: FaceletCube):
        """
        Function to convert FaceletCube into CubieCube

        :param fc: facelet cube to convert
        :return: CubieCube with facelet string definition applied.
        """

        # Create empty lists
        co = [0] * 8
        cp = [0] * 8

        # Loop through the corners in the current facelet string.
        for i, corner in enumerate(fc.corners):
            # Loop through the individual facelets.
            for o, f in enumerate(corner):
                # If the facelet is either a part of the top (0) or down (5) face.
                if f == 0 or f == 5:
                    # Break loop as orientation has been determined.
                    break

            # Loop through the facelets remaining in that corner, starting from the up or down facelet and moving
            # clockwise
            facelet1 = corner[(o + 1) % 3]
            facelet2 = corner[(o + 2) % 3]

            # For the corners that exist on a cube
            for j, default_corner in enumerate(corner_axes):
                # If two of the facelets match in corner in order, then it must be that corner and cannot be another
                # assuming all inputs have been sanitised.
                if facelet1 == default_corner[1] and facelet2 == default_corner[2]:
                    co[i] = o
                    cp[i] = j
                    break

        # Create empty lists
        eo = [0] * 12
        ep = [0] * 12

        # Loop through the corners in the current facelet string.
        for t, edge in enumerate(fc.edges):
            # Loop through the default edges.
            for k, cols in enumerate(edge_axes):
                # If the edge taken from string definition matches default edge with no flip.
                if edge == cols:
                    eo[t] = 0
                    ep[t] = k

                # If the edge taken from string definition matches default edge with flip.
                elif edge[0] == cols[1] and edge[1] == cols[0]:
                    eo[t] = 1
                    ep[t] = k

        return CubieCube(data=[cp, co, ep, eo])


__all__ = ["CubieCube", "MOVES", "FaceletCube, to_cubie_cube"]
