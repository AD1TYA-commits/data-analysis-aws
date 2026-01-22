# Architecture Pipeline

1. User opens the web app in a browser.
2. Browser sends a request to the Flask app running on EC2.
3. Flask fetches the CSV file from an S3 bucket.
4. Pandas reads and does the data.
5. Matplotlib generates a bar chart.
6. Flask returns the page with the chart to the browser.

Data is stored in S3 and compute runs on EC2.
