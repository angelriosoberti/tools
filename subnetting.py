import ipaddress
#Creacion de funcion para extear Direccion de red, Primer host, Ultimo Host, Direccion broadcast y Wildcast. 
# Subnet =  IP Address + 1
# First Host = Subnet + 1
# Broadcast = Subnet + GS (Group Size)
# Last Host = Broadcast - 1
# wildcast =  
def calculate_subnet_info(ip_with_mask):
    # separamos direccion ip y mascara
    ip, subnet_mask = ip_with_mask.split('/')
    
    # creacion de IP4Network object. segun documentacion strict= false siempre !!!
    network = ipaddress.IPv4Network(ip + '/' + subnet_mask, strict=False)

    # Subnet
    subnet = str(network.network_address)

    # First Host
    first_host = str(network.network_address + 1)

    # Last Host
    last_host = str(network.broadcast_address - 1)

    # Subnet Mask
    subnet_mask = str(network.netmask)

    # Broadcast Address
    broadcast_address = str(network.broadcast_address)

    # Wildcard Mask
    wildcard_mask = str(network.hostmask)

    return {
        "Subnet or Network ID": subnet,
        "First Host": first_host,
        "Last Host": last_host,
        "Subnet Mask": subnet_mask,
        "Broadcast Address": broadcast_address,
        "Wildcard Mask": wildcard_mask
    }

def main():
    print("Welcome to the Subnet Information Calculator!")
    print("This is a good tool made for students to get easily the information of a network")
    print("This was created for Angel Rios, and can find it in https://github.com/angelriosoberti/tools.git")
    print("This tool has a free licence.")

    while True:
        ip_with_mask = input("\nEnter IP address with subnet mask (e.g., 192.168.0.128/26): ")

        subnet_info = calculate_subnet_info(ip_with_mask)

        if subnet_info:
            print("\nSubnet Information:")
            for key, value in subnet_info.items():
                print(f"{key}: {value}")
            break
        else:
            print("Invalid input. Please enter a valid IP address with subnet mask.")

if __name__ == "__main__":
    main()
