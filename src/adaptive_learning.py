from collections import deque
import numpy as np
MEMORY_SIZE = 5000
BATCH_SIZE = 32
memory = deque(maxlen=MEMORY_SIZE)
def adaptive_update(model, x, y):
    """
    x: padded input of shape (1, MAX_LEN)
    y: label (0 or 1)
    """
    x = np.array(x).reshape(1, -1)
    y = np.array([y])
    memory.append((x, y))
    if len(memory) >= BATCH_SIZE:
        batch = list(memory)[-BATCH_SIZE:]
        xb = np.vstack([item[0] for item in batch])
        yb = np.vstack([item[1] for item in batch]).reshape(-1)
        model.fit(
            xb,
            yb,
            epochs=1,
            batch_size=8,
            verbose=0
        )
