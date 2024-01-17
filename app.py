from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/bmi-calculator')
def bmi_calculator():
    # Get query parameters
    height = request.args.get('height')
    weight = request.args.get('weight')

    # Check if both height and weight are provided
    if height is None or weight is None:
        return 'Please provide both height and weight as query parameters.'

    try:
        # Convert height and weight to float
        height = float(height)
        weight = float(weight)
    except ValueError:
        return 'Invalid height or weight. Please provide valid numeric values.'

    # Calculate BMI
    bmi = calculate_bmi(height, weight)

    bmi_data = None
    if bmi < 18.5:
        bmi_data = {'bmi': bmi, 'description': 'Underweight'}
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_data = {'bmi': bmi, 'description': 'Healthly weight'}
    elif bmi >= 25 and bmi <= 29.9:
        bmi_data = {'bmi': bmi, 'description': 'Overweight'}
    elif bmi >= 30 and bmi <= 34.9:
        bmi_data = {'bmi': bmi, 'description': 'Obese'}
    elif bmi >= 35 and bmi <= 39.9:
        bmi_data = {'bmi': bmi, 'description': 'Severely Obese'}
    else:
        bmi_data = {'bmi': bmi, 'description': 'Mobirdly Obese'}

    return jsonify(bmi_data)

def calculate_bmi(height, weight):
    # Formula for BMI: weight (kg) / (height (m))^2
    height_in_meters = height / 100  # Convert height from cm to meters
    bmi = weight / (height_in_meters ** 2)
    return round(bmi, 2)

if __name__ == '__main__':
    app.run(debug=True)
