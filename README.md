# lisbon-real-estate-data

The python script ```pt_re_spider.py``` is a scraper of Portuguese real estate website [casa.sapo.pt](https://casa.sapo.pt/), implemented in Python with Selenium. 
It extract data and save it to a excel CSV file.  

The scraped data is in Portuguese and contains the following fields:
- Property type
-	Location
-	Area
-	Asking price
-	Special Feature (ex.: pool or garage)
-	URL

Short descriptions were added in the script as comments to increase the code readability.

## Execution

The spider file ```pt_re_spider.py``` scrapes properties in Lisbon in [casa.sapo.pt](https://casa.sapo.pt/) with the given variables ```neighbourhood name``` and ```type```.
When a running the script 2 dialog boxes prompts for input, to answer select a neighbourhood name in the list below and consider the following types of property: ```t0```, ```t1```, ```t2```, ```t3```, ```t4```, ```t5``` e ```t6-ou-superior```.

| List of casasapo.pt Lisbon' neighbourhoods |
| ------------- |
| Ajuda |
| Alcântara |
| Alvalade |
| Areeiro |
| Arroios |
| Avenidas Novas |
| Beato |
| Belém |
| Benfica |
| Campo de Ourique |
| Campolide |
| Carnide |
| Estrela |
| Lumiar |
| Marvila |
| Misericórdia |
| Olivais |
| Parque da Nações |
| Penha de França |
| Santa Clara |
| Santa Maria Maior |
| Santo António |
| São Domingos de Benfica |
| São Vicente |

When running the script the data will be saved in your computer inside a directory ```C:\LxReData``` in csv files.

## Dependencies

Make sure you have the following libraries and modules installed:

-	BeautifulSoup4
-	CSV
-	Time
-	Tkinter
-	RE
-	Selenium
-	Webdriver-manager

Note: You also will need to have Firefox browser installed.
