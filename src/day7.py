from typing import Optional, NewType, Tuple

from tools import read_file, print_solution


ContainedBag = NewType('ContainedBag', Tuple[int, Optional[str]])
ProcessedRule = NewType('ProcessedRule', Tuple[str, list[ContainedBag]])


def clean_up_rules(rules: list[str]) -> list[ProcessedRule]:
	full_strip = lambda x: x.strip().rstrip()
	color_to_tuple = lambda x: (int(x[0]), y) \
		if (y := x[2:]) != ' other' else (0, None)

	color_content_list = [(l[0][:-6], l[1].replace('.', '').replace('\n', '')) \
		for rule in rules if (l := rule.split('contain'))]
	colors, contents = zip(*color_content_list)
	striped_and_split_contents = [map(full_strip, c) for content in contents \
		if (c := content.replace('bags', '').replace('bag', '').split(','))]
	contents_as_tuple = [list(map(color_to_tuple, rule)) \
		for rule in striped_and_split_contents]
	
	return list(zip(colors, contents_as_tuple))


def processed_rules_to_map(rules: list[ProcessedRule]) \
	-> dict[str, list[ContainedBag]]:
	
	return {key: value for key, value in rules}


def solution(rules: dict[str, list[ContainedBag]]) -> int:
	color_set = set()

	def container_count(target: str) -> int:
		count = 0
		for key, value in rules.items():
			colors = [clrs[1] for clrs in value]
			
			if target in colors and key not in color_set:
				count += container_count(key) + bool(target in colors)
				color_set.add(key)

		return count
	
	return container_count('shiny gold')


def filter_empty_bags(rules: dict[str, list[ContainedBag]]) -> list[str]:
	return [color for color, bags in rules.items() \
		if len(bags) == 1 and bags[0][1] is None]


def solution2(rules: dict[str, list[ContainedBag]]) -> int:
	empty_bags = filter_empty_bags(rules)
	bag_count_dict = {name: 1 for name in empty_bags}

	def count_sub_bags(target: str):
		if target in bag_count_dict:
			return bag_count_dict[target]

		count = sum(value * count_sub_bags(color) \
			for value, color in rules[target] if color is not None) + 1
		bag_count_dict[target] = count

		return count
	
	return count_sub_bags('shiny gold') - 1

if __name__ == '__main__':
	all_rules = read_file('../resources/inputd7.txt')
	processed_rules = clean_up_rules(all_rules) 
	processed_rules_as_map = processed_rules_to_map(processed_rules)
	print_solution(1, solution(processed_rules_as_map))
	print_solution(2, solution2(processed_rules_as_map))
