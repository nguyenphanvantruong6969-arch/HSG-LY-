from figlib import *
import os
OUT = os.environ.get('FIGDIR', '.')
p = lambda n: os.path.join(OUT, n)
pi = np.pi

# ================= Cau 1: h-t, a-t, v-t (trong) =================
T = 0.8; w = 2 * pi / T
t = np.linspace(0, 1.6, 800)
h = 0.60 + 0.15 * np.cos(w * t - pi / 3)
a = -w**2 * 0.15 * np.cos(w * t - pi / 3)
v = -w * 0.15 * np.sin(w * t - pi / 3)

def three_panel(path, with_v):
    fig, axs = plt.subplots(3, 1, figsize=(5.6, 7.0), sharex=True)
    ax = axs[0]; ax.plot(t, h, 'k'); ax.set_ylim(0.45, 0.75)
    ax.set_yticks(np.arange(0.45, 0.751, 0.05)); ax.set_yticklabels([f'{y:.2f}'.replace('.', ',') for y in np.arange(0.45, 0.751, 0.05)])
    graph_axes(ax, '', '$h$ (m)')
    ax = axs[1]; ax.plot(t, a, 'k'); ax.set_ylim(-10, 10); ax.set_yticks(np.arange(-10, 10.1, 2.5))
    ax.set_yticklabels([str(y).replace('.', ',') for y in np.arange(-10, 10.1, 2.5)])
    ax.axhline(0, color='k', lw=0.8); graph_axes(ax, '', '$a$ (m/s$^2$)')
    ax = axs[2]; ax.set_ylim(-1.5, 1.5); ax.set_yticks(np.arange(-1.5, 1.51, 0.5))
    ax.set_yticklabels([f'{y:.1f}'.replace('.', ',') for y in np.arange(-1.5, 1.51, 0.5)])
    ax.axhline(0, color='k', lw=0.8)
    if with_v: ax.plot(t, v, 'k')
    graph_axes(ax, '$t$ (s)', '$v$ (m/s)')
    ax.set_xlim(0, 1.6); ax.set_xticks(np.arange(0, 1.61, 0.2)); ax.set_xticklabels([f'{x:.1f}'.replace('.', ',') for x in np.arange(0, 1.61, 0.2)])
    for ax in axs: ax.tick_params(labelsize=8)
    fig.subplots_adjust(hspace=0.18)
    save(fig, path)
three_panel(p('d2_c1.png'), False)
three_panel(p('a_c1.png'), True)

# ================= Cau 2: gờ giảm tốc =================
fig, ax = blank_axes(5.6, 1.9)
ax.set_xlim(0, 12); ax.set_ylim(-0.6, 3.4)
x = np.linspace(0, 12, 800)
yy = np.zeros_like(x)
for c in (1.5, 4.5, 7.5, 10.5):
    m = np.abs(x - c) < 0.35
    yy[m] = 0.22 * (1 - ((x[m] - c) / 0.35)**2)
ax.plot(x, yy, 'k', lw=1.4)
ground(ax, 0, 12, -0.02, n=50, h=0.15)
# xe
block(ax, 1.9, 0.55, 2.5, 0.85, fc='#e6e6e6')
block(ax, 2.7, 1.4, 1.2, 0.55, fc='#f2f2f2')
for cx in (2.5, 3.8):
    ax.add_patch(Circle((cx, 0.35), 0.33, fc='#bdbdbd', ec='k', lw=1))
ax.annotate('', xy=(5.4, 1.0), xytext=(4.6, 1.0), arrowprops=dict(arrowstyle='->', lw=1.1))
ax.text(5.0, 1.15, '$v$', ha='center', fontsize=9)
dim(ax, (7.5, 0.9), (10.5, 0.9), '$L$', (9.0, 1.15), fs=9, ha='center')
ax.plot([7.5, 7.5], [0.3, 1.0], 'k:', lw=0.7); ax.plot([10.5, 10.5], [0.3, 1.0], 'k:', lw=0.7)
save(fig, p('d2_c2.png'))

