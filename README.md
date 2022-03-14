# retrieve_akamai_network_lists

Retrieve and save information of network list in your akamai account. Useful when auditing network list, migrating, or managing. Single pane of glass to look for a particular IP or subnet. The following information is saved to excel sheet for each network list.

- Network list name
- Network list description
- Active/Inactive/Modified in production
- Active/Inactive/Modified in staging
- Created by
- Created date
- List of IPs and subnet belonging to network list
- Number of elements in network list

## Requirements and installation

1. Must have an API client, best practice is to give API client read access only to network list. [More info](https://techdocs.akamai.com/developer/docs/authenticate-with-edgegrid)
2. Have API client credentials in `.edgerc` file in current directory.
3. Install dependencies `pip install -r requirements.txt`
4  To run `python3 akamai_network_lists.py`, a filename with the information will be created in current directory `akamai_network_lists.xlsx`.

Author: Walter Carbajal