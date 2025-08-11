def predict_temperature(t):
    a = 0.5
    b = -3
    c = 28
    T = a * t**2 + b * t + c
    return T

# Example usage
t = 5  # e.g., 5th hour or 5th day
T = predict_temperature(t)
print(f"Predicted temperature at t={t}: {T:.2f}°C")
