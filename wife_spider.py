# encoding: utf-8
from selenium import webdriver
import time


vars = {
    "url": "http://www.ganjuke.com/juziying.html",
    "username": "xxx",
    "password": "xxx"
}


driver = webdriver.Chrome()
driver.get(vars['url'])
# 点击登陆按钮
login = driver.find_element_by_css_selector("body > div.wrap > div.header-banner > div > div > div > a.btn-link-orange")
login.click()
time.sleep(4)
# 输入验证码
username_div = driver.find_element_by_id("J_u_login_username")
username_div.send_keys(vars["username"])
time.sleep(4)

#输入密码
passwd_div = driver.find_element_by_id("J_u_login_password")
passwd_div.send_keys(vars["password"])
time.sleep(4)

# 输入验证码
try:

    code_div = driver.find_element_by_id("J_login_code")
    if code_div:
        code = input("输入验证码: ")
        code_div.send_keys(code)
except:
    time.sleep(4)
# 通过二次定位找到用户名输入框

# 点击登录
driver.find_element_by_css_selector("[type='submit']").click()
time.sleep(4)

# 获取用户账号信息
info = driver.find_element_by_css_selector("body > div.wrap > div.header-banner > div > div > div > span:nth-child(1) > span")
print(info.text)
time.sleep(3)

# 选择"乙肝咋办"栏目
driver.find_element_by_css_selector("body > div.wrap > div.main_wrap > div > div.split-left >"
                                                " div.jzy-list > div:nth-child(8) > div.jzy-info > h3 > a").click()
time.sleep(4)

#  发帖
# 点击发帖按钮,此处选择不到发帖按钮
# driver.find_element_by_link_text("发帖").click()
driver.implicitly_wait(30)
# 打开发帖页面
driver.get('http://www.ganjuke.com/index.php?c=post&fid=533')
print(driver.title)
time.sleep(4)
# 输入帖子题目
atc_title = driver.find_element_by_css_selector("#J_atc_title")
print(atc_title.text)
atc_title.send_keys("乙肝传播途径不包括食物传播")
time.sleep(4)

# 切换到iframe内，输入帖子正文
driver.switch_to.frame(0)
# html = driver.execute_script("return document.documentElement.outerHTML")

atc_body = driver.find_element_by_css_selector("body")
atc_body.send_keys("""
    记者从国家卫生健康委员会官网了解到,病毒性肝炎是重要的公共卫生问题,在我国严重危害人民群众身体健康的肝炎主要包括经消化道传播的甲型肝炎、戊型肝炎和经血液、母婴和性传播的乙型肝炎、丙型肝炎等。

　　国家卫健委网站的资料显示,我国《有碍食品安全的疾病目录》中包括病毒性肝炎(甲型、戊型),但不包括乙肝,因为乙肝虽然属于危害较大的传染性疾病,但是传播途径不包括经食物传播,其传播途径主要有血液传播、母婴传播和性接触传播,日常工作或生活接触,如握手、拥抱、共同就餐等无血液暴露的行为不会传播乙肝。

　　记者查阅相关法律法规了解到,《中华人民共和国食品安全法》第四十五条规定:“患有国务院卫生行政部门规定的有碍食品安全疾病的人员,不得从事接触直接入口食品的工作。从事接触直接入口食品工作的食品生产经营人员应当每年进行健康检查,取得健康证明后方可上岗工作。”《有碍食品安全的疾病目录》中包含:“(一)霍乱、(二)细菌性和阿米巴性痢疾、(三)伤寒和副伤寒、(四)病毒性肝炎(甲型、戊型)、(五)活动性肺结核、(六)化脓性或者渗出性皮肤病。”也就是说,乙肝不在有碍食品安全的疾病之列,乙肝携带者可以取得健康证明,并上岗从事接触直接入口食品的工作。

　　《中华人民共和国食品安全法实施条例》第二十三条规定:“从事接触直接入口食品工作的人员患有痢疾、伤寒、甲型病毒性肝炎、戊型病毒性肝炎等消化道传染病,以及患有活动性肺结核、化脓性或者渗出性皮肤病等有碍食品安全的疾病的,食品生产经营者应当将其调整到其他不影响食品安全的工作岗位。”
""")
time.sleep(4)

# 切换回主页面
driver.switch_to.default_content()

button = driver.find_element_by_name('Submit')
print(button.text)
button.click()
driver.implicitly_wait(30)
time.sleep(10)
driver.close()
