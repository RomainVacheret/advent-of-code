from typing import Tuple
from tools import print_solution, read_file


def solution(directions: list[Tuple[str, int]]) -> int:
	depth = 0
	horizontal = 0

	for direction, value in directions:
		if direction == 'forward':
			horizontal += value
		elif direction == 'down':
			depth += value
		elif direction == 'up':
			depth -= value
	
	return depth * horizontal


def solution2(directions: list[Tuple[str, int]]) -> int:
	depth = 0
	horizontal = 0
	aim = 0

	for direction, value in directions:
		if direction == 'forward':
			horizontal += value
			depth += aim * value
		elif direction == 'down':
			aim += value
		elif direction == 'up':
			aim -= value
	
	return depth * horizontal


if __name__ == '__main__':
	directions = [(dir, int(val)) 
		for dir, val in [line.replace('\n', '').split(' ')  
			for line in read_file('../resources/input2.txt')]]

	print_solution(1, solution(directions))
	print_solution(2, solution2(directions))