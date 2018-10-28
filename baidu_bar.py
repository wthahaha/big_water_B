# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from os.path import dirname, join
from dotenv import load_dotenv
from config import config

env_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

username = os.getenv('username')
password = os.getenv('password')
if not password:
    username = config.get('bai_user')
    password = config.get('bai_pass')
vars = {
    "url": "https://tieba.baidu.com/index.html",
    "username": username,
    "password": password
}

# 无界面浏览器支持
chrome_options=Options()
chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()
driver.get(vars['url'])
# 点击登陆按钮
login = driver.find_element_by_css_selector("#com_userbar > ul > li.u_login > div > a")
print(login.text)
login.click()
time.sleep(4)
login_input = driver.find_element_by_css_selector("#TANGRAM__PSP_10__footerULoginBtn")
print(login_input.text)
login_input.click()
time.sleep(2)
username_input = driver.find_element_by_css_selector("#TANGRAM__PSP_10__userName")
password_input = driver.find_element_by_css_selector("#TANGRAM__PSP_10__password")
# 输入账号
username_input.send_keys(vars["username"])
time.sleep(3)
#输入密码
password_input.send_keys(vars["password"])
time.sleep(4)

# 输入验证码
try:

    code_div = driver.find_element_by_id("J_login_code")
    if code_div:
        code = input("输入验证码: ")
        code_div.send_keys(code)
except:
    time.sleep(2)
# 通过二次定位找到用户名输入框

# 点击登录
driver.find_element_by_css_selector("#TANGRAM__PSP_10__submit").click()
driver.implicitly_wait(30) # 等待跳转
# 获取用户关注的贴吧
my_bar = driver.find_element_by_css_selector("#j_u_username > div.u_menu_item.u_menu_username > a > span")
my_bar.click()
time.sleep(4)
selected_bar = driver.find_element_by_css_selector("#forum_group_wrap > a:nth-child(1)")
selected_bar.click()
time.sleep(4)

selected_item = driver.find_element_by_css_selector("#thread_top_list > li:nth-child(1) > div > div.col2_right.j_threadlist_li_right > div > div.threadlist_title.pull_left.j_th_tit > a")
selected_item.click()
time.sleep(4)

driver.close()
