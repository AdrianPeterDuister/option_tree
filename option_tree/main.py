# code runs here
from src.forward_tree import forward_tree
from src.backward_tree import euro_option, call, put, american_option_tree, american_option_tree_up_in, american_option_tree_up_out, american_option_tree_down_in, american_option_tree_down_out
import yaml

# option tree inputs
S_0 = 100.0
sigma = .10
n = 3
T = 1
K = 100.0
C = 110
r = 0.03
price_tree = forward_tree(S_0, sigma, n, T)
print(f"{'-' * 10} price tree:  {'-' * 10}")
print(price_tree)

euro_price = euro_option(tree=price_tree,f=call,sigma = sigma, r = r, n = n, T= T, K = K)
print(f"{'-' * 10} euopean style option price{'-' * 10}")
print(euro_price)

ami_tree = american_option_tree(tree=price_tree,f=call, sigma = sigma, r = r, n = n, T=T, K = K) 
print(f"{'-' * 10} american style option value tree {'-' * 10}")
print(ami_tree)

ui_tree = american_option_tree_up_in(tree=price_tree,f=call, sigma = sigma, r = r, n = n, T=T, K = K, C = C)
print(f"{'-' * 10} american style up and in option value tree {'-' * 10}")
print(ui_tree)
uo_tree = american_option_tree_up_out(tree=price_tree,f=call, sigma = sigma, r = r, n = n, T=T, K = K, C = C)
print(f"{'-' * 10} american style up and out option value tree {'-' * 10}")
print(uo_tree)
di_tree = american_option_tree_down_in(tree=price_tree,f=call, sigma = sigma, r = r, n = n, T=T, K = K, C = C)
print(f"{'-' * 10} american style down and in option value tree {'-' * 10}") 
print(di_tree)
