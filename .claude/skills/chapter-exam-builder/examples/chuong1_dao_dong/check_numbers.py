"""Independent numeric verification of every answer used in the three documents."""
import numpy as np
from math import pi, sqrt, exp, log, acos, atan2, cos, sin, degrees, radians
g = 10.0
R = {}

# ---------- DE 1, PHAN I ----------
R['q1'] = (60/120, 120/60)                                  # T, f
R['q6'] = None
# q8
w=10; A8=sqrt(4**2+(30/w)**2); R['q8']=(A8, w*sqrt(A8**2-3**2), w*sqrt(A8**2+9))
# q9
m=0.1; w=10; A=0.06; x=A/2; v=w*sqrt(A**2-x**2); W=0.5*m*w**2*A**2
R['q9']=(v*100, 0.75*W*1000, 0.25*W*1000, W*1000)
# q10
dl=0.025; w=sqrt(g/dl); R['q10']=(w, w*3, w*5.5, 10/ (0.025*100) )
# q11
T=0.6; w=2*pi/T
ts=[(a)/w for a in (5*pi/6, 7*pi/6, 5*pi/6+2*pi, 7*pi/6+2*pi)]
R['q11']=ts
# q13: A=6, T=.6, dt=.65 from VTCB
R['q13']=(4*6+6*0.5, 4*6*13/12, 24+6*sqrt(3)/2, 24+6)
# q12
w2=20/0.05; R['q12']=(0.5*0.1*w2*0.05**2*1000, 0.1*w2*0.05**2*1000/1, 0.5*0.1*(20/5)*0.05**2*1000)
# q14
k=40; mm=0.1; dl0=mm*g/k; A=0.04
R['q14']=(dl0*100, 30+dl0*100-4, k*(dl0+A))
# q15
gg=pi**2; l=1.0; a0=radians(9); w=sqrt(gg/l); S0=l*a0; vmax=w*S0
R['q15']=(vmax, 0.5*0.1*vmax**2*1000, 0.5*0.1*(2*vmax)**2*1000, S0, 0.1*vmax**2*1000, w*9)
# q16
R['q16']=(10*0.96**3, 40*0.96**6, 40*0.96**3, 10*0.88, 40*0.88, 10*0.96**6)
# q17
m=0.25;k=100;mu=0.2;A0=0.08; w=sqrt(k/m); x0=mu*m*g/k
R['q17']=(w, x0*100, w*(A0-x0), (A0-2*x0)*100, w*A0, w*(A0-2*x0), w*(A0+x0), (A0-4*x0)*100)
# q18
m=0.2; Tw=0.1
for Td in (0.2,0.1,0.4):
    w=2*pi/Td; w2=10*(2*(1/Td))**2*4/4  # placeholder
W=0.04
for Td in (0.2,0.1,0.4):
    w2=(2*10**0.5/Td)**2  # pi^2=10 -> (2 pi/T)^2 = 40/T^2
    A=sqrt(2*W/(m*w2)); R.setdefault('q18',[]).append((Td, A*100))
# q19
m=250;k=250000; T0=2*sqrt(10)*sqrt(m/k); R['q19']=(T0, 3/T0, 3/T0*3.6)
# q20
m=0.3;M=0.4;k=30;A=0.1; w=sqrt(k/m); vm=w*A; v2=m*vm/M; w2=sqrt(k/M); A2=v2/w2
R['q20']=(A2*100, 0.5*k*A2**2*1000, 0.5*k*A**2*1000, A*sqrt(m/M)*100, A*m/M*100, 0.5*k*(A*m/M)**2*1000)

# ---------- DE 1, PHAN II ----------
# c21
T=0.6; w=2*pi/T; A=10
R['c21']=dict(w=w, v0=-w*A*sin(pi/3), a0=-w**2*5, t=(5*pi/6-pi/3)/w)
# c22
k=2*0.08/0.04**2; A=sqrt(2*0.18/k); m=0.25; w=sqrt(k/m)
R['c22']=dict(k=k, A=A*100, w=w, T=2*pi/w, x=A/sqrt(3)*100, v=w*sqrt(A**2-(A/sqrt(3))**2)*100, dt=pi/w/2)
# c23
m=0.2;dl=0.025;k=m*g/dl; w=sqrt(k/m); A=0.05
R['c23']=dict(k=k,w=w,T=2*pi/w, lmax=40+2.5+5, lmin=40+2.5-5, Fmax=k*(dl+A), W=0.5*k*A**2, tn=(2*pi/w)/3)
# c24
R['c24']=dict(loss=1-0.98**2, dE=50*(1-0.98**2), P=50*(1-0.98**2)/2, n=log(0.5)/log(0.98**2), w34=0.98**34, w36=0.98**36)

