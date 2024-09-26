import os
import numpy as np
from solver import cube

SAVEFILE_NAME = "Pruning_tables.npz"


# class TableManager:
#     NO_Pcorner_coords = 40320

#     NO_P4edge_coords =

#     TABLE_KEYS = [
#         "Ocorner",
#         "Pcorner",
#         "Oedge",
#         "POSud_slice",
#         "UDslice_Oedge_pruning",
#         "UDslice_Ocorner_pruning",
#         "P4edge",
#         "P8edge",
#         "P4edge_P8edge_pruning",
#         "P4edge_Pcorner_pruning",
#     ]

#     tables = {}

#     @classmethod
#     def load_tables(cls, load=True, save=True):
#         table_file_path = os.path.join(os.getcwd(), SAVEFILE_NAME)

#         if os.path.isfile(table_file_path) and load:
#             print("Loading lookup tables from:", table_file_path)
#             cls.load_file(table_file_path)
#         else:
#             print("Creating lookup tables")
#             cls.create_tables()
#             if save:
#                 np.savez(table_file_path, **cls.tables)

#     @classmethod
#     def get_tables(cls, *args, **kwargs):
#         if cls.tables:
#             return cls.tables
#         else:
#             cls.load_tables(*args, **kwargs)
#             return cls.tables

#     @classmethod
#     def create_tables(self):
#         self.create_Ocorner()
#         self.create_Oedge()
#         self.create_POSud_slice()
#         self.create_UDslice_Ocorner_pruning()
#         self.create_UDslice_Oedge_pruning()

#         self.create_Pcorner()
#         self.create_P8edge()
#         self.create_P4edge()
#         self.create_P4edge_P8edge_pruning()
#         self.create_P4edge_Pcorner_pruning()

#     @classmethod
#     def load_file(cls, filename):
#         """Load the tables from the npz file, keeping them as numpy arrays."""
#         loaded_data = np.load(filename)
#         for key in cls.TABLE_KEYS:
#             cls.tables[key] = loaded_data[key]

#         # ---------------- Phase 1 moves tables ---------------------------
#         # @classmethod
#         # def create_Ocorner(cls):
#         """
#         Method to create the move table for corner orientation.
#         """

#         # Create blank cube to use for move table creation.
#         cc = cube.CubieCube()

#         # Create a blank template - 1 coordinate of the 2187 corner orientation permutations can be mapped to 18
#         # other corner orientation coordinates.
#         template = np.full((cls.NO_Ocorner_coords, 18), -1, dtype=int)

#         # For every one of the 2187 corner orientation permutations.
#         for coord in range(cls.NO_Ocorner_coords):
#             # For every one of the 6 possible moves.
#             for i, move in enumerate(cube.MOVES):
#                 # Set the cube to that permutation.
#                 cc.o_corner_coords = coord
#                 # For every power of each move.
#                 for power in range(3):
#                     # Apply the move, concerning only the orientation of the corners and ignore the permutation to
#                     # save time.
#                     cc.corner_orientation_move(move)
#                     # Record which corner orientation coordinates the permutation is mapped to by the move. Abstract
#                     # out every other piece of data.
#                     template[coord][(3 * i) + power] = cc.o_corner_coords

#         # Load the table into memory.
#         cls.tables["Ocorner"] = template

#     # @classmethod
#     # def create_Oedge(cls):
#     #     cc = cube.CubieCube()
#     #     template = np.full((cls.NO_Oedge_coords, 18), -1, dtype=int)

#     #     for coord in range(cls.NO_Oedge_coords):
#     #         for i, move in enumerate(cube.MOVES):
#     #             cc.o_edge_coords = coord
#     #             for power in range(3):
#     #                 cc.edge_orientation_move(move)
#     #                 template[coord][(3 * i) + power] = cc.o_edge_coords

#     #     cls.tables["Oedge"] = template

#     # @classmethod
#     # def create_POSud_slice(cls):
#     #     cc = cube.CubieCube()
#     #     template = np.full((cls.NO_POSud_slice_coords, 18), -1, dtype=int)

