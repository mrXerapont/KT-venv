import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sender.t_check_repeat import CheckRepeat
from sender.t_after_sending import AfterSending


class Sender:
    def __init__(self, id, desc, mailto, text, dtime, repeat):
        self.id = id
        self.desc = desc
        self.mailto = mailto
        self.text = text
        self.dtime = dtime
        self.repeat = repeat
        
    def sending(self):
        #settings for smtp connection
        mailserver = 'smtp.gmail.com'
        port = 587
        sender_email = 'ktsending@gmail.com'        
        password = 'FwFZAtfO' #not good, google solutions
        context = ssl.create_default_context()
        
        #email fields
        subject = "Notification from Sender"
        body = self.text
        receiver_email = self.mailto
        
        #configure email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject        
        message.attach(MIMEText(body, "plain"))
        text = message.as_string()
        
        #sending..
        
        server = smtplib.SMTP(mailserver)
        server.starttls(context=context)
        server.login(sender_email, password)        
        
        try:
            server.sendmail(sender_email, receiver_email, text)
            #check repeat type
            days = CheckRepeat(self.repeat).checking()
            if days == 0:                
                #delete if no repeat
                AfterSending(self.id).delete_task() 
            else:                
                #change date if repeated
                AfterSending(self.id).edit_task(days,self.dtime)
        except Exception as e:
            print (e)
            #change description if any error
            AfterSending(self.id).unsaccess_task()
        finally:
            server.quit()            
 
        
        
        
        
