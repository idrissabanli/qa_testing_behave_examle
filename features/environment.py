from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
    return context

def after_all(context):
    context.browser.close()