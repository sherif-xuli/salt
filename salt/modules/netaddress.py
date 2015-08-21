# -*- coding: utf-8 -*-
'''
Module for getting information about network addresses.

.. versionadded:: Boron

:depends: netaddr
'''

__virtualname__ = 'netaddress'

# Import third party libs
try:
    import netaddr
    HAS_NETADDR = True
except ImportError as e:
    print e
    HAS_NETADDR = False


def __virtual__():
    '''
    Only load if netaddr library exist.
    '''
    if not HAS_NETADDR:
        return False
    return __virtualname__


def list_cidr_ips(cidr):
    '''
    Get a list of IP addresses from a CIDR.

    CLI example::

        salt myminion netaddress.list_cidr_ips 192.168.0.0/20
    '''
    ips = netaddr.IPNetwork(cidr)
    return [str(ip) for ip in list(ips)]


def list_cidr_ips_ipv6(cidr):
    '''
    Get a list of IPv6 addresses from a CIDR.

    CLI example::

        salt myminion netaddress.list_cidr_ips_ipv6 192.168.0.0/20
    '''
    ips = netaddr.IPNetwork(cidr)
    return [str(ip.ipv6()) for ip in list(ips)]


def cidr_netmask(cidr):
    '''
    Get the netmask address associated with a CIDR address.

    CLI example::

        salt myminion netaddress.cidr_netmask 192.168.0.0/20
    '''
    ips = netaddr.IPNetwork(cidr)
    return str(ips.netmask)


def cidr_broadcast(cidr):
    '''
    Get the broadcast address associated with a CIDR address.

    CLI example::

        salt myminion netaddress.cidr_netmask 192.168.0.0/20
    '''
    ips = netaddr.IPNetwork(cidr)
    return str(ips.broadcast)
