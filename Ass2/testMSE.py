import numpy as np
size = 10

p = 0.5
realVar = p*(1-p)

MSE_s_n_minus_1 = 0
MSE_s_n = 0 
num_test = 400000
for i in range(num_test):
    # a = np.random.binomial(1,p,[size,])
    a = np.random.normal(size = [size,])

    mean = np.mean(a)
    s_n_minus_1 = np.sum(  (a - np.mean(a))**2  ) / (size-1)
    # print("S_n-1:",s_n_minus_1)
    MSE_s_n_minus_1 += (realVar-s_n_minus_1)**2

    s_n = np.sum(  (a - np.mean(a))**2  )  / (size)
    # print("S_n:",s_n)
    MSE_s_n += (realVar-s_n)**2

print(MSE_s_n_minus_1/num_test)
print(MSE_s_n/num_test)
print("MSE_s_n_minus_1 - MSE_s_n:", MSE_s_n_minus_1/num_test - MSE_s_n/num_test)