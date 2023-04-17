import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatter

def amdahl_speedup(p, n):
    return 1 / ((1 - p) + p / n)

# A list of p values you want to plot
p_values = [0.5, 0.75, 0.9, 0.95, 0.99]
N = 2**12+1
processors = np.linspace(1, N, 10**5)  # Number of processors

fig, ax = plt.subplots()
# Loop through the p_values list and plot each line
for i, p in enumerate(p_values):
    speedup = amdahl_speedup(p, processors)
    ax.plot(processors, speedup, label=f'p = {p}')
    max_value = round(np.max(speedup))
    cutoff_y = 10 ** (np.log10(max_value) - 3/20)
    cutoff_y = max_value*0.85
    for j, v in enumerate(processors):
        if amdahl_speedup(p, v) > cutoff_y:
            v = processors[j-1]
            ax.vlines(x=v, ymin=0, ymax=cutoff_y, linestyle='--', color='gray')
            break

# Set x-axis to log2 scale
ax.set_xscale('log', base=2)
ax.xaxis.set_major_formatter(LogFormatter(base=2, labelOnlyBase=True))
xticks = [2**i for i in range(int(np.log2(processors[-1]))+1) if 2**i <= processors[-1]]
ax.set_xticks(xticks)

ax.set_ylim([1, 20])
ax.set_xlim([1, N])
ax.text(256, 13.5, r'$S_p(N) = \frac{1}{(1-p) + \frac{p}{N}}$', fontsize=14)

plt.xlabel('Number of Processors $N$ ($log_2$ scale)')
plt.ylabel('Latency Speedup $S_p$')
plt.title('Amdahl\'s Law')
plt.legend()
plt.grid()
plt.savefig('amdahls_law.pdf', dpi=300)
plt.show()

