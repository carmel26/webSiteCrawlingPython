# # first version
# # import requests
# # from bs4 import BeautifulSoup
# # from urllib.parse import urljoin

# # # URL of the website to crawl
# # base_url = "https://nm-aist.ac.tz"

# # # Initialize a list to store the crawled documents
# # document_corpus = []

# # # Function to crawl a webpage and extract relevant content
# # def crawl_website():
# #     # Create a queue to store URLs to be crawled
# #     url_queue = [base_url]

# #     while url_queue:
# #         url = url_queue.pop(0)  # Get the next URL from the queue

# #         try:
# #             response = requests.get(url)
# #             soup = BeautifulSoup(response.content, 'html.parser')

# #             # Extract the content you want from the webpage
# #             # For example, if you want to extract the text from all paragraphs (p) on the page:
# #             paragraphs = soup.find_all('p')
# #             content = ' '.join([p.get_text() for p in paragraphs])

# #             # Store the extracted content in the document corpus
# #             document_corpus.append(content)

# #             # Extract links from the webpage and add them to the queue
# #             links = soup.find_all('a')
# #             for link in links:
# #                 href = link.get('href')
# #                 if href:
# #                     absolute_url = urljoin(url, href)
# #                     url_queue.append(absolute_url)

# #         except requests.exceptions.RequestException as e:
# #             print("Error: ", e)

# # # Start crawling the website
# # crawl_website()

# # # Print the crawled documents
# # for i, doc in enumerate(document_corpus):
# #     print("Document", i+1, ":", doc)


# second version
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# import time

# # URL of the website to crawl
# base_url = "https://nm-aist.ac.tz"

# # Initialize a list to store the crawled documents
# document_corpus = []

# # Function to crawl a webpage and extract relevant content
# def crawl_website():
#     # Create a queue to store URLs to be crawled
#     url_queue = [base_url]

#     while url_queue:
#         url = url_queue.pop(0)  # Get the next URL from the queue

#         try:
#             response = requests.get(url)
#             response.raise_for_status()  # Raise an exception if the response status code is an error

#             soup = BeautifulSoup(response.content, 'html.parser')

#             # Extract the content you want from the webpage
#             # For example, if you want to extract the text from all paragraphs (p) on the page:
#             paragraphs = soup.find_all('p')
#             content = ' '.join([p.get_text() for p in paragraphs])

#             # Store the extracted content in the document corpus
#             document_corpus.append(content)

#             # Extract links from the webpage and add them to the queue
#             links = soup.find_all('a')
#             for link in links:
#                 href = link.get('href')
#                 if href:
#                     absolute_url = urljoin(url, href)
#                     url_queue.append(absolute_url)

#         except requests.exceptions.RequestException as e:
#             print("Error: ", e)

#             # Retry the request after a delay
#             time.sleep(1)  # Adjust the delay as needed
#             url_queue.append(url)  # Add the URL back to the queue for retry

# # Start crawling the website
# crawl_website()

# # Print the crawled documents
# for i, doc in enumerate(document_corpus):
#     print("Document", i+1, ":", doc)


# third version

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# URL of the website to crawl
base_url = "https://nm-aist.ac.tz"

# Initialize a list to store the crawled documents
document_corpus = []

# Maintain a set of visited URLs to avoid revisiting the same page
visited_urls = set()

# Function to crawl a webpage and extract relevant content
def crawl_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the content you want from the webpage
        # For example, if you want to extract the text from all paragraphs (p) on the page:
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])

        # Store the extracted content in the document corpus
        document_corpus.append(content)

        # Extract links from the webpage and add them to the queue
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href:
                absolute_url = urljoin(url, href)
                if absolute_url not in visited_urls:
                    visited_urls.add(absolute_url)
                    crawl_website(absolute_url)

    except requests.exceptions.RequestException as e:
        print("Error: ", e)

# Start crawling the website
start_time = time.time()
crawl_website(base_url)
end_time = time.time()

# Print the elapsed time
print("Crawling completed in", end_time - start_time, "seconds.")

# Print the crawled documents
for i, doc in enumerate(document_corpus):
    print("Document", i+1, ":", doc)