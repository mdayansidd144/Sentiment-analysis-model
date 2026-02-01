from collections import deque
import numpy as np
memory = deque(maxlen = 5000)
def adaptive_update(model,x,y):
  memory.append((x,y))

  if len(memory)>=32:
    batch = memory[-32:]
    xb = np.vstack([x for x,_ in batch])
    yb = np.array([y for _, y in batch])
    model.fit(xb,yb,epochs=1,verbose=0)