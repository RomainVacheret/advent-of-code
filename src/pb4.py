from typing import Tuple

from tools import read_file, print_solution


def process_input(file_input: list[int]) -> Tuple[list[int], list[int]]:
	nb_sequence = list(map(int, file_input.pop(0).replace('\n', '').split(',')))
	del file_input[0]

	boards = []
	for line_idx in range(0, len(file_input), 6):
		x = ' '.join(file_input[line_idx:line_idx + 5]).replace('\n', '').split(' ')
		y = map(int, filter(lambda string : string not in (' ', ''), x))
		boards.append(list(y))		
	
	return (nb_sequence, boards)


def is_winning_board(checks: list[int], idx: int) -> bool:
	return all(checks[idx // 5 * 5:idx // 5 * 5 + 5]) or all(checks[idx % 5::5])


def compute_final_score(checks: list[int], board: list[int], number: int) -> int:
	return number * sum(nb for (nb, flag) in zip(board, checks) if not flag)


def solution(bingo_input: Tuple[list[int], list[int]]) -> int:
	numbers, boards = bingo_input
	called = [[0 for _ in range(25)] for _ in range(len(boards))]

	for number in numbers:
		for (board, check) in zip(boards, called):
			try:
				idx = board.index(number)
				check[idx] = 1
			except ValueError:
				continue

			if is_winning_board(check, idx):
				return compute_final_score(check, board, number)


def solution2(bingo_input: Tuple[list[int], list[int]]) -> int:
	numbers, boards = bingo_input
	called = [[0 for _ in range(25)] for _ in range(len(boards))]

	for number in numbers:
		current = 0

		while current < len(boards):
			board = boards[current]
			check = called[current]

			try:
				idx = board.index(number)
				check[idx] = 1
			except ValueError:
				current += 1
				continue
		
			if is_winning_board(check, idx):
				if len(boards) == 1:
					return compute_final_score(called[0], boards[0], number)	
				del boards[current]
				del called[current]
				current -= 1

			current += 1
	

if __name__ == '__main__':
	file_input = read_file('../resources/input4.txt')
	bingo_input = process_input(file_input)
	print_solution(1, solution(bingo_input))
	print_solution(2, solution2(bingo_input))