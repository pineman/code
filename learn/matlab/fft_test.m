close all
clear
clc
%% Signal (approximately continuous time)
tmin = -1;
tmax = 1;
dt = 0.0001;
t = tmin : dt : tmax - dt;
x = signal(t);

%% Sampling
fs = 100; % Sampling frequency
Ts = 1/fs; % Sampling period
nmin = ceil(tmin / Ts); % Number of samples from t < 0
nmax = floor(tmax / Ts); % Number of samples from t > 0
n = nmin:nmax; % Sample numbers [only n*Ts is time]
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
figure('Name','FT - Magnitude','NumberTitle','off');
stem(f, X_mag);
axis([-5 5 -0.1 0.6]);
figure('Name','FT - Phase','NumberTitle','off');
stem(f, X_phase);
axis([-5 5 -pi pi]);
figure('Name','FT - Real Part','NumberTitle','off');
stem(f, X_real);
axis([-5 5 -0.1 0.6]);
figure('Name','FT - Imaginary Part','NumberTitle','off');
stem(f, X_imag);
axis([-5 5 -0.6 0.6]);
figure('Name','Inverse Transform vs. Signal','NumberTitle','off');
hold on;
plot(t, x);
stem(n*Ts, xn);
stem(n*Ts, ifft(ifftshift(X))*N);
