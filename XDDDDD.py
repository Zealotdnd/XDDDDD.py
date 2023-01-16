import string
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
singapoor = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button")
singapoor.click()
element1 = driver.find_element(By.ID, "signupName")


def get_random_name():
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str


element1.send_keys(get_random_name())
element2 = driver.find_element(By.ID, "signupLastName")
element2.click()


def get_random_lastname():
    letters = string.ascii_letters
    result_str2 = ''.join(random.choice(letters) for i in range(8))
    return result_str2


element2.send_keys(get_random_lastname())
element3 = driver.find_element(By.ID, "signupEmail")
element3.click()
element3.send_keys("dmitriibelous8@gmail.com")
element4 = driver.find_element(By.ID, "signupPassword")
element4.click()


def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    name = random.choice(string.ascii_lowercase)
    name += random.choice(string.ascii_uppercase)
    name += random.choice(string.digits)
    name += random.choice(string.punctuation)
    for i in range(8):
        name += random.choice(random_source)

    name_list = list(name)
    random.SystemRandom().shuffle(name_list)
    name = ''.join(name_list)
    return name


password = get_random_password()
print(password)

element4.send_keys(password)
element5 = driver.find_element(By.ID, "signupRepeatPassword")
element5.click()
element5.send_keys(password)
element6 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")
element6.click()
time.sleep(4)
element7 = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button")
element7.click()
time.sleep(2)


def random_number():
    a = random.randint(0, 4)
    return a


number1 = random_number()


def random_number2():
    if number1 == 3:
        number3 = random.randint(0, 2)
    else:
        number3 = random.randint(0, 4)
    return number3


number2 = random_number2()
element8 = Select(driver.find_element(By.NAME, "carBrandId"))
element8.select_by_index(number1)
time.sleep(2)
element9 = Select(driver.find_element(By.NAME, "carModelId"))
element9.select_by_index(number2)
element10 = driver.find_element(By.NAME, "mileage")
element10.click()
element10.send_keys("30")
element11 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]")
element11.click()
time.sleep(1)
element12 = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div[1]/div[2]/button[2]")
element12.click()
element13 = driver.find_element(By.ID, "addExpenseMileage")
element13.clear()
element13.click()
time.sleep(1)
element13.send_keys("40")
element14 = driver.find_element(By.ID, "addExpenseLiters")
element14.click()
element14.send_keys("4")
element15 = driver.find_element(By.ID, "addExpenseTotalCost")
element15.click()
element15.send_keys("2")
time.sleep(1)
element16 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
element16.click()
time.sleep(1)
element17 = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-fuel-expenses/div/div[1]/div/button")
element17.click()
time.sleep(1)
element18 = driver.find_element(By.ID, "addExpenseMileage")
element18.click()
element18.clear()
element18.send_keys("60")
time.sleep(1)
element19 = driver.find_element(By.ID, "addExpenseLiters")
element19.click()
element19.clear()
element19.send_keys("5")
time.sleep(1)
element20 = driver.find_element(By.ID, "addExpenseTotalCost")
element20.click()
element20.clear()
element20.send_keys("30")
time.sleep(1)
element21 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
element21.click()
time.sleep(1)
element22 = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-fuel-expenses/div/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/button[2]/span")
element23 = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-fuel-expenses/div/div[2]/div/div[1]/table/tbody/tr[2]/td[5]/button[2]/span")
if element22.is_displayed() is True and element23.is_displayed() is True:
    print("Test Passed")
else:
    print("Test failed")
time.sleep(2)
driver.get("https://qauto2.forstudy.space/panel/settings")
time.sleep(4)
element24 = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-settings/div/div[2]/div/div[5]/div/button")
element24.click()
element25 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-remove-account-modal/div[3]/button[2]")
element25.click()

time.sleep(40)

