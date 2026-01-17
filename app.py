from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hackathon-secret-key' # Needed for sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' # Database file
db = SQLAlchemy(app)

# --- 1. SETUP LOGIN MANAGER ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# --- 2. DATABASE MODEL (User Table) ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create Database if it doesn't exist
with app.app_context():
    db.create_all()

# --- 3. MATH AI FUNCTION (From previous step) ---
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
    return [(m * year + b) for year in future_years]

# --- 4. ROUTES (Pages) ---

@app.route("/")
@login_required   # <--- THIS IS THE NEW PART
def home():
    # --- HARDCODED DATA (Safe & Fast) ---
    states = ["Uttar Pradesh", "Bihar", "Maharashtra", "West Bengal", "Madhya Pradesh", 
              "Rajasthan", "Tamil Nadu", "Gujarat", "Karnataka", "Andhra Pradesh"]
    age_0_5 = [32000000, 16000000, 15000000, 14000000, 15500000, 13000000, 8000000, 9500000, 9000000, 8500000]
    age_5_17 = [45000000, 30000000, 18000000, 17500000, 20000000, 17000000, 11000000, 12000000, 11000000, 10500000]
    age_18 = [140000000, 85000000, 95000000, 78000000, 60000000, 56000000, 62000000, 50000000, 52000000, 49000000]

    # AI Prediction
    years_data = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    enrolments_data = [900000000, 1050000000, 1150000000, 1220000000, 1250000000, 
                       1260000000, 1280000000, 1320000000, 1360000000, 1380000000, 1400000000]
    future_years = [2026, 2027, 2028]
    future_predictions = train_and_predict(years_data, enrolments_data, future_years)

    return render_template("index.html", 
                           user=current_user, # Pass user info to HTML
                           states=states, age_0_5=age_0_5, age_5_17=age_5_17, age_18=age_18,
                           years=years_data + future_years,
                           past_enrolment=enrolments_data + [None]*3,
                           future_enrolment=[None]*10 + [enrolments_data[-1]] + future_predictions)

# --- LOGIN & SIGNUP ROUTES ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # --- THIS WAS MISSING ---
        user = User.query.filter_by(username=username).first() 
        # ------------------------

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home')) # Redirects to Dashboard
        else:
            flash('Login Failed. Check details.')
            
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Create new user
        new_user = User(username=username, password=generate_password_hash(password, method='scrypt'))
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('profile'))
        except:
            flash("Username already exists.")
    return render_template('signup.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
# --- TEMPORARY ADMIN ROUTE ---
@app.route('/view-users')
def view_users():
    # 1. Get all users from the database
    all_users = User.query.all()
    
    # 2. Create a simple HTML list
    page_content = "<h1>Registered Users</h1><ul>"
    for user in all_users:
        page_content += f"<li><strong>ID:</strong> {user.id} | <strong>Username:</strong> {user.username} | <strong>Password (Hashed):</strong> {user.password}</li>"
    page_content += "</ul>"
    
    return page_content

if __name__ == "__main__":
    app.run(debug=True)