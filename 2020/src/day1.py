from typing import Iterable, Optional

from tools import read_file, print_solution


def solution(expense_report: Iterable[int]) -> Optional[int]:
	memo = set()
	for expense in expense_report:
		lookup_value = 2020 - expense

		if lookup_value in memo:
			return expense * lookup_value
		else:
			memo.add(expense)

	return None


def solution2(expense_report: Iterable[int]) -> Optional[int]:
	memo = dict()
	mem = set()
	for expense in expense_report:
		lookup_value = 2020 - expense

		if lookup_value in memo:
			return expense * memo[lookup_value]
		else:
			for v in mem:
				sum_ = v + expense
				if expense < 2020:
					memo[sum_] = v * expense
			mem.add(expense)

	return None


if __name__ == '__main__':
	values = read_file('../resources/inputd1.txt')
	values_as_int = list(map(int, values))
	print_solution(1, solution(values_as_int))
	print_solution(2, solution2(values_as_int))