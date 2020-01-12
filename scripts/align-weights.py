import numpy as np
import matplotlib.pyplot as plt

dat1 = (0.5327,0.5407,0.5867,0.5128,0.5867,0.5597,0.5068,0.5942,0.5862,0.5835,0.5837,0.5822,0.5839)
dat2 = (0.6486,0.6512,0.6664,0.6621,0.6664,0.6553,0.6455,0.6732,0.6762,0.6644,0.6739,0.6749,0.6765)

label1 = 'partial relevance' 
label2 = 'full relevance' 

# create plot
fig, ax = plt.subplots()
index = np.arange(len(dat1))
bar_width = 0.35
 
rects1 = plt.barh(index + 0 * bar_width, dat1, bar_width,
                 color='b', hatch=" ",
                 label=label1)
 
rects2 = plt.barh(index + 1 * bar_width, dat2, bar_width,
                 color='r', hatch=" ",
                 label=label2)
 
plt.xlabel('bpref score')
# plt.ylabel('Run')

#plt.title('')
x_sticks = ("opt-only","opd-opt-a6","opd-opt-a4","opd-only","uni-beta-1","uni-beta-2","uni-beta-3","2-beta-90","2-beta-75","2-beta-60","3-beta-80-3","3-beta-75-4","3-beta-70-4")
plt.yticks(index + bar_width, x_sticks)
plt.legend(loc=3)
plt.xlim([0.40, 0.7])
ax.invert_yaxis()
 
w, h =(5, 4.5)
fig.set_size_inches(w, h)
plt.tight_layout()

plt.show()
fig.savefig('./img/align-weights.eps')

plt.close(fig)    
