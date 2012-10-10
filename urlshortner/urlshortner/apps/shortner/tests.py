from django.utils import unittest
from django.test.client import Client
from shortner.views import index,search_assign,goto
from shortner.models import Ushort


class FirstTest(unittest.TestCase):
    
    
    def setUp(self):
        self.factory = RequestFactory()
    
    def setUp(self):
        self.client = Client()

       
    def test_detail1(self):             #test to check which template is being rendered
        res = Client()
        p = res.get('')
        print p.template.name
        self.assertEqual(p.status_code, 200)
           
    def test_detail2(self):
        res = Client()
        p = res.get('/assign/')
        print p.template[0].name
        print p.template[1].name
        self.assertEqual(p.status_code, 200)
    
    def test_detail3(self):             #test to check '/admin/' is valid url
        res = Client()
        p = res.get('/admin/')
        self.assertEqual(p.status_code, 200) 
   
    
    
    def test_detail4(self):       #test to check that key is redirected to desired url & wrong key is redirected to 404
        x = Ushort()
        x.longurl = "http://www.yahoo.com/cricketlive"
        x.shorturl = "cf1"
        x.save()
        p = self.client.get('/cf1/')
        self.assertEqual(p.status_code,302) 
        p = self.client.get('/fi89o/')
        print p.status_code
        self.assertEqual(p.status_code, 404) 
             
    
        
        
          
 


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
