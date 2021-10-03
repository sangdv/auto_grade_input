from os import read
import pandas as pd
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

def readfile(path):
    df = pd.read_csv(path, sep=';', engine='python')
    grade_lst = [ str(score).replace(",",".") for score in df.iloc[:,1]]
    stud_id_lst = [str(stud_id) for stud_id  in df.iloc[:,0]]

    return grade_lst, stud_id_lst

def auto_mark_input(opt):
    # Dang nhap website ctt-sis
    driver = webdriver.Chrome()
    driver.get("https://ctt-sis.hust.edu.vn/Account/Login.aspx")
    driver.maximize_window()

    # Nhap email
    email = driver.find_element_by_id("ctl00_ctl00_contentPane_MainPanel_MainContent_tbUserName_I")
    email.clear()
    email.send_keys(opt.email)
    email.send_keys(Keys.RETURN)

    # Nhap mat khau
    password = driver.find_element_by_id("ctl00_ctl00_contentPane_MainPanel_MainContent_tbPassword_I")
    password.clear()
    password.send_keys(opt.password)
    password.send_keys(Keys.RETURN)

    # Dung 5 giay de nguoi dung nhap captcha
    time.sleep(8)

    # Tu dong an nut dang nhap
    button = driver.find_element_by_id("ctl00_ctl00_contentPane_MainPanel_MainContent_btLogin")
    ActionChains(driver).move_to_element(button).click(button).perform()
    driver.implicitly_wait(5)

    # Click Nhap diem lop hoc
    menu = driver.find_element_by_id("ctl00_NavigationPanel_Navigation_NavigationTreeView_N0_0")
    ActionChains(driver).move_to_element(menu).click().perform()
    driver.implicitly_wait(3)

    # Tu dong dien ma lop hoc
    classcode = driver.find_element_by_id("ctl00_ContentHolder_pnHolder_cpASPxCallbackPanel_tbClassID_I")
    ActionChains(driver).move_to_element(classcode)
    classcode.send_keys(opt.classcode) 
    classcode.send_keys(Keys.RETURN)

    # An vao nut "Tim lop" 
    button = driver.find_element_by_id("ctl00_ContentHolder_pnHolder_cpASPxCallbackPanel_btFind")
    ActionChains(driver).move_to_element(button).click(button).perform()
    driver.implicitly_wait(5)
    time.sleep(2)


    # Tim table nhap diem va dem so luong sinh vien
    input_mark_table = driver.find_elements_by_xpath("//html/body/form/div[5]/section[2]/div[2]/div[2]/table/tbody/tr/td/div/div[1]/div[2]/table/tbody/tr/td/table[2]/tbody/tr")

    # Luu danh sach mssv va index tuong ung tren ctt-sis
    dict = {}
    for i in range(len(input_mark_table) - 1):
        xpath_str = "//*[@id='ctl00_ContentHolder_pnHolder_cpASPxCallbackPanel_gvInputMarks_DXDataRow" + str(i) +"']/td[2]"
        mssv = driver.find_element_by_xpath(xpath_str)
        dict[mssv.text] = i

    # Doc diem tu csv
    grade_lst, stud_id_lst = readfile(opt.gradefile)

    # Nhap diem tu csv
    for i in range(len(stud_id_lst)):
        if (0 > float(grade_lst[i]) or 10 < float(grade_lst[i])):
                print("Diem cua sinh vien " + stud_id_lst[i] + " la " + grade_lst[i] + " khong hop le")
                continue

        if stud_id_lst[i] in dict.keys():
            row_idx = dict[str(stud_id_lst[i])]
            tbl = driver.find_element_by_id("ctl00_ContentHolder_pnHolder_cpASPxCallbackPanel_gvInputMarks_cell" + str(row_idx) + "_5_tbGradeInput_I")
            tbl.clear()
            tbl.send_keys(grade_lst[i])
            tbl.send_keys(Keys.RETURN)
            time.sleep(0.5)
        else:
            print('Khong tim thay sinh vien co mssv ' + str(stud_id_lst[i]))
            
    input('Press a key to exit... ')
    driver.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', type=str, default='', help='email')
    parser.add_argument('--password', type=str, default='', help='password')
    parser.add_argument('--classcode', type=str, default='', help='class code')
    parser.add_argument('--gradefile', type=str, default='grade.csv', help='grade file that contains studentids and marks')
    opt = parser.parse_args()
    auto_mark_input(opt)
    

if __name__ == "__main__":
    main()