# creates forward propogated price tree function
import pandas as pd
import numpy as np

# option tree function:
def forward_tree(S0:float, sigma:float, n:int, T:float) -> np.matrix:
    # step size
    t = T / n
    # up movement 
    U = np.exp(sigma * np.sqrt(t))
    # down movement
    D = 1/U
    # empty matrix
    tree_matrix = np.zeros((n + 1, n + 1))
    # first collumn
    col_zero = (D ** np.arange(n+1)) * S0
       
    col_range = np.arange(n+1)
    
    tree_matrix = col_zero[:,None] * ((U / D) ** col_range)
    tree_matrix = np.round(np.tril(tree_matrix),4)

    return tree_matrix 
