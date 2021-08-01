from typing import NoReturn, Any

def read_file(filename) -> list[str]:
	with open(filename, 'r') as file:
		values = file.readlines()

	return values


def read_file_string(filename) -> str:
	with open(filename, 'r') as file:
		content = file.read()

	return content


def print_solution(part_nb: int, solution: Any) -> NoReturn:
	print(f'Solution part n°{part_nb}: {solution}')