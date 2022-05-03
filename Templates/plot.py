exec("".join(open('/home/pineman/.pythonrc', 'r').readlines()))

# x space
x = np.linspace(0.0, 10.0, 1000)
# y function, use np. math functions
y = np.sin(x)
plt.plot(x, y)

plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.grid(True)
plt.savefig('plot.png')
plt.show()
