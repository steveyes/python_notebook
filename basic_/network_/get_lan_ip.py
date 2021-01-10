from ipaddress import ip_address, ip_network, ip_interface


def get_lan_ip(prefix=24):
    import socket

    so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    so.connect(('8.8.8.8', 80))

    address = so.getsockname()[0]
    interface: ip_interface = ip_interface(f'{address}/{prefix}')

    # network = ip_network(f'{address}/{prefix}', strict=False)
    so.close()
    return interface.ip, interface.network, interface.netmask, interface.network.network_address


if __name__ == '__main__':
    ip, network, netmask, network_address = get_lan_ip()
    print(ip)
    print(network)
    print(netmask)
    print(network_address)
