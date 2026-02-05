import numpy as np
import matplotlib.pyplot as plt
def plot_ecg(timeline):
    if not timeline:
        return None

    x = np.arange(len(timeline))
    y = np.array(timeline)
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(x, y, color="#00ffcc", linewidth=2)
    ax.axhline(0.5, linestyle="--", color="gray", alpha=0.4)
    ax.set_title("Audience Sentiment Waveform")
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#0f172a")

    return fig
