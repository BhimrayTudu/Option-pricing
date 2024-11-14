# models.py
import math
from scipy.stats import norm

def monte_carlo_simulation(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility):
    d1 = (math.log(stock_price / strike_price) + (risk_free_rate + 0.5 * volatility ** 2) * time_to_maturity) / (volatility * math.sqrt(time_to_maturity))
    d2 = d1 - volatility * math.sqrt(time_to_maturity)
    call_price = stock_price * norm.cdf(d1) - strike_price * math.exp(-risk_free_rate * time_to_maturity) * norm.cdf(d2)
    return call_price

print(monte_carlo_simulation(105,100,1.0,0.05,0.2,100000))

