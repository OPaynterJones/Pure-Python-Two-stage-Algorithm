from enum import IntEnum
from typing import Union, Any

facelet_to_col = ["U", "R", "L", "F", "B", "D", "X"]


class Axes(IntEnum):
    """
    Integer values of each of the axis for quicker and more memory efficient manipulation.
    """

    U = 0
    R = 1
    L = 2
    F = 3
    B = 4
    D = 5


class Facelet_Indicies(IntEnum):
    """
    Facelets indices that reference the position of a facelet in the string definition of a cube.
    """

    U0 = 0
    U1 = 1
    U2 = 2
    U3 = 3
    U4 = 4
    U5 = 5
    U6 = 6
    U7 = 7
    U8 = 8
    R0 = 9
    R1 = 10
    R2 = 11
    R3 = 12
    R4 = 13
    R5 = 14
    R6 = 15
    R7 = 16
    R8 = 17
    L0 = 18
    L1 = 19
    L2 = 20
    L3 = 21
    L4 = 22
    L5 = 23
    L6 = 24
    L7 = 25
    L8 = 26
    F0 = 27
    F1 = 28
    F2 = 29
    F3 = 30
    F4 = 31
    F5 = 32
    F6 = 33
    F7 = 34
    F8 = 35
    B0 = 36
    B1 = 37
    B2 = 38
    B3 = 39
    B4 = 40
    B5 = 41
    B6 = 42
    B7 = 43
    B8 = 44
    D0 = 45
    D1 = 46
    D2 = 47
    D3 = 48
    D4 = 49
    D5 = 50
    D6 = 51
    D7 = 52
    D8 = 53


class URF_Facelet_Indices(IntEnum):
    U0 = 0
    U1 = 1
    U2 = 2
    U3 = 3
    U4 = 4
    U5 = 5
    U6 = 6
    U7 = 7
    U8 = 8
    R0 = 9
    R1 = 10
    R2 = 11
    R3 = 12
    R4 = 13
    R5 = 14
    R6 = 15
    R7 = 16
    R8 = 17
    F0 = 27
    F1 = 28
    F2 = 29
    F3 = 30
    F4 = 31
    F5 = 32
    F6 = 33
    F7 = 34
    F8 = 35


class Corner_Indices(IntEnum):
    """
    Indices of the default corners.
    """

    URF = 0
    UFL = 1
    ULB = 2
    UBR = 3

    DFR = 4
    DLF = 5
    DBL = 6
    DRB = 7


class Edge_Indices(IntEnum):
    UR = 0
    UF = 1
    UL = 2
    UB = 3

    DR = 4
    DF = 5
    DL = 6
    DB = 7

    FR = 8
    FL = 9
    BL = 10
    BR = 11


corner_facelet_indices: list[
    tuple[Facelet_Indicies, Facelet_Indicies, Facelet_Indicies]
] = [
    (Facelet_Indicies.U8, Facelet_Indicies.R0, Facelet_Indicies.F2),
    (Facelet_Indicies.U6, Facelet_Indicies.F0, Facelet_Indicies.L2),
    (Facelet_Indicies.U0, Facelet_Indicies.L0, Facelet_Indicies.B2),
    (Facelet_Indicies.U2, Facelet_Indicies.B0, Facelet_Indicies.R2),
    (Facelet_Indicies.D2, Facelet_Indicies.F8, Facelet_Indicies.R6),
    (Facelet_Indicies.D0, Facelet_Indicies.L8, Facelet_Indicies.F6),
    (Facelet_Indicies.D6, Facelet_Indicies.B8, Facelet_Indicies.L6),
    (Facelet_Indicies.D8, Facelet_Indicies.R8, Facelet_Indicies.B6),
]

edge_facelet_indices: list[Union[tuple[Facelet_Indicies, Facelet_Indicies], Any]] = [
    (Facelet_Indicies.U5, Facelet_Indicies.R1),
    (Facelet_Indicies.U7, Facelet_Indicies.F1),
    (Facelet_Indicies.U3, Facelet_Indicies.L1),
    (Facelet_Indicies.U1, Facelet_Indicies.B1),
    (Facelet_Indicies.D5, Facelet_Indicies.R7),
    (Facelet_Indicies.D1, Facelet_Indicies.F7),
    (Facelet_Indicies.D3, Facelet_Indicies.L7),
    (Facelet_Indicies.D7, Facelet_Indicies.B7),
    (Facelet_Indicies.F5, Facelet_Indicies.R3),
    (Facelet_Indicies.F3, Facelet_Indicies.L5),
    (Facelet_Indicies.B5, Facelet_Indicies.L3),
    (Facelet_Indicies.B3, Facelet_Indicies.R5),
]

corner_axes: list[tuple[Axes, Axes, Axes]] = [
    (Axes.U, Axes.R, Axes.F),
    (Axes.U, Axes.F, Axes.L),
    (Axes.U, Axes.L, Axes.B),
    (Axes.U, Axes.B, Axes.R),
    (Axes.D, Axes.F, Axes.R),
    (Axes.D, Axes.L, Axes.F),
    (Axes.D, Axes.B, Axes.L),
    (Axes.D, Axes.R, Axes.B),
]

edge_axes = [
    (Axes.U, Axes.R),
    (Axes.U, Axes.F),
    (Axes.U, Axes.L),
    (Axes.U, Axes.B),
    (Axes.D, Axes.R),
    (Axes.D, Axes.F),
    (Axes.D, Axes.L),
    (Axes.D, Axes.B),
    (Axes.F, Axes.R),
    (Axes.F, Axes.L),
    (Axes.B, Axes.L),
    (Axes.B, Axes.R),
]

