$$
Var(X) = E(X^2) - E(X)^2\\
Var(\bar{X}) = \frac{\sigma^2}{n}
$$

$$
\frac{\sum_{i=1}^n(X_i-\bar{X})^2}{n-1}=
\frac{\sum_{i=1}^n(Y_i)^2-n \cdot(\bar{X}-\mu)^2}{n-1}
$$

$$
Z_{0.05} = 1.645\\
Z_{0.025} = 1.96\\
Z_{0.005} = 2.576
$$

$$
\frac{\bar{X}-\mu}{\frac{\sigma}{\sqrt{n}}}=\frac{\sum_{i=1}^n X_i-n\mu}{\sqrt{n}\sigma}\to N(0,1)
$$

Normal:
$$
f_X(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{\frac{-1}{2}(\frac{x-\mu}{\sigma})^2}\\
M_Z(t)=e^{\frac{t^2}{2}}
$$

$$
X_1,...,X_n \text{ i.i.d}\sim N(\mu,\sigma^2)\implies\\
1.\bar{X}\sim N(\mu,\frac{\sigma^2}{n})\\
2. \bar{X}\perp S^2_n\\
3. \frac{(n-1)S^2_{n-1}}{\sigma^2}=\frac{nS^2_n}{\sigma^2}=\frac{\sum_{i=1}^1 (X_i-\bar{X})^2}{\sigma^2}\sim \chi^2(n-1)
$$

$$
\frac{Z}{\sqrt{\frac{U}{r}}}\sim t(r)
$$

$$
F \overset{def}= \frac{\frac{X}{r_1}}{\frac{Y}{r_2}}
$$




$$
M_{aX+b}(t)=e^{bt}M_X(at)\\
M_{X,Y}(t)=M_X(t)M_Y(t), if X\perp Y\\
\frac{d^k}{dt^k}M_X(0)=E(X^k)\\
\frac{d^k}{dt^k}M_X(t)=\int_{-\infty}^\infty x^ke^{tx}f_X(x)dx\\
$$


**Slutsky's theorem **
$$
Y_n\overset{d}\to V \and W_n\overset{p}\to c, then\\
Y_n+W_n\overset{d}\to V+c\\
W_nY_n\overset{d}\to cV\\
\frac{Y_n}{W_n}\overset{d}\to \frac{v}{c}
$$


**delta Method **
$$
\sqrt{n}(g(\bar{X})-g(\mu))\to N(0,|g'(\mu)\sigma|^2)\\
$$
**if g'(a)=0, g''(a) $\neq$ 0**
$$
n(g(\bar{Y_n})-g(a))\to b^2 \frac{g''(a)}{2}\chi^2(1)\\
$$


$$
N(\mu,\sigma^2)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}
$$

$$
\iint_Rf(x,y)dA = \iint_Sf(g(u,v),h(u,x))|\frac{\partial(x,y)}{\partial(u,v)}|\bar{A}\\
|\frac{\partial(x,y)}{\partial(u,v)}|=
\begin{vmatrix}
\frac{\partial x}{\partial u } && \frac{\partial x}{\partial v}\\
\frac{\partial y}{\partial u} && \frac{\partial y}{\partial v}
\end{vmatrix}
$$

$$
|J|=\frac{\partial(g_1^{-1},g_2^{-1})}{\partial(m,n)}\\
f_{M,N}(m,n)=||J||f_{X,Y}(g_1^{-1}(m,n),g_2^{-1}(m,n))
$$


$$
\frac{\sigma_Y^2S_X^2}{\sigma_X^2S_Y^2}\sim F(n-1,m-1)
$$

$$
P(\chi^2(n-1)<\frac{n-1}{S^2}{\sigma^2}<\chi^2(n-1))=1-\alpha\\
P(\frac{(n-1)S^2}{\chi^2(n-1)}<\frac{n-1}{S^2}{\sigma^2}<\frac{(n-1)S^2}{\chi^2(n-1)})=1-\alpha\\
$$

**only work  for continuous population**
$$
f_{X_{(i)}}(x)=\frac{n!f_X(x)}{(i-1)!(n-i)!}[F_X(x)]^{i-1}[1-F_X(x)]^{n-i}\\
f_{X_{(1)}}(x)=nf_X(x)[1-F_X(x)]^{n-1}\\
f_{X_{(n)}}(x)=nf_X(x)[F_X(x)]^{n-1}\\
f_{X_{(i)},X_{(j)}}(u,v)=\frac{n!f_X(u)f_X(v)}{(i-1)!(j-i-1)!(n-j)!}[F_X(u)]^{i-1}[F_X(v)-F_X(u)]^{j-i-1}[1-F_X(x)]^{n-j} \text{, for }u<v\\
f_{X(1),...,X(n)}=n!\prod^n_{i=1}f_X(x_i)
$$



**C-R INEQUALITY FOR $\theta$**
$$
Var(T(X))\geq \frac{1}{E[\frac{\partial}{\partial\theta} \ln{f_{X_1,...,X_n}(X_1,...,X_n|\theta)}]^2}
$$




