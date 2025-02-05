import datetime 

now = datetime.datetime.now()
print("Seconds since January 1, 1970: {:,f}".format(now.timestamp()), "or", f"{now.timestamp():.4e} in scientific notation")
formatted_date = now.strftime("%b %d %Y")
print(formatted_date)