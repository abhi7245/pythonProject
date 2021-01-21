class loginpage():
    def __init__(self,driver):
        self.driver=driver
        self.user_name_id="txtUsername"
        self.password_id="txtPassword"
        self.login_btn_id="btnLogin"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.user_name_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_btn_id).click()