# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(100000)
plt.hist(x,100)
plt.title('Normal distribution with u=0,sigma=1')
plt.savefig('.\png\matplotlib_histogram_2.png')
plt.show()