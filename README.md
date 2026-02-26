# AadhaarGati

**AI-Powered Decision Support System for Proactive Aadhaar Enrollment Planning.**
*[span_0](start_span)Built for the UIDAI Data Hackathon 2026 by Team CloudZ[span_0](end_span).*

## About the Project
AadhaarGati is a full stack analytical and predictive platform developed to address regional imbalance and infrastructure inefficiencies in the Aadhaar enrollment ecosystem. As adult enrollment reaches saturation in several states, traditional static enrollment models face diminishing returns. AadhaarGati provides a live analytics dashboard that enables administrators to identify bottlenecks and anticipate future enrollment demand.

## Key Features
* **[span_1](start_span)Predictive AI Engine:** Utilizes a custom Linear Regression model to forecast enrollment trends for 2026-2028[span_1](end_span).
* **[span_2](start_span)Demographic Shift Analysis:** Visually distinguishes stabilized adult demographic regions from high-growth child (0-5 & 5-17) regions[span_2](end_span).
* **[span_3](start_span)Custom Data Processing:** Built-in Python dictionary mapping and Pandas pipeline to clean, standardize, and aggregate raw government data[span_3](end_span).
* **[span_4](start_span)Interactive Dashboard:** Live analytics distinguishing stabilized regions from growth-focused districts[span_4](end_span).
* **Secure Access:** Implements robust security protocols for safe user authentication and database management.

## Tech Stack
* **[span_5](start_span)Backend:** Python, Flask[span_5](end_span)
* **[span_6](start_span)[span_7](start_span)Data Processing & AI:** Pandas, Linear Regression (Least Squares)[span_6](end_span)[span_7](end_span)
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
Future Scalability
GIS Spatial Mapping: Integration of map views to visualize "dark zones" overlayed with local hospital birth data.  
Real-Time Data Streams: Upgrading to process live API streams from UIDAI servers.  
Automated Resource Allocation: Expanding the AI model to recommend the exact number of enrollment kits needed per district dynamically.  
Team CloudZ
Jahangir Alam Mondal (Team Leader)  
Akash Samanta  
Suman Sahoo  
Supreeti Moulick  
Smriti Rahaman  
<!-- end list -->