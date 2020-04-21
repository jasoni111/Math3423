1. If {𝑋1,𝑋2, … , 𝑋100} is a r.s. from a distribution with mean 𝜇 and variance 16, find the
    approximate 95% C.I. for 𝜇(𝜇 + 3) by using 𝑥̅= 15. Please also show the detail how you
    get the random and confidence intervals

  use delta method:
$$
\sqrt{n}(g(\bar{X})-g(\mu))\to N(0,|g'(\mu)\sigma|^2)\\
g(x):=x^2+3x\\
g'(x)=2x\\
\bar{X}=15\\
\sigma^2=16\\
n=100\\
\sqrt{100}(270 - (\mu)(\mu+3) ) \sim N(0, (30\times 4)^2 )\\
\frac{\sqrt{100}(270 - (\mu)(\mu+3) )}{120} \sim \mathbb{Z}\\
P(c_1 < (\mu)(\mu+3) < c_2  ) = 0.95 \\
c_1 = 270 - 1.960 \times\frac{120}{\sqrt{100}} = 246.68
c_2 = 270 + 1.960 \times\frac{120}{\sqrt{100}} = 293.52
$$

2. If 𝑋 and 𝑌 are independent random variables from the standard normal distribution, then show that $\frac{X}{Y}\sim t(1)$.

   use  change of variable
   $$
   f_X(x)=\frac{e^{-\frac{x^2}{2}} }{\sqrt{2\pi}}\\
   f_{X,Y}(x,y) = \frac{e^{-\frac{x^2}{2}} }{\sqrt{2\pi}}\cdot \frac{e^{-\frac{y^2}{2}} }{\sqrt{2\pi}}\\
   =\frac{e^{-\frac{x^2+y^2}{2}}}{2\pi}\\
   \text{define } M:=g_1(X,Y)=\frac{X}{Y}\quad N:=g_2(X,Y)=Y\\
   X=g_1^{-1}(M,N)=MN \quad Y=g_2^{-1}(M,N)=N\\
   |J| = |\frac{\partial g_1^{-1},g_2^{-1}}{\partial m,n}|\\
   =\begin{vmatrix}
   n & m \\
   0 & 1\\
   \end{vmatrix} = n\\
   f_{M,N}(m,n) = |J|f_{X,Y}(g_1^{-1}(m,n),g_2^{-1}(m,n) )\\
   =|n|\frac{ e^{-\frac{{m^2n^2+n^2}}{2}} }{2\pi}\\
   f_{M}(m) = \int_{-\infty}^{\infty} |n| \frac{ e^{-\frac{{m^2n^2+n^2}}{2}}}{2\pi} dn\\
   = \frac{1}{2\pi}\int_{-\infty}^{\infty} |n| e^{-\frac{{m^2n^2+n^2}}{2}}  dn\\
   = \frac{1}{2\pi}\int_{-\infty}^{\infty} |n| e^{-\frac{n^2(m^2+1)}{2} }  dn\\
   $$
   Consider identity:
   $$
   \int xe^{cx^2}dx = \frac{1}{2c}e^{cx^2}
   $$
   and $|n|$ and $n^2$ are even function:
   $$
   f_{M}(m) = \frac{1}{2\pi}\int_{-\infty}^{\infty} |n| e^{-\frac{n^2(m^2+1)}{2} }  dn\\
   = \frac{1}{\pi}\int_{0}^{\infty} n e^{-\frac{n^2(m^2+1)}{2} }  dn\\
   = \frac{1}{\pi \cdot -2\frac{m^2+1}{2} }[e^{-\frac{n^2(m^2+1)}{2}} ]_0^{\infty} \\
   = \frac{- 1}{\pi \cdot (m^2+1) }(0 - 1)  \\
   = \frac{1}{\pi \cdot (m^2+1) }  \\
   $$
   
   which is the same as $f_{t(1)}$
   
   $$
   \frac{\Gamma(\frac{1+1}{2})}{\sqrt{\pi}\Gamma(0.5) }(1+x^2)^{-\frac{1+1}{2}}
   =\frac{1 }{\sqrt{\pi}\sqrt{\pi} }(1+x^2)^{-1}
   =\frac{1 }{\sqrt{\pi} (1+x^2) }
   $$
   