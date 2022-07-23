# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from ast import Assert
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "Any"
caps["appium:NewCommandTimeout"] = "50000"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)

tecla1 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_1")
tecla2 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_2")
tecla3 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_3")
tecla4 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_4")
tecla5 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_5")
tecla6 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_6")
tecla7 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_7")
tecla8 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_8")
tecla9 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_9")
tecla0 = driver.find_element(
    by=AppiumBy.ID, value="com.google.android.calculator:id/digit_0")


teclaX = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="×")
teclaIgual = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")


def multiplicar(tecla, operador, tecla2):

    tecla.click()
    operador.click()
    tecla2.click()
    teclaIgual.click()

    result = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final")

    somapython = int(tecla.text) * int(tecla2.text)
    somaappium = int(result.text)

    print('O resultado da soma via Appium foi: ', somaappium)
    print('O resultado da soma via Python foi: ', somapython)

    assert somapython == int(result.text), 'Resultados divergentes entre o python e o Appium'




multiplicar(tecla2, teclaX, tecla5)

limpar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="clear").click()

multiplicar(tecla5, teclaX, tecla5)


#time.sleep(2)  #wait implicito

#driver.make_gsm_call("101010", "call")
driver.send_sms("101010", "bom dia")

driver.quit()