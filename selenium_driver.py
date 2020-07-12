from selenium.webdriver.common.by import By 
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import*
import custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

	log = cl.customLogger(logging.DEBUG)

	def __init__(self,driver):
		self.driver = driver

	def screenShot(self,resultMessage):
		"""
		Takes screenshot of the current open web page
		"""
		fileName=resultMessage+ "." +str(round(time.time() * 2000)) + ".png"
		screenshotDirectory="../screenshots/"
		relativeFileName=screenshotDirectory+ fileName
		currentDirectory=os.path.dirname(__file__)
		destinationFile=os.path.join(currentDirectory,relativeFileName)
		destinationDirectory=os.path.join(currentDirectory,screenshotDirectory)

		try:
			if not os.path.exists(destinationDirectory):
				os.makedirs(destinationDirectory)
			self.driver.save_screenshot(destinationFile)
			self.log.info("Screenshot save to directory: " + destinationFile)
		except:
			self.log.error("### Exception Occurred")
			print_stack()

	def getTitle(self):
		return self.driver.title

	def getByType(self,locatorType):
		locatorType=locatorType.lower()
		if locatorType== "id":
			return By.ID

		elif locatorType== "name":
			return By.Name 

		elif locatorType=="xpath":
			return By.XPATH 

		elif locatorType=="css":
			return By.CSS_SELECTOR 

		elif locatorType=="class":
			return By.CLASS_NAME 

		elif locatorType== "link":
			return By.LINK_TEXT

		else:
			self.log.info("locator type " + locatorType + "not correct/supported")

		return False

	def getElement(self, locator,locatorType="id"):
		element=None
		try:
			locatorType=locatorType.lower()
			byType=self.getByType(locatorType)
			element=self.driver.find_element(byType,locator)
			self.log.info("Element Found with locator: " + locator + "and locatorType: " + locatorType)
		except:
			self.log.info("Element not found with locator: " +locator + "and locatorType: " + locatorType)
		return element

	def getElementList(self,locator,locatorType="id"):
		"""
		NEW METHOD
		Get list of elements
		"""
		element=None
		try:
			locatorType=locatorType.lower()
			byType=self.getByType(locatorType)
			element=self.driver.find_elements(byType,locator)
			self.log.info("Element list found with locator: " + locator +"and locatorType:"+locatorType)
		except:
			self.log.info("Element list not found with locator : " +locator +"and locatorType:" +locatorType)

		return element

	def elementClick(self,locator,locatorType="id",element=None):
		"""
		Click on an element -> MODIFIED
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator: # This means if locator is not empty
			    element=self.getElement(locator,locatorType)
			element.click()
			self.log.info("clicked on element with locator : " +locator+ "locatorType :" +locatorType)
		except:
			self.log.info("can not click on the element with locator: " +locator+ "locatorType:" +locatorType)
			print_stack()

	def sendKeys(self, data,locator,locatorType="id",element=None):
		"""
		Send keys to an element -> Modified
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator: #This means if locator is not empty
			    element=self.getElement(locator,locatorType)
			element.send_keys(data)
			self.log.info("Sent data on element with locator: " +locator+"locatorType:" +locatorType)
		except:
			self.log.info("cannot sent data on the element with locator: " +locator+"locatorType:" +locatorType)
			print_stack()


	def getText(self,locator="",locatorType="id",element=None,info=""):
		"""
		NEW METHOD
		Get "Text" on an element
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator: # This means if locator is not empty
			    self.log.debug("In locator condition")
			    element=self.getElement(locator,locatorType)
			self.log.debug("Before finding text")
			text=element.text
			self.log.debug("After finding element,size is : " +str(len(text)))
			if len(text)==0:
				text=element.get_attribute("innerText")
			if len(text)!=0:
				self.log.info("Getting text on element :: " + info)
				self.log.info("The text is :: '" +text+ "'")
				text=text.strip()
		except:
				self.log.error("Failed to get text on element" +info)
				print_stack()
				text=None
		return text


		

	def isElementPresent(self,locator="",locatorType="id",element=None):
		"""
		Check if element is present -> MODIFIED
		Either provide element or a combination of locator and locatorType
		"""
		try:
			if locator : # This means if locator is not empty
			    element=self.getElement(locator,locatorType)
			if element is not None:
				self.log.info("Element present with locator: " +locator + "locatorType: " +locatorType)
				return True

			else:
				self.log.info("Element not present with locator: " +locator+ "locatorType:" +locatorType)
				return False

		except:
			self.log.info("Element not found")
			return False

	def isElementDisplayed(self,locator="",locatorType="id",element=None):
		"""
		New Method
		Check if element is displyed
		Either provide element or a combination of locator and locatorType
		"""
		isDisplayed=False
		try:
			if locator: # This means if locator is not empty
			    element=self.getElement(locator,locatorType)
			if element is not None:
				isDisplayed=element.is_displayed()
				self.log.info("Element is displyed with locator: " +locator + "locatorType: " + locatorType)
			else:
				self.log.info("Element is not displyed with locator: " +locator +"locatorType:"+locatorType)
			return isDisplayed
		except:
			print("Element not found")
			return False

	def elementPresenceCheck(self,locator,byType):
		"""
		Check if element is present
		"""
		try:
			elementList=self.driver.find_elements(byType,locator)
			if len(elementList)>0:
				self.log.info("Element present with locator: "+locator +"locatorType: " +str(byType))
				return True

			else:
				self.log.info("Element is not present with locator: " +locator+ "locatorType: " +str(byType))
				return False

		except:
			self.log.info("Element not found")
			return False


	def waitForElement(self,locator,locatorType="id",timout=10,pollFrequency=0.5):
		element = None
		try:
			byType=self.getByType(locatorType)
			self.log.info("Waiting for maximum :: "+ str(timout)+ ":: second for element to be clickable")

			wait =WebDriverWait(self.driver,10,poll_frequency=1,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
			element=wait.until(EC.element_to_be_clickable((byType,"stopFilter_stop-0")))

			self.log.info("Element appeared on the web page")
		except:
			self.log.info("Element not appeared on the web page")
			print_stack()

		return element

	def webscroll(self,direction="up"):
		"""
		NEW METHOD
		"""
		if direction=="up":
			# scroll up
			self.driver.execute_script("window.scrollBy(0,-1000);")

		if direction=="down":
			#Scroll Down
			self.driver.execute_script("window.scrollBy(0,1000):")

			

        
