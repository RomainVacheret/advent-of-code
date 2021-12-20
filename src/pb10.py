from functools import reduce 

from tools import print_solution, read_file


chars = ['(', '[', '{', '<', ')', ']', '}', '>']


def solution(lines: list[str]) -> int:
	scores = [3, 57, 1197, 25137]
	count = 0

	for line in lines:
		stack = []

		for char in line:
			idx = chars.index(char)

			if idx < 4:
				stack.append(char)
			elif chars.index(stack.pop()) % 4 == idx % 4:
				continue
			else:
				count += scores[idx % 4]
	
	return count


def solution2(lines: list[str]) -> int:
	scores = [1, 2, 3, 4]
	counts = []

	for line in lines:
		stack = []

		for char in line:
			idx = chars.index(char)

			if idx < 4:
				stack.append(char)
			elif chars.index(stack.pop()) % 4 == idx % 4:
				continue
			else:
				stack.clear()
				break

		counts.append(reduce(lambda a, b: (a * 5 + b), 
			(scores[chars.index(char) % 4] for char in stack[::-1]), 0))

	filtered = list(filter(lambda x: x != 0, sorted(counts)))

	return filtered[len(filtered) // 2]


if __name__ == '__main__':
	lines = list(map(lambda string: string.replace('\n', ''), read_file('../resources/input10.txt')))

	print_solution(1, solution(lines))
	print_solution(2, solution2(lines))