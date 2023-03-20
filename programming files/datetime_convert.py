from datetime import datetime


#WHAT AN INCREDIBLE COMMENT


date_str = "2022-03-17 10:45:30"
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

# Mish was here, and left this comment :)
print(formatted_date)