#     #     for coord in range(cls.NO_POSud_slice_coords):
#     #         for i, move in enumerate(cube.MOVES):
#     #             cc.pos_udslice_coords = coord
#     #             for power in range(3):
#     #                 cc.edge_permutation_move(move)
#     #                 template[coord][(3 * i) + power] = cc.pos_udslice_coords

#     #     cls.tables["POSud_slice"] = template

#     # ------------------ Phase 1 pruning tables ----------------------------------
#     # @classmethod
#     # def create_UDslice_Ocorner_pruning(cls):
#     #     """
#     #     Method to construct the pruning table for use in the heuristic that combines corner orientation and UD-slice
#     #     edge positioning.
#     #     """

#     #     # Create a template that allows every corner orientation coordinate to intersect with every UD-slice edge
#     #     # position coordinate.
#     #     table = np.full(
#     #         (cls.NO_POSud_slice_coords, cls.NO_Ocorner_coords), -1, dtype=int
#     #     )
#     #     # Set the root of the search.
#     #     table[0][0] = 0
#     #     # Every combination of corner orientation and UD-slice edge position can be reached within 11 moves from the
#     #     # root of the search.
#     #     for depth in range(10):
#     #         # For every UD-slice edge position coordinate
#     #         for UDslice_edge_position_coord, twist_coordinate_collection in enumerate(
#     #             table
#     #         ):
#     #             # For every corner orientation per UD-slice edge position coordinate
#     #             for corner_orientation_coord, place in enumerate(
#     #                 twist_coordinate_collection
#     #             ):
#     #                 # If the position is reachable at this depth, explore and mark all connecting positions.
#     #                 if place == depth:
#     #                     # For every move of the 18 as described in the move tables.
#     #                     for move in range(18):
#     #                         # Look up new corner orientation coordinate.
#     #                         new_corner_orientation_coord = cls.tables["Ocorner"][
#     #                             corner_orientation_coord
#     #                         ][move]
#     #                         # Look up new UD-slice edge position coordinate.
#     #                         new_UDslice_edge_position_coord = cls.tables["POSud_slice"][
#     #                             UDslice_edge_position_coord
#     #                         ][move]
#     #                         # If the new position after a move has not been explored in previous iterations of the
#     #                         # breadth first search.
#     #                         if (
#     #                             table[new_UDslice_edge_position_coord][
#     #                                 new_corner_orientation_coord
#     #                             ]
#     #                             == -1
#     #                         ):
#     #                             # Mark for exploration in next iteration of search
#     #                             table[new_UDslice_edge_position_coord][
#     #                                 new_corner_orientation_coord
#     #                             ] = (depth + 1)

#     #     cls.tables["UDslice_Ocorner_pruning"] = table

#     # @classmethod
#     # def create_UDslice_Oedge_pruning(cls):
#     #     table = np.full((cls.NO_POSud_slice_coords, cls.NO_Oedge_coords), 1, dtype=int)
#     #     table[0][0] = 0

#     #     for depth in range(9):
#     #         for slice_row, combo_coords in enumerate(table):
#     #             for twist_column, place in enumerate(combo_coords):
#     #                 if place == depth:
#     #                     for move in range(18):
#     #                         slice = cls.tables["POSud_slice"][slice_row][move]
#     #                         twist = cls.tables["Oedge"][twist_column][move]
#     #                         if table[slice][twist] == -1:
#     #                             table[slice][twist] = depth + 1

#     #     cls.tables["UDslice_Oedge_pruning"] = table

#     # ----------------------------- Phase 2 move tables -------------------------------------
#     # @classmethod
#     # def create_Pcorner(cls):
#     #     cc = cube.CubieCube()
#     #     template = np.full((cls.NO_Pcorner_coords, 18), -1, dtype=int)
#     #     # 1 is fine, 0 and 2 are not fine unless its a ud face

#     #     for coord in range(cls.NO_Pcorner_coords):
#     #         for i, move in enumerate(cube.MOVES):
#     #             cc.p_corner_coords = coord
#     #             for power in range(3):
#     #                 cc.corner_permutation_move(move)
#     #                 if power != 1 and i % 5 != 0:
#     #                     template[coord][(3 * i) + power] = -1
#     #                 else:
#     #                     template[coord][(3 * i) + power] = cc.p_corner_coords

#     #     cls.tables["Pcorner"] = template

