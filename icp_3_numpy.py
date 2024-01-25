import numpy as np

# Using NumPy create random vector of size 20 having only float in the range 1-20. 
randvec = np.random.uniform(1, 20, 20)

# Then reshape the array to 4 by 5
arrayreshape = randvec.reshape(4, 5)

# Then replace the max in each row by 0 (axis=1)
arrayreshape[np.arange(arrayreshape.shape[0]), np.argmax(arrayreshape, axis=1)] = 0

print("Original Matrix:")
print(randvec)
print("\nReshaped Matrix:")
print(arrayreshape)
