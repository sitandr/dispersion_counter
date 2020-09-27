from dispersion.num_value import *


def sin(a):
	if type(a) == Num_value:
		return a.__sin__()
	else:
		return math.sin(a)


def cos(a):
	if type(a) == Num_value:
		return a.__cos__()
	else:
		return math.cos(a)


def tg(a):
	if type(a) == Num_value:
		return a.__tg__()
	else:
		return math.tan(a)


def ctg(a):
	if type(a) == Num_value:
		return a.__ctg__()
	else:
		return 1 / math.tan(a)


def log(a, b):
	if type(a) == Num_value:
		return a.__log__(b)
	else:
		return math.log(a, b)


def ln(a):
	if type(a) == Num_value:
		return a.__ln__()
	else:
		return math.log(a)


def arctg(a):
	if type(a) == Num_value:
		return a.__arctg__()
	else:
		return math.atan(a)


def console_text(text):
	strings = text.split('\n')

	for i in strings:
		t += i
		if is_not_full(i):
			t += '\n'
			continue
		console(t)
		t = ''


def console(string):
	"""
	Just input usual python commands. If you want to add a
	value with dispersion, input (x?y) or (x±y)
	"""
	last = 0
	string = string.replace('±', '?')
	while True:
		i = string.find('?', last)
		if i == -1:
			break
		last = i
		j_1 = string.rfind('(', 0, i)
		j_2 = string.rfind(')', i)
		if j_1 != -1 and j_2 != -1:
			string = (string[:j_1] + 'Num_value' + string[j_1:i] + ',' + string[i + 1:])
	# print(string)
	exec(string, globals())


def console_mode():
	""" Inputted text will be read using 'console' command """
	t = ''
	while True:
		string = input()
		t += string
		if string.strip() == 'exit()':
			break
		if is_not_full(string):
			t += '\n'
			continue
		console(t)
		t = ''


def is_not_full(string):
	return len(string) > 0 and (string.strip()[-1] == ':' or
	                            string[0] == '\t' or
	                            (len(string) >= 4 and string[:4] == '    '))


if __name__ == '__main__':
	console_mode()
