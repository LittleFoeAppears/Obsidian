import psutil
import smtplib
import csv
from email.mime.text import MIMEText
from datetime import datetime

def get_system_metrics():
    # Fetch the percentage of CPU utilization
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # Fetch memory usage details
    memory = psutil.virtual_memory()
    memory_percent = memory.percent  # Memory utilization as a percentage
    
    return cpu_percent, memory_percent

# Function to write metrics to a CSV file
def write_to_csv(cpu_percent, memory_percent):
    with open('system_metrics.csv', mode='a') as file:
        writer = csv.writer(file)
        # Writing the current datetime, CPU usage, and Memory usage to the CSV
        writer.writerow([datetime.now(), cpu_percent, memory_percent])

def send_email_alert(cpu_percent, memory_percent):
    msg = MIMEText(f"High resource usage detected: CPU {cpu_percent}%, Memory {memory_percent}%")
    msg['Subject'] = 'System Alert from El Doctor'
    msg['From'] = 'littlefoe_123456789@mail.be'
    msg['To'] = 'littlefoe_123456789@mail.be'

    with smtplib.SMTP('smtp.mail.be', 587) as server:
        server.starttls()
        server.login('littlefoe_123456789@mail.be', 'AnnoyingPassword123456789')
        server.send_message(msg)

def main():
    cpu_percent, memory_percent = get_system_metrics()
    write_to_csv(cpu_percent, memory_percent)
    if cpu_percent > 80 or memory_percent > 80:
        send_email_alert(cpu_percent, memory_percent)
    print(f"Metrics recorded: CPU {cpu_percent}%, Memory {memory_percent}%")

if __name__ == "__main__":
    main()
