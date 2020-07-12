import pytest
from selenium import webdriver
from webdriverfactory import WebDriverFactory 
#from login_page import LoginPage

@pytest.yield_fixture()
def setUp():
	print("Running method level setUp")
	yield
	print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request,browser):
	print("Running one time setUp")
	wdf=WebDriverFactory(browser)
	driver=wdf.getWebDriverInstance()
	# lp=LoginPage(driver)
	# lp.login("faheem","faheem")
	# if  browser=='chrome':
	# 	baseURL="https://stage.newsgallery.com/"
	# 	driver=webdriver.Chrome()
	# 	driver.maximize_window()
	# 	driver.implicitly_wait(3)
	# 	driver.get(baseURL)
	
	
	

	# 	print("Running tests on FF")
	# else:
	# 	baseURL="https://stage.newsgallery.com/"
	# 	driver=webdriver.Chrome()
	# 	driver.get(baseURL)
	
	# 	print("Running tests on chrome")

	if request.cls is not None:
		request.cls.driver=driver

	yield driver
	driver.quit()
	print("Running one time tearDown")


def pytest_addoption(parser):
	parser.addoption("--browser")
	parser.addoption("--osType",help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
	return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
	return request.config.getoption("--osType")
