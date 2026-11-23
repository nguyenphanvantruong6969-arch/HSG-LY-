from figlib import *
import os
OUT = os.environ.get('FIGDIR', '.')
p = lambda n: os.path.join(OUT, n)
pi = np.pi

# ---- Cau 7: hai dao dong ----
t = np.linspace(0, 1.4, 600)
x1 = 4 * np.cos(2 * pi * (t - 0.1) / 1.2)
x2 = 3 * np.cos(2 * pi * (t - 0.4) / 1.2)
fig, ax = plt.subplots(figsize=(3.3, 2.1))
ax.plot(t, x1, 'k', label='(1)'); ax.plot(t, x2, 'k--', label='(2)')
ax.axhline(0, color='k', lw=0.8)
ax.set_xlim(0, 1.4); ax.set_ylim(-4.6, 4.8)
ax.set_xticks(np.arange(0, 1.41, 0.1)); ax.set_xticklabels([f'{v:.1f}'.replace('.', ',') if i % 2 == 0 else '' for i, v in enumerate(np.arange(0, 1.41, 0.1))], fontsize=7)
ax.set_yticks([-4, -3, -2, -1, 0, 1, 2, 3, 4]); ax.tick_params(labelsize=7)
graph_axes(ax, '$t$ (s)', '$x$ (cm)')
ax.legend(loc='lower right', fontsize=7, frameon=True)
save(fig, p('d1_q7.png'))

# ---- Cau 12: a-x ----
fig, ax = plt.subplots(figsize=(3.0, 2.3))
ax.plot([-5, 5], [20, -20], 'k')
ax.axhline(0, color='k', lw=0.8); ax.axvline(0, color='k', lw=0.8)
ax.plot([-5, -5], [0, 20], 'k:', lw=0.8); ax.plot([5, 5], [0, -20], 'k:', lw=0.8)
ax.plot([-5, 0], [20, 20], 'k:', lw=0.8); ax.plot([0, 5], [-20, -20], 'k:', lw=0.8)
ax.set_xlim(-7.5, 7.5); ax.set_ylim(-25, 25)
ax.set_xticks([-5, 5]); ax.set_yticks([-20, 20]); ax.tick_params(labelsize=8)
ax.set_xlabel('$x$ (cm)', loc='right'); ax.set_ylabel('$a$ (m/s$^2$)', loc='top', rotation=0, labelpad=-30)
save(fig, p('d1_q12.png'))

# ---- Cau 18: Wt-t ----
t = np.linspace(0, 0.2, 600)
fig, ax = plt.subplots(figsize=(3.3, 2.0))
ax.plot(t, 20 + 20 * np.cos(2 * pi * t / 0.1), 'k')
ax.set_xlim(0, 0.21); ax.set_ylim(0, 45)
ax.set_xticks(np.arange(0, 0.201, 0.05)); ax.set_xticklabels(['0', '0,05', '0,10', '0,15', '0,20'])
ax.set_yticks([0, 10, 20, 30, 40]); ax.tick_params(labelsize=8)
graph_axes(ax, '$t$ (s)', '$W_t$ (mJ)')
save(fig, p('d1_q18.png'))

# ---- Cau 22: Wt-x ----
x = np.linspace(-6, 6, 400)
fig, ax = plt.subplots(figsize=(3.6, 2.5))
ax.plot(x, 5 * x**2, 'k')
ax.axhline(180, color='k', ls='--', lw=0.8)
ax.plot([4, 4], [0, 80], 'k:', lw=0.8); ax.plot([-4, 4], [80, 80], 'k:', lw=0.8)
ax.plot([4], [80], 'ko', ms=3)
ax.set_xlim(-7.4, 7.4); ax.set_ylim(0, 205)
ax.set_xticks([-6, -4, -2, 0, 2, 4, 6]); ax.set_xticklabels(['$-A$', '$-4$', '$-2$', '0', '2', '4', '$A$'])
ax.set_yticks([0, 80, 180]); ax.set_yticklabels(['0', '80', '180']); ax.tick_params(labelsize=8)
ax.text(-7.1, 188, '$W$', fontsize=9)
ax.set_xlabel('$x$ (cm)', loc='right'); ax.set_ylabel('$W_t$ (mJ)', loc='top', rotation=0, labelpad=-6)
save(fig, p('d1_c22.png'))

# ---- Cau 23: lo xo dung ----
fig, ax = blank_axes(3.4, 2.6)
ax.set_xlim(0, 7); ax.set_ylim(0, 5.4)
for xc, tag in ((1.6, 'a'), (5.0, 'b')):
    ax.plot([xc - 0.8, xc + 0.8], [5.0, 5.0], 'k', lw=1.4)
    for i in range(9):
        xx = xc - 0.8 + 1.6 * i / 8
        ax.plot([xx, xx + 0.14], [5.0, 5.14], 'k', lw=0.6)
spring(ax, (1.6, 5.0), (1.6, 3.2), n=7, w=0.16)
ax.text(1.6, 2.75, '(a)', ha='center', fontsize=8)
dim(ax, (0.6, 5.0), (0.6, 3.2), '$\\ell_0$', (0.15, 4.1), fs=9)
spring(ax, (5.0, 5.0), (5.0, 2.7), n=8, w=0.16)
block(ax, 4.55, 1.9, 0.9, 0.8, label='$m$')
ax.plot([4.0, 6.2], [3.2, 3.2], 'k:', lw=0.8)
ax.plot([4.0, 6.2], [2.3, 2.3], 'k--', lw=0.6)
dim(ax, (6.0, 3.2), (6.0, 2.7), '$\\Delta\\ell_0$', (6.15, 2.95), fs=9)
ax.text(6.25, 2.3, 'O', fontsize=9, va='center')
ax.annotate('', xy=(3.9, 1.5), xytext=(3.9, 2.3), arrowprops=dict(arrowstyle='->', lw=0.9))
ax.text(3.55, 1.45, '$x$', fontsize=9, ha='center')
ax.text(5.0, 1.45, '(b)', ha='center', fontsize=8)
save(fig, p('d1_c23.png'))

# ---- Cau 24: duong cong hong ----
f = np.linspace(0.5, 1.6, 400)
def curve(gam, f=f): return 1 / np.sqrt((1 - f**2)**2 + (gam * f)**2)
fig, ax = plt.subplots(figsize=(3.4, 2.3))
ax.plot(f, curve(0.18), 'k')
ax.axvline(1, color='k', ls='--', lw=0.7)
ax.set_xlim(0.5, 1.65); ax.set_ylim(0, 6.8)
ax.set_xticks([1]); ax.set_xticklabels(['$f_0$']); ax.set_yticks([])
ax.set_xlabel('$f$', loc='right'); ax.set_ylabel('Biên độ', loc='top', rotation=90, fontdict=VI) if False else ax.set_ylabel('$A$', loc='top', rotation=0, labelpad=-4)
ax.text(1.04, 5.5, '(lực cản nhỏ)', fontdict=VI)
save(fig, p('d1_c24.png'))
print('de1 figs ok')
