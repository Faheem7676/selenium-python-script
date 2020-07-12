"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
  self.check_point.markFinal("Test Name",result,"Message")
"""

#import
#from login_page import SeleniumDriver
import custom_logger as cl
import logging
from basepage import BasePage
class TestStatus(BasePage):

	log=cl.customLogger(logging.INFO)

	def __init__(self,driver):
		"""

		Inits CheckPoint class

		"""

		super(TestStatus,self).__init__(driver)
		self.resultList= []


	def setResult(self,result,resultMessage):
		try:
			if result is not None:
				if result:
					self.resultList.append("PASS")
					self.log.info("### VERIFICATION SUCCESSFULL:: + " + resultMessage)
				else:
				    self.resultList.append("FAIL")
				    self.log.info("### VERIFICATION FAIL :: + "+ resultMessage)
				    self.screenShot(resultMessage)

			else:
			    self.resultList.append("FAIL")
			    self.log.error("### VERIFICATION FAIL :: + "+ resultMessage)
			    self.screenShot(resultMessage)
		except:
			self.resultList.append("FAIL")
			self.log.error("### Exception Occurred !!!")
			self.screenShot(resultMessage)


	def mark(self,result,resultMessage):
		"""

		Mark the result of the verification point in a test case
		"""

		self.setResult(result,resultMessage)

	def markFinal(self,testName,result,resultMessage):
		"""

		Mark the final result of the verification point in a test case
		This needs to be called at least once in a test case
		This should be final test status of the test case
		"""

		self.setResult(result,resultMessage)

		if "FAIL" in self.resultList:
			self.log.error(testName + " ### Test Failed")
			self.resultList.clear()
			assert True==False
		else:
			self.log.info(testName + "### Test Successfull")
			self.resultList.clear()
			assert True ==True






