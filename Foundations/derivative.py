from typing import Callable 
from numpy import ndarray 

def deriv(func: Callable[[ndarray], ndarray], 
          input_: ndarray, 
          delta: float = 0.001) -> ndarray: 
    """Evaluates the derivative of a function "func" at each element in the "input_" array.

    Args:
        func (Callable[[ndarray], ndarray]): The function for which the derivative is calculated.
        input_ (ndarray): The input array.
        delta (float, optional): The change in the inputs for numerical differentiation. Defaults to 0.001.

    Returns:
        ndarray: An array containing the derivative values corresponding to each element in the input array.
    """
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)
