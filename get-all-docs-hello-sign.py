import requests
import os
import time

# Your HelloSign API key
API_KEY = 'YOUR KEY HERE!!!'

# Function to get all signature requests, handling pagination
def get_all_signature_requests():
    signature_requests = []
    page = 1
    while True:
        url = f'https://api.hellosign.com/v3/signature_request/list?page={page}'
        response = requests.get(url, auth=(API_KEY, ''))
        if response.status_code == 200:
            data = response.json()
            signature_requests.extend(data.get('signature_requests', []))
            if len(data.get('signature_requests', [])) < 20:  # Assuming each page has 20 requests
                break
            page += 1
        else:
            print("Failed to retrieve signature requests:", response.text)
            break
    return signature_requests

# Function to download a document by signature request ID and title
def download_document(signature_request_id, document_title, save_dir="hellosign_docs"):
    url = f'https://api.hellosign.com/v3/signature_request/files/{signature_request_id}'
    response = requests.get(url, auth=(API_KEY, ''), stream=True)
    if response.status_code == 200:
        # Ensure save directory exists
        os.makedirs(save_dir, exist_ok=True)
        
        # Replace any problematic characters in the document title
        safe_title = "".join([c if c.isalnum() or c in (' ', '-', '_') else "_" for c in document_title])
        file_path = os.path.join(save_dir, f'{safe_title}.pdf')
        
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        print(f"Downloaded: {file_path}")
    else:
        print(f"Failed to download document for request {signature_request_id}: {response.text}")

# Function to wait and display a countdown
def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"Waiting... {remaining} s", end="\r")
        time.sleep(1)
    print("Let's continue!")

# Main function to download all documents in batches
def download_all_documents():
    signature_requests = get_all_signature_requests()
    if signature_requests:
        for index, request in enumerate(signature_requests):
            signature_request_id = request.get('signature_request_id')
            document_title = request.get('title', f'document_{signature_request_id}')
            download_document(signature_request_id, document_title)
            
            # Wait for 61 seconds after every 20 requests to avoid API requests rate limits
            if (index + 1) % 20 == 0:
                countdown(61)
    else:
        print("No signature requests found.")

# Run the script
if __name__ == "__main__":
    download_all_documents()
