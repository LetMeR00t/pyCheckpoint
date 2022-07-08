from restfly.endpoint import APIEndpoint

from .service_tcp import ServiceTCPAPI
from .service_udp import ServiceUDPAPI
from .service_icmp import ServiceICMPAPI
from .service_icmp6 import ServiceICMP6API


class ServiceApplications(APIEndpoint):
    @property
    def service_tcp(self):
        """The interface object for the network objects type "Service TCP" Management."""
        return ServiceTCPAPI(self)

    @property
    def service_udp(self):
        """The interface object for the network objects type "Service UDP" Management."""
        return ServiceUDPAPI(self)

    @property
    def service_icmp(self):
        """The interface object for the network objects type "Service ICMP" Management."""
        return ServiceICMPAPI(self)

    @property
    def service_icmp6(self):
        """The interface object for the network objects type "Service ICMP6" Management."""
        return ServiceICMP6API(self)
