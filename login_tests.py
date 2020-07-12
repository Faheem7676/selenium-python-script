from selenium import webdriver
from teststatus import TestStatus 
from selenium.webdriver.common.by import By
from login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp","setUp")


class LoginTests(unittest.TestCase):

	@pytest.fixture(autouse=True)
	def classSetup(self,oneTimeSetUp):
		self.lp=LoginPage(self.driver)
		self.ts=TestStatus(self.driver)

	
	
	

	@pytest.mark.run(order=2)


	def test_validLogin(self):
		self.lp.login("faheem","faheem")
		result1=self.lp.verifyLoginTitle()
		#assert result1==True
		self.ts.mark(result1,"Verified Title")
		

		result2=self.lp.verifyLoginSuccessfull()
		#assert result2==True
		self.ts.markFinal("test_validLogin",result2,"login was sucessfull")
		
		
		

	@pytest.mark.run(order=1)

	def test_invalidLogin(self):
		
		self.lp.login()
		result=self.lp.verifyLoginFailed()
		self.ts.mark(result,"VerifiedLoginFailed")
		#assert result==True
		result3=self.lp.verifybeforeLogin()
		self.ts.markFinal("test_invalidLogin",result3,"Verifyed Before Login")
		



	
		