#     # @classmethod
#     # def create_P8edge(cls):
#     #     cc = cube.CubieCube()
#     #     template = np.full((cls.NO_P8edge_coords, 18), -1, dtype=int)

#     #     # allow single turns of the up and down face, and double turns of everything else
#     #     # for up and down face, anything will go - so move % 3 = 0
#     #     # for other faces, power must be 1 or not at all
#     #     for coord in range(cls.NO_P8edge_coords):
#     #         for i, move in enumerate(cube.MOVES):
#     #             cc.p_8edge_coords = coord
#     #             for power in range(3):
#     #                 cc.edge_permutation_move(move)
#     #                 if power != 1 and i % 5 != 0:
#     #                     template[coord][(3 * i) + power] = -1
#     #                 else:
#     #                     template[coord][(3 * i) + power] = cc.p_8edge_coords
#     #     cls.tables["P8edge"] = template

#     # @classmethod
#     # def create_P4edge(cls):
#     #     cc = cube.CubieCube()
#     #     template = np.full((cls.NO_P4edge_coords, 18), -1, dtype=int)
#     #     # allow single turns of the up and down face, and double turns of everything else
#     #     # for up and down face, anything will go - so move % 3 = 0
#     #     # for other faces, power must be 1 or not at all
#     #     for coord in range(cls.NO_P4edge_coords):
#     #         for i, move in enumerate(cube.MOVES):
#     #             cc.p_4edge_coords = coord
#     #             for power in range(3):
#     #                 cc.edge_permutation_move(move)
#     #                 if power != 1 and i % 5 != 0:
#     #                     template[coord][(3 * i) + power] = -1
#     #                 else:
#     #                     template[coord][(3 * i) + power] = cc.p_4edge_coords
#     #     cls.tables["P4edge"] = template

#     # ---------------------------- Phase 2 pruning tables -----------------------------
#     # @classmethod
#     # def create_P4edge_Pcorner_pruning(cls):
#     #     table = np.full((cls.NO_P4edge_coords, cls.NO_Pcorner_coords), -1, dtype=int)
#     #     table[0][0] = 0
#     #     for depth in range(14):
#     #         for P4edge_row, combo_coords in enumerate(table):
#     #             for Pcorner_column, place in enumerate(combo_coords):
#     #                 if place == depth:
#     #                     for move in range(18):
#     #                         edge4 = cls.tables["P4edge"][P4edge_row][move]
#     #                         Pcorner = cls.tables["Pcorner"][Pcorner_column][move]
#     #                         if edge4 == -1 or Pcorner == -1:
#     #                             continue
#     #                         if table[edge4][Pcorner] == -1:
#     #                             table[edge4][Pcorner] = depth + 1

#     #     cls.tables["P4edge_Pcorner_pruning"] = table

#     # @classmethod
#     # def create_P4edge_P8edge_pruning(cls):  # Not working
#         table = np.full((cls.NO_P4edge_coords, cls.NO_P8edge_coords), -1, dtype=int)
#         table[0][0] = 0
#         for depth in range(13):
#             for P4edge_row, combo_coords in enumerate(table):
#                 for P8edge_column, place in enumerate(combo_coords):
#                     if place == depth:
#                         for move in range(18):
#                             edge4 = cls.tables["P4edge"][P4edge_row][move]
#                             edge8 = cls.tables["P8edge"][P8edge_column][move]
#                             if edge4 == -1 or edge8 == -1:
#                                 continue
#                             if table[edge4][edge8] == -1:
#                                 table[edge4][edge8] = depth + 1

#         cls.tables["P4edge_P8edge_pruning"] = table


class LookupTable:
    """
    Base class to handle loading, saving, and retrieving data from tables.
    """

    def __init__(self, size, table_name):
        self.size = size
        self.table_name = table_name
        self.table = np.full(size, -1, dtype=int)

    def load_table(self, data):
        """Load data into the table."""
        self.table = data

    def save_table(self):
        """Return the table to be saved."""
        return self.table

    def create_table(self):
        """Abstract method for creating tables. To be implemented by subclasses."""
        raise NotImplementedError


