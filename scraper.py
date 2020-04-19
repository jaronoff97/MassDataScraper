import time
import re
import atexit

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


f = open("data.txt", "w")


@atexit.register
def goodbye():
    f.close()


service = Service('/Users/jea/Downloads/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)

# SET CRITERIA
driver.get('http://masslandrecords.com/suffolk/')
icon = driver.find_element_by_css_selector("div#Navigator1_SearchCriteria1_WidgetContainer")
driver.execute_script("arguments[0].style.visibility = 'visible';", icon)
driver.execute_script("__doPostBack('Navigator1$SearchCriteria1$LinkButton04','')")

time.sleep(3)


# # OPEN DOC PAGE
frombox = driver.find_element_by_css_selector("input#SearchFormEx1_ACSTextBox_DateFrom")
frombox.clear()
frombox.send_keys('11/1/2019')
tobox = driver.find_element_by_css_selector("input#SearchFormEx1_ACSTextBox_DateTo")
tobox.clear()
tobox.send_keys("12/31/2019")

time.sleep(1)

driver.find_element_by_css_selector("input#SearchFormEx1_BtnAdvanced").click()

time.sleep(1)


select = Select(driver.find_element_by_xpath("//select[@name='SearchFormEx1$ACSDropDownList_Towns']"))
select.deselect_all()

driver.find_element_by_xpath("//select[@name='SearchFormEx1$ACSDropDownList_Towns']/option[text()='BOSTON']").click()
driver.find_element_by_xpath("//select[@name='SearchFormEx1$ACSDropDownList_DocumentType']/option[text()='DEED']").click()

time.sleep(1)
driver.find_element_by_css_selector("input#SearchFormEx1_btnSearch").click()
time.sleep(3)


def get_data_for_table(selector):
    try:
        table = driver.find_element_by_css_selector(selector)
        trs = table.find_elements_by_tag_name('tr')
        for row in trs:
            # Get the columns (all the column 2)
            col = row.find_elements_by_tag_name('td')
            f.write(",".join([c.text for c in col]))
            f.write("\n")
    except Exception as e:
        print(e)
        return


def find_data_on_page():
    elements = driver.find_elements_by_css_selector('a[id*=DocList1_GridView_Document_]')
    pattern = re.compile(r".*ButtonRow_Doc.*")
    found_ids = []
    for element in elements:
        try:
            match = pattern.match(element.get_property("id"))
        except Exception as e:
            print(e)
            continue
        if match:
            found_ids.append(element.get_property("id"))
    for f_id in found_ids:
        query = "a[id*={0}]".format(f_id.split(" ")[0])
        query = query.replace(".", "")
        element = driver.find_element_by_css_selector(query)
        element.click()
        time.sleep(1)
        try:
            pass
        except Exception as e:
            raise e
        get_data_for_table("table#DocDetails1_GridView_Property")
        get_data_for_table("table#DocDetails1_GridView_Details")


while True:
    find_data_on_page()
    time.sleep(2)
    try:
        next_button = driver.find_element_by_css_selector('a[id*=DocList1_LinkButtonNext]')
        next_button.click()
        time.sleep(3)
    except Exception as e:
        print(e)
        break

time.sleep(50)  # Let the user actually see something!
driver.quit()