# ---------- DE 2 ----------
# c1
Tc=0.8; w=2*pi/Tc; A=0.15
R['c1']=dict(w=w, f=1/Tc, vmax=w*A, amax=w**2*A, k=w**2)
# c2
m=1000;k=160000; T0=2*pi/sqrt(k/m)
R['c2']=dict(T0=T0, f0=1/T0, T0_pi10=2*sqrt(10)*sqrt(m/k), v=3/0.5, kmh=3/0.5*3.6, f10=10/3, f_res=2.0)
# c4
M=0.7;m=0.3;k=100;h=0.2; v0=sqrt(2*g*h); V=m*v0/(m+M); w=sqrt(k/(m+M)); x0=m*g/k
A=sqrt(x0**2+(V/w)**2)
R['c4']=dict(v0=v0,V=V,w=w,x0=x0*100,A=A*100, loss=0.5*m*v0**2-0.5*(m+M)*V**2, W=0.5*k*A**2, eq=(m+M)*g/k*100, Fmax=k*((m+M)*g/k+A), phi=-(pi-acos(1/sqrt(5))))
# c5
M=0.3;m=0.2;k=200; w=sqrt(k/(M+m))
R['c5']=dict(w=w, dl=(M+m)*g/k*100, Amax=g/w**2*100, Nmax=m*(g+w**2*0.02), Nmin=m*(g-w**2*0.02), mu=w**2*0.02/g)
# c6
m=0.2;k=20;mu=0.1; F=mu*m*g; x0=F/k; w=sqrt(k/m); A0=0.09
amps=[A0]; 
while amps[-1]>x0+1e-12: amps.append(amps[-1]-2*x0)
R['c6']=dict(x0=x0*100,w=w,T=2*pi/w, amps=[a*100 for a in amps], nhalf=len(amps)-1, t=(len(amps)-1)*pi/w, S=0.5*k*(A0**2-amps[-1]**2)/F, vmax=w*(A0-x0), mu_range=(k*0.03/(m*g), k*0.09/(m*g)))
# c7
l=0.8; w=sqrt(2*g/l); S=1e-4; rho=1000
R['c7']=dict(w=w,T=2*pi/w, A=sqrt(0.03**2+(0.2/w)**2), vmax=w*0.05, W=rho*g*S*0.05**2, keff=2*rho*g*S, mass=rho*S*l, phi=acos(0.6))
# c8
a=7.5; gp=sqrt(g**2+a**2); l=1.25
R['c8']=dict(gp=gp, beta=degrees(atan2(a,g)), T=2*pi*sqrt(l/gp), Tpi10=2*sqrt(10)*sqrt(l/gp), vmax=sqrt(gp/l)*l*0.08, W=0.5*0.2*gp*l*0.08**2, Tlift=2*pi*sqrt(l/(g+2.5)))
# c9
m=400;k=160000;lam=400; al=lam/(2*m); w0=sqrt(k/m); Om=sqrt(w0**2-al**2); L=5.0
F0=800
def B(w): return (F0/m)/sqrt((w0**2-w**2)**2+4*al**2*w**2)
R['c9']=dict(al=al,w0=w0,Om=Om,T=2*pi/Om,drop=1-exp(-al*2*pi/Om), vres=w0*L/(2*pi), vres_kmh=w0*L/(2*pi)*3.6,
             Bmax=B(w0)*100, B10=B(2*pi*10/L)*100, w10=2*pi*10/L, Bstat=F0/k*100, Q=w0/(2*al), P=0.5*lam*w0**2*B(w0)**2, lamcrit=2*m*w0)
for k_,v_ in R.items(): print(k_, v_)