# ================= Cau 3: T^2 theo l =================
l = np.array([0.30, 0.40, 0.50, 0.60, 0.70, 0.80])
t10 = np.array([11.0, 12.8, 14.1, 15.6, 16.7, 18.0])
T2 = (t10 / 10)**2
def t2plot(path, fit):
    fig, ax = plt.subplots(figsize=(3.9, 2.9))
    ax.plot(l, T2, 'ko', ms=4)
    if fit:
        s, b = np.polyfit(l, T2, 1)
        xx = np.array([0, 0.9]); ax.plot(xx, s * xx + b, 'k-', lw=1)
    ax.set_xlim(0, 0.9); ax.set_ylim(0, 3.6)
    ax.set_xticks(np.arange(0, 0.91, 0.1)); ax.set_xticklabels([f'{x:.1f}'.replace('.', ',') for x in np.arange(0, 0.91, 0.1)])
    ax.set_yticks(np.arange(0, 3.61, 0.4)); ax.set_yticklabels([f'{y:.1f}'.replace('.', ',') for y in np.arange(0, 3.61, 0.4)])
    ax.tick_params(labelsize=8)
    graph_axes(ax, '$\\ell$ (m)', '$T^2$ (s$^2$)')
    save(fig, path)
t2plot(p('d2_c3.png'), False)
t2plot(p('a_c3.png'), True)

# ================= Cau 4: vat roi dinh len dia =================
fig, ax = blank_axes(3.0, 3.6)
ax.set_xlim(0, 5); ax.set_ylim(0, 6.6)
ground(ax, 0.8, 4.2, 0.4, n=14, h=0.14)
spring(ax, (2.5, 0.4), (2.5, 2.4), n=8, w=0.2)
block(ax, 1.65, 2.4, 1.7, 0.4, fc='#d0d0d0', label='$M$', fs=9)
ax.add_patch(Circle((2.5, 5.6), 0.3, fc='#8c8c8c', ec='k'))
ax.text(3.0, 5.6, '$m$', fontsize=9, va='center')
dim(ax, (1.2, 5.3), (1.2, 2.8), '$h$', (0.85, 4.05), fs=9)
ax.plot([1.0, 2.2], [5.3, 5.3], 'k:', lw=0.7); ax.plot([1.0, 1.65], [2.8, 2.8], 'k:', lw=0.7)
ax.annotate('', xy=(2.5, 3.3), xytext=(2.5, 4.4), arrowprops=dict(arrowstyle='->', lw=1))
ax.text(2.7, 3.9, '$\\vec{v}_0$', fontsize=9)
save(fig, p('d2_c4.png'))

# ================= Cau 5: hai vat chong len nhau =================
fig, ax = blank_axes(5.8, 2.7)
ax.set_xlim(0, 11); ax.set_ylim(0, 5)
# (a) thang dung
ground(ax, 0.8, 3.8, 0.4, n=14, h=0.14)
spring(ax, (2.3, 0.4), (2.3, 2.1), n=7, w=0.2)
block(ax, 1.5, 2.1, 1.6, 0.6, fc='#d0d0d0', label='$M$')
block(ax, 1.8, 2.7, 1.0, 0.45, fc='#f0f0f0', label='$m$', fs=8)
ax.text(2.3, -0.15, '(a)', ha='center', fontsize=9)
# (b) nam ngang
ground(ax, 6.0, 10.6, 0.9, n=22, h=0.14)
ax.plot([6.0, 6.0], [0.9, 3.0], 'k', lw=1.4)
for i in range(9): ax.plot([6.0, 5.85], [0.9 + 2.1 * i / 8, 0.9 + 2.1 * i / 8 + 0.15], 'k', lw=0.6)
spring(ax, (6.0, 1.7), (7.6, 1.7), n=6, w=0.18)
block(ax, 7.6, 0.9, 1.6, 1.6, fc='#d0d0d0', label='$M$')
block(ax, 7.9, 2.5, 1.0, 0.7, fc='#f0f0f0', label='$m$', fs=8)
ax.text(8.4, -0.15, '(b)', ha='center', fontsize=9)
save(fig, p('d2_c5.png'))

