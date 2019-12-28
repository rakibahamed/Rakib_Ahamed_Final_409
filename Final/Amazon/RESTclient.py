
import requests
import json



urlC = 'http://127.0.0.1:8000/api/List_customers/'
urlA = 'http://127.0.0.1:8000/api/List_addresses/'
urlAC = 'http://127.0.0.1:8000/api/List_orders/'
urlT = 'http://127.0.0.1:8000/api/List_products/'


def getCustomers():
    r = requests.get(urlC).json()
    print(r)
    jsondata = r
    print(jsondata[0])
    firstCustomer = jsondata[0]
    return firstCustomer


def createCustomer():
    rakib = {'first_name':'Rakib', 'last_name':'Ahamed', 'prime_customer':'Y'}
    r = requests.post(urlC, json=rakib).json()

def createAddress(customer):
    cid = customer['id']
    address = {'fk': cid, 'street': '1017 ape street', 'city':'fairfax', 'state':'VA', 'zip':'20170'}
    r = requests.post(urlA, json=address).json()
    print(r)
    return r

def createOrder(customer):
    cid = customer['id']
    account = {'fk': cid ,'total': 999,'payment_type':'C','exp_date': '2019-12-01','account_number': '123456790'}
    r = requests.post(urlAC, json= account).json()
    print(r)
    return r

def updateCustomer(customer):
    cid = customer['id']
    urlCU = urlC + str(cid) + '/'
    CU = {'last_name':'sir Ahamed'}
    customer.update(CU)
    print(urlCU)
    r = requests.put(urlCU, data=customer).json()
    print(r)

def updateAddress(address):
    cid = address['id']
    urlAU = urlA + str(cid) + '/'
    aU = {'street':'54567 Wall street'}
    address.update(aU)
    print(urlAU)
    r = requests.put(urlAU, data=address).json()
    print(r)

def updateOrder(order):
    print(order)
    cid = order['order_number']
    urlACU = urlAC + str(cid) + '/'
    aU = {'total':1000000}
    order.update(aU)
    print(urlACU)
    r = requests.put(urlACU, data=order).json()
    print(r)

def createProduct(account):
    cid = account['order_number']
    transaction = {'fk': cid, 'description': 'Macbook', 'quantity': 1}
    r = requests.post(urlT, json=transaction).json()
    print(r)
    transaction = {'fk': cid, 'description': 'Popeyes', 'quantity': 1}
    r = requests.post(urlT, json=transaction).json()
    print(r)

def getTransactions():
    r = requests.get(urlT).json()
    print(r)

createCustomer()
customer = getCustomers()
address = createAddress(customer)
order = createOrder(customer)
updateCustomer(customer)
updateAddress(address)
updateOrder(order)
createProduct(order)
getTransactions()


