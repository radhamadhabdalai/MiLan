# On remembrance of a very honourable day of one of the finest founding members of modern Odisha state entitled as "Utkal Gourav Madhu Babu" 


# This repository contains implementations of preliminary mathematical background for machine learning
The following implementations are done using python 3,8. Students, Engineers, Reseraches, Scientists and authors are encouraged
to write these codes completely on native languages. They should advise and instruct others to write and verify the same with python or C.

Program Lists
-------------------------------------------------------------------------------------------------------------------------------
1.Polynomial root (all roots of simple polynomial, tested for quadratic only till now)
Reference - How to solve a polynomial. Python implementation of Newton’s… _ by #Revathi Suriyadeepan# _ Analytics Vidhya _ Medium_good
The main idea is to find the root of polynomial using Newton Raphson's method. Then divide the polynimail with (x-root). Then from the quotient polynomial find the root once gain and do it repeatedly.


2. Vandermonde-Matrix appproach- I am following William's work which is best suited for simple polynomial with real roots.(Still working)

The idea behind Vandermonde-Matrix generalized approach is

A x= Y
Where
A = Vandermonde matrix, x for given coefficients [c0, c1, c2,c3,......,cn]
It is assumed there are n such polynomial equations and Y is the output

From these n number of equations you have to calculate the root points using least square estimation and SVD calculation. This was implemented in LAPACK package in FORTRAn by ancient saints.(This had been implemnted and optimized using Delphi processor)

This is somehow very familiar with polynomial interpolation approach.(Need to resarch further).

This matrix approach with super fast SVD part (to find eigen values which are roots of polynomials) is better than number-1 approach and backward substitution part also.

NUMPY library (roots method np.ling,roots) uses this approach.

MATLAB's fsolve function uses different variant but similar approach.

Reference - "Solid" Kiran Achyutuni's deep dive.......
(You should work more on this)

Other interseting approachces will be added later after further studies and implementations.


2. Matrix algebra(This has been started) 

# Om Sree Sree Ganshay Namoh
# Om Sree Sree Bankeswaray Namoh 
Solving a system of linear equations using SVD decmosition, Eigen decompositions, Pseudo-Inverse has been added in the code.
This will run on Aryabhatt coprocessor :)


3. Eigen values (QR method) and Vectors
#Without using numpy library (Actually they use the QR implementation, that you can write as given small code snippets)
Reference- 
1.https://gist.github.com/RRisto/5f2bf3e5950e1682e9bdae09d8938f67#file-eigen_qr-py
2.https://rosettacode.org/wiki/QR_decomposition#Python 
3. http://mlwiki.org/index.php/Gram-Schmidt_Process


# The softwares required for this application
1. Python 3.8
2. Numpy Library
3. Pandas Library
4. Scikit-Learn
5.scipy
6.sympy

# Python already installed (Ubuntu 18.04)
# conda commands for installing those libraries
1. conda install numpy
2. conda install pandas
3. conda install scikit-learn
4. conda install matplotlib
5. conda install python-graphviz
6. conda install pydotplus
7.conda install sympy
8.conda install scipy


# Python course for machine learning will be there after sometime


Copyright (c) 2023, 2024 Radhamadhab Dalai, ITER , Siksha O Aanusandhan University, 
Odisha, India
Author's email address :  radhamadhabdalai@soa.ac.in

