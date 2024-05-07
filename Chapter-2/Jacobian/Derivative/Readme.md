
###########################Om Sree Sree Bankeshwaray Namoh###########################

################################sAlternate Differentiation ############################


# Looking forward towards pioneers in the computaion world , afew good works have been mentioned here (Before touching LLVM and Intel level infrastructure these works should be given priority and more works should be completed on these areas.)

1)  J.M. has already supplied some excellent ways of performing numerical differentiation, including
methods like Cauchy's formula. There is a simple method that I use that gets me first derivatives at
near machine precision levels. It is the complex step derivative: f ′ (x)
= Im(x+ih / h)
, where h can be
chosen to be the machine epsilon (see citeseerx.ist.psu.edu/viewdoc/... for guidance). It is trivial to
implement in any language with a complex number datatype (e.g. Fortran). – Gilead May 8, 2011 at


2)

If your function is badly behaved (e.g. noisy, very oscillatory), no method will perform properly
(differentiation is numerically very unstable ). That being said, for "nice functions", I have good
18
experience with polynomial (Richardson) extrapolation methods. This paper and this paper
give hints on how you might write your own implementation. I will note that this is the method
implemented in the NAG numerical libraries (with of course a few wrinkles of their own).
There are two possible alternatives if for some reason you don't want to use Richardsonian
methods. One is to use Cauchy's differentiation formula:


f (t)
where it is up to you to choose a suitable counterclockwise contour γ (a circle is customary);
the other is to use the "Lanczos derivative".





3.

For those who are not too familiar with Taylor series, it will be a necessity to be able to
differentiate a function in a point many times. Given that the normal definition of the
mathematical derivative of a function will require immense precision for higher order
derivatives, I've decided to use Cauchy's integral formula instead. With a little bit of work,
I've managed to rearrange the formula a little bit, as you can see on this picture: Rearranged
formula . This provided me with much more accurate results on higher order derivatives than
the traditional definition of the derivative. Here is the function i am currently using to
differentiate a function in a point:
def myDerivative ( f, x, dTheta, degree ):
riemannSum = 0
theta = 0
while theta < 2 *np.pi:
functionArgument = np.complex128(x + np.exp( 1j *theta))
secondFactor = np.complex128(np.exp(- 1j * degree * theta))
riemannSum += f(functionArgument) * secondFactor * dTheta
theta += dTheta
return factorial(degree)/( 2 *np.pi) * riemannSum.real



4.. I seem to have come up with a solution to the problem. I did this by rearranging Cauchy's
2
integral formula in a different way, by exploiting that the initial contour integral can be an
arbitrarily large circle around the point of differentiation. Be aware that it is very important that
the function is analytic in the complex plane for this to be valid.
New formula
Also this gives a new function for differentiation:
def myDerivative ( f, x, dTheta, degree, contourRadius ):
riemannSum = 0
theta = 0
while theta < 2 *np.pi:
functionArgument = np.complex128(x + contourRadius*np.exp( 1j *theta))
secondFactor = ( 1 /contourRadius)**degree*np.complex128(np.exp(- 1j *
degree * theta))
riemannSum += f(functionArgument) * secondFactor * dTheta
theta += dTheta
return factorial(degree) * riemannSum.real / ( 2 *np.pi)
This gives me a very accurate differentiation of high orders. For instance I am able to
differentiate f(x)=e^x 50 times without a problem.







5. In addition to J.M. answer: this paper
5
https://www.sciencedirect.com/science/article/pii/S0021904512000123 (Differentiation by
integration using orthogonal polynomials, a survey, by E. Diekema and T.H. Koornwinder, doi:
10.1016/j.jat.2012.01.003 ) provides further insight into Lánczos's derivative and its
generalizations for n-th order derivatives. By the way, it says that the Lánczos's (1956)
derivative formula goes back to Cioranescu (1938) and Haslam-Jones (1953).



6. Complex step differentiation (CSD) is well known as an efficient numerical differentiation
method:

 ̅  ̅  ̅ .
This method requires the function to be analytic (differentiable as a complex function). 


6.

In numerical linear algebra, the Jacobi method is an iterative algorithm for determining the solutions of a strictly diagonally dominant system of linear equations. Each diagonal element is solved for, and an
approximate value is plugged in. The process is then iterated until it converges. This algorithm is a
stripped-down version of the Jacobi transformation method of matrix diagonalization. The method is
named after Carl Gustav Jacob Jacobi.
Reference:
Applied Numerical Methods Using MATLAB®
Author(s): Won Young Yang, Wenwu Cao, Tae‐Sang Chung, John Morris
First published:14 January 2005
Print ISBN:9780471698333 |Online ISBN:9780471705192 |DOI:10.1002/0471705195
Copyright © 2005 John Wiley & Sons, Inc.



7.

Method of precision increase by averaging with application to numerical differentiation
Andrej Liptaj ∗Method of precision increase by averaging with application to numerical differentiation
Andrej Liptaj ∗



8. Richardson’s Interpolation

9. Differentiation by interpolation

Try - Generalized Jacobi-Gauss-Lobatto interpolation _ Frontiers of Mathematics



10. In the following reference

S. B. Sahoo, M. Acharya and B. P. Acharya , “Numerical Evaluation of Derivatives of Functions” , IOSR Journal of Mathematics (IOSR-JM) e-ISSN: 2278-5728, p-ISSN:2319-765X. Volume 10, Issue 2 Ver. VI (Mar-Apr. 2014), PP 72-75

Using Cauchy’s integral and Gauss-Legendre approximation the derivative of standard functions has been evaluated.  

#############################################################################
Copyright (c) 2023, 2024 , Prof. Radhamadhab Dalai, ITER , Siksha O Aanusandhan University, 
Odisha, India
Author's email address :  radhamadhabdalai@soa.ac.in
##############################################################################

