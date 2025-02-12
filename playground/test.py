
import numpy as np

q = np.array([1.1538,0.3077,-0.4615])
M = np.array([[1,-4,3],[1,-2,5],[1,-1,4],[1,1,1],[1,2,-1],[1,4,3]])
vals = []
for row in M:
    print(row)
    print(np.dot(q, row))
    vals.append(abs(np.dot(q,row)))


closest = min(vals)
norm = np.sqrt(np.dot(q.T,q))
margin = closest/norm
print(f"margin: {margin}")


R = np.sqrt(1+4+25)
mistake =(R/margin)**2
print(f"mistake: {mistake}")