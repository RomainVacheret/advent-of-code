import math

from typing import Optional

from tools import read_file, print_solution


def compute_value(sequence: list[str], mm, letters) -> int:
	for char in sequence[:-1]:
		mid = sum(mm) / 2
		lower = char == letters[0]
		mm[lower] = math.floor(mid) if lower else math.ceil(mid)

	return mm[sequence[-1] == letters[1]]
	

def compute_seat_id(boarding_pass: str) -> int:
	mmr = [0, 127]
	mmc = [0, 7]
	row = boarding_pass[:7]
	column = boarding_pass[7:]
	row_value = compute_value(row, mmr, ('F', 'B'))
	column_value = compute_value(column, mmc, ('L', 'R'))

	return row_value * 8 + column_value


def compute_seats_ids(boarding_pass: list[str]) -> list[int]:
	return [compute_seat_id(boarding_pass) for boarding_pass in boarding_passes]
	
		
def solution(boarding_passes: list[str]) -> int:
	return max(compute_seats_ids(boarding_passes))


def solution2(board_passes: list[str]) -> Optional[int]:
	seats_ids = compute_seats_ids(board_passes)
	sorted_ids = sorted(seats_ids)

	for idx, seat_id in enumerate(sorted_ids[1:-1]):
		if sorted_ids[idx] == seat_id - 2:
			return seat_id - 1

	return None

		
if __name__ == '__main__':
	boarding_passes = read_file('../resources/inputd5.txt')
	reformated_boarding_passes = [boarding_pass.rstrip() for boarding_pass in boarding_passes]
	print_solution(1, solution(reformated_boarding_passes))
	print_solution(2, solution2(reformated_boarding_passes))
