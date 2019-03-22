t = -1.75:1e-3:1.75;
plot(t, square(t*2*pi));
hold on;
plot(t, gradient(square(2*pi*t)));