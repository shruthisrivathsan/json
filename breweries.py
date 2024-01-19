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
    def get_breweries_by_states(states):
        breweries_list = []
        breweries_count = []
        for state in states:
            jsonResponse = requests.get()
            params = {"by_state": state} 
        return breweries_list
    
    def get_breweries_count(states):
        breweries_count = []
        for state in states:
            jsonResponse = requests.get()
            params = {"by_state": state} 
        return breweries_count

    if __name__ == "__main__":
        states_to_search = ["Alaska", "Maine", "New York"]
        breweries_data = get_breweries_by_states(states_to_search)
        
        for state, count in breweries_count.items():
            print(f"Number of breweries: {count}")

url = "https://www.openbrewerydb.org/"
obj = JSONPlaceHolder(url)
breweries = obj.get_breweries_by_states()
count = obj.get_breweries_count()

