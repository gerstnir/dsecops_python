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


def save_report(report_text):    
    output_path = "/opt/target-data/public/centos_report.txt"
    
    with open(output_path, "w") as file:
        file.write(report_text)


def main():
    report_text = create_report()
    save_report(report_text)
    print("CentOS report created successfully.")


if __name__ == "__main__":
    main()