### Step 1: Plan Network
nbr of VLANs and which devices will be in each VLAN
ex: VLAN for management, sales, etc.


### Step 2: Create VLANs on the master Switch
open master switch CLI
create a VLAN ID then name it (for every subnets)
```CLI
enable
configure terminal
vlan 10
name Management
vlan 20
name Sales
exit

```

### Step3: Assign VLAN to Ports
still in the CLI of main switch 
get port for subnet/VLAN and set that VLAN for that port
```BASH
interface FastEthernet0/1
switchport mode access
switchport access vlan 10
exit

```

### Step4: Configure Trunking on exit port
still in the CLI of main switch 
get port for exiting (to other switch or router)
```BASH
interface FastEthernet0/24  # port you want to trunk
switchport mode trunk
switchport trunk allowed vlan add 10,20  # all VLANs allowed on this trunk
exit

```

### Step5: