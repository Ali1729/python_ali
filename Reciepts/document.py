from positions import *
from PIL import Image, ImageFont, ImageDraw

import pandas as pd
from datetime import datetime

def divide_into_days(birth_day, birth_month):
    if birth_day < 10:
        birth_day1 = 0
        birt_day2 = birth_day

    elif birth_day <20:
        birth_day1 = 1
        birth_day2 = list(str(birth_day))[1]

    elif birth_day <30:
        birth_day1 = 0
        birth_day2 = list(str(birth_day))[1]

    if birth_month <10:
        birth_month1 = 0
        birht_month2 = list(str(birth_month))[1]

    else:
        birth_month1 =1 
        birth_month2 = list(str(birth_month))[1]

    return birth_day1,birth_day2,birth_month1, birth_month2


def print_to_image(excel_path):
    df1 = pd.read_excel(excel_path, "TEMPLATESHEET", skiprow = 6, nrows =2000, usecols = "A:x")
    list_of_images =[]
    for index, row in df1.iterrows():
        new_image = Image.open("recpt.jpg")
        birth_date= row["DAte Of Birth"]
        elob_birth_date = birth_date.strftime("%B %d, %Y")
        birth_month = birth_date.month
        birth_day = birth_date.day
        birth_year = birth_date.year
        birth_day1, birth_day2, birth_month1, birth_month2 = divide_into_days(birth_day,birth_month)
        birth_year1, birth_year2, birth_year3, birth_year4  = str(birth_year)[0],str(sbirth_year)[1],str(birth_year)[2],str(birth_year)[3]

        image_editable = ImageDraw.Draw(my_image)
        image_editable.text(pos_admission_n, str(row["ADMIN]"]).strip(), color_t, font=title_font)
        image_editable.text(pos_student_name, str(row["Applicant NAme"]).strip(), color_t, font= title_font)
        image_editable.text(pos_group, str(row["Course"]),color_t, font=title_font)
        image_editable.text((360,548),"2007", color_t, font=title_font)
        image_editable.text((600,544),"2011", color_t, font=title_font)
        new_image_name = str(row["ADMN"]).strip()+".png"
        new_image.save(new_image_name)
        list_of_images.append(new_image_name)

    
    new_list_images=[]
    for i in list_of_images:
        image_i = Image.open(i)
        new_list_images.append(image_i)
    
    im_obj = Image.open("recpt.jpg")
    im_obj.save("reciepts.pdf",save_all=True,append_images=new_list_images)

excel_path = "ADMINREGISTER.xlsx"
print_to_image(excel_path)