# Create the U move.
cpU = [
    Corner_Indices.UBR,
    Corner_Indices.URF,
    Corner_Indices.UFL,
    Corner_Indices.ULB,
    Corner_Indices.DFR,
    Corner_Indices.DLF,
    Corner_Indices.DBL,
    Corner_Indices.DRB,
]
coU = [0, 0, 0, 0, 0, 0, 0, 0]
epU = [
    Edge_Indices.UB,
    Edge_Indices.UR,
    Edge_Indices.UF,
    Edge_Indices.UL,
    Edge_Indices.DR,
    Edge_Indices.DF,
    Edge_Indices.DL,
    Edge_Indices.DB,
    Edge_Indices.FR,
    Edge_Indices.FL,
    Edge_Indices.BL,
    Edge_Indices.BR,
]
eoU = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

UP = [cpU, coU, epU, eoU]

# Create the R move.
cpR = [
    Corner_Indices.DFR,
    Corner_Indices.UFL,
    Corner_Indices.ULB,
    Corner_Indices.URF,
    Corner_Indices.DRB,
    Corner_Indices.DLF,
    Corner_Indices.DBL,
    Corner_Indices.UBR,
]
coR = [2, 0, 0, 1, 1, 0, 0, 2]
epR = [
    Edge_Indices.FR,
    Edge_Indices.UF,
    Edge_Indices.UL,
    Edge_Indices.UB,
    Edge_Indices.BR,
    Edge_Indices.DF,
    Edge_Indices.DL,
    Edge_Indices.DB,
    Edge_Indices.DR,
    Edge_Indices.FL,
    Edge_Indices.BL,
    Edge_Indices.UR,
]
eoR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

RIGHT = [cpR, coR, epR, eoR]

# Create the F move.
cpF = [
    Corner_Indices.UFL,
    Corner_Indices.DLF,
    Corner_Indices.ULB,
    Corner_Indices.UBR,
    Corner_Indices.URF,
    Corner_Indices.DFR,
    Corner_Indices.DBL,
    Corner_Indices.DRB,
]
coF = [1, 2, 0, 0, 2, 1, 0, 0]
epF = [
    Edge_Indices.UR,
    Edge_Indices.FL,
    Edge_Indices.UL,
    Edge_Indices.UB,
    Edge_Indices.DR,
    Edge_Indices.FR,
    Edge_Indices.DL,
    Edge_Indices.DB,
    Edge_Indices.UF,
    Edge_Indices.DF,
    Edge_Indices.BL,
    Edge_Indices.BR,
]
eoF = [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]

FRONT = [cpF, coF, epF, eoF]

# Create the D move.
cpD = [
    Corner_Indices.URF,
    Corner_Indices.UFL,
    Corner_Indices.ULB,
    Corner_Indices.UBR,
    Corner_Indices.DLF,
    Corner_Indices.DBL,
    Corner_Indices.DRB,
    Corner_Indices.DFR,
]
coD = [0, 0, 0, 0, 0, 0, 0, 0]
epD = [
    Edge_Indices.UR,
    Edge_Indices.UF,
    Edge_Indices.UL,
    Edge_Indices.UB,
    Edge_Indices.DF,
    Edge_Indices.DL,
    Edge_Indices.DB,
    Edge_Indices.DR,
    Edge_Indices.FR,
    Edge_Indices.FL,
    Edge_Indices.BL,
    Edge_Indices.BR,
]
eoD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DOWN = [cpD, coD, epD, eoD]


# Create the L move.
cpL = [
    Corner_Indices.URF,
    Corner_Indices.ULB,
    Corner_Indices.DBL,
    Corner_Indices.UBR,
    Corner_Indices.DFR,
    Corner_Indices.UFL,
    Corner_Indices.DLF,
    Corner_Indices.DRB,
]
coL = [0, 1, 2, 0, 0, 2, 1, 0]
epL = [
    Edge_Indices.UR,
    Edge_Indices.UF,
    Edge_Indices.BL,
    Edge_Indices.UB,
    Edge_Indices.DR,
    Edge_Indices.DF,
    Edge_Indices.FL,
    Edge_Indices.DB,
    Edge_Indices.FR,
    Edge_Indices.UL,
    Edge_Indices.DL,
    Edge_Indices.BR,
]
eoL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LEFT = [cpL, coL, epL, eoL]

# Create the B move.
cpB = [
    Corner_Indices.URF,
    Corner_Indices.UFL,
    Corner_Indices.UBR,
    Corner_Indices.DRB,
    Corner_Indices.DFR,
    Corner_Indices.DLF,
    Corner_Indices.ULB,
    Corner_Indices.DBL,
]
coB = [0, 0, 1, 2, 0, 0, 2, 1]
epB = [
    Edge_Indices.UR,
    Edge_Indices.UF,
    Edge_Indices.UL,
    Edge_Indices.BR,
    Edge_Indices.DR,
    Edge_Indices.DF,
    Edge_Indices.DL,
    Edge_Indices.BL,
    Edge_Indices.FR,
    Edge_Indices.FL,
    Edge_Indices.UB,
    Edge_Indices.DB,
]
eoB = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1]
BACK = [cpB, coB, epB, eoB]


raw_colours = ["White", "Green", "Red", "Orange", "Yellow", "Blue"]
