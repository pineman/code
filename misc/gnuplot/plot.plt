set terminal pngcairo enhanced font 'Verdana,10'
set output 'output.png'

# optional
set xlabel "X values"
set ylabel "Y values"
set title "Plot of Y values"
set grid

plot "new" using 0:1 with linespoints title 'Y values'

