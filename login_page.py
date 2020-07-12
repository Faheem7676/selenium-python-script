from selenium.webdriver.common.by import By
#from selenium_driver import SeleniumDriver
import custom_logger as cl
import logging
from basepage import BasePage



class LoginPage(BasePage):

	log = cl.customLogger(logging.DEBUG)
	#log = cl.customLogger(logging.DEBUG)

	def __init__(self,driver):
		super().__init__(driver)
		self.driver=driver

	# locators

	_login_link="guest-login-button"
	_email_field="id_username"
	_password_field="id_password"
	_loginbutton="login_button"

	

	def clickLoginLink(self):
		self.elementClick(self._login_link,locatorType="id")


	def enterEmail(self,email):
		self.sendKeys(email,self._email_field)

	def enterPassword(self,password):
		self.sendKeys(password,self._password_field)

	def clickLoginButton(self):
		self.elementClick(self._loginbutton,locatorType="id")
		print("summaya")






	def login(self,email="",password=""):

		self.clickLoginLink()
		self.enterEmail(email)
		self.enterPassword(password)
		self.clickLoginButton()

		

	def verifyLoginSuccessfull(self):
		result = self.isElementPresent("//*[@id='user-profile-pic']",locatorType="xpath")
		#userIcon=driver.find_element(By.ID,"user-profile-pic")
		return result


	def verifyLoginFailed(self):
		result =self.isElementPresent("//*[@id='login-form']/div[1]/p",locatorType="xpath")
		return result



	def verifyAfterlogin_Recent_From_My_places(self):
		result = self.isElementPresent("//*[@id='recentNewsCity']/div/h5/text()",locatorType='xpath')
		return result


	def verifyLoginTitle(self):
		return self.verifyPageTitle("NewsGallery | People's Own Media")


	def verifybeforeLogin(self):
		return self.isElementPresent("//*[@id='wrapper']/div[3]/div/div[1]/div/div[1]/div/h3",locatorType="xpath")

	

