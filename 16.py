from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("file:///C:/Users/User/Downloads/tip_calc/tip_calc/index.html")
billamt = dr.find_element(by="id",value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="id",value="peopleamt").send_keys("s")
dr.find_element(by="id",value="calculate").click()
actual = dr.find_element(by="id", value="tip").text
expected = "5"
assert expected == actual