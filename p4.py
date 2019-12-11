from pprint import pprint
import mysql.connector
import json

def getCss(file):
        console.log(file)

def getQuery(query):
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
        data = str(data).replace('\'','\"')
        print data
        return data        
def application(env,start_response):
	"""main uwsgi application"""
        html = 'text/html'
        if ".css" in env['PATH_INFO']:
                html = 'text/css'
        if ".js" in env['PATH_INFO']:
                html = 'application/javascript'
        start_response('200 OK',[('Content-Type',html)])
        path = "/home/student/projects/p4/index.html"
        file = open(path)        
        if "trucks.html" in env['PATH_INFO']:
                path = "/home/student/projects/p4/trucks.html"
                print(path)
                file = open(path)
                        
        if "cars.html" in env['PATH_INFO']:
                path = "/home/student/projects/p4/cars.html"
                file = open(path)
                
        if "motorcycles.html" in env['PATH_INFO']:
                path = "/home/student/projects/p4/motorcycles.html"
                file = open(path)
        if "jquery.min.js" in env['PATH_INFO']:
                print(env['PATH_INFO'])
                file=open('/home/student/projects/p4/js/jquery.min.js')
        if "jquery-migrate.min.js" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/js/jquery-migrate.min.js')
        if "bootstrap.min.js" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/js/bootstrap.min.js')
        if "wow.min.js" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/js/wow.min.js')
        if "animate.css" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/animate.css')
        if "animate.min.css" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/animate.min.css')
        if "bootstrap-theme.css" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/bootstrap-theme.css')
        if "bootstrap-theme.css.map" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/bootstrap-theme.css.map')
        if "bootstrap-theme.min.css" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/bootstrap-theme.min.css')
        if "bootstrap.css" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/bootstrap.css')
        if "bootstrap.css.map" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/bootstrap.css.map')
        if "bootstrap.min.css" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/bootstrap.min.css')
        if "font-awesome.css" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/font-awesome.css')
        if "font-awesome.min.css" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/font-awesome.min.css')
        if "style.css" in env['PATH_INFO']:
                file=open('/home/student/projects/p4/css/style.css')

        query = env['QUERY_STRING']
        if len(query) > 0:
                return getQuery(query)	
                print("returned data")
        file = file.read()
        #pprint(env)
        return file.encode()
                                
                        
        
        

  

