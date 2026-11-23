import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle, Polygon

plt.rcParams.update({
    'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix', 'font.size': 9,
    'axes.linewidth': 0.8, 'savefig.dpi': 300, 'lines.linewidth': 1.2,
    'xtick.direction': 'in', 'ytick.direction': 'in',
})
VI = {'family': 'DejaVu Serif', 'size': 8}

def save(fig, path):
    fig.savefig(path, bbox_inches='tight', pad_inches=0.04, facecolor='white')
    plt.close(fig)

def spring(ax, p0, p1, n=8, w=0.12, lw=1.0, end=0.14):
    p0 = np.array(p0, float); p1 = np.array(p1, float)
    d = p1 - p0; L = np.linalg.norm(d); u = d / L; nrm = np.array([-u[1], u[0]])
    pts = [p0, p0 + u * L * end]
    inner = L * (1 - 2 * end)
    for i in range(n * 2):
        s = L * end + inner * (i + 0.5) / (2 * n)
        pts.append(p0 + u * s + nrm * w * (1 if i % 2 == 0 else -1))
    pts += [p0 + u * L * (1 - end), p1]
    xs, ys = zip(*pts)
    ax.plot(xs, ys, 'k', lw=lw, solid_joinstyle='round')

def ground(ax, x0, x1, y, n=None, h=0.12, up=False):
    ax.plot([x0, x1], [y, y], 'k', lw=1.2)
    n = n or int((x1 - x0) / 0.18)
    s = 1 if up else -1
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        ax.plot([x, x - h], [y, y + s * h], 'k', lw=0.6)

def dim(ax, p, q, text=None, tpos=None, style='<->', fs=9, color='k', lw=0.8, ha='left', va='center'):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle=style, lw=lw, color=color,
                                                     shrinkA=0, shrinkB=0))
    if text:
        ax.text(*(tpos or ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)), text, fontsize=fs, ha=ha, va=va)

def block(ax, x, y, w, h, fc='#d9d9d9', lw=1.0, label=None, fs=9):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec='k', lw=lw))
    if label:
        ax.text(x + w / 2, y + h / 2, label, ha='center', va='center', fontsize=fs)

def blank_axes(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_aspect('equal'); ax.axis('off')
    return fig, ax

def graph_axes(ax, xlabel, ylabel, grid=True):
    ax.set_xlabel(xlabel, loc='right'); ax.set_ylabel(ylabel, loc='top', rotation=0, labelpad=-4)
    if grid:
        ax.grid(True, which='major', color='0.55', lw=0.5)
        ax.grid(True, which='minor', color='0.85', lw=0.3)
        ax.minorticks_on()
