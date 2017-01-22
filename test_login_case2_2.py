import pytest

@pytest.fixture
def selenium(selenium):
    selenium.maximize_window()
    return selenium

def step_case2_2_1(selenium, base_url):
    #step 2.1.1
    #open tested page

    selenium.get(base_url)

def step_case2_2_2(selenium):
    #step 2.1.2
    #open login page
    element=selenium.find_element_by_id("login_link")
    element.click()

def step_case2_2_3(selenium, variables):
    #step 2.1.3
    #filled in valid username
    element=selenium.find_element_by_id("id_login-username")
    element.send_keys(variables["username"])

def step_case2_2_4(selenium, variables):
    #step 2.1.4
    #filled in valid password
    element=selenium.find_element_by_id("id_login-password")
    #invalid password
    element.send_keys(variables["invalidpass"])

def step_case2_2_5(selenium):
    #step 2.1.5
    #click on submit button
    #pytest.set_trace()
    element=selenium.find_element_by_name("login_submit")
    element.click()

def step_case2_2_6(selenium):
    #step 2.1.6
    #test if login wasn't successful
    element=selenium.find_element_by_xpath('//*[@id="login_form"]/div[1]/strong')

    assert "errors" in element.text
    selenium.quit()

def test_case_2_2(selenium, base_url, variables):
    selenium.get(base_url)
    step_case2_2_1(selenium, base_url)
    step_case2_2_2(selenium)
    step_case2_2_3(selenium, variables)
    step_case2_2_4(selenium, variables)
    step_case2_2_5(selenium)
    step_case2_2_6(selenium)
