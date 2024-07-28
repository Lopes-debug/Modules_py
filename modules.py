
# import numpy as np
# import matplotlib.pyplot as plt

# vendas = [1203, 219, 3901, 5590, 385, 918, 1834, 1981, 910, 1999, 1891, 7540]
# meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

# plt.plot(meses,vendas)
# plt.ylabel('vendas')
# plt.xlabel('meses')
# plt.axis([0,12, 0 , max(vendas)+300])
# plt.show()

# meses = np.arange(1, 51)

# plt.plot (meses, vendas, color='brown')
# plt.axis([0,50,0,max(vendas)+200])
# plt.xlabel('Meses')
# plt.ylabel('Vendas')
# plt.show()

# plt.figure(1, figsize=(15, 3))
# plt.subplot(1,3,1)
# plt.plot(meses,vendas, color='black')

# plt.subplot(1,3,2)
# plt.scatter(meses,vendas)

# plt.subplot(1,3,3)
# plt.bar(meses,vendas)

# plt.show()

# vendas = np.random.randint(100, 300, 5)
# print(vendas)