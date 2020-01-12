import numpy as np
import matplotlib.pyplot as plt

def keep_idx(i):
    if i in [0, 1, 3, 5, 8, 9, 10, 11, 13, 15, 17]:
        return False
    return True;

def filter_tup(t):
    tmp = [item for idx, item in enumerate(t) if keep_idx(idx)]
    return tuple(tmp)
 
dat1 = (0.6667,0.6875,0.5617,0.2500,0.4898,0.2500,0.2653,1.0000,1.0000,0.9630,0.8450,0.0000,0.8333,1.0000,0.7083,1.0000,0.5600,1.0000,0.5800)  
dat2 = (0.6667,0.6875,0.5123,0.2500,0.7143,0.2500,0.3673,1.0000,1.0000,0.9630,0.8471,0.0000,0.8056,1.0000,0.4375,1.0000,0.4400,1.0000,0.5100)
dat3 = (0.6667,0.6875,0.6080,0.2500,0.6531,0.2500,0.2653,1.0000,1.0000,0.9630,0.8574,0.0000,0.8056,1.0000,0.3889,1.0000,0.4700,1.0000,0.4000)
dat4 = (0.6667,0.6875,0.5895,0.2500,0.7449,0.2500,0.2449,0.8889,1.0000,0.9630,0.8554,0.0000,0.6944,1.0000,0.3194,1.0000,0.3800,1.0000,0.3800)  
dat5 = (0.6667,0.6875,0.6358,0.2500,0.7245,0.2500,0.2449,0.7778,1.0000,0.9630,0.8471,0.0000,0.6944,1.0000,0.3333,1.0000,0.3500,1.0000,0.3700)

label1 = 'k=1' 
label2 = 'k=2' 
label3 = 'k=3' 
label4 = 'k=4' 
label5 = 'k=5' 

# create plot
fig, ax = plt.subplots()
index = np.arange(len(filter_tup(dat1)))
bar_width = 0.14
 
plt.bar(index + 0 * bar_width, filter_tup(dat1), bar_width, color='b', label=label1)
plt.bar(index + 1 * bar_width, filter_tup(dat2), bar_width, color='r', label=label2)
plt.bar(index + 2 * bar_width, filter_tup(dat3), bar_width, color='g', label=label3)
plt.bar(index + 3 * bar_width, filter_tup(dat4), bar_width, color='grey', label=label4)
plt.bar(index + 4 * bar_width, filter_tup(dat5), bar_width, color='maroon', label=label5)
 
plt.xlabel('Queries (NTCIR-12)')
plt.ylabel('bpref')
# plt.title('uni-1 score changes over k (full relevance)')
x_sticks = tuple(str(i) for i in range(1, 21) if i != 2) + tuple(['overall'])
plt.xticks(index + bar_width, filter_tup(x_sticks), rotation='30')
plt.legend()
 
w, h =(6, 6)
fig.set_size_inches(w, h)
plt.show()
fig.savefig('./img/uni-weights-diff-k.eps')
plt.close(fig)    
