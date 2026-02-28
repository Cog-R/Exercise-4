def fahr_to_celsius(temp_fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
    temp_fahrenheit (float or int): Temperature in degrees Fahrenheit

    Returns:
    float: Temperature converted to degrees Celsius
    """

    # Subtract 32 from the Fahrenheit temperature
    # then divide by 1.8 to convert to Celsius
    temp_celsius = (temp_fahrenheit - 32) / 1.8
    return temp_celsius

def temp_classifier(temp_celsius):
    """
    Classify a temperature in Celsius into numeric categories.

    Categories:
    0 → very cold (below -2°C)
    1 → cold (-2°C to 1.999...°C)
    2 → cool (2°C to 14.999...°C)
    3 → warm/hot (15°C and above)

    Parameters:
    temp_celsius (float or int): Temperature in degrees Celsius

    Returns:
    int: Category number (0, 1, 2, or 3)
    """
    
    if temp_celsius < -2:
        return (0)
    elif -2 <= temp_celsius < 2:
        return (1)
    elif 2 <= temp_celsius <15:
        return (2)
    else:
        return (3)
