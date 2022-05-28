from typing import Any, NoReturn

def print_solution(part_nb: int, solution: Any) -> NoReturn:
	print(f'Solution part n°{part_nb}: {solution}')


def read_file(filename: str) -> list[str]:
	with open(filename, 'r') as file:
		return file.readlines()

	