def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

N = 16
square_root_bisection (N)


"""
Bisection Method for Square Root Approximation

This function uses the Bisection Method (a binary search technique) to approximate
the square root of a non-negative number. The algorithm works by narrowing down the 
interval [low, high] that contains the square root by repeatedly checking the midpoint. 
At each step, the interval is halved depending on whether the midpoint squared is 
greater than or less than the target number.

This method guarantees convergence for continuous functions and is especially useful 
when a fast, reliable square root approximation is needed without using built-in math functions.
"""
