from solver.cube import CubieCube, FaceletCube, to_cubie_cube
from solver.phases import Phase1, Phase2


class Solver:
    

    def __init__(self, cube_definition):
        if isinstance(cube_definition, str):
            self.facelet_cube = FaceletCube(cube_definition)
            self.cc = to_cubie_cube(self.facelet_cube)
        elif isinstance(cube_definition, FaceletCube):
            self.facelet_cube = cube_definition
            self.cc = to_cubie_cube(self.facelet_cube)
        elif isinstance(cube_definition, CubieCube):
            self.cc = cube_definition
        else:
            raise ValueError(
                "Unsupported cube definition type. Must be a string, FaceletCube, or CubieCube."
            )

        self.phase1 = Phase1()
        self.phase2 = Phase2()

        self.final_solutions = []

    def find_solution(self):
        if self.cc.is_solved():
            return None

        else:
            moves1, powers1 = self.phase1.find_solution(self.cc)

            # apply partial solution to cube
            cc = CubieCube(data=self.cc.to_data_array(), moves=(moves1, powers1))

            moves2, powers2 = self.phase2.find_solution(cc)

            return [moves1 + moves2, powers1 + powers2]
