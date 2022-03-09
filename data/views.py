from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import JsonResponse

import json
import MySQLdb
db = MySQLdb.connect("localhost","root","","django")
# Create your views here.
def home(request):
    return render(request, 'home.html')

def output(request):
    results= request.GET['servers']
    return render(request, 'output.html',{'servers':results}) 

def get_customer(request):
    
    db1=db.cursor()
    db1.execute('SELECT * FROM customer')
    result = db1.fetchall()
    cust_dict=[]

    for i in result:
        temp=dict({})
        temp['id']=i[0]
        temp['name']=i[1]
        cust_dict.append(temp)
    return JsonResponse({'customers':cust_dict})

def get_product(request):
   
        c_id=request.GET['c_id1']
        
        db1=db.cursor()
        db1.execute('SELECT * FROM products where c_id='+c_id)
        result = db1.fetchall()
        prod_dict=[]
        for i in result:
            temp=dict({})
            temp['id']=i[0]
            temp['name']=i[1]
            prod_dict.append(temp)
        return JsonResponse({'products':prod_dict})

def get_server(request):
   
        p_id=request.GET['p_id1']
        
        db1=db.cursor()
        db1.execute('SELECT * FROM server where p_id='+p_id)
        result = db1.fetchall()
        server_dict=[]
        for i in result:
            temp=dict({})
            temp['id']=i[0]
            temp['name']=i[1]
            server_dict.append(temp)
        return JsonResponse({'server':server_dict})
