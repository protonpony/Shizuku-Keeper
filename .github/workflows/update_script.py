# update_script.py (Python Example)
import requests
from bs4 import BeautifulSoup
import re # For removing extra spaces

URL = 'https://llamalab.com/automate/community/flows/51012' # Your target webpage
OUTPUT_FILE = 'README.md'

# Define markers for replacement
START_MARKER = '<!-- START_SK_CONTENT -->'
END_MARKER = '<!-- END_SK_CONTENT -->'

# Fetch content
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Find elements with itemprop="description" (example)
items = soup.find_all(itemprop="description") # Adjust 'description' as needed

markdown_content = ""
for item in items:
    # Extract text and clean it up
    text = item.get_text(strip=True)
    # Add more cleaning if needed (e.g., using regex for specific formats)
    # text = re.sub(r'\s+', ' ', text) # Replace multiple spaces with one
    markdown_content += f"- {text}\n"

# Read existing README
with open(OUTPUT_FILE, 'r') as f:
    content = f.read()

# Replace content between markers
# Regex to find and replace content between markers, including markers themselves
pattern = re.compile(f'{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}', re.DOTALL)
new_content = pattern.sub(f'{START_MARKER}{markdown_content}{END_MARKER}', content)

# Write back to README if changed (the action handles commit/push)
with open(OUTPUT_FILE, 'w') as f:
    f.write(new_content)
