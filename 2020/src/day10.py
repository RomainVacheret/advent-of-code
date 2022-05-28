from tools import read_file, rstrip_lines, print_solution


def solution(adapters: list[int]) -> int:
	difference_map = {1: 0, 2: 0, 3: 0}
	last_adapter = 0

	for adapter in adapters:
		difference_map[adapter - last_adapter] += 1
		last_adapter = adapter

	return difference_map[1] * difference_map[3]


def tree_walker(adapters: list[int], counts: dict[int, int], current: int) -> int:
	value = adapters[current]

	if value in counts:
		return counts[value]
	elif value == adapters[-1]:
		return 1

	count = sum(tree_walker(adapters, counts, next_idx) for idx in range(1, 4) \
		if (next_idx := current + idx) < len(adapters) \
			and adapters[next_idx] - value <= 3)
	counts[value] = count

	return count


def solution2(adapters: list[int]) -> int:
	new_adapters = adapters.copy()
	new_adapters.insert(0, 0)
	return tree_walker(new_adapters, dict(), 0)


if __name__ == '__main__':
	all_adapters  = read_file('../resources/inputd10.txt')
	processed_adapters = [int(adapter) for adapter in rstrip_lines(all_adapters)]
	sorted_adapters = sorted(processed_adapters)
	sorted_adapters.append(sorted_adapters[-1] + 3)
	print_solution(1, solution(sorted_adapters))
	print_solution(2, solution2(sorted_adapters))