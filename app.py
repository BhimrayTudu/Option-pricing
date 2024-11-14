from flask import Flask, request, jsonify, render_template
from monte_carlo import monte_carlo_simulation  # Assuming monte_carlo_simulation function is correctly defined in monte_carlo module

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    """
    Render the index.html template for the home page.
    """
    return render_template("index.html")

@app.route('/calculate-option-price', methods=['POST'])
def calculate_option_price():
    """
    Endpoint to calculate the price of an option using Monte Carlo simulation.
    Expects JSON data with the following fields:
    - stock_price: Current price of the underlying asset.
    - strike_price: Strike price of the option.
    - time_to_maturity: Time until the option expires (in years).
    - risk_free_rate: Annual risk-free interest rate (decimal).
    - volatility: Annual volatility of the underlying asset (decimal).
    - simulations: Number of simulations to run for the Monte Carlo simulation.
    - option_type: Type of option ('call' or 'put').
    
    Returns:
    - JSON response with the calculated option price.
    """
    data = request.json
    
    # Check if all required fields are present in the JSON data
    required_fields = ['stock_price', 'strike_price', 'time_to_maturity', 'risk_free_rate', 'volatility', 'simulations', 'option_type']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Extract parameters from JSON data and convert to appropriate types
    stock_price = float(data['stock_price'])
    strike_price = float(data['strike_price'])
    time_to_maturity = float(data['time_to_maturity'])
    risk_free_rate = float(data['risk_free_rate'])
    volatility = float(data['volatility'])
    simulations = int(data['simulations'])
    option_type = data['option_type']
    
    # Calculate option price using monte_carlo_simulation function
    option_price = monte_carlo_simulation(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility, simulations, option_type)
    
    # Return JSON response with the calculated option price and HTTP status code 200 (OK)
    return jsonify({'option_price': option_price}), 200

if __name__ == '__main__':
    app.run(debug=True)
