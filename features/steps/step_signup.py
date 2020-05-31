from behave import when, then

### Scenario1
@when('I go to the link  "{link}"')
def step_goto_link(context, link):
    context.browser.get(link)

@then('there title should be "{title}"')
def step_test_title(context, title):
    assert context.browser.title == title

@when('I write "{email}", "{username}", "{password}", "{confirm_password}" to the inputs And click the button')
def step_goto_link(context, email, username, password, confirm_password):
    context.browser.find_element_by_css_selector('#email').send_keys(email)
    context.browser.find_element_by_css_selector('#username').send_keys(username)
    context.browser.find_element_by_css_selector('#password').send_keys(password)
    context.browser.find_element_by_css_selector('#pass_confirm').send_keys(confirm_password)
    context.browser.find_element_by_css_selector('body > div > form > dl > dt:nth-child(5) > input.btn.btn-success').click()

@then('I redirect to the link "{link}"')
def step_redirect(context, link):
    actual_link = context.browser.current_url
    assert link == actual_link




