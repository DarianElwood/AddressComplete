from AddressComplete import AddressComplete

client = AddressComplete.AddressComplete("HG31-BT62-ZX13-EK35")

def retrieve_find():
    results = client.retrieve("CA|CP|B|1982312")
    print(results)
    
    
if __name__ == "__main__":
    retrieve_find()