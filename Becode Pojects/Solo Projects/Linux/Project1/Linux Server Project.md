---
---
---
# Detailed Server Configuration
#### Netplan:
> - set netplan configs 00
> 	```
> 	sudo nano /etc/netplan/00-installer-config.yaml
> 	```
> 	```
> 	network: 
> 		version: 2 
> 		renderer: networkd 
> 		ethernets: 
> 			enp0s3: 
> 				dhcp4: no 
> 				addresses: [192.168.56.2/24] 
> 				nameservers: 
> 					addresses: [192.168.56.1, 8.8.8.8]
> 	```
> - set netplan configs 01
> 	```
> 	sudo nano /etc/netplan/01-installer-config.yaml
> 	```
> 	```
> 	network: 
> 		version: 2 
> 		ethernets: 
> 			enp0s8: 
> 				dhcp4: true
> 	```
> 	```
> 	sudo netplan apply
> 	```
> ---
#### SSH Access:

> - **Install SSH Server:**
>     
>     
>     
> 	```
> 	sudo apt update sudo apt install openssh-server
>     
> 	```
> - **Verify SSH Service:**
>     
>     
> 	```
> 	sudo systemctl status ssh
>     ```
> ---
#### DHCP Server Setup:

> - **Install ISC DHCP Server:**
>     
>     
> 	```
> 	sudo apt install isc-dhcp-server
> 	```
> - **Configure ISC DHCP Server:**
>     - Edit the interface configuration file:
>         
>         
>         
>         ```
>         sudo nano /etc/default/isc-dhcp-server
>         ```  
>         
> 	        
> 		```
> 		DHCPDv4_CONF=/etc/dhcp/dhcpd.conf  
> 		INTERFACESv4="enp0s3"  
> 		INTERFACESv6="" 
> 		```
> 			
> 
>         
>     - Add the network interface DHCP should run on:
>         
>         
>         
>         ```
>         INTERFACESv4="enp0s3"
>         ```
>         
>     - Configure the DHCP service:
>         
>         
>         
>         ```
>         sudo nano /etc/dhcp/dhcpd.conf
>         ```
>     
>         
>         
>         
> 		```
> 		option domain-name "little.becode";
> 		option domain-name-servers 8.8.8.8, ns.little.becode;
> 
> 		default-lease-time 600;
> 		max-lease-time 7200;
> 		```
> 		
> 		```
> 		subnet 192.168.56.0 netmask 255.255.255.0 {
> 			range 192.168.56.10 192.168.56.20;
> 			option routers 192.168.56.1;
> 			option broadcast-address 192.168.56.255;
> 		}
> 		```
>         
>     - Restart the DHCP service to apply changes:        
> 		```
> 	    sudo systemctl restart isc-dhcp-server
> 	    sudo systemctl status isc-dhcp-server
> 		```
>         
> ---
#### DNS with Bind:

> - **Install Bind:**
>     
>     
>     
>     ```
>     sudo apt install bind9 bind9utils bind9-doc
>     ```
>     
> - **Configure Forwarders:**
>     - Edit the options file:
>         
>         
>         
>         ```
>         sudo nano /etc/bind/named.conf.options
>         ```
>         
>     
>         
>         
>         
> 		```
> 	    forwarders {     
> 			8.8.8.8;
> 		    8.8.4.4; 
> 	    };
> 		```
>         
>     
>         
>         
>         
> 		```
> 	    allow-query { 192.168.56.0/24; };
> 		```
>         
> - **Set Up a Zone File for Your Local Domain:**
>     - Edit the local configuration file:
>         
>         
>         
>         ```
>         sudo nano /etc/bind/named.conf.local
>         ```
>         
>     - Add a zone for your internal domain:
>         
>         
>         
> 		```
> 	    zone "internal.little.becode" {     
> 	        type master;     
> 	        file "/etc/bind/zones/db.internal.little.becode"; 
> 	    };
>         
> 		```
>     - Create the directory for your zone:
>         
>         
>         
>         ```
>         sudo mkdir -p /etc/bind/zones
>         ```
>         
>     
>         
>         
>         
> 		```
> 	    sudo nano /etc/bind/zones/db.internal.little.becode
> 		```
>         
>     
>         
>         
>         ```
> 
>         $TTL    604800 
>         @       IN      SOA     internal.little.becode. admin.internal.little.becode. (
> 	                               2         ; Serial
> 	                          604800         ; Refresh
> 		                       86400         ; Retry
> 		                     2419200         ; Expire            
> 				            604800 )       ; Negative Cache TTL 
> 		; name servers 
> 		@       IN      NS      ns.internal.little.becode.  
> 		
> 		; A records for name server and localhost 
> 		ns      IN      A       192.168.56.2 
> 		@       IN      A       192.168.56.2 
> 		www 	IN      A       192.168.56.2
>         ```
>     - Check your configuration for errors:
>         
>         
>         
> 		```
> 	    sudo named-checkconf 
> 	    sudo named-checkzone internal.little.becode /etc/bind/zones/db.internal.little.becode
> 		```
>         
>         
>         
>         ```
>         sudo systemctl restart bind9
>         ```
> ---
#### HTTP Server and MariaDB for GLPI:

