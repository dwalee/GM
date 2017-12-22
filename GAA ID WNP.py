import time
import config
import user
from selenium import webdriver

#xpath = "C:\\Users\\hztzny\\AppData\\Local\\Programs\\Python\\Python36-32\\selenium\\webdriver\\firefox\\geckodriver.exe"
xpath = "C:\\Users\\hztzny\\Desktop\\GSMC\\GeckoDriver\\chromedriver.exe"
#Open up a Chrome browser and navigate to webpage
driver = webdriver.Chrome(executable_path=xpath)
url = "https://idm-d2wipl.onstar.gm.com:21101/security/logon.jsp"
driver.get(url)

my_email = driver.find_element_by_name("username").send_keys(config.GM_Username)
my_password = driver.find_element_by_name("password").send_keys(config.GCCX_Password)
submit = driver.find_element_by_name("submit").click()
#time.sleep(2)

info_len = len(user.z_id)
for i in range(info_len):
	add_user = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/a[7]').click()
	#time.sleep(2)

	user_id = driver.find_element_by_name("userID")
	user_id.clear()
	user_id.send_keys(user.z_id[i])

	first_name = driver.find_element_by_name("firstName")
	first_name.clear()
	first_name.send_keys(user.first[i])

	last_name = driver.find_element_by_name("lastName")
	last_name.clear()
	last_name.send_keys(user.last[i])
	
	user_email = driver.find_element_by_name("email")
	user_email.clear()
	user_email.send_keys(user.u_email[i])

	role_length = len(user.gaa_role_of_choice)
	for i in range(role_length):
		gaa_roles = driver.find_element_by_xpath('//*[@value="%s"]' % user.gaa_role_of_choice[i])
		gaa_roles.click()

	user_password = driver.find_element_by_name("password").send_keys(user.password)
	user_password_again = driver.find_element_by_name("passwordAgain").send_keys(user.password)

	add = driver.find_element_by_name('submit').click()