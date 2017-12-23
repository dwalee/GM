import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver

#Name mass closure list file massclosurelist then this will
#open the file with the mass closure list
workbook = xlrd.open_workbook('massclosurelist.xls')

#Get input from user to find incident
parent = input("Enter the parent incident ")

#Search for incident
#xpath = "C:\\Users\\hztzny\\AppData\\Local\\Programs\\Python\\Python36-32\\selenium\\webdriver\\firefox\\geckodriver.exe"
xpath = "C:\\Users\\hztzny\\Desktop\\GSMC\\GeckoDriver\\chromedriver.exe"
#Open up a Chrome browser and navigate to webpage
driver = webdriver.Chrome(executable_path=xpath)
#Open up ITSM website
url = "https://itsm.gm.com"
driver.get(url)
#Click on Incident Managment tab
incidentMan = driver.find_element_by_class_name("x-panel-header-text").click()
#Click Search Incicdent tab
searchIncident = driver.find_element_by_class_name("x-tree-node-anchor").click()
#Click Incident number edit box
IncidentNumber = browser.find_element_by_id("X11Edit")
#Give input from user to the edit box
emailElem.send_keys(parent)
#Click search to search for parent incident
searchforInc = driver.find_element_by_class_name("x-btn-text").click()
#Click parent incident checkbox for incident
parentCheckBox = driver.find_element_by_class_name("xCheckboxIcon").click()

#Find all incident numbers in the row
incidents = sheet.row(0)
for i in range(incdients):





