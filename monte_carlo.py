#!/usr/bin/env python
# coding: utf-8

import numpy as np

def monte_carlo_simulation(S, K, T, r, sigma, simulations, option_type='call'):
    """
    Calculate the price of a European call or put option using Monte Carlo simulation.
    
    Parameters:
        S (float): Current price of the underlying asset (e.g., stock).
        K (float): Strike price of the option.
        T (float): Time to expiration of the option (in years).
        r (float): Annual risk-free interest rate (as a decimal).
        sigma (float): Annual volatility of the underlying asset (as a decimal).
        simulations (int): Number of simulations to run.
        option_type (str): Type of the option, either 'call' or 'put'. Default is 'call'.
        
    Returns:
        float: The price of the option.
    """
    dt = T
    rand = np.random.standard_normal(simulations)
    future_stock_prices = S * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * rand)
    
    if option_type == 'call':
        option_payoff = np.maximum(0, future_stock_prices - K)
    elif option_type == 'put':
        option_payoff = np.maximum(0, K - future_stock_prices)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    option_price = np.exp(-r * T) * np.mean(option_payoff)
    
    return option_price

# Example usage:
S = 105  # Current stock price
K = 100  # Strike price
T = 1.0  # Time to expiration (in years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility
simulations = 100000  # Number of simulations

call_price = monte_carlo_simulation(S, K, T, r, sigma, simulations, option_type='call')
put_price = monte_carlo_simulation(S, K, T, r, sigma, simulations, option_type='put')

print("Call option price:", call_price)
print("Put option price:", put_price)