# -------------- PHASE 1 --------------
class OcornerTable(LookupTable):
    """
    Table for corner orientation move table.
    """

    n_coords = 2187

    def __init__(self):
        super().__init__((OcornerTable.n_coords, 18), "Ocorner")

    def create_table(self):
        """
        Method to create the move table for corner orientation.
        """

        # Create blank cube to use for move table creation.
        cc = cube.CubieCube()

        # For every one of the 2187 corner orientation permutations.
        for coord in range(self.size[0]):
            # For every one of the 6 possible moves.
            for i, move in enumerate(cube.MOVES):
                # Set the cube to that permutation.
                cc.o_corner_coords = coord
                # For every power of each move.
                for power in range(3):
                    # Apply the move, concerning only the orientation of the corners and ignore the permutation to
                    # save time.
                    cc.corner_orientation_move(move)
                    # Record which corner orientation coordinates the permutation is mapped to by the move. Abstract
                    # out every other piece of data.
                    self.table[coord][(3 * i) + power] = cc.o_corner_coords


class OedgeTable(LookupTable):
    """
    Table for edge orientation move table.
    """

    n_coords = 2048

    def __init__(self):
        super().__init__((OedgeTable.n_coords, 18), "Oedge")

    def create_table(self):
        cc = cube.CubieCube()
        for coord in range(self.size[0]):
            for i, move in enumerate(cube.MOVES):
                cc.o_edge_coords = coord
                for power in range(3):
                    cc.edge_orientation_move(move)
                    self.table[coord][(3 * i) + power] = cc.o_edge_coords


class POSudSliceTable(LookupTable):
    """
    Table for edge permutation (UD-slice) move table.
    """

    n_coords = 495

    def __init__(self):
        super().__init__((POSudSliceTable.n_coords, 18), "POSud_slice")

    def create_table(self):
        cc = cube.CubieCube()
        for coord in range(self.size[0]):
            for i, move in enumerate(cube.MOVES):
                cc.pos_udslice_coords = coord
                for power in range(3):
                    cc.edge_permutation_move(move)
                    self.table[coord][(3 * i) + power] = cc.pos_udslice_coords


class UDsliceOcornerPruningTable(LookupTable):
    """
    Pruning table for corner orientation and UD-slice permutation.
    """

    def __init__(self):
        super().__init__(
            (POSudSliceTable.n_coords, OcornerTable.n_coords), "UDslice_Ocorner_pruning"
        )

    def create_table(self):
        # load needed tables
        Ocorner_move_table = TableManager.Ocorner.table
        POSud_slive_move_table = TableManager.POSud_slice.table

        # Create a template that allows every corner orientation coordinate to intersect with every UD-slice edge
        # position coordinate.
        # Set the root of the search.
        self.table[0][0] = 0
        # Every combination of corner orientation and UD-slice edge position can be reached within 11 moves from the
        # root of the search.
        for depth in range(10):
            # For every UD-slice edge position coordinate
            for UDslice_edge_position_coord, twist_coordinate_collection in enumerate(
                self.table
            ):
                # For every corner orientation per UD-slice edge position coordinate
                for corner_orientation_coord, place in enumerate(
                    twist_coordinate_collection
                ):
                    # If the position is reachable at this depth, explore and mark all connecting positions.
                    if place == depth:
                        # For every move of the 18 as described in the move tables.
                        for move in range(18):
                            # Look up new corner orientation coordinate.
                            new_corner_orientation_coord = Ocorner_move_table[
                                corner_orientation_coord
                            ][move]
                            # Look up new UD-slice edge position coordinate.
                            new_UDslice_edge_position_coord = POSud_slive_move_table[
                                UDslice_edge_position_coord
                            ][move]
                            # If the new position after a move has not been explored in previous iterations of the
                            # breadth first search.
                            if (
                                self.table[new_UDslice_edge_position_coord][
                                    new_corner_orientation_coord
                                ]
                                == -1
                            ):
                                # Mark for exploration in next iteration of search
                                self.table[new_UDslice_edge_position_coord][
                                    new_corner_orientation_coord
                                ] = (depth + 1)


