from selenium import webdriver
from time import sleep
from getpass import getpass


#Nöbet raporları
dagenel = """Gelen kullanıcılarla ilgilenildi. Rutinler alındı. Genel işe gidildi. Bir sonraki nöbetçilerin nöbete hazır oldukları teyit edildi."""
da = """Gelen kullanıcılarla ilgilenildi. Rutinler alındı. Bir sonraki nöbetçilerin nöbete hazır oldukları teyit edildi."""
op = """Gelen kullanıcılarla ilgilenildi. Rutinler alındı. Bir sonraki nöbetçilerin nöbete hazır oldukları teyit edildi."""


#Kullanıcı giriş yapar.
def bilgiler():
    global username, password
    try:
        username = input("\nKullanıcı adınız: ")
        password = getpass("Şifre: ")
    except:
        print("\n\n!!! ERROR !!!")
        quit()

def login():
    global driver
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get("https://mercek.itu.edu.tr")
    sleep(1)
    usernamefind = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_tbUserName"]').send_keys(username)
    sleep(1)
    passwordfind = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_tbPassword"]').send_keys(password)
    sleep(1)
    girisbuton = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnLogin"]').click()


#Nöbet tipi seçimine göre rapor belirleme
def seçim():
    global cevap
    print("\nNöbet tipi seçiniz:\n1)Danışma+Genel İş\n2)Danışma\n3)Operatör\n")
    cevap = int(input("1, 2, 3 şeklinde giriş yapınız:\t"))
    if cevap not in (1, 2, 3):
        print("\n"+"!"*3+" Yanlış numara tuşladınız. "+"!"*3)
        quit()


#Otomatik rapor yazar
def raporyazma():
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gvNobetci_ctl03_btnDevret"]').click()
    sleep(1)
    rapor =driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbNobetAciklama"]')
    if cevap == 1:
        rapor.send_keys(dagenel)
    elif cevap == 2:
        rapor.send_keys(da)
    elif cevap == 3:
        rapor.send_keys(op)
        

#Buranın geri dönüşü yok, burdan sonra submitledin gitti :)
def submit():
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lbKaydet"]').click()


#Execution
seçim()
bilgiler()
login()
raporyazma()
