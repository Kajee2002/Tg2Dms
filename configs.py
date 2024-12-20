from google.colab import userdata


class configs(object):
    API_ID=userdata.get("API_ID", "")
    API_HASH=userdata.get("API_HASH", "")
    BOT_TOKEN=userdata.get("BOT_TOKEN", "")
    UserName=userdata.get("UserName", "")
    Password=userdata.get("Password", "")
    LoginDetail=f'userdata.get("DMS_USERNAME", ""):userdata.get("DMS_PASSWORD", "")'
    Header = '"OCS-APIRequest: true"'
    UploadPoint = '"https://dms.uom.lk/remote.php/webdav/"'
    SharePoint = '"https://dms.uom.lk/ocs/v2.php/apps/files_sharing/api/v1/shares?format=json"'
