from typing import NewType
from functools import reduce

from tools import read_file, print_solution


Slope = NewType('Slope', tuple[int, int])


def solution(map_: list[str], slop:Slope) -> int:
	height = len(map_)
	width = len(map_[0])
	x, y = 0, 0
	count = 0

	while y < height - 1:
		x = (x + slop[0]) % width
		y += slop[1]
		count += map_[y][x] == '#'

	return count 


def solution2(map_: list[str], slopes: list[Slope]) -> int:
	func = lambda x, y: x * y
	return reduce(func, [solution(map_, slop) for slop in slopes])


if __name__ == '__main__':
	map_ = read_file('../resources/inputd3.txt')
	map_ = [line.rstrip() for line in map_]
	print_solution(1, solution(map_, (3, 1)))
	print_solution(2, solution2(map_, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))