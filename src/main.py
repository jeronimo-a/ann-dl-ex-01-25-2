''' Exercícios 01 - Data '''

import numpy as np
from matplotlib import pyplot as plt

N_SAMPLES = 100

CLASS_0 = ( (2, 3), (0.8, 2.5))
CLASS_1 = ( (5, 6), (1.2, 1.9))
CLASS_2 = ( (8, 1), (0.9, 0.9))
CLASS_3 = ((15, 4), (0.5, 2.0))

def generate_data(CLASS_data, n_samples) -> np.ndarray[np.ndarray, np.ndarray]:
    dim_0 = np.random.normal(loc=CLASS_data[0][0], scale=CLASS_data[1][0], size=n_samples)
    dim_1 = np.random.normal(loc=CLASS_data[0][1], scale=CLASS_data[1][1], size=n_samples)
    return np.array(list(zip(dim_0, dim_1)))

class_0_data = generate_data(CLASS_0, N_SAMPLES)
class_1_data = generate_data(CLASS_1, N_SAMPLES)
class_2_data = generate_data(CLASS_2, N_SAMPLES)
class_3_data = generate_data(CLASS_3, N_SAMPLES)

plt.scatter(class_0_data[:,0], class_0_data[:,1], color='red', label='Classe 0')
plt.scatter(class_1_data[:,0], class_1_data[:,1], color='blue', label='Classe 1')
plt.scatter(class_2_data[:,0], class_2_data[:,1], color='green', label='Classe 2')
plt.scatter(class_3_data[:,0], class_3_data[:,1], color='purple', label='Classe 3')
plt.xlabel('Dimensão 0')
plt.ylabel('Dimensão 1')
plt.title('Dados Gerados')
plt.savefig('data.png')