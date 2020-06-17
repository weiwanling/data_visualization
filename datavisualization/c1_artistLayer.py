from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure 
fig=Figure()
canvas=FigureCanvas(fig)

import numpy as np
x=np.random.randn(10000)

ax=fig.add_subplot(111)
ax.hist(x,100)

ax.set_title('Normal distribution with u=0,sigma=1')
fig.savefig('.\png\matplotlib_histogram_1.png')