import requests

class JSONPlaceHolder:

    #create a method to access data from the url
    def __init__(self,url):
        self.url = url
    
    #create a method to get check server status 
    def request(self):
        self.response = requests.get(self.url)
        if self.server_status() == 200:
            return self.response.json()

    #create a method to get status code 
    def server_status(self):
        return self.response.status_code
    
    #create a method to access the country and its currency from the json data and create it as a list
    def display_ccc(self):
        c_data = []
        jsonResult = self.request()
        for entry in jsonResult:
            country_name = entry["name"]["common"]
            currency_name = entry["currencies"]
            currency_symbol = list(entry["currencies"].values())[0]["symbol"]
            c_entry = {
                "country_name": country_name,
                "currency_name": currency_name,
                "currency_symbol": currency_symbol,
            }
            c_data.append(c_entry)
        return c_data   
    
    #create a method to display the
    def dollar(self):
        dollar_data = []
        jsonResult =self.request()
        self.currencies = jsonResult.get("currencies", {})
        for entry in jsonResult:
            if entry == "dollar":
                dollar_data.append(entry["name"]["common"])
        return dollar_data

    def euro(self):
        euro_data = []
        jsonResult =self.request()
        self.currencies = jsonResult.get("currencies", {})
        for entry in jsonResult:
            if entry == "euro":
                euro_data.append(entry["name"]["common"])
        return euro_data

url = "https://restcountries.com/v3.1/all"
obj = JSONPlaceHolder(url)
countries =obj.display_ccc()
dollars = obj.dollar()
euros = obj.euro()
print(countries)


