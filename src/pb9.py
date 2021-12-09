from tools import print_solution, read_file


def solution(lava: list[list[int]]) -> int:
	result = []
	func_filter = lambda pair: (0 <= pair[0] < len(lava) and 0 <= pair[1] < len(lava[0]))

	for row_idx, col in enumerate(lava):
		for col_idx, val in enumerate(col):
			neighbors = [(row_idx + 1, col_idx) , (row_idx - 1, col_idx), 
				(row_idx, col_idx + 1), (row_idx, col_idx - 1)]
			possible_neighbors = filter(func_filter, neighbors)
			neighbor_values = [lava[neighbor[0]][neighbor[1]] for neighbor in possible_neighbors]

			if all(neighbor_value > val for neighbor_value in neighbor_values):
				result.append(val + 1)
	
	return sum(result)


if __name__ == '__main__':
	lava = [list(map(int, line.replace('\n', ''))) \
		for line in read_file('../resources/input9.txt')]
	print_solution(1, solution(lava))