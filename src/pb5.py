from typing import NewType

from tools import print_solution, read_file


Coordinates = NewType('Coordinates', list[list[int]])


def func(a, b, c, d):
	m1 = max(a, c)
	m2 = min(a, c)
	m3 = max(b, d)
	m4 = min(b, d)

	return m1 - m2 == m1 % ((m2 or 2) or 1) and m3 - m4 == m3 % ((m4 or 2) or 1)


def get_hv_range(coords: Coordinates) -> Coordinates:
	(a, b), (c, d) = coords

	if a == c:
		return [(a, val) for val in range(min(b, d), max(b, d) + 1)]
	elif b == d:
		return [(val, b) for val in range(min(a, c), max(a, c) + 1)]
	else:
		return None
	

def solution(vents: list[str]) -> int:
	filtered = list(filter(lambda x: x is not None, 
		(get_hv_range(coord) for coord in vents)))
	d = {}

	for coords in filtered:
		for coord in coords:
			d[coord] = 1 if coord not in d else d[coord] + 1

	return len(list(filter(lambda x: x > 1, d.values())))


if __name__ == '__main__':
	vents = [[list(map(int, coord.split(','))) 
		for coord in line.replace('\n', '').split(' -> ')] 
			for line in read_file('../resources/input5.txt')]	

	print_solution(1, solution(vents))