# ================= Cau 6: ma sat truot =================
fig, ax = blank_axes(5.8, 2.1)
ax.set_xlim(0, 11); ax.set_ylim(0, 3.6)
ground(ax, 0.8, 10.4, 0.5, n=48, h=0.14)
ax.plot([0.8, 0.8], [0.5, 2.7], 'k', lw=1.4)
for i in range(9): ax.plot([0.8, 0.65], [0.5 + 2.2 * i / 8, 0.5 + 2.2 * i / 8 + 0.15], 'k', lw=0.6)
spring(ax, (0.8, 1.15), (5.6, 1.15), n=12, w=0.2)
block(ax, 5.6, 0.5, 1.3, 1.3, fc='#d0d0d0', label='$m$')
ax.plot([5.6, 5.6], [1.9, 2.4], 'k:', lw=0.8)
ax.text(5.6, 2.55, 'O', ha='center', fontsize=9)
ax.annotate('', xy=(10.2, 2.4), xytext=(7.8, 2.4), arrowprops=dict(arrowstyle='->', lw=1))
ax.text(10.3, 2.4, '$x$', fontsize=9, va='center')
ax.text(9.0, 1.0, '$\\mu$', fontsize=9, ha='center')
save(fig, p('d2_c6.png'))

# ================= Cau 7: ong chu U =================
fig, ax = blank_axes(3.0, 3.0)
ax.set_xlim(0, 7); ax.set_ylim(0, 6.4)
wd = 0.9; xl = 1.2; xr = 4.0       # mep trai cua hai nhanh
cxu = (xl + xr + wd) / 2; Ro = (xr + wd - xl) / 2; Ri = Ro - wd
yb = 2.4                              # tam cung U
top = 5.9
th = np.linspace(pi, 2 * pi, 80)
xo = cxu + Ro * np.cos(th); yo = yb + Ro * np.sin(th)
xi = cxu + Ri * np.cos(th); yi = yb + Ri * np.sin(th)
# chat long
ll, lr = 4.95, 4.05
liq_x = np.r_[xl + 0.03, xo[::-1][:0], xo, xr + wd - 0.03]
poly_x = np.r_[xl + 0.03, xo, xr + wd - 0.03, xr + wd - 0.03, xr + 0.03, xi[::-1], xl + wd - 0.03, xl + wd - 0.03]
poly_y = np.r_[ll, yo, lr, yb, yb, yi[::-1], yb, ll]
# xay dung da giac don gian: phan ong ben trai, cung, ben phai
left = [(xl + 0.03, ll), (xl + wd - 0.03, ll), (xl + wd - 0.03, yb)]
right = [(xr + 0.03, yb), (xr + 0.03, lr), (xr + wd - 0.03, lr)]
arc_out = list(zip(xo[::-1], yo[::-1]))
arc_in = list(zip(xi, yi))
pts = [(xl + 0.03, ll), (xl + wd - 0.03, ll)] + arc_in + [(xr + 0.03, lr), (xr + wd - 0.03, lr)] + arc_out[:0] + list(zip(xo[::-1], yo[::-1]))[::-1][:0]
# da giac: tu mat trai -> xuong theo mep trong -> cung trong -> len mat phai -> ngang -> xuong theo mep ngoai -> cung ngoai nguoc -> len
pts = [(xl + 0.02, ll), (xl + wd, ll)] + [(xl + wd, yb)] + arc_in[1:-1] + [(xr, yb), (xr, lr), (xr + wd, lr), (xr + wd, yb)] + list(zip(xo, yo))[::-1][1:-1] + [(xl, yb)]
ax.add_patch(Polygon(pts, closed=True, fc='#c8d8ea', ec='none'))
# thanh ong
ax.plot([xl, xl, *xo, xr + wd, xr + wd], [top, yb, *yo, yb, top], 'k', lw=1.3)
ax.plot([xl + wd, xl + wd, *xi, xr, xr], [top, yb, *yi, yb, top], 'k', lw=1.3)
ax.plot([xl, xl + wd], [ll, ll], 'k', lw=1.3); ax.plot([xr, xr + wd], [lr, lr], 'k', lw=1.3)
yeq = (ll + lr) / 2
ax.plot([0.4, 6.1], [yeq, yeq], 'k--', lw=0.7)
ax.text(6.2, yeq, 'O', va='center', fontsize=9)
dim(ax, (0.7, yeq), (0.7, ll), '$y$', (0.2, (yeq + ll) / 2), fs=9)
dim(ax, (5.7, yeq), (5.7, lr), '$y$', (5.8, (yeq + lr) / 2), fs=9)
ax.text(cxu, 0.55, '$\\ell$ = tổng chiều dài cột chất lỏng', ha='center', fontdict=VI) if False else None
save(fig, p('d2_c7.png'))

