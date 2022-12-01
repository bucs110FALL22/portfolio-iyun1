import json
import requests
  
def holiday_result(input_year = 0, country_id = None):  
  response = requests.get("https://date.nager.at/api/v3/PublicHolidays/",input_year,"/",country_id).json()
  response.load(response)

def main():
  input_year = input("Please enter a year: ")
  input_country = input("Please enter the country code of a country to determine its holidays of the selected year: ")  
  holiday_get = holiday_result(input_year, input_country)
  print(holiday_get)

main()

# response = requests.get("https://date.nager.at/api/v3/PublicHolidays/1976/143").json()
# print(response.get("name"))