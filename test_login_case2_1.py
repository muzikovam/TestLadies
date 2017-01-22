import pytest

@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium

def step_case2_1_1(selenium, base_url):
    #step 2.1.1
    #open tested page

    selenium.get(base_url)

def step_case2_1_2(selenium):
    #step 2.1.2
    #open login page
    element=selenium.find_element_by_id("login_link")
    element.click()

def step_case2_1_3(selenium, variables):
    #step 2.1.3
    #filled in valid username
    element=selenium.find_element_by_id("id_login-username")
    element.send_keys(variables['username'])

def step_case2_1_4(selenium, variables):
    #step 2.1.4
    #filled in valid password
    element=selenium.find_element_by_id("id_login-password")
    element.send_keys(variables['password'])

def step_case2_1_5(selenium):
    #step 2.1.5
    #click on submit button
    #pytest.set_trace()
    element=selenium.find_element_by_name("login_submit")
    element.click()

def step_case2_1_6(selenium):
    #step 2.1.6
    #test if login was successful
    # element=selenium.find_element_by_xpath('//*[@id="messages"]/div/div')
    element=selenium.find_element_by_id("messages")
    assert "Welcome back" in element.text
    selenium.quit()

def test_case_2_1(selenium, base_url, variables):
    selenium.get(base_url)
    step_case2_1_1(selenium, base_url)
    step_case2_1_2(selenium)
    step_case2_1_3(selenium, variables)
    step_case2_1_4(selenium, variables)
    step_case2_1_5(selenium)
    step_case2_1_6(selenium)
