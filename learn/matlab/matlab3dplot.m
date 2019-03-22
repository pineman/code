%close all; clear; clc;

%graphics_toolkit("qt");
graphics_toolkit("gnuplot");

x = linspace(-8, 8, 41)';
y = x;
[X,Y] = meshgrid(x,y);
%r = sqrt(X.^2 + Y.^2);
r = sqrt(X.^2 + Y.^2) + eps;
Z = sin(r)./r;
surf(X, Y, Z);

% From octave's source code:
##tx = linspace (-8, 8, 41)';
##ty = tx;
##[xx, yy] = meshgrid (tx, ty);
##r = sqrt (xx .^ 2 + yy .^ 2) + eps;
##tz = sin (r) ./ r;
##surf (tx, ty, tz);