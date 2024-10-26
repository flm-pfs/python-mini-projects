import requests
from bs4 import BeautifulSoup

def scrape_website(url):
	try:
		response = requests.get(url)  # Send a GET request to the specified URL
		response.raise_for_status()  # Raise an exception if the response status code is not 2xx
	except requests.exceptions.HTTPError as errh:
		print("HTTP Error:", errh)  # Handle HTTP errors
	except requests.exceptions.ConnectionError as errc:
		print("Error Connecting:", errc)  # Handle connection errors
	except requests.exceptions.Timeout as errt:
		print("Timeout Error:", errt)  # Handle timeout errors
	except requests.exceptions.RequestException as err:
		print("Error:", err)  # Handle other request exceptions
	
	soup = BeautifulSoup(response.content, 'html.parser')  # Create a BeautifulSoup object to parse the HTML content
	return soup

def extract_data(soup):
	# Example: Extracting all the links from the webpage
	links = []
	for link in soup.find_all('a'):  # Find all <a> tags in the parsed HTML
		href = link.get('href')  # Get the value of the 'href' attribute
		if href:
			links.append(href)  # Append the link to the list of links
	return links

def main():
	url = input("Enter the URL to scrape: ")  # Prompt the user to enter a URL
	soup = scrape_website(url)  # Scrape the website and get the parsed HTML
	if soup:
		data = extract_data(soup)  # Extract data from the parsed HTML
		print("Extracted Links:")
		for link in data:
			print(link)  # Print each extracted link

if __name__ == "__main__":
	main()  # Call the main function when the script is executed
