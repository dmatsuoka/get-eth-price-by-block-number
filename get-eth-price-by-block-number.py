import pandas
import numpy
import requests
import time

def get_eth_price(block_number, dune_api_key):
    headers = {"X-Dune-API-Key": dune_api_key}
    base_url = f"https://api.dune.com/api/v1/query/2424632/execute"
    parameters = {"block_number" : block_number}
    execution_response = requests.request("POST", base_url, headers=headers, json={"query_parameters" : parameters})
    execution_data = execution_response.json()
    execution_id = execution_data["execution_id"]
    results_url = f"https://api.dune.com/api/v1/execution/"+execution_id+"/results?api_key="+dune_api_key
    time.sleep(10)

    for i in range(10, 21, 10): #Try again after 10 secs, then 20 secs
        try:
            results_response = requests.request("GET", results_url)
            results_data = results_response.json()
            price_of_eth = results_data["result"]["rows"][0]["price"]
            print("The price of ETH at block "+str(block_number)+" was "+str(price_of_eth))
            return(price_of_eth)
        except:
            time.sleep(i)

if __name__ == "__main__":
    print('Enter block number:')
    block_number = input()
    print('Enter Dune API key:')
    dune_api_key = input()
    get_eth_price(block_number, dune_api_key)