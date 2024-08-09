# Count Less or Equal

This project provides Python implementations for counting the number of elements in one list that are less than or equal to elements in another list. The project includes both a brute-force approach and a slightly more optimized approach using NumPy for performance improvements. Although these two approaches work well with small lists, another approach should be considered for cases using large lists. An alternative approach could be using sorting and binary search, but because of time constraints this alternative is left out for future improvements.<br/> Also, to fully evaluate the effectiveness of these different approaches, a comparison of their performance across various dataset sizes should be implemented. 

## Project Structure

- **`counter.py`**: Contains the main logic for counting elements using both brute-force and NumPy-optimized methods.
- **`test_counter.py`**: Unit tests for verifying the correctness of the functions in `counter.py`.

## Functions

- **`count_less_or_equal_brute_force(equipo_a: list, equipo_b: list) -> list`**<br/>
Counts the number of elements in equipo_a that are less than or equal to each element in equipo_b using a brute-force approach.

  1. `Parameters`:
     1. equipo_a: List of integers.
     2. equipo_b: List of integers.
  2. `Returns`: A list of integers where each element corresponds to the count for each element in equipo_b.
  3. `Time Complexity`: O(m x n), where m is the number of elements in equipo_b and n is the number of elements in equipo_a.<br/><br/>

  
- **`count_less_or_equal_numpy(equipo_a: list, equipo_b: list) -> list`**<br/>
Counts the number of elements in equipo_a that are less than or equal to each element in equipo_b using NumPy for optimized performance.

    1. `Parameters`:
        1. equipo_a: List of integers.
        2. equipo_b: List of integers.
    2. `Returns`: A list of integers where each element corresponds to the count for each element in equipo_b.
    3. `Time Complexity`: Approximately O(m x n), but with faster computations due to NumPy’s optimizations.