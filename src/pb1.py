from tools import print_solution, read_file


def solution(depths: list[int]) -> int:
	return sum([int(depths[idx] < depths[idx + 1]) for idx in range(len(depths) -1)])


def solution2(depths: list[int]) -> int:
	return solution([depths[idx] + depths[idx +1] + depths[idx + 2] for idx in range(len(depths) - 2)])


if __name__ == '__main__':
	depths = list(map(int, read_file('../resources/input1.txt')))

	print_solution(1, solution(depths))
	print_solution(2, solution(depths))