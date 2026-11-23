# -*- coding: utf-8 -*-
"""Mau ve hinh. Chay: FIGDIR=<thu muc> PYTHONPATH=scripts python3 figs_template.py"""
import os
from figlib import *
OUT = os.environ.get('FIGDIR', '.')

# Do thi co luoi, nhan truc bang mathtext (dau phay thap phan: dung dinh dang chu, khong dung mathtext cho so).
t = np.linspace(0, 4, 50)
fig, ax = plt.subplots(figsize=(3.3, 2.1))
ax.plot(t, 2 * t, 'k')
ax.set_xlim(0, 4.2); ax.set_ylim(0, 9)
graph_axes(ax, '$t$ (s)', '$x$ (m)')
save(fig, os.path.join(OUT, 't_fig.png'))

# So do: lo xo va khoi (spring, block, ground, dim tu figlib)
fig, ax = blank_axes(3.0, 2.0)
ax.set_xlim(0, 7); ax.set_ylim(0, 4)
ground(ax, 0.5, 6.5, 0.5, n=24)
spring(ax, (1.0, 1.3), (3.8, 1.3), n=7, w=0.2)
block(ax, 3.8, 0.5, 1.3, 1.6, label='$m$')
save(fig, os.path.join(OUT, 't_diagram.png'))
print('figs ok')
