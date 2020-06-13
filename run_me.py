from pages.accountDetails import AccountDetail
from pages.costa import Costa
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
email = input("isi email asli : ")
accountdetails = AccountDetail()
info = accountdetails.getInfo()
print(info)
costa = Costa(info, email)
costa.start_process()
