import numpy as np

print( '                            Welcome!\n')

print( '\n    This program will evaluate an integral as a sum of'
       '\n   sub-intevals by using four algorithms: The left Riemann'
       '\n  sum, the right Riemann sum, trapezoidal rule, and Simpson Rule.')

print('\n   We are going to be integrating t + 5cos(wt) in two forms:'
      '\n one integrand with w  = 2 and another integrand with w = 80.'
      '\n  We are also going to perform each algorithm and integrand'
      '\n           for a "doubling-sequence" of K-values.\n')

print('    First we are going to compute the integrand with w = 2\n')


Ti = 3   #initial value for time
Tf = 11  #final value for time
w = 2    #angular frequency 

# The doubling sequence of K-values we want is K = 4, 8, 16...4096
Ki = 4   #first K-value
NKarr = 11 #total number of K's

Klist = [Ki*(2**nK) for nK in range(NKarr)] #computes doubling sequence for 4 for all nK values in NKarr
Karr = np.array(Klist) #converts the list to an array

#define each integration method
LeftA = np.array([0 for nK in range(NKarr)])
RightA = np.array([0 for nK in range(NKarr)])
TrapA = np.array([0 for nK in range(NKarr)])
SimpA = np.array([0 for nK in range(NKarr)])
                 
#define discrete time steps for each method
dY_LeftA = np.array([0 for nK in range(NKarr)])
dY_RightA = np.array([0 for nK in range(NKarr)])
dY_TrapA = np.array([0 for nK in range(NKarr)])
dY_SimpA = np.array([0 for nK in range(NKarr)])

hA = np.array([0 for nK in range(NKarr)])

#calculate the numerical accuracy of each integration method with the exact definite integral
for nK in range (NKarr):
    K = Karr[nK]

    h = (Tf-Ti)/K  #equidistant time grid with constant stepwidth
    Y_exact = ((Tf**2)/2 + (5/w)*np.sin(w*Tf))- ((Ti**2)/2 + (5/w)*np.sin(w*Ti)) #definte integral
    leftsum = 0 #lower limit
    rightsum = 0
    trapsum = 0
    simpsum = 0

#Left and Right Riemann sums
    for k in range(K+1): #tabulate at each K in NKarr
        t_k = Ti + k*h   #time steps
        f_k = t_k + 5*np.cos(w*t_k) #function with time steps
        leftsum = leftsum + h*f_k 
        rightsum = rightsum + h*f_k
        
#Simpson rule
        if k == 0:
            g_k = h/3
        elif k == K:
            g_k = h/3
        elif 0 < k and k < K and k%2 == 1:
            g_k = 4*h/3
        elif 0 < k and k < K and k%2 == 0:
            g_k = 2*h/3

        simpsum = simpsum + g_k*f_k

    f_0 = Ti + 5*np.cos(w*Ti)
    f_K = Tf + 5*np.cos(w*Tf)

    leftsum = leftsum - h*f_k
    rightsum = rightsum - h*f_0

#Trapezoidal rule
    trapsum = (leftsum + rightsum)/2

    LeftA[nK] = leftsum
    RightA[nK] = rightsum
    TrapA[nK] = trapsum
    SimpA[nK] = simpsum

#Accurancy between exact result and the various methodical results 
    dY_LeftA[nK] = np.abs(leftsum - Y_exact)
    dY_RightA[nK] = np.abs(rightsum - Y_exact)
    dY_TrapA[nK] = np.abs(trapsum - Y_exact)
    dY_SimpA[nK] = np.abs(simpsum - Y_exact)


#Print results    
print(' The resulted values are... \n'
      '\n Left Riemann sum:  '  + str(LeftA)  + '\n'
      ' Right Riemann sum: '  + str(RightA) + '\n'
      ' Trapezodial rule:  '  + str(TrapA)  + '\n'
      ' Simpson rule:      '  + str(SimpA)  + '\n')

print(' These are the values of the calculated numerical integration error... \n'
      '\n Left Riemann sum:  ' + str(dY_LeftA)  + '\n'
      ' Right Riemann sum: ' + str(dY_RightA) + '\n'
      ' Trapezoidal Rule:  ' + str(dY_TrapA)  + '\n'
      ' Simpson Rule:      ' + str(dY_SimpA)  + '\n')




print('\n    Now we are going to compute the integrand with w = 80\n')

w = 80 #angular frequency at 80

#same steps are followed...
for nK in range (NKarr):
    K = Karr[nK]

    h = (Tf-Ti)/K
    Y_exact = ((Tf**2)/2 + (5/w)*np.sin(w*Tf))- ((Ti**2)/2 + (5/w)*np.sin(w*Ti))
    leftsum = 0
    rightsum = 0
    trapsum = 0
    simpsum = 0

    for k in range(K+1):
        t_k = Ti + k*h
        f_k = t_k + 5*np.cos(w*t_k)
        leftsum = leftsum + h*f_k
        rightsum = rightsum + h*f_k
        
        if k == 0:
            g_k = h/3
        elif k == K:
            g_k = h/3
        elif 0 < k and k < K and k%2 == 1:
            g_k = 4*h/3
        elif 0 < k and k < K and k%2 == 0:
            g_k = 2*h/3

        simpsum = simpsum + g_k*f_k

    f_0 = Ti + 5*np.cos(w*Ti)
    f_K = Tf + 5*np.cos(w*Tf)

    leftsum = leftsum - h*f_k
    rightsum = rightsum - h*f_0

    trapsum = (leftsum + rightsum)/2

    LeftA[nK] = leftsum
    RightA[nK] = rightsum
    TrapA[nK] = trapsum
    SimpA[nK] = simpsum

    dY_LeftA[nK] = np.abs(leftsum - Y_exact)
    dY_RightA[nK] = np.abs(rightsum - Y_exact)
    dY_TrapA[nK] = np.abs(trapsum - Y_exact)
    dY_SimpA[nK] = np.abs(simpsum - Y_exact)
    

print(' The resulted values are... \n'
      ' \n Left Riemann sum:  '  + str(LeftA)  + '\n'
      ' Right Riemann sum: '  + str(RightA) + '\n'
      ' Trapezodial rule:  '  + str(TrapA)  + '\n'
      ' Simpson rule:      '  + str(SimpA)  + '\n')

print(' These are the values of the calculated numerical integration error... \n'
      ' \n Left Riemann sum:  ' + str(dY_LeftA)  + '\n'
      ' Right Riemann sum: ' + str(dY_RightA) + '\n'
      ' Trapezoidal Rule:  ' + str(dY_TrapA)  + '\n'
      ' Simpson Rule:      ' + str(dY_SimpA)  + '\n')

print('                             The End!')
