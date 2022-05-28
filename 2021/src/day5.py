from typing import NewType

from tools import print_solution, read_file


Coordinates = NewType('Coordinates', list[list[int]])


def get_range(coords: Coordinates, solution: int) -> Coordinates:
	(a, b), (c, d) = coords
	abs1 = abs(a - c)
	abs2 = abs(b - d)

	if a == c:
		return [(a, val) for val in range(min(b, d), max(b, d) + 1)]
	elif b == d:
		return [(val, b) for val in range(min(a, c), max(a, c) + 1)]
	elif solution == 2 and abs1 == abs2: # TODO -> improve
		tmp =[(a, b), (c, d)]
		f = tmp[a > c]
		s = tmp[a < c]
		cond = f[1] > s[1]
		return [(count + f[0], f[1] + count * (-1 if cond else 1)) \
			for count in range(abs(a - c) + 1 )]

	return None
	
def solution(vents: list[str], solution_nb: int) -> int:
	filtered = list(filter(lambda x: x is not None, 
		(get_range(coord, solution_nb) for coord in vents)))
	d = {}

	for coords in filtered:
		for coord in coords:
			d[coord] = 1 if coord not in d else d[coord] + 1

	return len(list(filter(lambda x: x > 1, d.values())))


if __name__ == '__main__':
	vents = [[list(map(int, coord.split(','))) 
		for coord in line.replace('\n', '').split(' -> ')] 
			for line in read_file('../resources/input5.txt')]	

	print_solution(1, solution(vents, 1))
	print_solution(2, solution(vents, 2))