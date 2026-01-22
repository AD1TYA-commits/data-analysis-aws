# AWS Data Analysis Web App

A minimal cloud-based web application that fetches Spotify data from AWS S3, analyzes it using Pandas, and visualizes insights with Matplotlib using a Flask server running on EC2.

---

## 🏗 Project Structure
.
├── app.py
├── requirements.txt
├── README.md
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── data/
│ └── data.csv

## 🛠 Tech Stack
- Python
- Flask
- Pandas
- Matplotlib
- AWS EC2
- AWS S3
- HTML / CSS

---

## 🔍 What This Project Does
- Reads a CSV file stored in AWS S3
- Analyze data using Pandas
- Finds top 5 albums with the most songs
- Generates a bar chart using Matplotlib
- Displays the chart on a web page using Flask

---
## ☁️ AWS Usage
- **S3**: Stores the Spotify CSV dataset
- **EC2**: Hosts the Flask web application
- **IAM Role**: Grants EC2 permission to access S3 securely

---

## 🚀 Future Improvements
- Move compute from EC2 to AWS Lambda
- Add API Gateway for REST access
- Cache results to reduce recomputation
- Add CloudWatch logging and monitoring
- Containerize using Docker

---
