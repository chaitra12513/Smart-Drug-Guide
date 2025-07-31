import sqlite3

# Connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create doctors table
cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialization TEXT NOT NULL,
    experience INTEGER NOT NULL,
    contact TEXT NOT NULL,
    location TEXT NOT NULL
)''')

# Create appointments table
cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER NOT NULL,
    patient_name TEXT NOT NULL,
    appointment_date TEXT NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
)''')





# Add sample doctors (Run only once)
cursor.executemany('INSERT INTO doctors (name, specialization, experience, contact, location) VALUES (?, ?, ?, ?, ?)', [
    ("Dr. Sandeep Budhiraja", "Gastroenterology & Hepatology", 29, "9876543210", "Saket"),
    ("Dr. Harit Chaturvedi","Cancer Care / Oncology, Thoracic Oncology, Surgical Oncology, Robotic Surgery, Head & Neck Oncology, Breast Cancer", 40, "8765432109", "Saket"),
    ("Dr. Anant Kumar", "Urology, Kidney Transplant, Robotic Surgery", 40, "7654321098", "Saket"),
    ("Dr. Balbir Singh", "Cardiac Sciences, Cardiology, Cardiac Electrophysiology-Pacemaker, Interventional Cardiology",45,"3567546789","Saket"),
    ("Dr. Pradeep Chowbey","Laparoscopic / Minimal Access Surgery, Bariatric Surgery / Metabolic, Institute of Laparoscopic, Endoscopic & Bariatric Surgery, Robotic Surgery",50,"7834562345","Saket"),
    ("Dr. Dinesh Khullar","Nephrology, Kidney Transplant",35,"9864536787","Saket"),
])

conn.commit()
conn.close()

print("Database setup complete!")