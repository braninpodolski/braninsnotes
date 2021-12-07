---
title: Implicit vs Explicit Differentiation
title_custom: true
tags: [Notebooks/Calculus AB]
created: '2021-12-02T16:36:46.958Z'
modified: '2021-12-02T17:02:25.727Z'
---

# Implicit vs Explicit
Explicit Differentiation
: A function in which we solve for $y$

Implicit Differentiation
: A function of $x$ and $y$ which equals a different value'


## Explicit
Derived normally using standard rules
The derivative of $x$ is always multiplied by $\frac{dx}{dx}$, but it is truncated as it equals $1$

$$
\begin{aligned}
y &= 5x^3 + 8x^2-2x \\
y\prime &= 5(3)x^2+8(2)x-2(1) \\
y\prime &= 15x^2+16x-3
\end{aligned}
$$

## Implicit
Solve for $\frac{dy}{dx}$
The derivative of each $y$ value is multiplied by $\frac{dy}{dx}$

$$
\begin{aligned}
2x^4+5y^5-5x+2y &= 5 \\ 
2(4)x^3+5(5)y^4\frac{dy}{dx}-5+2\frac{dy}{dx} &= 0 \\
8x^3+25y^4\frac{dy}{dx}-5+2\frac{dy}{dx} &=0 \\
25y^4\frac{dy}{dx}+2\frac{dy}{dx} &= 5-8x^3 \\
\frac{dy}{dx}\times(25y^4+2) &= 5-8x^3 \\
\frac{dy}{dx} &= \frac{5-8x^3}{25y^4+2}
\end{aligned}
$$
