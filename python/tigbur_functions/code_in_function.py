# # def fun(x,y):
# #     print(x,y)

# x = 3
# y = 5

# print(x,y)


def create_report():
    hostname = "centos-target"
    operating_system = "CentOS Stream 10"
    ip_address = "192.168.100.20"
    created_by = "serviceuser"
    status = "OK"
    report = f"""CentOS Target Report
--------------------
Hostname: {hostname}
Operating System: {operating_system}
IP Address: {ip_address}
Created By: {created_by}
Status: {status}
"""
    return report



hostname = "centos-target"
operating_system = "CentOS Stream 10"
ip_address = "192.168.100.20"
created_by = "serviceuser"
status = "OK"

report = "CentOS Target Report\n--------------------\nHostname: " + hostname + "\nOperating System: " + operating_system

print(report)