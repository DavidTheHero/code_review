import os

CLIENT_ID = "4ca4e380-5a55-4c2d-9edc-353a5ed859bd" # Application (client) ID of app registration

CLIENT_SECRET = "Lnv8Q~Wm6uyi~ZPzXhtUUKIBTWZtrcR6ZnLgQdm5" 

# AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
AUTHORITY = "https://login.microsoftonline.com/gendvn.onmicrosoft.com"

REDIRECT_PATH = "/getAToken"

ENDPOINT = 'https://graph.microsoft.com/v1.0/users/dev@gendvn.onmicrosoft.com/sendMail'

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All", "Mail.ReadWrite", "Mail.Send"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session