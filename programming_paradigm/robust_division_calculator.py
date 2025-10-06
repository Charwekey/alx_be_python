# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling division by zero and invalid inputs.
    Returns a message with the result or an error message.
    """
    try:
        # Convert inputs to floats (will raise ValueError if non-numeric)
        num = float(numerator)
        den = float(denominator)

        # Perform division (may raise ZeroDivisionError)
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
