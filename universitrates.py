import requests
import json

result=requests.get("http://universities.hipolabs.com/search?country=latvia")
univerities = json.loads(result.content)#iedod datus json formātā
uni_list=[]
for uni in univerities:
    uni_list.append(uni['name'])
uni_list=list(dict.fromkeys(uni_list))#metode, kas atgriež vārdnīcu ar norādītajām atslēgām un norādīto vērtību
uni_list.sort()#kārtošana
for uni in uni_list:#izvade
    print(uni)
