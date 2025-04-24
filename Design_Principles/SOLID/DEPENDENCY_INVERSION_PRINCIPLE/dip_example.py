"""
    Let's consider an example where we have a EmailService class
    that sends emails using a specific email provider (e.g., Gmail).
"""

class EmailService:
    def __init__(self, gmail_service):
        self.email_service = gmail_service()

    def send_email(self, sender, recipient, subject, body):
        self.email_service.send_email(sender, recipient, subject, body)

class GmailService:
    def send_email(self, sender, recipient, subject, body):
        # logic to send email
        return

email_service = EmailService(GmailService) # directly depending on gmail_service, one of the way to send emails

"""
    In this example, the EmailService class directly depends on the GmailClient class, 
    a low-level module that implements the details of sending emails using the Gmail API.

    This violates the DIP because the high-level EmailService module is tightly coupled
    to the low-level GmailClient module.

    To adhere to the DIP, we can introduce an abstraction (interface) for email clients:
"""

class EmailClient:
    def send_email(self, sender, recipient, subject, body):
        raise NotImplementedError

class GmailClient:
    def send_email(self, sender, recipient, subject, body):
        # logic to send email via gmail
        return

class OutLookClient:
    def send_email(self, sender, recipient, subject, body):
        # logic to send email via outlook
        return

class EmailSendingService:
    def __init__(self, email_client):
        self.email_client = email_client

    def send_email(self, sender, recipient, subject, body):
        self.email_client.send_email(sender, recipient, subject, body)

gmail_client = GmailClient()
email_service = EmailService(gmail_client)
email_service.send_email("adam@gmail.com", "brian@gmail.com", "intro", "sending email via gmail")

outlook_client = OutLookClient()
email_service = EmailSendingService(outlook_client)
email_service.send_email("adam@gmail.com", "brian@gmail.com", "intro", "sending email via outlook")

"""
    Now, the EmailService class depends on the EmailClient abstraction, 
    and the low-level email client implementations (GmailClient and OutlookClient)
    depend on the abstraction.
    
    This follows the DIP, resulting in a more flexible and extensible design.
"""