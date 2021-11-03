import math


def convert_fun_two_arg_to_one_arg(f_two_arg, c):
	def fun_return(d):
		return f_two_arg([d, c])
	return fun_return


def passive_search(f, val_min = -2, val_max = 2, e = 0.1):
	step = e / 2
	n = math.ceil((val_max - val_min) / step)
	best = [val_min + step, f(val_min + step)]
	for i in range(2, n):
		if f(val_min + step * i) < best[1]:
			best = [val_min + step * i, f(val_min + step * i)]
	return best[0]


def golden_section(f, val_min = 6, val_max = 10, e = 0.1):
	coefficient = (5 ** 0.5 - 1) / 2
	length = (val_max - val_min) * coefficient
	c1, c2 = val_max - length, val_min + length
	while (val_max - val_min) > e:
		fun_w_c1_set, fun_w_c2_set = convert_fun_two_arg_to_one_arg(f, c1), convert_fun_two_arg_to_one_arg(f, c2)
		d_min_w_c1, d_min_w_c2 = passive_search(fun_w_c1_set), passive_search(fun_w_c2_set)
		if f([d_min_w_c1, c1]) < f([d_min_w_c2, c2]):
			val_max = c2
			length = (val_max - val_min) * coefficient
			c2 = val_min + length
		else:
			val_min = c1
			length = (val_max - val_min) * coefficient
			c1 = val_max - length
	c = val_min + (val_max - val_min) / 2
	function_with_c_set = convert_fun_two_arg_to_one_arg(f, c)
	ws = [passive_search(function_with_c_set, -4, 4), c]
	return [ws, f(ws)]
