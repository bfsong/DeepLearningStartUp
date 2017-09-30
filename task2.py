#进阶任务2
import numpy as np

def func(a):
    if a < 0.0:
        return 0.0
    else:
        return a

print('处理前')
r = np.random.randn(100)
print(r)
print('处理后')
vfunc = np.vectorize(func)
print(vfunc(r))
