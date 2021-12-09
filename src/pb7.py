from functools import wraps

from tools import print_solution, read_file


def get_cost(distance: int, d: dict={}) -> int:
	if distance not in d:
		d[distance] = sum(range(distance + 1))
		
	return d[distance]


def solution(positions: list[int]) -> int:
	return min(sum(abs(position - current) for current in positions) for position in range(max(positions)))


def solution2(positions: list[int]) -> int:
	return min(sum(get_cost(abs(position - current + 1)) for current in positions) for position in range(max(positions)))


if __name__ == '__main__':
	positions = list(map(int, read_file('../resources/input7.txt')[0].split(',')))
	print_solution(1, solution(positions))
	print_solution(2, solution2(positions))