# ================= Cau 8: xe va thang may =================
fig, ax = blank_axes(5.8, 2.7)
ax.set_xlim(0, 11); ax.set_ylim(0, 5.2)
ground(ax, 0.3, 5.0, 0.55, n=26, h=0.12)
block(ax, 0.9, 0.55, 2.9, 0.5, fc='#e0e0e0')
for cx in (1.4, 3.3): ax.add_patch(Circle((cx, 0.35), 0.22, fc='#bdbdbd', ec='k'))
ax.plot([2.35, 2.35], [3.9, 1.05], 'k', lw=0.6, ls='--')
ang = np.radians(36.87)
bx, by = 2.35 + 2.4 * np.sin(ang), 3.9 - 2.4 * np.cos(ang)
ax.plot([2.35, bx], [3.9, by], 'k', lw=1.1)
ax.add_patch(Circle((bx, by), 0.2, fc='#6e6e6e', ec='k'))
ax.plot([1.9, 2.8], [3.9, 3.9], 'k', lw=1.4)
ax.annotate('', xy=(4.9, 0.8), xytext=(4.0, 0.8), arrowprops=dict(arrowstyle='->', lw=1.2))
ax.text(4.45, 0.95, '$\\vec{a}$', ha='center', fontsize=9)
ax.text(2.0, 2.4, '$\\beta$', fontsize=9)
ax.text(2.35, 0.15, '(a)', ha='center', fontsize=9)
# thang may
block(ax, 6.6, 0.5, 3.0, 4.3, fc='white', lw=1.2)
ax.plot([8.1, 8.1], [4.8, 4.0], 'k', lw=1.4)
ax.plot([8.1, 8.1], [4.0, 1.9], 'k', lw=1.1)
ax.add_patch(Circle((8.1, 1.7), 0.22, fc='#6e6e6e', ec='k'))
ax.annotate('', xy=(10.5, 3.4), xytext=(10.5, 2.2), arrowprops=dict(arrowstyle='->', lw=1.2))
ax.text(10.65, 2.8, '$\\vec{a}$', fontsize=9, va='center')
ax.text(8.1, 0.15, '(b)', ha='center', fontsize=9)
ax.plot([7.5, 8.7], [4.0, 4.0], 'k', lw=1.4)
save(fig, p('d2_c8.png'))

# ================= Cau 9: mo hinh giam xoc =================
fig, ax = blank_axes(5.6, 2.9)
ax.set_xlim(0, 12); ax.set_ylim(-0.8, 6)
x = np.linspace(0, 12, 600); yr = 0.35 * np.cos(2 * pi * x / 5.0 - 1.0) + 0.5
ax.plot(x, yr, 'k', lw=1.3)
xw = 5.0; yw = 0.35 * np.cos(2 * pi * xw / 5.0 - 1.0) + 0.5 + 0.55
ax.add_patch(Circle((xw, yw), 0.55, fc='#cfcfcf', ec='k'))
spring(ax, (xw - 0.35, yw + 0.1), (xw - 0.35, 3.6), n=6, w=0.17)
# giam chan
ax.plot([xw + 0.35, xw + 0.35], [yw + 0.1, 2.0], 'k', lw=1.1)
ax.add_patch(Rectangle((xw + 0.2, 2.0), 0.3, 1.3, fc='white', ec='k', lw=1))
ax.plot([xw + 0.35, xw + 0.35], [3.3, 3.6], 'k', lw=1.1)
ax.plot([xw + 0.2, xw + 0.5], [2.5, 2.5], 'k', lw=0.8)
block(ax, xw - 1.5, 3.6, 3.0, 0.9, fc='#d9d9d9', label='$m$')
ax.annotate('', xy=(xw + 1.0, 5.4), xytext=(xw - 1.0, 5.4), arrowprops=dict(arrowstyle='->', lw=1.1))
ax.text(xw, 5.55, '$v$', ha='center', fontsize=9)
dim(ax, (xw - 2.5, 0.05), (xw + 2.5, 0.05), '$L$', (xw, -0.3), fs=9, ha='center') if False else None
# L giua hai dinh
ax.plot([1.0, 1.0], [-0.55, 0.35], 'k:', lw=0.7); ax.plot([6.0, 6.0], [-0.55, 0.35], 'k:', lw=0.7)
dim(ax, (1.0, -0.45), (6.0, -0.45), '', None)
ax.text(3.5, -0.4, '$L$', ha='center', va='bottom', fontsize=9)
ax.text(xw - 0.8, 3.0, '$k$', fontsize=9, ha='right'); ax.text(xw + 0.75, 2.6, '$\\lambda$', fontsize=9)
save(fig, p('d2_c9.png'))

