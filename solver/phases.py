from solver.cube import CubieCube
from solver.tables import TableManager


class Phase:
    """
    This is an abstract class for the phases. Both Phase 1 and Phase 2 follow a similar process, however there
    are nuances between the two in some methods that much be overridden.
    """

    # Load/generate the move and pruning tables required to perform the search and use the heuristic

    # def __init__(self, cube: CubieCube, length: int = 30):
    def __init__(self, length: int = 30):
        """
        Constructs empty lists and attributes required for the search.

        :param cube: CubieCube object that is the root of the search for this phase.
        :param length: integer that serves as the maximum length of the search.
        """

        self.max_depth: int = length

        # make empty stacks to hold the history of the search for backtracking
        self.moves: list[int] = [-1] * length
        self.powers: list[int] = [-1] * length
        self.h_costs: list[int] = [-1] * length

        self.coordinate1: list[int] = [0] * length
        self.coordinate2: list[int] = [0] * length
        self.coordinate3: list[int] = [0] * length

    def find_solution(self):
        """
        Method to perform the search of Phase N. Handles iterating upper bound on depth of search.

        :return: tuple of moves and powers of solution
        """
        for upper_depth_bound in range(self.max_depth):
            n = self.ida(0, upper_depth_bound)
            if n > 0:  # If the search has found a solution
                return (
                    [i for i in self.moves if i != -1],
                    [j for j in self.powers if j != -1],
                )

    def h(self, node_depth: int) -> int:
        """
        Abstract function for heuristic used in Phase N search to provide a lower bound on the number of moves
        required to solve a position.

        :param node_depth: node depth used to look up current position of cube and relevant coordinates.
        :return: Lower bound on number of moves required to solve position at node_depth.
        """

        pass

    def ida(self, node_depth: int, q: int) -> int:
        """
        Abstract function for iterative depth search to find solutions for Phase N.

        :param node_depth:
        :param q:
        :return: -1 if no solution found at current position; n > 0 if solution found.
        """

        pass


