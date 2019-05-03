exec(open(__import__('os').environ.get('PYTHONSTARTUP')).read())


# The matlab script takes a signal as input and from a given sample frequency
# determines the number of samples needed.
# The signal is also assumed  to be "continous time" and includes information
# about its time interval.
#
# Here the time interval is a function of N, the number of samples.

tmin = -3
tmax = 3
Ts = 0.05 # sampling period
Fs = 1/Ts
t = np.arange(tmin, tmax, Ts) # sample space
N = len(t)
y = np.cos(2*np.pi*t)
plt.plot(t, y)
plt.show()

Y = np.fft.fftshift(np.fft.fft(y))/N
f = np.linspace(-Fs/2, Fs/2, N)
plt.plot(f, abs(Y))
plt.show()
