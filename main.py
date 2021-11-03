import plots as plt
import matplotlib.pyplot as mpl
import algorithms as alg


D = 0
C = 8
E = 0.001


def fun(x, ws):
	return ws[0] + x * ws[1]


def fun_by_weights_fun(fun_frame, ws):
	def fun_by_weights(x):
		return fun_frame(x, ws)
	return fun_by_weights


def fun_ref(x):
	return fun_by_weights_fun(fun, [D, C])(x)


def fun_error_to_fun_by_weights(dots):
	def fun_to_return(ws):
		fun_predicted = fun_by_weights_fun(fun, ws)
		return sum((fun_predicted(x) - dots[1][i]) ** 2 for i, x in enumerate(dots[0]))
	return fun_to_return


def gradient(dots):
	c = (len(dots[0]) * sum(x * dots[1][i] for i, x in enumerate(dots[0])) - sum(dots[0]) * sum(dots[1])) / (
			len(dots[0]) * sum(x ** 2 for x in dots[0]) - sum(dots[0]) ** 2)
	return [(sum(dots[1]) - c * sum(dots[0])) / len(dots[0]), c]


def f_args_from_list_to_positional(fun_to_modify):
	def f_return(w0, w1):
		return fun_to_modify([w0, w1])
	return f_return


def conduct_experiment(rf, a, b, N, A):
	dots = plt.get_dots(rf, a, b, N, A)
	error_fun = fun_error_to_fun_by_weights(dots)
	gs_search = alg.golden_section(error_fun)
	coefficients = gradient(dots)
	mpl.title(f'plots w/ A = {A}')
	plt.add_fun_to_plot(mpl, rf, 'given function')
	plt.add_fun_to_plot(mpl, fun_by_weights_fun(fun, gs_search[0]), 'golden-passive function')
	plt.add_fun_to_plot(mpl, fun_by_weights_fun(fun, coefficients), 'gradient function')
	plt.add_dots_to_plot(mpl, dots)
	mpl.legend()
	mpl.show()
	with open('results.txt', 'a') as file:
		file.write(f'experiment w/ A = {A}\n')
		file.write(f'golden-passive coeffs: {gs_search[0]}\n')
		file.write(f'lowest squares method coeffs: {coefficients}\n\n')
	plt.graph(f_args_from_list_to_positional(error_fun), -4, 4, 4, 12, f'err-fun-sur w/ A ={A}')
	return [dots, coefficients, error_fun, alg.golden_section(error_fun)]


def main():
	a, b, N, A1, A2 = -4, 2, 24, 10, 0

	with open('results.txt', 'w') as file:
		file.write(f'data given:\nd = w0 = {D}\nc = w1 = {C}\n\n')

	conduct_experiment(fun_ref, a, b, N, A1)
	conduct_experiment(fun_ref, a, b, N, A2)


if __name__ == '__main__':
	main()
