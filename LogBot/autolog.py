
from selenium import webdriver
import getpass

def loginBOT(usr, pas):
    br = webdriver.Firefox()
    br.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fartist%2F7mz6tB1Og2yzxP74wxDVrn")

    user = br.find_element_by_id("login-username")
    user.clear()
    user.send_keys(usr)

    passwd = br.find_element_by_id("login-password")
    passwd.clear()
    passwd.send_keys(pas)

    btn = br.find_element_by_id("login-button")
    btn.click()

if __name__ == "__main__":
    with open("accounts.txt") as f:
        for i, line in enumerate(f):
            line = line.strip()
            # print('line {:3d}: {}'.format(i, line))

            if len(line) > 0:
                # this will only run when the line is NOT empty

                data, _ = line.split('|',1)
                usr, pwd = data.split(':')
                usr = usr.strip()
                pwd = pwd.strip()

                print('line {:3d} usr: {}'.format(i, usr))
                print('line {:3d} pwd: {}'.format(i, pwd))

                loginBOT(usr, pwd)