> - **Install Apache, PHP, and MariaDB:**
>     
> 
>     
> 	```
> 	sudo apt install apache2 mariadb-server php php-mysql libapache2-mod-php
> 	
> 	sudo apt install php-curl php-fileinfo php-gd php-json php-mbstring php-xml php-cli php-cgi php-ldap php-imap php-xmlrpc php-cas
> 
> 	sudo systemctl restart apache2
> 	```
> - **Secure MariaDB:**
>     
> 
>     
>     ```
>     sudo mysql_secure_installation
>     ```
> 
> - **Creating a Database for GLPI:**
> 
> 	
> 	- Log into the MariaDB shell:
> 	    
> 	
> 	    
> 		```
> 		sudo mysql -u root -p
> 		```
> 	- Create a new database for GLPI (name `glpi` for simplicity):
> 	    
> 
> 	    
> 		```
> 		CREATE DATABASE glpi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
> 	    
> 		```
> 	- Create a new database user and grant it privileges to the `glpi` database. Replace `'yourpassword'` with a strong password:
> 	    
> 
> 	    
> 		```
> 		GRANT ALL PRIVILEGES ON glpi.* TO 'glpiuser'@'localhost' IDENTIFIED BY 'yourpassword';
> 	    
> 		```
> 	- Flush the privileges to ensure the changes take effect and then exit the MariaDB shell:
> 	    
> 
> 	    
> 		```
> 		FLUSH PRIVILEGES; 
> 		EXIT;
> 	    ```
> ---
#### Set Up GLPI:
> - Go to the GLPI download page (https://glpi-project.org/downloads/) 
> 	get link for the latest version of GLPI.
> 	```
> 	wget https://github.com/glpi-project/glpi/releases/download/10.0.14/glpi-10.0.14.tgz
> 	```
> 	
> - Extract the file to the web server's document root. Adjust based on the version:
> 	```
> 	sudo tar -xzf glpi-10.0.14.tgz -C /var/www/html/
> 	```
> 
> - Set Apache to use glpi
> 	```
> 	sudo nano /etc/apache2/sites-available/default-ssl.conf
> 	```
> 	```
> 	ServerAdmin little@localhost
> 
> 	DocumentRoot /var/www/html/glpi
> 	```
> 	```
> 	sudo systemctl restart apache2
> 	```
> 
> - Install and setup GLPI in mozzila browser using server ip on https port
> 	```
> 	https://192.168.56.2
> 	```
> ---
#### Create Backup script:
> - **Create a Backup Script:**
>     - Create a script file:
>         
>         
>         
> 		```
> 		sudo nano /usr/local/bin/backup_configs.sh    
> 		```
>         
>     - Add the following, adjusting paths as needed:
>         
>         ```
>         #!/bin/bash 
>         BACKUP_DIR="/path/to/backup/directory" 
>         DATE=$(date +%Y-%m-%d) 
>         tar -czf $BACKUP_DIR/config-backup-$DATE.tar.gz /etc/dhcp /etc/bind /etc/apache2 /var/www/html
> 		```
>     - Make the script executable:
>         
>         
>         
>         ```
>         sudo chmod +x /usr/local/bin/backup_configs.sh
> 		```
>         
> - **Schedule the Backup with Cron:**
>     - Edit the crontab file:
>         
>       
>         
>         ```
>         sudo crontab -e
> 		```
>         
>     - Add a line to run the script weekly (adjust the time as desired):
>         
>         
>         
>         ```
>         0 2 * * 0 /usr/local/bin/backup_configs.sh
> 		```
> ---

