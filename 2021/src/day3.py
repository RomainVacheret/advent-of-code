from tools import read_file, print_solution


def ones_or_zeros(binaries: list[str], idx: int, default: str, func) -> list[str]:
	ones = []
	zeros = []

	for binary in binaries:
		ones.append(binary) if binary[idx] == '1' else zeros.append(binary)

	length = len(ones) - len(zeros)

	if length == 0:
		return ones if default == '1' else zeros

	return ones if func(length) else zeros


def solution(binaries: list[str]) -> int:
	arr = [0 for _ in range(len(binaries[0]))] 

	for binary in binaries:
		for (idx, val) in enumerate(binary):
			arr[idx] += 1 if val == '1' else 0

	gamma = ['1' if val > len(binaries) // 2 else '0' for val in arr]

	return int(str_arr := ''.join(gamma), 2) * int(''.join('1' if val == '0' else '0' for val in str_arr), 2)


def solution2(binaries: list[str]) -> int:
	current_list_oxy = binaries
	current_list_co2 = binaries

	for idx in range(len(binaries[0])):
		current_list_co2 = current_list_co2 if len(current_list_co2) == 1 else \
			ones_or_zeros(current_list_co2, idx, '0', lambda x: x < 0)
		current_list_oxy = current_list_oxy if len(current_list_oxy) == 1 else \
			ones_or_zeros(current_list_oxy, idx, '1', lambda x: x > 0)

	return int(''.join(current_list_oxy[0]), 2) * int(''.join(current_list_co2[0]), 2)


if __name__ == '__main__':
	binaries = read_file('../resources/input3.txt')
	processed_binaries = list(map(lambda x: x[:-1], binaries[:-1])) + [binaries[-1]]
	print_solution(1, solution(processed_binaries))
	print_solution(2, solution2(processed_binaries))
