"""
    UserManager class is responsible for authentication, user profile updates and email sending
"""

class UserManager:
    def authenticate_user(self, username, password):
        # handle authentication
        pass

    def update_user_profile(self, user_id, user_profile_data):
        # update user profile data
        pass

    def sent_email_notification(self, user_email, message):
        # send email to the user
        pass

""" SOLID Design"""

class UserAuthentication:
    def authenticate_user(self, username, password):
        pass # handle authentication

class UpdateUserProfile:
    def update_user_profile(self, user_id, user_profile_data):
        pass # update user profile data

class SendEmailNotification:
    def send_email_notification(self, user_email, message):
        pass # send email notification to the user

"""
    Now, each class has a single, well-defined responsibility. 
    Changes to user authentication won't affect the email notification logic,
    & vice versa, improving maintainability and reducing the risk of unintended side effects.
"""