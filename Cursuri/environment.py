from Pages.login_page import LoginPage
from Pages.forgot_pass_page import ForgotPassPage
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.forgot_pass_page = ForgotPassPage()

def after_all(context):
    context.browser.close()