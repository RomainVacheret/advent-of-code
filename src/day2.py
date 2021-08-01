from tools import read_file, print_solution


def parse_line(line: str) -> dict:
	policy, password = line.split(':')
	rules, letter = policy.split(' ')
	min_, max_ = rules.split('-')
	return {
		'min': int(min_), 
		'max': int(max_), 
		'let': letter, 
		'psw': password.replace(' ', '').replace('\n', '')}


def solution(elts: list[dict]) -> int:
	count = 0
	for elt in elts:
		cnt = elt['psw'].count(elt['let'])
		if elt['min'] <= cnt <= elt['max']:
			count += 1

	return count


def solution2(elts: list[dict]) -> int:
	count = 0
	for elt in elts:
		psw = elt['psw']
		let = elt['let']
		if (psw[elt['min'] - 1] == let) ^ (psw[elt['max'] - 1] == let):
			count += 1

	return count


if __name__ == '__main__':
	text = read_file('../resources/inputd2.txt')
	lines = [parse_line(line) for line in text]
	print_solution(1, solution(lines))
	print_solution(2, solution2(lines))