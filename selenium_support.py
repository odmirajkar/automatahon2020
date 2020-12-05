"""
class to support selenium projects accepting the command line parameter
@Auther - OnkarM
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.remote_connection import RemoteConnection
import argparse
from os import environ
import sys
import os



class selenium_support():
    """
    Main class support selenium

    """
    def __init__(self):
        """
        Constructor for class. 
        add required arguments 
        """
        self.parser = argparse.ArgumentParser(description='CAP Selenium support library')
        self.parser.add_argument('--browser', type=str,default='Chrome', help='Browser valid values [Chrome,Firefox,Opera,Default is Chrome]')
        self.parser.add_argument('--driverpath', type=str,default='Syspath',required=False, help='Optional parameter,Driver path for browser, default is system path, if using remote driver mention remote driver path')
        self.parser.add_argument('--binarypath', type=str,default='Syspath', required=False, help='Optional parameter for browser binary path')
        self.parser.add_argument('--remote', type=bool,default=False, required=False,  help='Boolean parameter, optional parameter, use when for use of remote driver ')
       

    def init(self):
        """
        initialize browser & driver
        """
        args=self.parser.parse_args()
        print(args)
        self.is_lambda=False
        try:
            os.mkdir('./screenshot')
        except:
            pass
        browser = args.browser
        if browser.lower() == 'chrome':
            chrome_options = Options()
            if args.binarypath != 'Syspath':
                chrome_options.binary_location = args.binarypath

            if args.driverpath != 'Syspath' and args.remote == False:
                driver_path=args.driverpath
                print(driver_path)
                self.driver = webdriver.Chrome(executable_path=driver_path,chrome_options=chrome_options)
            elif args.remote:
                driver_path=args.driverpath
                capabilities = {
                'platform': 'ANY',
                'browserName': 'chrome',
                'version': '',
                'window-size':'Maximized'
                }
                self.driver =webdriver.Remote(driver_path,desired_capabilities=capabilities)    
            else:
                self.driver=webdriver.Chrome(chrome_options=chrome_options)
                
        elif browser.lower() == 'firefox':
            options = Options()
            if args.binarypath != 'Syspath':
                options.binary_location = args.binarypath

            if args.driverpath != 'Syspath' and args.remote == False:
                driver_path=args.driverpath
                self.driver = webdriver.Firefox(executable_path=driver_path,options=options)
            elif args.remote:
                driver_path=args.driverpath
                capabilities = {
                'platform': 'ANY',
                'browserName': 'Firefox',
                'version': '',
                'window-size':'Maximized'
                }
                self.driver =webdriver.Remote(driver_path,desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)    
            else:
                self.driver=webdriver.Firefox(options=options)
                
        elif browser.lower() == 'opera':
            chrome_options = Options()
            if args.binarypath != 'Syspath':
                chrome_options.binary_location = args.binarypath

            if args.driverpath != 'Syspath' and args.remote == False:
                driver_path=args.driverpath
                self.driver = webdriver.Chrome(executable_path=driver_path,chrome_options=chrome_options)
            elif args.remote:
                driver_path=args.driverpath
                capabilities = {
                'platform': 'ANY',
                'browserName': 'Opera',
                'version': '',
                'window-size':'Maximized'
                }
                self.driver =webdriver.Remote(driver_path,desired_capabilities=webdriver.DesiredCapabilities.OPERA)
            else:
                self.driver=webdriver.Chrome(chrome_options=chrome_options) 
        


    def take_screenshot(self,name,path='./screenshot'):
        """
        function to take SS

        """
        if self.is_lambda  :
            filename ='/tmp/screenshot' +"/"+name
        else:
            filename=path+'/'+name
        self.driver.save_screenshot(filename)
