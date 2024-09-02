To configure the IP address for a virtual interface, such as a VLAN interface, on a Cisco switch, you would typically use the following commands:

```csharp
interface vlan <vlan_number> 
ip address <IP_address> <subnet_mask>
```

example

```arduino
Switch(config)# interface vlan 10
Switch(config-if)# ip address 192.168.10.2 255.255.255.0

```

This would configure the IP address 192.168.10.2 with a subnet mask of 255.255.255.0 for VLAN 10 on the switch.