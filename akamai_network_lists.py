import requests
from akamai.edgegrid import EdgeGridAuth,EdgeRc
import os
from urllib.parse import urljoin

cur_dir = os.getcwd()
edgerc = EdgeRc(f'{cur_dir}/.edgerc')
section = 'default'

baseurl = 'https://%s' % edgerc.get(section, 'host')
api_endpoint = '/network-list/v2/network-lists?includeElements=false&extended=false'

s = requests.Session()
s.auth = EdgeGridAuth.from_edgerc(edgerc, section)

result = s.get(urljoin(baseurl, api_endpoint))



print(result.text)