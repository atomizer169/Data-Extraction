from datetime import date
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from zipfile import ZipFile
import os
import time 

#link
url = "http://www.nemweb.com.au/REPORTS/ARCHIVE/Dispatch_SCADA/"

#setting the date to the file download
today = date.today()
year = today.strftime("%Y")
day  = int(today.strftime("%d"))-2
month = today.strftime("%m")

curr_date = year+month+str(day)

#creating the link text to download the file
link_text = "PUBLIC_DISPATCHSCADA_" + curr_date + ".zip"

#starting web driver
options = Options()
options.binary_location = "" #"add the path to the web driver or if it is in the same as the python installation it will not be required"

driver_path = ""#'add the path to the web driver or if it is in the same as the python installation it will not be required'

browser = webdriver.Firefox(executable_path = driver_path, options=options)
browser.get(url)

#clicking the element and download file.
last = browser.find_element("link text",link_text)
last.click()
time.wait(25)
browser.close()


# loading the file.zip and creating a zip object
with ZipFile(r"Downloads\PUBLIC_DISPATCHSCADA_20230424.zip", 'r') as zObject:
  
    # Extracting all the members of the zip 
    # into a specific location.
    zObject.extractall(path="D:\\Python\\extraacted Files\\")


#further extracting files 

dir_name = "" #"Path to the dir to save the downloaded files" or add a file dialog to let the user select
extension = ".zip"

# change directory from working dir to dir with files
Target_dir = "" #"Path to the dir to save the downloaded files" or add a file dialog to let the user select

for file in os.listdir(dir_name):
#    print(file)
    if file.endswith(".zip"):
        abs_file_path = os.path.join(dir_name, file)
        print(abs_file_path)
        with ZipFile(abs_file_path, 'r') as zObject:
            zObject.extractall(path = Target_dir)
            







