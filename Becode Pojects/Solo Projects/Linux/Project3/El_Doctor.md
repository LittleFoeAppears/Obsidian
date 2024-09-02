
- to be able to use psutil in my python script
```bash
pip3 install psutil
```
- simple basic script
```python
import psutil
import csv
from datetime import datetime

# Function to fetch CPU and Memory usage
def get_system_metrics():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    return cpu_percent, memory_percent

# Function to write metrics to a CSV file
def write_to_csv(cpu_percent, memory_percent):
    with open('system_metrics.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), cpu_percent, memory_percent])

# Main function
def main():
    cpu_percent, memory_percent = get_system_metrics()
    write_to_csv(cpu_percent, memory_percent)
    print(f"Metrics recorded: CPU {cpu_percent}%, Memory {memory_percent}%")

if __name__ == "__main__":
    main()

```

- make a cron and locate your script
```bash
0 * * * * /usr/bin/python3 /opt/el_doctor.py
```


- Updated script with full ncurse visualization
[link](<file:///C:\Users\Falbo\Desktop\Little Foe vault 1\Becode Pojects\Solo Projects\El_doctor.py>)