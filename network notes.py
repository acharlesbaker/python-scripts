# SSH to Multiple Devices from devices file
from netmiko import ConnectHandler
 
with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'roger',
            'password': 'cisco'
        }
 
        net_connect = ConnectHandler(**Router)
 
        hostname = net_connect.send_command('show run | i host')
        hostname.split(" ")
        hostname,device = hostname.split(" ")
        print ("Backing up " + device)
 
        filename = '/home/roger/python-scripts-for-network-engineers/backups/' + device + '.txt'
        # to save backup to same folder as script use below line and comment out above line 
        # filename = device + '.txt' 
 
        showrun = net_connect.send_command('show run')
        showvlan = net_connect.send_command('show vlan')
        showver = net_connect.send_command('show ver')
        log_file = open(filename, "a")   # in append mode
        log_file.write(showrun)
        log_file.write("\n")
        log_file.write(showvlan)
        log_file.write("\n")
        log_file.write(showver)
        log_file.write("\n")
 
# Finally close the connection
net_connect.disconnect()



# notes

import netmiko

# connect to network device
connection = netmiko.ConnectHandler(ip="x.x.x.x", deveice_type="cisco_ios", username="username", password="cisco")


# build network device for netmiko using IP from list of IPs in txt file 
IP_LIST = open('18_routers')
for IP in IP_LIST:
    RTR = {
        'device_type': 'cisco_ios',
        'ip':   IP,
        'username': 'admin',
        'password': 'admin',
    }

# send config to network device from text file, 
  print ('\n Connecting to the Router ' + IP.strip() + '\n')
    try:
        net_connect = ConnectHandler(**RTR)
    except NetMikoTimeoutException:
        print ('Device not reachable' )
        continue

    except NetMikoAuthenticationException:
        print ('Authentication Failure' )
        continue

    except SSHException:
        print ('Make sure SSH is enabled' )
        continue

    output = net_connect.send_config_from_file(config_file='18_router_config')
    print(output)

    print('\n Saving the Router configuration \n')
    output = net_connect.save_config()
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)

