# AadhaarGati

**AI-Powered Decision Support System for Proactive Aadhaar Enrollment Planning.**
*Built for the UIDAI Data Hackathon 2026 by Team CloudZ.*

## About the Project
AadhaarGati is a full stack analytical and predictive platform developed to address regional imbalance and infrastructure inefficiencies in the Aadhaar enrollment ecosystem. As adult enrollment reaches saturation in several states, traditional static enrollment models face diminishing returns. AadhaarGati provides a live analytics dashboard that enables administrators to identify bottlenecks and anticipate future enrollment demand.

## Key Features
* **Predictive AI Engine:** Utilizes a custom Linear Regression model to forecast enrollment trends for 2026-2028.
* **Demographic Shift Analysis:** Visually distinguishes stabilized adult demographic regions from high-growth child (0-5 & 5-17) regions.
* **Custom Data Processing:** Built-in Python dictionary mapping and Pandas pipeline to clean, standardize, and aggregate raw government data.
* **Interactive Dashboard:** Live analytics distinguishing stabilized regions from growth-focused districts.
* **Secure Access:** Implements robust security protocols for safe user authentication and database management.

## Tech Stack
* **Backend:** Python, Flask
* **Data Processing & AI:** Pandas, Linear Regression (Least Squares)
* **Database:** SQLite, SQLAlchemy
* **Frontend:** HTML5, CSS3, JavaScript, Chart.js
* **Development Environment:** VS Code

## Project Structure
```text
AadhaarGati/
├── instance/
│   └── users.db               
├── static/
│   ├── style.css              
│   └── bg.jpg                 
├── templates/
│   ├── index.html             
│   ├── login.html             
│   ├── signup.html            
│   └── dashboard.html         
├── app.py                     
├── Enrollment.ipynb           
├── requirements.txt           
└── README.md

🚀 Future Scalability
* GIS Spatial Mapping:** Integration of map views to visualize "dark zones" overlayed with local hospital birth data.
* Real-Time Data Streams:** Upgrading to process live API streams from UIDAI servers.
* Automated Resource Allocation:** Expanding the AI model to recommend the exact number of enrollment kits needed per district dynamically.

👥 Team CloudZ
* Jahangir Alam Mondal (Team Leader)
* Akash Samanta
* Suman Sahoo
* Supreeti Moulick
* Smriti Rahaman
