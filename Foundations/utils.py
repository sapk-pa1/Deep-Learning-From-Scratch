from typing import Callable , List 
from numpy import ndarray 


# A Function takes in an ndarray as an argument and produces an ndarray 
array_function = Callable[[ndarray], ndarray]

# A chain is a list of function 
Chain = List[array_function]

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

def chain_length_2(chain: Chain, 
                   a: ndarray) -> ndarray: 
    """Evaluates two functions in a row, in a Chain 

    Args:
        chain (Chain): list of functions 
        a (ndarray): input

    Returns:
        ndarray: output from appling the input to the chain of functions 
    """
    assert len(chain) ==2 
    # Length of the cchain shoud be 2 

    f1 = chain[0]
    f2= chain[1]

    return f2(f1(a))