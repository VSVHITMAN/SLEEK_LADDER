from selenium import webdriver
from bs4 import BeautifulSoup
import pandas
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse", type=int, default= 3)
args=parser.parse_args()

# Set the URL you want to scrape from
url = 'https://www.oyorooms.com/hotels-in-bhopal/?page='
page_num_Max = args.page_num_max

scraped_info_list = []

for page in range(1, page_num_Max):
# Connect to the website using ChromeDriver
    driver = webdriver.Chrome()
    driver.get(url + str(page))

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the data you want to scrape
    all_hotels = soup.find_all('div', class_='hotelCardListing')


    # Extract and print the data    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice__finalPrice"}).text
    # try....except
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            pass 
        
        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})

        amenities_list = []
        try:
            for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
                amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())     
        except AttributeError:
            pass
        hotel_dict["amenities"] = ''.join(amenities_list[:-1])
        
        scraped_info_list.append(hotel_dict)    
#This will create a .csv file to store scraped data
dataFrame = pandas.DataFrame(scraped_info_list)
print("Creating csv")
dataFrame.to_csv("Scraped_Data.csv")

# Close the browser window
driver.quit()
