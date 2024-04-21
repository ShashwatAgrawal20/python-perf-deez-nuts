# Performance Benchmarking
## Removing Duplicate List Items While Maintaining Order

This Python script benchmarks different methods for removing duplicates from a list while preserving the order of elements. It compares their execution times to identify the most efficient approach for this task.

## Methods Tested:
1. [**Using `dict.fromkeys()` with Key Retrieval**](main.py#L5-L6)
2. [**Using `dict.fromkeys()` Without Retrieving Keys**](main.py#L9-L10)
3. [**Using Classic Looping with a Set**](main.py#L13-L21)
4. [**Using Classic Looping**](main.py#L24-L29)

### Understanding the Working:
- The script generates a **list of million random integers between 0 and 50.**
- Each method is executed 100 times, and the execution time for each is measured.
- The output displays the time taken for each method in seconds.

#### Sample Output:
```output
Time using_dict_fromkeys: 3.123974360001739 seconds
Time using_dict_fromkeys_without_keys: 2.6290600829997857 seconds
Time using_classing_loop_with_set: 2.790389466998022 seconds
Time using_classing_loop: 38.75640665500032 seconds
```

## Observations:
- As shown in the sample output, for large lists, the performance impact can be significant.
- The methods using dictionaries (dict.fromkeys()) perform similarly and are the fastest.
- Classic looping techniques are significantly slower, especially when not utilizing a set to track seen elements.

## Conclusion:
- For efficiently removing duplicates from a list while preserving order, using dictionaries (`dict.fromkeys()`) is recommended due to their superior performance.
- Classic looping techniques, while simple, are less efficient for large datasets.
