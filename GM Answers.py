import time
import config
import user
from selenium import webdriver

#xpath = "C:\\Users\\hztzny\\AppData\\Local\\Programs\\Python\\Python36-32\\selenium\\webdriver\\firefox\\geckodriver.exe"
xpath = "C:\\Users\\hztzny\\Desktop\\GSMC\\GeckoDriver\\chromedriver.exe"
#Open up a firefox browser and navigate to webpage
driver = webdriver.Chrome(executable_path=xpath)
#url = "http://econpy.pythonanywhere.com/ex/001.html"
url = "https://gma-authors-na.gm.com/InfoManager/WebObjects/InfoManager.woa?repository=GMA"
driver.get(url)
time.sleep(2)

users = driver.find_element_by_class_name('mainNavItem').click()
#my_email = driver.find_element_by_name("username").send_keys(config.GM_Username)
#my_password = driver.find_element_by_name("password").send_keys(config.GM_Password)
#submit = driver.find_element_by_class_name("submit").click()

info_len = len(user.z_id)
for i in range(info_len):
	add = driver.find_element_by_xpath('/html/body/div/div[3]/table/tbody/tr/td[1]/table/tbody/tr[2]/td/div/div[2]/div/ul/li[1]/div/a[1]').click()

	first_name = driver.find_element_by_name("firstName").send_keys(user.first[i])
	last_name = driver.find_element_by_name("lastName").send_keys(user.last[i])
	login_value = driver.find_element_by_name("loginValue").send_keys(user.z_id[i])
	user_password = driver.find_element_by_name("password").send_keys(user.password)
	user_verify_password = driver.find_element_by_name("retypePassword").send_keys(user.password)
	user_email = driver.find_element_by_name("userEmail").send_keys(user.u_email[i])

	display_name = driver.find_element_by_name('1.48.1.3.2.8.1.1.24').click()
	display_email = driver.find_element_by_name('1.48.1.3.2.8.1.1.27').click()

	default_locale = driver.find_element_by_name('1.48.1.3.2.8.1.1.41.5').send_keys('English United States')
	default_view = driver.find_element_by_name('1.48.1.3.2.8.1.1.43.4').send_keys('OnStar')
	reporting_group = driver.find_element_by_name('1.48.1.3.2.8.1.1.45.3').send_keys(user.reporting_group)

	expand = driver.find_elements_by_xpath('//*[@src="/InfoManager/resources/application/images/plus.gif"]')
	expand[1].click()

	OnStar = list()
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.0.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.1.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.2.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.3.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.4.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.5.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.6.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.7.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.8.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.9.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.10.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.11.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.12.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.13.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.14.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.15.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.16.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.17.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.18.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.19.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.20.0.1.0.6.CVSiteSelectorTreeLine.3.0')
	OnStar.append('1.48.1.3.2.8.1.1.51.1.0.0.4.1.3.0.3.0.1.1.0.21.0.1.0.6.CVSiteSelectorTreeLine.3.0')

	for i in range(22):
		access = driver.find_element_by_name(OnStar[i]).click()

	security_roles = driver.find_elements_by_name('1.48.1.3.2.8.1.1.57.3')

	view_filter = security_roles[0].click()
	onstar_advisor = security_roles[1].click()
	iAuth = security_roles[4].click()
	tools_menu = security_roles[5].click()

	save_user_properties = driver.find_element_by_xpath('//*[@href="javascript:SubmitForm(\'saveChanges\')"]')
	save_user_properties.click()

	done = driver.find_element_by_xpath("//*[@src='/InfoManager/resources/application/images/right.gif']")
	done.click()
