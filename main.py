import matplotlib.pyplot as plt
import random


def fun_decorator(f, ws):
	def f_returned(x):
		return ws[0] + ws[1] * x
	return f_returned


@fun_decorator([0, 8])
def fun(x):
	return 8 * x


def fun_error_decorator(f_to_calculate_error_to, xs, yds):
	def fe(x):
		return sum((f_to_calculate_error_to(x) - yds[i]) ** 2 for i, x in enumerate(xs))
	return fe


def gradient(dots):
	c = (len(dots[0]) * sum(x * dots[1][i] for i, x in enumerate(dots[0])) - sum(dots[0]) * sum(dots[1])) / (
			len(dots[0]) * sum(x ** 2 for x in dots[0]) - sum(dots[0]) ** 2)
	d = (sum(dots[1]) - c * sum(dots[0])) / len(dots[0])
	return [d, c]


def get_dots(ff, aa, bb, nn, ss):
	v, step = [[], []], (bb - aa) / (nn - 1)
	v[0] = [aa + step * i for i in range(nn)]
	v[1] = [ff(vx) + ss * random.uniform(-0.5, 0.5) for vx in v[0]]
	return [v[0], v[1]]


def do_plot_dots(plot, dots, do = ''):
	plot.scatter(dots[0], dots[1])
	if do == 'show':
		plot.show()
	else:
		return plot


def do_plot_fun(f, dots, do = ''):
	plt.title('function plot w/ dots')
	plt.plot(dots[0], [f(xs) for xs in dots[0]])
	if do == 'show':
		plt.show()
	else:
		return plt


def main():
	# setting the variables
	a, b, n, s = -4, 2, 24, 10

	# drawing the function
	dots = get_dots(fun, a, b, n, s)
	do_plot_dots(do_plot_fun(fun, dots), dots, do = 'show')

	# gradient search used to find weights
	coefficients = gradient(dots)
	print(coefficients)

	# getting the error function
	fe = fun_error_decorator(fun, dots[0], dots[1])


if __name__ == '__main__':
	main()
