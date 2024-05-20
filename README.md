As part of my internship project, I developed a Python program that provides real-time stock prices from a popular financial news website (Google Finance). The program utilizes web scraping techniques, data extraction, and data storage methods to ensure accurate and structured data is obtained.

Implementation Details

The Python script imports essential tools such as BeautifulSoup, requests, time, pandas, matplotlib.pyplot, and logging to handle errors. A maximum number of retries was set to three, with a delay time of ten seconds between retries. Any errors encountered during the web scraping process are logged in a separate file (errors.log).
The program fetches the most active stocks' data from the financial news website and extracts the symbols, full names, prices, price changes, and percentage changes. The extracted data is organized into a pandas dataframe and cleaned up using pandas methods such as strip(), replace(), and astype().
