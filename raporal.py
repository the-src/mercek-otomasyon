from selenium import webdriver
from time import sleep
from getpass import getpass


# Nöbet raporları
dagenel = """Gelen kullanıcılarla ilgilenildi. Rutinler alındı. Genel işe gidildi. Bir sonraki nöbetçilerin nöbete hazır oldukları teyit edildi."""
da = """Gelen kullanıcılarla ilgilenildi. Rutinler alındı. Bir sonraki nöbetçilerin nöbete hazır oldukları teyit edildi."""
op = """Arayan kullanıcılarla ilgilenildi. Rutinler alındı. Bir sonraki nöbetçilerin nöbete hazır oldukları teyit edildi."""


# Kullanıcı giriş yapar.
try:
    username = input("\nKullanıcı adınız: ")
    password = getpass("Şifre: ")
except:
    print("\n\n!!! ERROR !!!")
    quit()


def login():
    global driver
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get("https://mercek.itu.edu.tr")
    sleep(1)
    usernamefind = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_tbUserName"]').send_keys(username)
    sleep(1)
    passwordfind = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_tbPassword"]').send_keys(password)
    sleep(1)
    girisbuton = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_btnLogin"]').click()


# Nöbet tipi seçimine göre rapor belirleme
def seçim():
    global cevap
    print("\nNöbet tipi seçiniz:\n1)Danışma+Genel İş\n2)Danışma\n3)Operatör\n")
    cevap = int(input("1, 2, 3 şeklinde giriş yapınız:\t"))
    if cevap not in (1, 2, 3):
        print("\n"+"!"*3+" Yanlış numara tuşladınız. "+"!"*3)
        quit()


def imha():
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_lbIsEkle"]').click()
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_ddlRutinIsTipi"]/option[9]').click()
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_tbRutinIs"]').send_keys('Yapıldı.')
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_btRutinIsEkle"]').click()


def tutanak():
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_lbIsEkle"]').click()
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_ddlRutinIsTipi"]/option[6]').click()
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_tbRutinIs"]').send_keys('Yapıldı.')
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_btRutinIsEkle"]').click()


def temizlik():
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_lbIsEkle"]').click()
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_ddlRutinIsTipi"]/option[10]').click()
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_tbRutinIs"]').send_keys('Yapıldı.')
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_btRutinIsEkle"]').click()


def devral():
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gvSonrakiNobetci_ctl03_btnDevral"]/img').click()


def devret():
    driver.find_element_by_xpath('//*[@id="lnkBtnDevret"]').click()
    sleep(1)
    rapor = driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_tbNobetAciklama"]')
    if cevap == 1:
        rapor.send_keys(dagenel)
    elif cevap == 2:
        rapor.send_keys(da)
    elif cevap == 3:
        rapor.send_keys(op)
    driver.find_element_by_xpath(
        '//*[@id="ctl00_ContentPlaceHolder1_lbKaydet"]').click()


def todo():
    print('\n\n1)Kağıt imha rutini\n2)Tutanak toplanması rutini\n3)Temizlik rutini\n4)Nöbet devral\n5)Nöbet devret\n')
    job = int(input("\nNe yapılacak --->  "))
    match job:
        case 1:
            login()
            imha()
        case 2:
            login()
            tutanak()
        case 3:
            login()
            temizlik()
        case 4:
            login()
            devral()
        case 5:
            seçim()
            login()
            devret()
        case _:
            print("Belirtilen aralıkta seçim yapınız!!")


# Execution
todo()
