from addresscomplete import AddressComplete

# Replace with your own API key
# Get your API key from: https://www.canadapost-postescanada.ca/cpc/en/business/marketing/campaigns/addresscomplete.page
client = AddressComplete("YOUR_API_KEY_HERE")

def find_address():
    results = client.retrieve("CA|CP|ENG|3X1-R2J")
    print(results)
    
    
if __name__ == "__main__":
    find_address()