class UDsliceOedgePruningTable(LookupTable):
    """
    Pruning table for edge orientation and UD-slice permutation.
    """

    def __init__(self):
        super().__init__(
            (POSudSliceTable.n_coords, OedgeTable.n_coords), "UDslice_Oedge_pruning"
        )

    def create_table(self):
        Oedge_move_table = TableManager.Oedge.table
        POSud_slive_move_table = TableManager.POSud_slice.table

        self.table[0][0] = 0
        for depth in range(9):
            for slice_row, combo_coords in enumerate(self.table):
                for twist_column, place in enumerate(combo_coords):
                    if place == depth:
                        for move in range(18):
                            slice = POSud_slive_move_table[slice_row][move]
                            twist = Oedge_move_table[twist_column][move]
                            if self.table[slice][twist] == -1:
                                self.table[slice][twist] = depth + 1


# -------------- PHASE 2 --------------
class PcornerTable(LookupTable):
    """
    Table for corner permutation move table.
    """

    n_coords = 40320

    def __init__(self):
        super().__init__((PcornerTable.n_coords, 18), "Pcorner")

    def create_table(self):
        # 1 is fine, 0 and 2 are not fine unless its a ud face
        cc = cube.CubieCube()
        for coord in range(self.size[0]):
            for i, move in enumerate(cube.MOVES):
                cc.p_corner_coords = coord
                for power in range(3):
                    cc.corner_permutation_move(move)
                    if power != 1 and i % 5 != 0:
                        self.table[coord][(3 * i) + power] = -1
                    else:
                        self.table[coord][(3 * i) + power] = cc.p_corner_coords


class P8edgeTable(LookupTable):
    """
    Table for corner permutation move table.
    """

    n_coords = 40320

    def __init__(self):
        super().__init__((P8edgeTable.n_coords, 18), "Pcorner")

    def create_table(self):
        cc = cube.CubieCube()
        # allow single turns of the up and down face, and double turns of everything else
        # for up and down face, anything will go - so move % 3 = 0
        # for other faces, power must be 1 or not at all
        for coord in range(self.size[0]):
            for i, move in enumerate(cube.MOVES):
                cc.p_8edge_coords = coord
                for power in range(3):
                    cc.edge_permutation_move(move)
                    if power != 1 and i % 5 != 0:
                        self.table[coord][(3 * i) + power] = -1
                    else:
                        self.table[coord][(3 * i) + power] = cc.p_8edge_coords


class P4edgeTable(LookupTable):
    """
    Table for corner permutation move table.
    """

    n_coords = 24

    def __init__(self):
        super().__init__((P4edgeTable.n_coords, 18), "Pcorner")

    def create_table(self):
        cc = cube.CubieCube()
        # allow single turns of the up and down face, and double turns of everything else
        # for up and down face, anything will go - so move % 3 = 0
        # for other faces, power must be 1 or not at all
        for coord in range(self.size[0]):
            for i, move in enumerate(cube.MOVES):
                cc.p_4edge_coords = coord
                for power in range(3):
                    cc.edge_permutation_move(move)
                    if power != 1 and i % 5 != 0:
                        self.table[coord][(3 * i) + power] = -1
                    else:
                        self.table[coord][(3 * i) + power] = cc.p_4edge_coords


class P4edgePcornerPruningTable(LookupTable):
    """
    Pruning table for UD-slice permutation (specific) and corner permutation.
    """

    def __init__(self):
        super().__init__(
            (P4edgeTable.n_coords, PcornerTable.n_coords), "UDslice_Oedge_pruning"
        )

    def create_table(self):
        P4edge_table = TableManager.P4edge.table
        Pcorner_table = TableManager.Pcorner.table

        self.table[0][0] = 0
        for depth in range(14):
            for P4edge_row, combo_coords in enumerate(self.table):
                for Pcorner_column, place in enumerate(combo_coords):
                    if place == depth:
                        for move in range(18):
                            edge4 = P4edge_table[P4edge_row][move]
                            Pcorner = Pcorner_table[Pcorner_column][move]
                            if edge4 == -1 or Pcorner == -1:
                                continue
                            if self.table[edge4][Pcorner] == -1:
                                self.table[edge4][Pcorner] = depth + 1


