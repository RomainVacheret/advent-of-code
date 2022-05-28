from typing import Tuple
from functools import reduce

from tools import print_solution, read_file


def get_low_point(lava: list[list[int]]) -> list[list[int]]:
	result = []
	func_filter = lambda pair: (0 <= pair[0] < len(lava) and 0 <= pair[1] < len(lava[0]))

	for row_idx, col in enumerate(lava):
		for col_idx, val in enumerate(col):
			neighbors = [(row_idx + 1, col_idx) , (row_idx - 1, col_idx), 
				(row_idx, col_idx + 1), (row_idx, col_idx - 1)]
			possible_neighbors = filter(func_filter, neighbors)
			neighbor_values = [lava[neighbor[0]][neighbor[1]] for neighbor in possible_neighbors]

			if all(neighbor_value > val for neighbor_value in neighbor_values):
				result.append((row_idx, col_idx))
	return result


def solution(lava: list[list[int]]) -> int:
	return sum(map(lambda pair: lava[pair[0]][pair[1]] + 1, get_low_point(lava)))


def solution2(lava: list[list[int]]) -> int:
	low_points = get_low_point(lava)
	visited = [[0 for _ in range(len(lava[0]))] for _ in range(len(lava))]
	dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
	queue = []
	bassins = []

	for p in low_points:
		queue.append((p, -1))
		count = 0 

		while len(queue):
			point, value = queue.pop(0)

			if point[0] < 0 or point[0] >= len(lava) or point[1] < 0 \
				or point[1] >= len(lava[0]) or visited[point[0]][point[1]]:
				continue

			current = lava[point[0]][point[1]]

			if current == 9:
				visited[point[0]][point[1]] = 1
			elif current > value:
				count += 1
				for dir in dirs:
					next_point = (point[0] + dir[0], point[1] + dir[1])
					queue.append((next_point, current))
				visited[point[0]][point[1]] = 1

		bassins.append(count)

	return reduce(lambda a, b: a * b, sorted(bassins)[-3::])


if __name__ == '__main__':
	lava = [list(map(int, line.replace('\n', ''))) \
		for line in read_file('../resources/input9.txt')]

	print_solution(1, solution(lava))
	print_solution(2, solution2(lava))