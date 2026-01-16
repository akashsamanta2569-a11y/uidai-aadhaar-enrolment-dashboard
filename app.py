from flask import Flask, render_template

app = Flask(__name__)


def train_and_predict(years, values, future_years):
    n = len(years)
    sum_x = sum(years)
    sum_y = sum(values)
    sum_xy = sum(y * v for y, v in zip(years, values))
    sum_x2 = sum(y * y for y in years)

    
    try:
        m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        b = (sum_y - m * sum_x) / n
    except ZeroDivisionError:
        return []

    
    predictions = [(m * year + b) for year in future_years]
    return predictions

@app.route("/")
def home():
   
    states = ["Uttar Pradesh", "Bihar", "Maharashtra", "West Bengal", "Madhya Pradesh", 
              "Rajasthan", "Tamil Nadu", "Gujarat", "Karnataka", "Andhra Pradesh"]
    
   
    age_0_5 = [32000000, 16000000, 15000000, 14000000, 15500000, 13000000, 8000000, 9500000, 9000000, 8500000]
    age_5_17 = [45000000, 30000000, 18000000, 17500000, 20000000, 17000000, 11000000, 12000000, 11000000, 10500000]
    age_18 = [140000000, 85000000, 95000000, 78000000, 60000000, 56000000, 62000000, 50000000, 52000000, 49000000]

   
    years_data = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    enrolments_data = [
        900000000, 1050000000, 1150000000, 1220000000, 1250000000, 
        1260000000, 1280000000, 1320000000, 1360000000, 1380000000, 1400000000
    ]

    
    future_years = [2026, 2027, 2028]
    future_predictions = train_and_predict(years_data, enrolments_data, future_years)

    
    years_list = years_data + future_years
    past_data = enrolments_data + [None, None, None]
    
    
    last_real_val = enrolments_data[-1]
    prediction_data = [None] * (len(years_data)-1) + [last_real_val] + future_predictions

    return render_template(
        "index.html",
        states=states,
        age_0_5=age_0_5,
        age_5_17=age_5_17,
        age_18=age_18,
        years=years_list,
        past_enrolment=past_data,
        future_enrolment=prediction_data
    )

if __name__ == "__main__":
    app.run(debug=True)