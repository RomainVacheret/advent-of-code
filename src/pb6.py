from tools import print_solution, read_file


def solution(fishes: list[int], days: int) -> int:
	counts = [fishes.count(nb) for nb in range(9)]

	for _ in range(days):
		counts.append(counts[0])
		counts[7] += counts[0] 
		del counts[0]

	return sum(counts)


if __name__ == '__main__':
	fishes = list(map(int, read_file('../resources/input6.txt')[0].split(',')))

	print_solution(1, solution(fishes, 80))
	print_solution(2, solution(fishes, 256))