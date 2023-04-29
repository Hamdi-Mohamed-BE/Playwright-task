import re
from playwright.sync_api import Page, Browser, sync_playwright
from config import settings
import json
import time


class TaskBuilder:
    def __init__(self, url : str):
        self.url = url
    
    def build(self):
        """
        Build the task
        """
        with sync_playwright() as p:
            # init browser instance
            browser = p.chromium.launch(headless=not settings.DEBUG)
            # create new page
            page = browser.new_page()
            # navigate to url
            self.navigate_to_url(page)
            # login to agent portal
            self.agent_login(page)
            # close browser
            browser.close()
    
    def navigate_to_url(self, page : Page):
        """
        Navigate to the url
        """
        page.goto(self.url)
    
    def agent_login(self, page : Page):
        """
        Login to the agent portal
        """
        print("Logging in to agent portal")
        # find all element of class skb_text
        self.wait_for_selector(page, ".skb_text")
        elements = page.query_selector_all(".skb_text")
        # selected all the sub a tags
        elements = [element.query_selector("a") for element in elements]
        # filter out the None values
        elements = [element for element in elements if element]
        # get the href attribute
        hrefs = [element.get_attribute("href") for element in elements]
        # navigate to base url + href
        page.goto(self.url + hrefs[0].replace("..", ""))
        # wait for the login form to appear
        self.wait_for_selector(page, ".skb_text")
        # find input field with name phone_login
        input_field = page.query_selector("input[name=phone_login]")
        # type in the user id
        input_field.type(settings.USER_ID)
        # find input field with name phone_pass
        input_field = page.query_selector("input[name=phone_pass]")
        # type in the password
        input_field.type(settings.PASS)
        # find the login button of id : login_sub
        login_button = page.query_selector("#login_sub")
        # click the login button
        login_button.click()
        # login to agent Campaign Login
        self.agent_campaign_login(page)

    def agent_campaign_login(self, page : Page):
        """
        Login to the agent campaign login
        """
        print("Logging in to agent campaign login")
        # wait for the campaign login form to appear
        self.wait_for_selector(page, ".skb_text")
        # find input field with name VD_login
        input_field = page.query_selector("input[name=VD_login]")
        # type in the user id
        input_field.type(settings.USER_ID)
        # find input field with name VD_pass
        input_field = page.query_selector("input[name=VD_pass]")
        # type in the password
        input_field.type(settings.PASS)
        # find the login button of id : login_sub
        login_button = page.query_selector("#login_sub")
        # click the login button
        login_button.click()
        # find drop down with id: VD_campaign
        self.wait_for_selector(page, "#VD_campaign")
        drop_down = page.query_selector("#VD_campaign")
        # click the drop down
        drop_down.click()
        time.sleep(1)
        # select all the options
        options = page.query_selector_all("#VD_campaign option")
        # serialize the options using the html content
        options = [option.inner_html() for option in options]
        print("len of options", len(options))
        self.save_to_json(options)
        print("Options saved to options.json")

    def save_to_json(self, options : list):
        """
        Save the options to a json file
        """
        with open("options.json", "w") as f:
            json.dump(options, f)


    def wait_for_selector(self, page : Page, selector : str):
        """
        Wait for the selector to appear
        """
        page.wait_for_selector(selector)


if __name__ == "__main__":
    task = TaskBuilder("https://dialer018.talkasiavoip.cc")
    task.build()