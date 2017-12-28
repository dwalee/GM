import xlrd
from bs4 import BeautifulSoup
from selenium import webdriver

#Name mass closure list file massclosurelist then this will
#open the file with the mass closure list


#Get input from user to find incident
inputParent = input("Enter Parent Incident")
inputAssignGroup = input("Enter the Assignment group you need ")
inputResolution = input("Enter the Resolution")
inputAssignee = input("Enter your GMID")


workbook = xlrd.open_workbook("massclosurelist.xlsx")

def searchTab():
    #Search for incident
    #xpath = "C:\\Users\\hztzny\\AppData\\Local\\Programs\\Python\\Python36-32\\selenium\\webdriver\\firefox\\geckodriver.exe"
    xpath = "C:\\Users\\vzkbv1\\Desktop\\GSMC\\GeckoDriver\\chromedriver.exe"
    #Open up a Chrome browser and navigate to webpage
    driver = webdriver.Chrome(executable_path=xpath)
    #Open up ITSM website
    url = "https://itsm.gm.com"
    driver.get(url)

    #Click on Incident Managment tab
    incidentMan = driver.find_element_by_xpath("ext-gen-top307")
    incidentMan.click()

    #Click Search Incicdent tab
    searchIncident = driver.find_element_by_xpath("//ul[@class='x-tree-node']")
    searchIncident.find_element_by_xpath(".//a[@tabname='ext-gen-top332']").click()


#Click Incident number edit box
incidentNumber = driver.find_element_by_id("X11Edit")
incidentNumber.send_keys(inputParent)

def fillForm():
    #Give input from user to the edit box
    incidentNumber = driver.find_element_by_id(x11)
    incidentNumber.send_keys(inputParent)

    #Click search to search for parent incident
    searchforInc = driver.find_element_by_id("ext-gen-top570")
    searchIncident.click()

def linkTicket():
    #Click parent incident checkbox for incident
    parentCheckBox = driver.find_elements_by_xpath("//input[@name='instance/master.incident' and @value ='true']")
    parentCheckBox.click()
    
    #Write Assignment Group in edit box
    assignmentG = driver.find_element_by_id("x95")
    assignmentG.send_keys(inputAssignGroup)

    #Write your GMID in Assignee edit box
    assignee = driver.find_element_by_class_id("x99")
    assignee.send_keys(inputAssignee)

    #Keyword fill out
    keyword1.driver.find_element_by_class_id("29")
    keyword1.send_keys("Itoc-Resolved")

    #Save and Exit
    save = driver.find_element_by_id("ext-gen-listdetail-1-155")
    save.click()

       

fillForm()
linkTicket()
#Find all incident numbers in the row
i = 0
while i <= len(sheet.col(0)):
    if col != "":

        #Click search to search for parent incident
        searchforInc = driver.find_element_by_id("ext-gen-top570")
        searchIncident.click()
        
        #Give input from user to the edit box
        incidentNumber = driver.find_element_by_id("X11Edit")
        incidentNumber.send_keys(sheet.cell(i,0).value)

        #Link incident to parent ticket
        linkToParent = driver.find_element_by_class_id("X37")
        linkToParent.send_keys(inputParent)

        #Save and Exit
        save = driver.find_element_by_class_id("ext-gen-listdetail-1-155")
        save.click()
    else:
        break
        




