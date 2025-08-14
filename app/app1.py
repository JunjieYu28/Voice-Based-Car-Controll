import requests
import BeautifulSoup

def fetch_classification_results(url):
    # Fetch the web page content
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the web page. Status code: {response.status_code}")

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the classification results
    # Note: You need to inspect the web page to find the correct HTML structure
    # For example, if the results are in a table, you might look for <table> elements
    results = []
    for row in soup.find_all('tr'):  # Assuming results are in a table row
        columns = row.find_all('td')
        if len(columns) >= 2:
            category = columns[0].text.strip()
            count = int(columns[1].text.strip())
            if count == 1:
                results.append(category)

    return results

def main():
    url = 'https://studio.edgeimpulse.com/studio/584185/impulse/1/classification?sampleId=1531598925'
    try:
        categories = fetch_classification_results(url)
        output = ', '.join(categories)
        print(output)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
