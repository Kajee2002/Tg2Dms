from google.colab import userdata as userdata


class Configs(object):
    #Bot configurations
    API_ID=userdata.get("API_ID")
    API_HASH=userdata.get("API_HASH")
    BOT_TOKEN=userdata.get("BOT_TOKEN")
    
    #Dms configurations
    UserName=userdata.get("UserName")
    Password=userdata.get("Password")
    LoginDetail=f'userdata.get("UserName"):userdata.get("Password")'
    Header = '"OCS-APIRequest: true"'
    UploadPoint = '"https://dms.uom.lk/remote.php/webdav/"'
    SharePoint = '"https://dms.uom.lk/ocs/v2.php/apps/files_sharing/api/v1/shares?format=json"'
