
import pytest

@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium

def step_case3_1_1(selenium, base_url):

    #open tested page

    selenium.get(base_url)

def step_case3_1_2(selenium):

    #open login page
    element=selenium.find_element_by_id("login_link")
    element.click()
    #filled in valid username
    element=selenium.find_element_by_id("id_login-username")
    element.send_keys("muzikovam@gmail.com")
    #filled in valid password
    element=selenium.find_element_by_id("id_login-password")
    element.send_keys("blablabla")
    #click on submit button
    element=selenium.find_element_by_name("login_submit")
    element.click()

def step_case3_1_3(selenium):
    #step 2.1.6
    #click on "Clothing"
    element=selenium.find_element_by_xpath('//*[@id="default"]/div[2]/div/div/aside/div[2]/ul/li[1]/a')
    element.click()

def step_case3_1_4(selenium):
    #open product detail
    element=selenium.find_element_by_xpath('//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[1]/article/h3/a')
    element.click()

def step_case3_1_5(selenium):
    #add to basket
    element=selenium.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    element.click()

def step_case3_1_6(selenium):
    element=selenium.find_element_by_xpath('//*[@id="messages"]/div[1]/div')
    assert "has been added to your basket" in element.text

def test_case_3_1(selenium, base_url):
    selenium.get(base_url)
    step_case3_1_1(selenium, base_url)
    step_case3_1_2(selenium)
    step_case3_1_3(selenium)
    step_case3_1_4(selenium)
    step_case3_1_5(selenium)
    step_case3_1_6(selenium)
    selenium.quit()