class P4edgeP8EdgePruningTable(LookupTable):
    """
    Pruning table for UD-slice permutation (specific) and other edge permtuation (specific).
    """

    def __init__(self):
        super().__init__(
            (P4edgeTable.n_coords, P8edgeTable.n_coords), "UDslice_Oedge_pruning"
        )

    def create_table(self):
        P4edge_table = TableManager.P4edge.table
        P8edge_table = TableManager.P8edge.table

        self.table[0][0] = 0
        for depth in range(14):
            for P4edge_row, combo_coords in enumerate(self.table):
                for Pcorner_column, place in enumerate(combo_coords):
                    if place == depth:
                        for move in range(18):
                            edge4 = P4edge_table[P4edge_row][move]
                            Pcorner = P8edge_table[Pcorner_column][move]
                            if edge4 == -1 or Pcorner == -1:
                                continue
                            if self.table[edge4][Pcorner] == -1:
                                self.table[edge4][Pcorner] = depth + 1


class TableManager:
    """
    Manages the creation, loading, and saving of all lookup tables.
    """

    # Phase 1
    Ocorner = OcornerTable()
    Oedge = OedgeTable()
    POSud_slice = POSudSliceTable()

    UDslice_Ocorner_pruning = UDsliceOcornerPruningTable()
    UDslice_Oedge_pruning = UDsliceOedgePruningTable()

    # Phase 2
    Pcorner = PcornerTable()
    P8edge = P8edgeTable()
    P4edge = P4edgeTable()

    P4edge_Pcorner_pruning = P4edgePcornerPruningTable()
    P4edge_P8edge_pruning = P4edgeP8EdgePruningTable()

    @classmethod
    def start(cls, load=True, save=True):
        table_file_path = os.path.join(os.getcwd(), SAVEFILE_NAME)
        if os.path.isfile(table_file_path) and load:
            print("Loading lookup tables from:", table_file_path)
            cls.load_file(table_file_path)
        else:
            print("Creating lookup tables")
            cls.create_tables()
            if save:
                cls.save_file(table_file_path)

    @classmethod
    def create_tables(cls):
        cls.Ocorner.create_table()
        cls.Oedge.create_table()
        cls.POSud_slice.create_table()

        cls.UDslice_Ocorner_pruning.create_table()
        cls.UDslice_Oedge_pruning.create_table()

        # Phase 2
        cls.Pcorner.create_table()
        cls.P8edge.create_table()
        cls.P4edge.create_table()

        cls.P4edge_Pcorner_pruning.create_table()
        cls.P4edge_P8edge_pruning.create_table()

    @classmethod
    def load_file(cls, filename):
        loaded_data = np.load(filename)
        cls.Ocorner.load_table(loaded_data["Ocorner"])
        cls.Oedge.load_table(loaded_data["Oedge"])
        cls.POSud_slice.load_table(loaded_data["POSud_slice"])

        cls.UDslice_Ocorner_pruning.load_table(loaded_data["UDslice_Ocorner_pruning"])
        cls.UDslice_Oedge_pruning.load_table(loaded_data["UDslice_Oedge_pruning"])

        cls.Pcorner.load_table(loaded_data["Pcorner"])
        cls.P8edge.load_table(loaded_data["P8edge"])
        cls.P4edge.load_table(loaded_data["P4edge"])

        cls.P4edge_Pcorner_pruning.load_table(loaded_data["P4edge_Pcorner_pruning"])
        cls.P4edge_P8edge_pruning.load_table(loaded_data["P4edge_P8edge_pruning"])

    @classmethod
    def save_file(cls, filename):
        np.savez(
            filename,
            Ocorner=cls.Ocorner.save_table(),
            Oedge=cls.Oedge.save_table(),
            POSud_slice=cls.POSud_slice.save_table(),
            UDslice_Ocorner_pruning=cls.UDslice_Ocorner_pruning.save_table(),
            UDslice_Oedge_pruning=cls.UDslice_Oedge_pruning.save_table(),
            Pcorner=cls.Pcorner.save_table(),
            P8edge=cls.P8edge.save_table(),
            P4edge=cls.P4edge.save_table(),
            P4edge_Pcorner_pruning=cls.P4edge_Pcorner_pruning.save_table(),
            P4edge_P8edge_pruning=cls.P4edge_P8edge_pruning.save_table(),
        )
