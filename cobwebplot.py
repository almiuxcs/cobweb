from matplotlib import pyplot as plt 
import numpy as np

def plot(a, x0=0.1):	

	x = np.linspace(0, 1, 1000)
	y = 2 * x * (1 - x)

	plt.plot(x, y, color="black")
	plt.plot([0, 1], [0, 1], color="red")
	plt.show()


if __name__ == "__main__":
	plot(2)