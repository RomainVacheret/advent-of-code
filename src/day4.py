import re

from typing import Final

from tools import read_file_string, print_solution


MANDATORY_FIELDS: Final = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def are_passport_fields_valid(passport: dict) -> bool:
	return all(field in passport for field in MANDATORY_FIELDS)


def solution(passports: list[str]) -> int:
	return len(list(filter(are_passport_fields_valid, passports)))


def process_passport_data(passport: str) -> dict:
	passport = passport.replace('\n', ' ')
	fields = passport.split(' ')
	return {l[0]: l[1] for field in fields if (l := field.split(':'))}


def is_passport_valid(passport: dict) -> bool:
	is_byr_valid = len(x := passport['byr']) == 4 and 1920 <= int(x) <= 2002
	is_iyr_valid = len(x := passport['iyr']) == 4 and 2010 <= int(x) <= 2020 
	is_eyr_valid = len(x := passport['eyr']) == 4 and 2020 <= int(x) <= 2030
	is_hgt_cm_valid = (x := passport['hgt']).endswith('cm') and 150 <= int(x[:-2]) <= 193
	is_hgt_in_valid = (x := passport['hgt']).endswith('in') and 59 <= int(x[:-2]) <= 76
	is_hgt_valid = is_hgt_in_valid or is_hgt_cm_valid 
	is_hcl_valid = re.compile(r'^#[0-9a-f]{6,}').match(passport['hcl']) is not None
	is_ecl_valid = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	is_pid_valid = len(x := passport['pid']) == 9 and x.isdigit()

	return all((is_byr_valid, is_iyr_valid, is_eyr_valid, is_hcl_valid,
		is_hgt_valid, is_ecl_valid, is_pid_valid))


def solution2(passports: list[dict]) -> int:
	func = lambda p: are_passport_fields_valid(p) and is_passport_valid(p)
	return len(list(filter(func, passports)))


if __name__ == '__main__':
	file_content = read_file_string('../resources/inputd4.txt')
	passports = file_content.split('\n\n')
	print_solution(1, solution(passports))
	processed_passports = [process_passport_data(passport) for passport in passports]
	print_solution(2, solution2(processed_passports))