import requests
import time, os
from dotenv import load_dotenv

load_dotenv('./.env')

# Replace 'YOUR_API_KEY' with your actual API key
api_key = os.getenv('HTML2PDF_KEY')
url = 'https://api.html2pdf.app/v1/generate'

# Parameters for the API call
params = {
    'html': 'https://resume.kanakjr.in/',
    'apiKey': api_key,
    'format': 'A3',
    # 'width': 1800,#450,
    # 'height': 1950,#580,
    'marginLeft': 2,
    'marginRight': 2,
    'scale': 0.8,
    'waitFor': 5,
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Assuming you want to save the PDF file to disk
    #  filename = output+timestamp.pdf
    filename = f'output-{time.time()}.pdf'
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'PDF successfully created and saved as {filename}')
else:
    print('Failed to generate PDF. Status code:', response.status_code)