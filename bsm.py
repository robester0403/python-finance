# Black scholes model calculations
import numpy as np
from scipy.stats import norm

r = 0.05 # interest rate
S = 30 # Underlying stock price
K = 40 # Strike price
T = 240/365 # Time to maturity
sigma = 0.3 # Volatility

def blackScholes(r, S, K, T, sigma, type="C"): # this function returns the price of a call or put option
  d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
  d2 = d1 - sigma*np.sqrt(T) # d2 is the same as d1 but with a different value
  try:
    if type == "C":
      price = S*norm.cdf(d1, 0 , 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1) # cdf is the cumulative distribution function
    elif type == "P":
      price = K*np.exp(-r*T)*norm.cdf(-d2,0,1) - S*norm.cdf(-d1,0 ,1)
    return price
  except:
      print("Error")
print('Option price is:')
print(round(blackScholes(r, S, K, T, sigma, type="C"), 2))