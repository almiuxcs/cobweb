from matplotlib import pyplot as plt 
import numpy as np

def plot(a, x0=0.1):

	# Plot f(x) = ax(1 - x)
	x = np.linspace(0, 1, 1000)
	fx = a * x * (1 - x)	
	plt.plot(x, fx, color="black")
	
	# Plot y = x
	plt.plot([0, 1], [0, 1], color="red")

	# Plot f^50(x0)
	next_x = a * x0 * (1 - x0)
	plt.plot([x0, x0], [0, next_x], color="black")
	plt.plot([x0, next_x], [next_x, next_x], color="red")

	plt.show()


def main():
	plot(2)
	

if __name__ == "__main__":
	main()