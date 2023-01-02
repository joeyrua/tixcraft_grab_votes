import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = uc.Chrome()
wait = ui.WebDriverWait(URL, 10)
URL.maximize_window()
URL.get("https://tixcraft.com/")#進入拓元購票系統

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/ul/li[3]/a"))
member_login = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/ul/li[3]/a").click()#會員登入

time.sleep(1)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div/div/div[2]/a[2]"))
login_menthod = URL.find_element(
    "xpath", "/html/body/div[3]/div/div/div[2]/a[2]").click()#選擇google登入
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))
google_account = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
google_account.send_keys("yellow145258789")#登入帳號
google_account.send_keys(Keys.ENTER)

time.sleep(1)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))
google_password = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
google_password.send_keys("juan145258789145258789")#登入密碼
google_password.send_keys(Keys.ENTER)

time.sleep(1)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[2]"))
one = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[2]").click()#選擇驗證方式

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[1]/div/nav/ul/li[1]/a"))
program_infromation = URL.find_element(
    "xpath", "/html/body/div[1]/div[1]/div/nav/ul/li[1]/a").click()#節目消息

time.sleep(1)


wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/button"))
cookie_btn = URL.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/button").click()#接受cookie

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/div[1]/div/div[8]/div/a/img"))
select_baseball = URL.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/div[1]/div/div[8]/div/a/img").click()#選擇棒球賽事



time.sleep(1)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/ul/li[1]"))
select_now_buy = URL.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/ul/li[1]").click()#現在購買

time.sleep(1)
URL.execute_script("window.scrollTo(0,500)")  # 往下滑動

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/div[2]/div[2]/div/table/tbody/tr[9]/td[4]/input"))

select_date = URL.find_element(
    "xpath", "/html/body/div[1]/section/div/div/div/div[2]/div[2]/div/table/tbody/tr[9]/td[4]/input").click()#選擇日期


wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul[4]/li[5]/a"))
select_seat = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul[4]/li[5]/a").click()#選擇位子

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[1]/table/tbody/tr[1]/td[2]/select"))
down = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[1]/table/tbody/tr[1]/td[2]/select").click()#下拉式選單

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[1]/table/tbody/tr[1]/td[2]/select/option[5]"))
four_sheet = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[1]/table/tbody/tr[1]/td[2]/select/option[5]").click()#選擇四個位子

ActionChains(URL).move_by_offset(0,0).click().perform()#按下空白區

time.sleep(5)#等待輸入完驗證碼的時間SS

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[2]/div[3]/label/input"))
check = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[2]/div[3]/label/input").click()#同意條款

wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[2]/div[4]/button[2]"))
confirm = URL.find_element(
    "xpath", "/html/body/div[1]/div[2]/div[2]/div/form/div[2]/div[4]/button[2]").click()#確認
