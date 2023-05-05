from behave import *
from screens.log_in_screen import LoginScreen
from screens.article_information_screen import ArticleInformationScreen


@Given('we are in the "Article" screen')
def ste_impl(context):
    login_screen = LoginScreen(context)
    login_screen.login("standard_user", "secret_sauce")
    login_screen.tap_element(*login_screen.btn_login)


@When('we tap in the firt article from the first item')
def step_impl(context):
    articleInformation = ArticleInformationScreen(context)
    articleInformation.tap_element(*articleInformation.btn_article)


@Then('we validate that the article name is correct')
def step_impl(context):
    articleInformation = ArticleInformationScreen(context)
    assert articleInformation.productos_mostrados(*articleInformation.lbl_name_article)
    assert articleInformation.productos_mostrados(*articleInformation.lbl_price_article)
