import requests
from akamai.edgegrid import EdgeGridAuth,EdgeRc
import os
from urllib.parse import urljoin
import json
from openpyxl import Workbook
from openpyxl.styles import NamedStyle,Font, Alignment, Border,Side


cur_dir = os.getcwd()
edgerc = EdgeRc(f'{cur_dir}/.edgerc')
section = 'default'

baseurl = 'https://%s' % edgerc.get(section, 'host')
api_endpoint = '/network-list/v2/network-lists?includeElements=true&extended=true'

s = requests.Session()
s.auth = EdgeGridAuth.from_edgerc(edgerc, section)

result = s.get(urljoin(baseurl, api_endpoint))

if result.status_code == 200:
    result = result.json()
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Akamai Network Lists'
    header = NamedStyle(name="header")
    header.font = Font(bold=True)
    header.border = Border(bottom=Side(border_style="thin"))
    header.alignment = Alignment(horizontal="center", vertical="center")
    
    count = 0
    for item in result['networkLists']:
        if count == 0:
            sheet.append(['Name','Description','Production','Staging','Created by','Created Time', 'IPs/Subnets','Element count'])
            header_row = sheet[1]
            for cell in header_row:
                cell.style = header
            count += 1
        else:
            if 'description' in item:
                des = item['description']
            else:
                des = ''
            if 'list' in item:
                ips_subnets = ','.join(item['list'])
            else:
                ips_subnets = ''

            sheet.append([
                item['name'],
                des,
                item['productionActivationStatus'],
                item['stagingActivationStatus'],
                item['createdBy'],
                item['createDate'],
                ips_subnets,
                item['elementCount']
            ])
        
    workbook.save(filename=f'{cur_dir}/akamai_network_lists.xlsx')
        
    