# %%
'''
## Matplot example

** Run the cell below to import some packages and show a line plot **
'''

# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
