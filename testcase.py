import unittest
from selenium_support import selenium_support
import time
import sys
import HtmlTestRunner
from os import path

class Test_ATT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #time.sleep(80)
        cls.support=selenium_support()
        retry =5
        while retry:
            
            
            #url="https://automatahon20.cpsatexam.org/challenge1/"
            url="https://automatahon20b1.cpsatexam.org/challenge1/"
            try:
                cls.support.init()
                if cls.support.driver:
                    cls.support.driver.get(url)
                    #cls.support.take_screenshot('att.png')
                    print(cls.support.driver.title)
                    break
            except:    
                retry=retry -1
                print("connection failed retry pending ",retry)
                time.sleep(10) 
        if retry == 0:
            cls.assertEqual(1,2,"Failed to connect to browser")
        
    
    def test_one_2(self):
        try:
            self.support.driver.find_element_by_xpath("//i[@class='eicon-close']").click()
        except:
            pass
        element = self.support.driver.find_element_by_xpath("//div[@class='eael-progressbar-title' and contains(text() ,'Cognizant')]/../div[@class='eael-progressbar eael-progressbar-line eael-progressbar-line-stripe eael-progressbar-line-animate-rtl']") # you can use ANY way to locate element
        coordinates = element.location_once_scrolled_into_view # returns dict of X, Y coordinates
        self.support.driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        print(element.get_attribute("data-count"))
        percentage=element.get_attribute("data-count")
        self.assertEqual(element.get_attribute("data-count"),"90")
        try:
            self.support.driver.get("https://agiletestingalliance-new-staging.dxpsites.net/leaderboard/")
            self.support.driver.find_element_by_xpath("//i[@class='eicon-close']").click()
        except:
            pass
        element=self.support.driver.find_element_by_xpath("//td[text()='Cognizant Technology Solutions']/../td[3]")
        elements=self.support.driver.find_elements_by_xpath("//table[@class='ea-advanced-data-table ea-advanced-data-table-tablepress ea-advanced-data-table-91859b1']//tbody/tr")
        total=0
        print(len(elements))
        for ind,e in enumerate(elements):
            total=total+int(e.find_element_by_xpath('../tr[{}]//td[3]'.format(ind+1)).text)
            print(int(e.find_element_by_xpath('../tr[{}]//td[3]'.format(ind+1)).text))
        print(total)
        self.assertEqual(percentage,int(element.text)/total*100)


    
    
    def test_one_1(self):
        try:
            url="https://automatahon20b1.cpsatexam.org/challenge1/"
            cls.support.driver.get(url)
            self.support.driver.find_element_by_xpath("//i[@class='eicon-close']").click()
            time.sleep(10)
            self.support.driver.find_element_by_xpath("//div[@class='eael-sticky-video-player2 out']")    
        except:
            self.assertEqual("1","2","Vdio not found")    
    

    """
    def test_one_3(self):
        self.support.driver.get("https://agiletestingalliance-new-staging.dxpsites.net/")
        self.support.driver.find_element_by_xpath("//i[@class='eicon-close']").click()
        element=self.support.driver.find_element_by_xpath("//h2[text()='Why #ATAGTR2020']/../../..//strong")
        data=element.text
        print(data)
        #The program has 4 Keynotes, 2 Panel discussions, 7 Hands on Labs, 26 Interactive session, 14 Lightning sessions
        data_values=data.split(" ")
        value_dict={}
        for ind,data in enumerate(data_values):
            if "Lightning" in data:
                value_dict['Lightning Talks'] = data[ind-1]
            elif "Interactive" in data:
                value_dict['Interactive Sessions'] = data[ind-1]
            elif "Hands" in data:
                value_dict['Labs/Workshop'] = data[ind-1]
            elif "Panel" in data:
                value_dict['Panel'] = data[ind-1]     
            elif "Kaynotes" in data:
                value_dict['Kaynotes']=data[ind -1]

        categories=['Interactive Sessions','Lightning Talks','Labs/Workshop','Panel Discussion','Kaynotes']
        for category in categories:
            self.support.driver.get("https://automatahon20.cpsatexam.org/challenge1/")
            element=self.support.driver.find_element_by_xpath("//div[@class='elementor-counter-title' and contains(text(),'{}')]/..//span[@class='elementor-counter-number']".format(category))
            value=element.get_attribute('data-to-value')
            print(value)
            self.assertEqual(value_dict[category],value)

            #https://agiletestingalliance-new-staging.dxpsites.net/
            #The program has 4 Keynotes, 2 Panel discussions, 7 Hands on Labs, 26 Interactive session, 14 Lightning sessions.

            break
            
            
    """        
   
    
    
    @classmethod
    def tearDownClass(cls):
        cls.support.driver.quit()    
       
    def test_api(self):
        import requests
        response=requests.get("http://ergast.com/api/f1/2017/circuits.json")    
        self.assertEqual(response.status_code,200)
        print(response.json())
    

        

        
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
