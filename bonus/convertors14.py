def convert(feet, inches):
    if feet == '':
        feet = 0
    elif inches == '':
        inches = 0
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    return meters