# ================= Dap an: hinh bo sung =================
# Coulomb x-t
m, k, mu = 0.2, 20.0, 0.1; x0 = mu * m * 10 / k; wv = np.sqrt(k / m)
A0 = 0.09
tt = []; xx = []; cur = A0; sgn = 1; t0 = 0
for n in range(5):
    center = sgn * x0   # VTCB tam thoi: cung phia voi diem xuat phat
    Ai = cur - x0 if True else cur
    ts = np.linspace(0, pi / wv, 80)
    # trong nua chu ki thu n, vat dao dong quanh center voi bien do (cur - x0) tu x=sgn*cur
    xs = center + (sgn * cur - center) * np.cos(wv * ts)
    tt.append(t0 + ts); xx.append(xs)
    t0 += pi / wv; cur = cur - 2 * x0; sgn = -sgn
    if cur <= x0 + 1e-9: 
        pass
    if n == 3: break
tt = np.concatenate(tt); xx = np.concatenate(xx) * 100
fig, ax = plt.subplots(figsize=(4.4, 2.4))
ax.plot(tt, xx, 'k'); ax.axhline(0, color='k', lw=0.7)
ax.set_xlabel('$t$ (s)', loc='right'); ax.set_ylabel('$x$ (cm)', loc='top', rotation=0, labelpad=-4)
ax.tick_params(labelsize=8); ax.grid(True, color='0.8', lw=0.4)
save(fig, p('a_c6.png'))

# Cau 24 (De1): hai duong cong hong
f = np.linspace(0.5, 1.6, 400)
def curve(g): return 1 / np.sqrt((1 - f**2)**2 + (g * f)**2)
fig, ax = plt.subplots(figsize=(3.6, 2.4))
ax.plot(f, curve(0.18), 'k', label='lực cản nhỏ'); ax.plot(f, curve(0.5), 'k--', label='lực cản lớn')
ax.axvline(1, color='k', ls=':', lw=0.7)
ax.set_xlim(0.5, 1.65); ax.set_ylim(0, 6.5); ax.set_xticks([1]); ax.set_xticklabels(['$f_0$']); ax.set_yticks([])
ax.set_xlabel('$f$', loc='right'); ax.set_ylabel('$A$', loc='top', rotation=0, labelpad=-4)
ax.legend(prop={'family': 'DejaVu Serif', 'size': 7}, frameon=False)
save(fig, p('a_c24.png'))

# Cau 9: bien do duong cong
w0, al, F0m = 20.0, 0.5, 2.0
ww = np.linspace(2, 40, 1200)
Bw = F0m / np.sqrt((w0**2 - ww**2)**2 + 4 * al**2 * ww**2) * 100
fig, ax = plt.subplots(figsize=(4.4, 2.6))
ax.plot(ww, Bw, 'k'); ax.set_yscale('log')
ax.plot([20], [10], 'ko', ms=3); ax.plot([4 * pi], [0.825], 'ko', ms=3)
ax.annotate('$\\omega=\\omega_0$,  $B=10$ cm', (20, 10), (24, 5.5), fontsize=8, arrowprops=dict(arrowstyle='-', lw=0.6))
ax.annotate('$v=36$ km/h,  $B\\approx0{,}83$ cm', (4 * pi, 0.825), (17, 0.35), fontsize=8, arrowprops=dict(arrowstyle='-', lw=0.6))
ax.set_xlabel('$\\omega$ (rad/s)', loc='right'); ax.set_ylabel('$B$ (cm)', loc='top', rotation=0, labelpad=-4)
ax.grid(True, which='both', color='0.85', lw=0.4); ax.tick_params(labelsize=8)
ax.set_ylim(0.1, 30)
save(fig, p('a_c9.png'))
print('de2 figs ok')
