from typing import NewType, NoReturn, Tuple

from tools import read_file, print_solution


Instruction = NewType('Instruction', list[str, int])


def from_strings_to_instructions(instructions: list[str]) -> list[Instruction]:
	return [[instruction[:3], int(instruction[4:].replace('\n', ''))] \
		for instruction in instructions]


def next_inst(instructions: list[Instruction], idx: int, acc: int, index_set: set) \
	-> Tuple[int, bool]:

	if idx in index_set:
		return acc, False

	if idx >= len(instructions):
		return acc, True

	inst, value = instructions[idx]
	next_idx = idx + 1

	if inst == 'acc':
		acc += value
	elif inst == 'jmp':
		next_idx = idx + value

	index_set.add(idx)
	return next_inst(instructions, next_idx, acc, index_set)


def solution(instructions: list[Instruction]) -> int:
	return next_inst(instructions, 0, 0, set())[0]


def filter_jmp_nop(instructions: list[Instruction]) -> list[int]:
	return [idx for idx, instruction in enumerate(instructions) if instruction[0] != 'acc']


def switch_instruction(instructions: list[Instruction], idx: int) -> NoReturn:
	instructions[idx][0] = 'jmp' if instructions[idx][0] == 'nop' else 'nop'


def solution2(instructions: list[Instruction]) -> int:
	jmp_nop_instructions = filter_jmp_nop(instructions)

	for instruction_idx in jmp_nop_instructions:
		switch_instruction(instructions, instruction_idx)
		result = next_inst(instructions, 0, 0, set())
		switch_instruction(instructions, instruction_idx)
		if result[1]:
			break	
	
	return result[0]
	

if __name__ == '__main__':
	instructions_as_string = read_file('../resources/inputd8.txt')
	instructions = from_strings_to_instructions(instructions_as_string)
	print_solution(1, solution(instructions))
	print_solution(2, solution2(instructions))