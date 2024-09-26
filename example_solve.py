from solver import Solver
from solver.cube import CubieCube, FaceletCube, to_cubie_cube

test = CubieCube()

test.shuffle()
s = Solver(test)
moves, powers = s.find_solution()
test.apply_move_array(moves, powers)
print(moves, powers)
print(test.is_solved())
