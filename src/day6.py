from tools import read_file_string, print_solution, rstrip_lines


def process_group_answers(answers: list[str]) -> int:
	return len(set(answers))


def solution(all_answers: list[list[str]]) -> int:
	return sum(process_group_answers(group) for group in all_answers)


def process_group_answers_everyone(answers: list[str]) -> int:
	answers_set = set(answers[0])

	for answer in answers[1:]:
		answers_set = answers_set.intersection(answer)

	return len(answers_set)


def solution2(all_answers: list[list[str]]) -> int:
	return sum(process_group_answers_everyone(group) for group in all_answers)


if __name__ == '__main__':
	answers = read_file_string('../resources/inputd6.txt')
	answers_per_group = answers.split('\n\n')
	processed_answers_per_group = [answer.replace('\n', '') \
		for answer in answers_per_group]
	print_solution(1, solution(processed_answers_per_group))
	answers_per_person = [answer.split('\n') for answer in answers_per_group]
	print_solution(1, solution2(answers_per_person))