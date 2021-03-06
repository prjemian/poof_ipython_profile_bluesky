"""
Configure matplotlib in interactive mode for Jupyter notebook
"""

__all__ = [
    "plt",
]

from ..session_logs import *

logger.info(__file__)

# %matplotlib inline
get_ipython().magic("matplotlib inline")
import matplotlib.pyplot as plt

plt.ion()
