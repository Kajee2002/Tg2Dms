import os

class Configs(object):
    #Bot configurations
    API_ID=int(os.environ.get("API_ID"))
    API_HASH=os.environ.get("API_HASH")
    BOT_TOKEN=os.environ.get("BOT_TOKEN")
    
    #Dms configurations
    UserName=os.environ.get("UserName")
    Password=os.environ.get("Password")
    LoginDetail=f'{os.environ.get("UserName")}:{os.environ.get("Password")}'
    Header = '"OCS-APIRequest: true"'
    UploadPoint = '"https://dms.uom.lk/remote.php/webdav/"'
    SharePoint = '"https://dms.uom.lk/ocs/v2.php/apps/files_sharing/api/v1/shares?format=json"'
