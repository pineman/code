close all; clear; clc;

%% Signal (approximately continuous time)
tmin = -3;
tmax = 3;
dt = 1e-3;
t = tmin : dt : tmax - dt;
x = signal(t);

%% Sampling
fs = 10; % Sampling frequency
Ts = 1/fs; % Sampling period
nmin = ceil(tmin / Ts); % Number of samples from t < 0
nmax = floor(tmax / Ts); % Number of samples from t > 0
n = nmin:nmax-1; % Sample numbers [time is n*Ts]
xn = signal(n*Ts); % Sample the signal at n*Ts seconds (every Ts seconds)
N = length(n); % Number of samples

%% Frequency transform
% MATLAB's fft() computes the DFT
df = fs/N; % Frequency bins
% Nyquist theorem:
% At sample frequency fs, only frequency components up to fs/2 Hz are
% faithfully reconstructed, so only plot until there.
f = -fs/2 : df : fs/2-df; % Frequency domain
X = fftshift(fft(signal(n*Ts))/N);
X_mag = abs(X);
X_phase = angle(X);
X_real = real(X);
X_imag = imag(X);

%% Plots
figure('Name','Signal and Samples','NumberTitle','off');
hold on;
plot(t, x);
stem(n*Ts, xn);
figure('Name','DFT - Magnitude','NumberTitle','off');
stem(f, X_mag);
axis([-5 5 -0.1 0.6]);
figure('Name','DFT - Phase','NumberTitle','off');
stem(f, X_phase);
axis([-5 5 -pi pi]);
figure('Name','DFT - Real Part','NumberTitle','off');
stem(f, X_real);
axis([-5 5 -0.1 0.6]);
figure('Name','DFT - Imaginary Part','NumberTitle','off');
stem(f, X_imag);
axis([-5 5 -0.6 0.6]);
figure('Name','Inverse Transform vs. Signal','NumberTitle','off');
hold on;
plot(t, x);
stem(n*Ts, xn);
stem(n*Ts, ifft(ifftshift(X))*N);

function y = signal(t)
	y = rectpuls(t, 1);
	%y = heaviside(t, 1);
	%y = cos(4*pi*t);
end
