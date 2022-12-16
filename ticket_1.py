#from selenium import webdriver
import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = uc.Chrome()
wait = ui.WebDriverWait(URL, 10)
URL.get("https://tixcraft.com/")

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/ul/li[3]/a"))
member_login = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/ul/li[3]/a").click()

time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div/div/div[2]/a[2]"))
login_menthod = URL.find_element(
    "xpath", "/html/body/div[3]/div/div/div[2]/a[2]").click()
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))
google_account = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
google_account.send_keys("yellow145258789")  # 帳號
google_account.send_keys(Keys.ENTER)

time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))
google_password = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
google_password.send_keys("juan145258789145258789")  # 密碼
google_password.send_keys(Keys.ENTER)

time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[2]"))
one = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[2]").click()  # google驗證1

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/nav/ul/li[1]"))
program_infromation = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/nav/ul/li[1]").click()  # 節目資訊

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/div[1]/div/div[4]"))
select_baseball = URL.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/div[1]/div/div[4]").click()  # 選擇棒球經典賽

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/button"))
cookie_btn = URL.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/button").click()  # 接受cookie

time.sleep(1)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/ul/li[1]"))
select_now_buy = URL.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/ul/li[1]").click()  # 選擇立即購票


URL.execute_script("window.scrollTo(0,500)")  # 往下滑動

time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/div[2]/div[2]/div/table/tbody/tr[8]/td[4]/input"))
select_date = URL.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/div[2]/div[2]/div/table/tbody/tr[8]/td[4]/input")  # 選擇時間

ActionChains(URL).move_to_element(select_date).click().perform()

time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul[4]/li[4]/a"))
select_seat = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul[4]/li[4]/a").click()  # 選擇位子
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[1]/table/tbody/tr[1]/td[2]/select"))
down = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[1]/table/tbody/tr[1]/td[2]/select").click()  # 下拉式選單

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[1]/table/tbody/tr[1]/td[2]/select/option[5]"))
four_sheet = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[1]/table/tbody/tr[1]/td[2]/select/option[5]").click()  # 選擇4張

ActionChains(URL).move_by_offset(0, 0).click().perform()  # 滑鼠點選空白區


wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[2]/div[3]/label/input"))
check = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[2]/div[3]/label/input").click()  # 打勾

time.sleep(5)

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[2]/div[4]/button[2]"))
confirm = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[2]/div[4]/button[2]").click()
# 購票確定
