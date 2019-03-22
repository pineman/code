import matplotlib.pyplot as plt
import numpy as np

# x space
x = np.arange(0, 256, 1)
# y function, use np. math functions
y = [255,  255,  254,  254,  254,  253,  253,  253,  252,  252,  252,  251,  251,  251,  250,  250,  250,  249,  249,  249,  248,  248,  248,  247,  247,  247,  246,  246,  246,  245,  245,  245,  244,  244,  244,  243,  243,  243,  242,  242,  242,  241,  241,  241,  240,  240,  240,  239,  239,  239,  238,  238,  238,  237,  237,  237,  236,  236,  236,  235,  235,  235,  234,  234,  234,  233,  233,  233,  232,  232,  232,  231,  231,  231,  230,  230,  230,  229,  229,  229,  228,  228,  228,  227,  227,  227,  226,  226,  226,  225,  225,  225,  224,  224,  224,  223,  223,  222,  222,  222,  221,  221,  221,  220,  220,  220,  219,  219,  219,  218,  218,  218,  217,  217,  217,  216,  216,  216,  215,  215,  215,  214,  214,  214,  213,  213,  213,  212,  212,  212,  211,  211,  211,  210,  210,  210,  209,  209,  209,  208,  208,  208,  207,  207,  207,  206,  206,  206,  205,  205,  205,  204,  204,  204,  203,  203,  203,  202,  202,  202,  201,  201,  201,  200,  200,  200,  199,  199,  199,  198,  198,  198,  197,  197,  197,  196,  196,  196,  195,  195,  195,  194,  194,  194,  193,  193,  193,  192,  192,  192,  191,  191,  188,  185,  182,  179,  176,  173,  170,  167,  164,  161,  158,  155,  152,  149,  146,  143,  140,  137,  134,  131,  128,  125,  122,  119,  116,  113,  110,  107,  104,  101,  98,  95,  93,  90,  87,  84,  81,  78,  75,  72,  69,  66,  63,  60,  57,  54,  51,  48,  45,  42,  39,  36,  33,  30,  27,  24,  21,  18,  15,  12,  9,  6,  3,  0]
plt.plot(x, y)

plt.xlabel('Iterations (chosen 255)')
plt.ylabel('Blue (255: no blue, 0: 100% blue)')
plt.title('')
plt.grid(True)
plt.savefig('plot.png')
plt.show()
