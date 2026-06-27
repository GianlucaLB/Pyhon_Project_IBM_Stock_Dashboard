
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

# The make_graph function has been modified to use Matplotlib for static graphs. Earlier, it used Plotly to generate interactive dashboards, which caused issues when uploading the notebook in the MARK assignment submission.
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Stock price
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()

## Question 1: Use yfinance to Extract Stock Data

#Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is `TSLA`.

msft = yf.Ticker("TSLA")

#Using the ticker object and the function `history` extract stock information and save it in a dataframe named `tesla_data`. Set the `period` parameter to ` "max" ` so we get information for the maximum amount of time.

tesla_data = msft.history(period="max")

#**Reset the index** using the `reset_index(inplace=True)` function on the tesla_data DataFrame and display the first five rows of the `tesla_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.

tesla_data.reset_index(inplace=True)
tesla_data.head()

## Question 2: Use Webscraping to Extract Tesla Revenue Data

#Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named `html_data`.

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

html_data = requests.get(url)

#Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`.

soup = BeautifulSoup(html_data.text,'html.parser')

#Using `BeautifulSoup` or the `read_html` function extract the table with `Tesla Revenue` and store it into a dataframe named `tesla_revenue`. The dataframe should have columns `Date` and `Revenue`.


dataframe = []

tables_body = soup.find_all("tbody")[1]
table_tr = tables_body.find_all('tr')

for line in table_tr:
    row_data = line.find_all('td')
    data = [d_data.text.strip() for d_data in row_data]
    dataframe.append(data)

tesla_revenue = pd.DataFrame(dataframe,columns=['Date','Revenue'])


#Execute the following line to remove the comma and dollar sign from the `Revenue` column. 

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"",regex=True)

tesla_revenue["Revenue"] = tesla_revenue["Revenue"].astype(int)

#Execute the following lines to remove an null or empty strings in the Revenue column.

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

#Display the last 5 row of the `tesla_revenue` dataframe using the `tail` function. Take a screenshot of the results.

print(tesla_revenue.tail(5))

## Question 3: Use yfinance to Extract Stock Data

#Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is `GME`.

gme = yf.Ticker('GME')

#Using the ticker object and the function `history` extract stock information and save it in a dataframe named `gme_data`. Set the `period` parameter to ` "max" ` so we get information for the maximum amount of time.

gme_data = gme.history(period='max')

#**Reset the index** using the `reset_index(inplace=True)` function on the gme_data DataFrame and display the first five rows of the `gme_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 3 to the results below.

gme_data.reset_index(inplace=True)

gme_data.head(5)

## Question 4: Use Webscraping to Extract GME Revenue Data

#Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named `html_data_2`

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'

#Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`.

page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

#Using `BeautifulSoup` or the `read_html` function extract the table with `GameStop Revenue` and store it into a dataframe named `gme_revenue`. The dataframe should have columns `Date` and `Revenue`. Make sure the comma and dollar sign is removed from the `Revenue` column.


gme_empty = []

tables_body_gme = soup.find_all("tbody")[1]
tables_tr_gme = tables_body_gme.find_all('tr')

for line in tables_tr_gme:
    td_data = line.find_all('td')
    data_gme = [clean_data.text.strip() for clean_data in td_data]
    gme_empty.append(data_gme)

gme_revenue = pd.DataFrame(gme_empty,columns=['Date','Revenue'])

#Remove the comma and dollar sign, an null or empty strings from the Revenue column.

gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"",regex=True).astype(int)


gme_revenue.dropna(inplace=True)

gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

#Display the last five rows of the `gme_revenue` dataframe using the `tail` function. Take a screenshot of the results.

gme_revenue.tail(5)


## Question 5: Plot Tesla Stock Graph

#Use the `make_graph` function to graph the Tesla Stock Data, also provide a title for the graph. Note the graph will only show data upto June 2021.


make_graph(tesla_data, tesla_revenue, 'Tesla')

## Question 6: Plot GameStop Stock Graph

#Use the `make_graph` function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`. Note the graph will only show data upto June 2021.

make_graph(tesla_data, tesla_revenue, 'Tesla')
