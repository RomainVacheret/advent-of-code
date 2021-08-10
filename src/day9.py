from typing import Optional

from tools import read_file, print_solution, rstrip_lines


def to_int(iterable: list[str]) -> list[int]:
	return [int(val) for val in rstrip_lines(iterable)]


def solution(numbers: list[int]) -> Optional[int]:
	for idx, number in enumerate(numbers[25:]):
		flag = False
		range_ = numbers[idx: idx + 26]
		for a in range_:
			for b in range_:
				if a != b and a + b == number:
					flag = True
					break

			if flag: 
				break
		if not flag:
			return number

	return None


def solution2(numbers: list[int], target: int) -> Optional[int]:
	contiguous = []

	for idx in range(len(numbers)):
		for val in numbers[idx:]:
			contiguous.append(val)
			sum_ = sum(contiguous)

			if len(contiguous) >= 2 and sum_ == target:
				return min(contiguous) + max(contiguous)
			elif sum_ > target:
				while sum(contiguous) > target:
					del contiguous[0]

	return None

if __name__ == '__main__':
	number_list = read_file('../resources/inputd9.txt')
	formated_number_list = to_int(number_list)
	result = solution(formated_number_list)
	print_solution(1, result)
	print_solution(2, solution2(formated_number_list, result))