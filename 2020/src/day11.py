from typing import NoReturn, Tuple, NewType, Optional
from collections.abc import Callable

from tools import read_file, print_solution, rstrip_lines


Coordonates = NewType('Coordonates', Tuple[int, int])
CountOccupiedSeatsFunction = NewType(
	'CountOccupiedSeatsFunction',
	Callable[[list[str], Coordonates], int])


def get_occupied_seats_count(seats: list[str], idx: Coordonates) -> int :
	count = 0

	for idx1 in range(max(0, idx[0] - 1), min(len(seats), idx[0] + 2)):
		for idx2 in range(max(0, idx[1] - 1), min(len(seats[0]), idx[1] + 2)):
			if idx != (idx1, idx2):
				count += int(seats[idx1][idx2] == '#')
	
	return count


switch_seat_state: Callable[str, str] = lambda state: '#' if state == 'L' else 'L'
is_floor: Callable[str, str] = lambda state: state == '.'


def apply_rules(
	seats: list[str], 
	occupied_seats_func: CountOccupiedSeatsFunction,
	empty_seats_tolerence: int) -> list[int]:

	return [[switch_seat_state(seat) if not is_floor(seat) and \
		(((occupied_seats := occupied_seats_func(
			seats, 
			(line_idx, seat_idx))) >= empty_seats_tolerence and \
				seat == '#') or (seat == 'L' and occupied_seats == 0)) else seat \
			for seat_idx, seat in enumerate(line)] \
				for line_idx, line in enumerate(seats)]


def standardized_solution(
	seats: list[str], 
	func: CountOccupiedSeatsFunction,
	threshold: int) -> int:

	last = seats

	while 1:
		new_state = apply_rules(last, func, threshold)
		
		if new_state == last:
			return sum(char == '#' for line in new_state for char in line)

		last = new_state


def solution(seats: list[str]) -> int:
	return standardized_solution(seats, get_occupied_seats_count, 4)


def get_next_seat(
	seats: list[str], 
	seat: Coordonates, 
	func_to_apply: Tuple[int, int]) -> Optional[Coordonates]:
		
	max_height = len(seats)
	max_width = len(seats[0])
	next_coordonate = (
		seat[0] + func_to_apply[0],
		seat[1] + func_to_apply[1])

	return next_coordonate if 0 <= next_coordonate[0] < max_height and \
		0 <= next_coordonate[1] < max_width else None


def is_next_seat_occupied(
	seats: list[str], 
	seat: Coordonates, 
	func_to_apply: Tuple[int, int]) -> bool:

	while 1:
		coordonates = get_next_seat(seats, seat, func_to_apply)
		
		if coordonates is None or \
			(next_seat := seats[coordonates[0]][coordonates[1]]) == 'L':
			return False
		elif next_seat == '#':
			return True

		seat = coordonates


def get_occupied_seats_count_improved(seats: list[str], idx: Coordonates) -> int:
	count = 0

	for idx1 in range(-1, 2):
		for idx2 in range(-1, 2):
			if (0, 0) != (idx1, idx2):
				count += int(is_next_seat_occupied(seats, idx, (idx1, idx2)))

	return count


def solution2(seats: list[str]) -> int:
	return standardized_solution(seats, get_occupied_seats_count_improved, 5)


if __name__ == '__main__':
	puzzle_input = read_file('../resources/inputd11.txt')
	lines = [rstrip_lines(line.replace('\n', '')) for line in puzzle_input]
	print_solution(1, solution(lines))
	print_solution(2, solution2(lines))