"""プロットのベース

```python
with Figure(n_col, n_row) as fig:
    ax,_ = subplot_instance.plot(*args, **kwargs)
```
を実現する。

with 構文に
* enter -> シングルトンの生成
* exit -> シングルトンの破棄
を行えばよさそう。
"""
from typing import Optional
import matplotlib.pyplot as plt

class PlotBase():
    def __init__(self):
        self.ax = None

    def set_ax(fig):
        assert isinstance(fig, Figure)
        self.ax = fig.get_ax()

    def plot(self):
        raise ValueError('not impliment')


class Figure():
    def __init__(self, n_row:int, n_col:int):
        """
        Parameters
        ----------
        n_col: int

        n_row: int
        """
        self.n_row = n_row
        self.n_col = n_col
        self.max_ax = n_row * n_row
        self.current_ax = 0
        fig, ax = plt.subplots(n_row, n_col)
        self.figure = fig
        self.ax = ax

    def __del__(self):
        self.figure.close()

    def plot(plot_obj):
        assert isinstance(plot_obj, PlotBese)
        plot_obj.set_ax(self)
        ret = plot_obj.plot()
        return ret

    def get_ax(self, idx:Optional[int]=None):
        """get ax

        Parameters
        ----------
        idx: Optional[int]
        """
        if idx is None:
            idx = self.current_ax
        row, col = self.__idx_to_2d(idx)
        return self.ax[row, col]

    def get_figure(self):
        return self.figure

    def __idx_to_2d(self, idx):
        row = idx // self.n_row
        col = idx % self.n_col
        return row, col

    def next_ax(self):
        current = self.current_ax + 1
        assert current < self.max_ax, "ax の最大値越え"
        return

    def __get_next_ax(self):
        next_ax = self.current_ax + 1
        assert current < self.max_ax, "ax の最大値越え"
        return next_ax

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.figure.show()
        self.current_ax = 0
        return