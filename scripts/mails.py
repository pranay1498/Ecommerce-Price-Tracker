import smtplib

USER = "USERMAIL@gmail.com"
PASSWORD = "PASSWORD"

def sendMail(datadict, product_link, receiver):
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpobj.ehlo()
    #smtpobj.starttls()
    smtpobj.login(USER, PASSWORD)
    availability = '' if datadict['availability'] == '' else "Avalability: "+datadict['availability']
    body = f'''Subject:Your product is in range!
    \n\n
    Product Name: {datadict['title']}
    Current Price: {datadict['price']}
    {availability}
    Product Link: {product_link}'''
    smtpobj.sendmail(USER, receiver, body)
    smtpobj.quit()
