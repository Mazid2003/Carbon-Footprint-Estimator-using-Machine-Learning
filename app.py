from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('cf_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        form_data = [
            float(request.form.get('electricity_kwh_per_month')),
            float(request.form.get('natural_gas_therms_per_month')),
            float(request.form.get('vehicle_miles_per_month')),
            float(request.form.get('house_area_sqft')),
            float(request.form.get('water_usage_liters_per_day')),
            float(request.form.get('public_transport_usage_per_week')),
            int(request.form.get('household_size')),
            int(request.form.get('home_insulation_quality')),
            float(request.form.get('meat_consumption_kg_per_week')),
            int(request.form.get('laundry_loads_per_week')),
            int(request.form.get('recycles_regularly')),
            int(request.form.get('composts_organic_waste')),
            int(request.form.get('uses_solar_panels')),
            int(request.form.get('energy_efficient_appliances')),
            int(request.form.get('heating_type')),
            int(request.form.get('diet_type')),
            int(request.form.get('owns_pet')),
            int(request.form.get('smart_thermostat_installed')),
        ]
        
        # Convert to 2D array
        input_data = np.array(form_data).reshape(1, -1)
        
        # Predict
        prediction = model.predict(input_data)[0]
        
        return render_template('index.html', prediction=round(prediction, 2))
    
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
