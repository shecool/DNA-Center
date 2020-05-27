import requests
import json
import csv

################ LOGIN ######################
# This uses the DevNet Sandbox - Replace with appropriate credentials
# Use env file for more security :)
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

user = "devnetuser"
pw = "Cisco123!"

response = requests.post(url, auth=(user, pw)).json()
token = response["Token"]

############ GET Site HEALTH STATS ################

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/site-health"

querystring = {"timestamp": ""}

headers = {
    "x-auth-token": token,
    "Accept": "*/*",
}

response = requests.get(url, headers=headers, params=querystring).json()


sites = response["response"]

# Create a new CSV to export the site data to
with open("Site-Clients.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["Site", "Wireless Clients", "Wired Clients", "Total Number of Clients"]
    )

    for site in sites:
        # Parse clients per site
        # Print to cmdline
        # Export to a csv as well.
        print(f"Site: {site['siteName']}")
        print(f"Wireless Clients: {site['numberOfWirelessClients']}")
        print(f"Wireless Clients: {site['numberOfWiredClients']}")
        print(f"Wireless Clients: {site['numberOfClients']}")
        print("-----------------------------------")
        writer.writerow(
            [
                site["siteName"],
                site["numberOfWirelessClients"],
                site["numberOfWiredClients"],
                site["numberOfClients"],
            ]
        )
