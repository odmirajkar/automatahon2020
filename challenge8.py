import unittest
from selenium_support import selenium_support
import time
import sys
import HtmlTestRunner
from os import path
import requests
import json 
import csv

class Test_API(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #time.sleep(80)
        cls.support=selenium_support()
        
        
       
    
    @classmethod
    def tearDownClass(cls):
       pass  
       
    def test_2(self):
        
        response=requests.get("http://34.68.51.180:4000/api/v1/companies")    
        self.assertEqual(response.status_code,200)
        print(response.text)
        
        data=json.loads(response.text)
        names=[]
        for d in data:
            names.append(d['name'])
        
        print(names)
        with open('data.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.assertTrue(row['name'] in names)

            
    
    def test_1(self):
        
        with open('data.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_dict={"name": row['name'],"tel": row['phone'],"email":row['email']}
                response=requests.post("http://34.68.51.180:4000/api/v1/companies",json=user_dict)
                print(response.status_code)
                self.assertEqual(response.status_code,201)  

    def test_3(self):
        with open('data.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_dict={"name": row['name'],"tel": row['phone'],"email":row['email']}
                response=requests.delete("http://34.68.51.180:4000/api/v1/companies/{}".format(user_dict['name']))
                print(response.status_code)
                self.assertEqual(response.status_code,204)  

    def test_4(self):
        
        response=requests.get("http://34.68.51.180:4000/api/v1/companies")    
        self.assertEqual(response.status_code,200)
        print(response.text)
        
        data=json.loads(response.text)
        names=[]
        for d in data:
            names.append(d['name'])
        
        print(names)
        with open('data.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.assertFalse(row['name'] in names)

    def test_5(self):
        
        response=requests.delete("http://34.68.51.180:4000/api/v1/companies/{}".format('does not exrist'))
        print(response.status_code)
        print(response.text)
        self.assertFalse(response.status_code,204)              
        
        
def main(out = sys.stderr, verbosity = 2): 
    loader = unittest.TestLoader() 
    #import os

    #module=os.path.splitext(os.path.basename(__file__))[0]
    #suite = loader.loadTestsFromName(module+'.TestCases.test_b')
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    print(suite)
    #unittest.TextTestRunner(out, verbosity = verbosity).run(suite) 
    #output_file = open("HTML_Test_Runner_ReportTest.txt", "w")
    report_filder='./report'

    html_runner = HtmlTestRunner.HTMLTestRunner(
        #    stream=output_file,
            report_title='HTML Reporting ',
            descriptions='HTML Reporting ',
            output=report_filder
        )
    #unittest.TestRunner()
    html_runner.run(suite)


if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store', dest='config_value',help='Store a simple value')
    results = parser.parse_args()
    print ('config_value     =', results.config_value)
    Test_Zypher.config=results.config_value
    #unittest.main(verbosity=2)
    """
    
    #time.sleep(30)
    main()
    #with open('testing.out', 'w') as f: 
    #    main(f)
