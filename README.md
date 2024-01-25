Video Link: https://drive.google.com/file/d/1DBRJUmMOFMrEWasL8ryak8rkbGFIiLzX/view?usp=sharing
**ICP-3 Employee Code**

Class variable to count the number of Employees
Constructor for the Employee class.
Parameters:
- name: Name of the employee
- family: Family information of the employee
- salary: Salary of the employee
- department: Department in which the employee works

Increment the employee count when a new employee is created
In function  average_salary calculates the average salary of a list of employees.
Parameters:
- employees: List of Employee objects
Returns:
- Average salary of the employees
  
Creates a Fulltime Employee class that inherits from Employee class and constructor for the FulltimeEmployee class.
Parameters:
- name: Name of the employee
- family: Family information of the employee
- salary: Salary of the employee
- department: Department in which the employee works

Creates instances of Fulltime Employee class and Employee class and call their member functions.

Prints the average salary and total number of employees

**ICP-3 Numpy Package code**

Using NumPy created random vector of size 20 having only float in the range 1-20.

randvec = np.random.uniform(1, 20, 20)

This line uses NumPy's np.random.uniform function to generate an array (randvec) of 20 random float values. The uniform function generates random samples from a uniform distribution between the specified range [1, 20).

Then reshaped the array to 4 by 5

arrayreshape = randvec.reshape(4, 5)

Here, the reshape method is used to reshape the original 1D array (randvec) into a 2D array (arrayreshape) with dimensions 4x5. The resulting array will have 4 rows and 5 columns.

Then replaced the max in each row by 0 (axis=1)

arrayreshape[np.arange(arrayreshape.shape[0]), np.argmax(arrayreshape, axis=1)] = 0

This line utilizes advanced indexing to replace the maximum value in each row of the 2D array (arrayreshape) with 0. It uses np.arange(arrayreshape.shape[0]) to create an array of row indices and np.argmax(arrayreshape, axis=1) to find the indices of the maximum values along each row. These indices are then used to replace the corresponding elements with 0.

Finally, the code prints the original random vector (randvec) and the reshaped matrix (arrayreshape). This allows you to observe the original array and the modified array with maximum values replaced by 0.
