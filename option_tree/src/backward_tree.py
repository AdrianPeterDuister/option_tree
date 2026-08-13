# creates backward propogated value tree functions
import numpy as np
from scipy.stats import binom

# call and put otion payof functions
def call(S:float,K:float) -> float:
    return max(S - K, 0)

def put(S:float,K:float) -> float:
    return max(K - S, 0)
# vectorize call and put functions
call = np.vectorize(call)

put = np.vectorize(put)


# vanilla european option price
def euro_option(tree:np.array, f:object, sigma:float, r:float , n:int, T:float, K:float) -> float:
    # step size
    t = T / n
    # up movement 
    U = np.exp(sigma * np.sqrt(t))
    # down movement
    D = 1/U
    # probability of upstep
    p = (np.exp(r*t) - D) / (U - D)
    # payof tree
    ST = np.tril(f(tree,K))
    #vector of column vector indices
    k = np.arange(n+1)
    # vector of probabilities for each terminal value
    prob_vector = binom.pmf(k=k, n=n, p=p)
    # PV of expexted value (price)
    price = (prob_vector @ ST[n,:]) * np.exp(-r *T)

    return float(price)


    
    



# vanilla american option tree
def american_option_tree(tree:np.array, f:object, sigma:float, r:float , n:int, T:float, K:float) -> np.array:
    # step size
    t = T / n
    # up movement 
    U = np.exp(sigma * np.sqrt(t))
    # down movement
    D = 1/U
    # probability of upstep
    p = (np.exp(r*t) - D) / (U - D)
    # payof tree
    ST = np.tril(f(tree,K))
    
    #fliped payof tree
    f_ST =   np.flip(ST,axis=0)
    value_tree = np.zeros((n+1,n+1))
    value_tree[0,:] = f_ST[0,:]
    for row in range(1,n+1):
        hold_value = ((1-p) * value_tree[row-1,:] + p * np.append(value_tree[row-1,1:],0)) * np.exp(-r*t)
        excercise_value = f_ST[row,:]
        value_tree[row,:] = np.maximum(hold_value, excercise_value)
    value_tree = np.flip(value_tree,axis=0)
    return np.tril(value_tree)
            
    
# up-and-in american option function
def american_option_tree_up_in(tree:np.array, f:object, sigma:float, r:float , n:int, T:float, K:float, C:float) -> np.array:
    # step size
    t = T / n
    # up movement 
    U = np.exp(sigma * np.sqrt(t))
    # down movement
    D = 1/U
    # probability of upstep
    p = (np.exp(r*t) - D) / (U - D)
    # payof tree
    ST = np.tril(f(tree,K))
    
    # threshold for up and in
    if np.sum(np.diag(tree) >= C) == 0:
        return "Option is never over, value = 0"
    threshold_line = n + 1 - np.sum(np.diag(tree) >= C)
    # prune payof tree
    ST[:, :threshold_line] = 0

    #fliped payof tree
    f_ST =   np.flip(ST,axis=0)
    value_tree = np.zeros((n+1,n+1))
    value_tree[0,:] = f_ST[0,:]
    for row in range(1,n+1):
        hold_value = ((1-p) * value_tree[row-1,:] + p * np.append(value_tree[row-1,1:],0)) * np.exp(-r*t)
        excercise_value = f_ST[row,:]
        value_tree[row,:] = np.maximum(hold_value, excercise_value)
    value_tree = np.flip(value_tree,axis=0)
    return np.tril(value_tree)




# up-and-out american option function
def american_option_tree_up_out(tree:np.array, f:object, sigma:float, r:float , n:int, T:float, K:float, C:float) -> np.array:
    # step size
    t = T / n
    # up movement 
    U = np.exp(sigma * np.sqrt(t))
    # down movement
    D = 1/U
    # probability of upstep
    p = (np.exp(r*t) - D) / (U - D)
    # payof tree
    ST = np.tril(f(tree,K))
    
    # threshold for up and in
    threshold_line = n + 1 - np.sum(np.diag(tree) >= C)
    # prune payof tree
    ST[:, threshold_line:] = 0

    #fliped payof tree
    f_ST =   np.flip(ST,axis=0)
    value_tree = np.zeros((n+1,n+1))
    value_tree[0,:] = f_ST[0,:]
    for row in range(1,n+1):
        hold_value = ((1-p) * value_tree[row-1,:] + p * np.append(value_tree[row-1,1:],0)) * np.exp(-r*t)
        excercise_value = f_ST[row,:]
        value_tree[row,:] = np.maximum(hold_value, excercise_value)
    value_tree = np.flip(value_tree,axis=0)
    return np.tril(value_tree)



# down-and-in american option function
def american_option_tree_down_in(tree:np.array, f:object, sigma:float, r:float , n:int, T:float, K:float, C:float) -> np.array:
    # step size
    t = T / n
    # up movement 
    U = np.exp(sigma * np.sqrt(t))
    # down movement
    D = 1/U
    # probability of upstep
    p = (np.exp(r*t) - D) / (U - D)
    # payof tree
    ST = np.tril(f(tree,K))
    
    # threshold for up and in
    if np.sum(tree[:,0] <= C) == 0:
        return "Option is never under, value = 0"
    threshold_line = n + 1 - np.sum(tree[:,0] <= C)
    # prune payof tree
    ST = np.tril(ST, k= -threshold_line)
    

    #fliped payof tree
    f_ST =   np.flip(ST,axis=0)
    value_tree = np.zeros((n+1,n+1))
    value_tree[0,:] = f_ST[0,:]
    for row in range(1,n+1):
        hold_value = ((1-p) * value_tree[row-1,:] + p * np.append(value_tree[row-1,1:],0)) * np.exp(-r*t)
        excercise_value = f_ST[row,:]
        value_tree[row,:] = np.maximum(hold_value, excercise_value)
    value_tree = np.flip(value_tree,axis=0)
    return np.tril(value_tree)


