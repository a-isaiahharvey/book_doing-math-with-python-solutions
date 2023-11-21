import sys
import matplotlib.pyplot as plt


def quad_func_calc():
    x_values = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y_values = []
    for x in x_values:
        # Calculate the value of quadratic function
        y_values.append(x**2 + x * 2 + 1)
    draw_graph(x_values, y_values)


def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('x-axis')

    plt.ylabel('y-axis')
    plt.title('Quadratic Function')


if __name__ == '__main__':
    quad_func_calc()
    plt.savefig(sys.stdout.buffer)
