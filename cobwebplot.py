from matplotlib import pyplot as plt 
import numpy as np

def plot(a, x0=0.1, iterations=50):
	""" Plot a cobweb graph using the equation:
		a * x * (1 - x)
	
		It does 50 iterations to plot the graph. 
		
		The default value of x0 is 0.1 and it must 
		be in the interval ]0, 1[
	"""

	# If x0 isn't valid 
	if x0 <= 0 or x0 >= 1: return

	plt.title("Cobweb Plot")

	# Plot f(x) = ax(1 - x)
	x = np.linspace(0, 1, 1000)
	fx = a * x * (1 - x)	
	plt.plot(x, fx, color="black", label="f(x) = ax(1-x)")
	
	# Plot y = x
	plt.plot([0, 1.2], [0, 1.2], color="red")

	# Plot f^50(x0)
	last_x, last_y = x0, 0
	for _ in range(iterations):
		next_x = a * last_x * (1 - last_x)
		# Plot vertical line 
		plt.plot([last_x, last_x], [last_y, next_x], color="black")
		# Plot horizontal line
		plt.plot([last_x, next_x], [next_x, next_x], color="red")

		last_x, last_y = next_x, next_x

	plt.show()


def main():
	plot(4, 0.2)
	

if __name__ == "__main__":
	main()