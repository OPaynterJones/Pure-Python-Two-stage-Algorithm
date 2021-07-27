setup = """
Cparity: dict[int, int] = {
    0: 0,
    1: 2,
    2: 1}
"""

s = """
def get_orientation_builtins(index: int) -> int:
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

    return int(f"{n}{Cparity[parity]}")
get_orientation_builtins(1494)
"""
from timeit import repeat
print(sum(repeat(stmt=s, setup=setup, repeat=5))/5)