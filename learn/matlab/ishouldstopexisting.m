figure('Name','RLC série','NumberTitle','off');
hold on;

my_legend = {};
R = 10;
C = 270e-12;
for L = [0 1e-9 5e-9 10e-9 15e-9]
    rlc_s = tf([1, 0], [L/R, 1, 1/(R*C)]);
    step(rlc_s);
    my_legend{end+1} = strcat('L = ', num2str(L));
end
legend(my_legend);
grid;
