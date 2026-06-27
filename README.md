# **IBM Stock Dashboard project**


In this project, my first task was to extract Tesla and GameStop financial data using the yfinance Python library. The second task was to use web scraping to extract Tesla and GameStop revenue data using BeautifulSoup.

After extracting the data using BeautifulSoup, I created an empty DataFrame to store all the information, using a for loop to iterate through the HTML table and populate the DataFrame.

I also had to clean the Revenue column by removing commas and dollar signs, and filter out null or empty strings using dropna and tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""].

When all the data was ready, I used a function provided by IBM to visualize it using Matplotlib.

Python libraries used:

yfinance — for extracting financial data

pandas — for data cleaning and DataFrame manipulation

requests — for accessing the webpage

BeautifulSoup — for parsing the HTML and extracting the relevant tables
