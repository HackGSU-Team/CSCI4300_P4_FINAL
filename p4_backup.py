from pprint import pprint
import mysql.connector
import json
def application(env,start_response):
    """main uwsgi application"""
    start_response('200 OK',[('Content-Type','text/html')])
    path = "/home/student/projects/p4/index.html"
    file = open(path)
    query = env['QUERY_STRING']
    if(len(env['PATH_INFO']) > 4):
        if ".css" in env['PATH_INFO']:
            print("loading styles")
            path = "styles.css"
            file = open(path)
            style=file.read()
            return style.encode()
        if "trucks.html" in env['PATH_INFO']:
            path = "/home/student/projects/p4/trucks.html"
            print(path)
            file = open(path)
        if "cars.html" in env['PATH_INFO']:
            path = "/home/student/projects/p4/cars.html"
            file=open(path)
        if "motorcycles.html" in env['PATH_INFO']:
            path="/home/student/projects/p4/motorcycles.html"
            file=open(path)
    if(len(query) > 0):
        print(type(query))
        creds={
            'user':'foo',
            'database':'carshow',
            'password':'Foo_Pass1',
            'auth_plugin':'mysql_native_password'
        }
        cnx = mysql.connector.connect(**creds)
        cursor = cnx.cursor(dictionary=True)
        queryStr = "SELECT * FROM products WHERE productLine=\"{}\"".format(query)
        cursor.execute(queryStr)
        orders =cursor.fetchall()
        print(orders)
        data=[]
        for order in orders:
            prodCode = order['productCode']
            prodName = order['productName']
            prodLine = order['productLine']
            year = order['year']
            make = order['make']
            model = order['model']
            color = order['color']
            quantity = order['quantityInStock']
            image = order['picture']
            cost = order['MSRP']
            row = {}
            row['productCode'] = str(prodCode)
            row['productName'] = str(prodName)
            row['productLine']=str(prodLine)
            row['year']=str(year)
            row['make']=str(make)
            row['model']=str(model)
            row['color']=str(color).capitalize()
            row['quantityInStock'] = str(quantity)
            row['MSRP']=str('${:,.2f}'.format(cost))
            row['picture']=str(image)
            data.append(row)
        print(data)
        data = str(data).replace('\'','\"')
        print data
        return data
    print("After return data");
    html = file.read()
    return html.encode()
 
        
    
