# boot.py -- run on boot-up
import ugit

wlan = ugit.wificonnect('se7en', 'Combo@123')

# backup internal files
# ugit.backup() # saves to ugit.backup file

# Pull single file
# ugit.pull('file_name.ext', 'Raw_github_url')

# Pull all files
ugit.pull_all()
