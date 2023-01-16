import string
import random


def get_random_name():
    random_source = string.ascii_letters + string.digits + string.punctuation
    name = random.choice(string.ascii_lowercase)
    name += random.choice(string.ascii_uppercase)
    name += random.choice(string.digits)
    name += random.choice(string.punctuation)
    for i in range(6):
        name += random.choice(random_source)
        name_list = list(name)
        random.SystemRandom().shuffle(name_list)
        return name
    print("first name is", get_random_name())
    print("second name is", get_random_name())
    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element(By.NAME, 'carBrandId'))
    select.select_by_value(value1)

    def value_2():
        if number == 0:
            value = "0: 1"
        elif number == 1:
            value = "1: 2"
        elif number == 2:
            value = "2: 3"
        elif number == 3:
            value = "3: 4"
        else:
            value = "4: 5"
        return value

    def value_1():
        if number1 == 0:
            value = "0: 1"
        elif number1 == 1:
            value = "1: 2"
        elif number1 == 2:
            value = "2: 3"
        elif number1 == 3:
            value = "3: 4"
        else:
            value = "4: 5"
        return value
