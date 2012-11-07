from django.utils import unittest
from django.test.client import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from shortner.views import index,search_assign,goto
from shortner.models import Ushort


class FirstTest(unittest.TestCase):
    
    
    def setUp(self):
        self.factory = RequestFactory()
    
    def setUp(self):
        self.client = Client()
           
    def test_renderbase(self):        
        """this test check which templates is being rendered 
         on the base url
        """ 
        request = Client()
        response = request.get('')
        print response.template.name
        self.assertEqual(response.status_code, 200)
           
    def test_rendersign(self):
        """this test also checks the templates which are 
        being rendered at '/assign/'(url)
        """         
        request = Client()
        response = request.get('/assign/')
        print response.template[0].name
        print response.template[1].name
        self.assertEqual(response.status_code, 200)
    
    def test_validd(self):             
        """this test checks wheather '/admin/' is a valid url """
        request = Client()
        response = request.get('/admin/')
        self.assertEqual(response.status_code, 200) 
   
    
    
    def test_redirects(self):
        """"this test checks valid short url is redirected to
        the desired url and invalid short url is redirected 
        to 404
        """
        newobj = Ushort()
        newobj.longurl = "http://www.yahoo.com/cricketlive"
        newobj.shorturl = "cf1"
        newobj.save()
        response = self.client.get('/cf1/')
        self.assertEqual(response.status_code,302) 
        #now test for invalid url
        response = self.client.get('/fi89o/')
        print response.status_code
        self.assertEqual(response.status_code, 404) 
             
    
   

    def test_yasss(self):
        """test cheks the short url is generated and redirected"""
        driver = webdriver.Firefox()
        driver.implicitly_wait(3000)
        driver.get("http://localhost:8000/")
        driver.find_element_by_name("lurl").clear()
        driver.find_element_by_name("lurl").send_keys("http://www.facebook.com/ysalfy")
        driver.find_element_by_id("short").click()
        #now get the shoturl and find if it is redirected to the desired longurl
        x=driver.find_element_by_id("foo").get_attribute("value")
        driver.get(x)
        self.assertEqual(str(driver.current_url),"http://www.facebook.com/ysalfy")
    if __name__ == '__main__':
        test_yasss(self)
                
        
          
 


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