class Phase1(Phase):
    """
    Subclass for managing the search of the first phase of the Two-Phase Algorithm.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find_solution(self, cube: CubieCube):
        # Initialising the first coordinates and costs using Phase 1 coordinates
        self.coordinate1[0] = cube.o_corner_coords
        self.coordinate2[0] = cube.o_edge_coords
        self.coordinate3[0] = cube.pos_udslice_coords

        self.h_costs[0] = self.h(0)  # Get cost of starting position

        return super().find_solution()

    def h(self, node_depth: int) -> int:
        """
        Function to provide a lower bound on the number of moves
        required to solve a position in Phase 1

        :param node_depth: node depth used to look up current position of cube and relevant coordinates
        :return: Lower bound on number of moves required to solve position at node_depth
        """

        return max(
            TableManager.UDslice_Oedge_pruning.table[self.coordinate3[node_depth]][
                self.coordinate2[node_depth]
            ],
            TableManager.UDslice_Ocorner_pruning.table[self.coordinate3[node_depth]][
                self.coordinate1[node_depth]
            ],
        )

    def ida(self, node_depth: int, sol_length_upper_bound: int) -> int:
        """
        Function for performing search to find solutions for Phase N

        :param node_depth: depth of current location in the search
        :param sol_length_upper_bound: upper bound on the length of the solution
        :return: -1 if no solution found at current position; n > 0 if solution found
        """

        # Check if the position has reached the target subgroup H1
        if self.h(node_depth) == 0:
            # Backtrack and end search
            return node_depth

        # If lower bound of cube state is bigger than solution length upper bound, prune search branch
        elif self.h_costs[node_depth] <= sol_length_upper_bound:
            # Do move on each face <U, L, R, F, B, D>
            for move in range(6):
                # Dont allow duplciates
                if node_depth > 0 and self.moves[node_depth - 1] in (move, move + 3):
                    # TODO can optimise to remove check altogether I think
                    continue
                else:
                    # Do each move 3 times to cover double turns, inverse turns of a face
                    for power in range(3):

                        # Record the move and power
                        self.moves[node_depth] = move
                        self.powers[node_depth] = power + 1

                        # Calculate the position in pruning tables
                        table_index = (move * 3) + power

                        # Update the coordinates of the new cube state
                        self.coordinate1[node_depth + 1] = TableManager.Ocorner.table[
                            self.coordinate1[node_depth]
                        ][table_index]
                        self.coordinate2[node_depth + 1] = TableManager.Oedge.table[
                            self.coordinate2[node_depth]
                        ][table_index]
                        self.coordinate3[node_depth + 1] = TableManager.POSud_slice.table[
                            self.coordinate3[node_depth]
                        ][table_index]

                        # Update cost
                        self.h_costs[node_depth + 1] = self.h(node_depth + 1)

                        # Continue searching
                        continue_search = self.ida(
                            node_depth + 1, sol_length_upper_bound - 1
                        )

                        if continue_search >= 0:
                            # found solution, return
                            return continue_search

        # If search path exceeds depth at some point
        return -1


class Phase2(Phase):
    """
    Subclass for managing the search of the first phase of the Two-Phase Algorithm.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find_solution(self, cube: CubieCube):
        # Initialising the first coordinates and costs using Phase 2 coordinates
        self.coordinate1[0] = cube.p_4edge_coords
        self.coordinate2[0] = cube.p_corner_coords
        self.coordinate3[0] = cube.p_8edge_coords

        self.h_costs[0] = self.h(0)  # Get cost of starting position

        return super().find_solution()

    def h(self, node_depth: int) -> int:
        """
        Function to provide a lower bound on the number of moves
        required to solve a position in Phase 1

        :param node_depth: node depth used to look up current position of cube and relevant coordinates
        :return: Lower bound on number of moves required to solve position at node_depth
        """

        return max(
            TableManager.P4edge_P8edge_pruning.table[self.coordinate1[node_depth]][
                self.coordinate3[node_depth]
            ],
            TableManager.P4edge_Pcorner_pruning.table[self.coordinate1[node_depth]][
                self.coordinate2[node_depth]
            ],
        )

    def ida(self, node_depth: int, sol_length_upper_bound: int) -> int:
        """
        Function for performing search to find solutions for Phase N

        :param node_depth: depth of current location in the search
        :param q: upper bound on the length of the solution
        :return: -1 if no solution found at current position; n > 0 if solution found.
        """

        # Check if the position is solved
        if self.h(node_depth) == 0:
            # Backtrack and end search.
            return node_depth

        # If lower bound of cube state is bigger than solution length upper bound, prune search branch
        elif self.h_costs[node_depth] <= sol_length_upper_bound:
            # Do move on each face <U, L, R, F, B, D>
            for move in range(6):
                # Dont allow duplciates
                if node_depth > 0 and self.moves[node_depth - 1] in (move, move + 3):
                    continue
                else:
                    # Do each move 3 times to cover double turns, inverse turns of a face
                    for move_power in range(3):
                        # If move is not a double and not performed on the <U, D> faces.
                        if move_power != 1 and move % 5 != 0:
                            # TODO can hard code this or use generator
                            continue

                        # Record the move and power
                        self.moves[node_depth] = move
                        self.powers[node_depth] = move_power + 1

                        # Calculate the position in pruning tables
                        table_index = (move * 3) + move_power

                        # Update the coordinates of the new cube state
                        self.coordinate1[node_depth + 1] = TableManager.P4edge.table[
                            self.coordinate1[node_depth]
                        ][table_index]
                        self.coordinate2[node_depth + 1] = TableManager.Pcorner.table[
                            self.coordinate2[node_depth]
                        ][table_index]
                        self.coordinate3[node_depth + 1] = TableManager.P8edge.table[
                            self.coordinate3[node_depth]
                        ][table_index]

                        # Update cost
                        self.h_costs[node_depth + 1] = self.h(node_depth + 1)

                        # Continue searching
                        continue_search = self.ida(
                            node_depth + 1, sol_length_upper_bound - 1
                        )

                        if continue_search >= 0:
                            # found solution, return
                            return continue_search

        # If search path exceeds depth at some point
        return -1
