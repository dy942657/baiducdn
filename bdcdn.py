# -*- coding: UTF-8 -*-

import sys
import cdn_conf
from baidubce.exception import BceServerError
from baidubce.services.cdn.cdn_client import CdnClient


class CdnClient(object):
    def __init__(self):
        self.cdn_client = CdnClient(cdn_conf.config)

    def list_domains(self):
        """
        list_domains
        """
        try:
            response = self.cdn_client.list_domains()
            # print(response.domains)
            return response.domains
        except Exception as e:
            print("list_domains error:{}".format(e))

    def set_domain_https(self, domain, certId):
        """
        set single domain https
        """
        try:
            https = {
                'enabled': True,
                'certId': certId
            }
            response = self.cdn_client.set_domain_https(domain, https)
            print("set {} https \n certId: {}\n ok \n".format(domain, certId))
        except BceServerError as e:
            print("set {} https \n certId: {}\n error:{} \n".format(domain,
                                                                    certId, e))

    def set_domains_https(self, certId):
        """
        set all domain https
        """
        list_domains = self.list_domains()
        for _ in list_domains:
            # debug
            # print(_.name)
            # if _.name == 'abc.bdcloud.cn':
            #     print(_.name)
            self.set_domain_https(_.name, certId)


def main():
    arg = sys.argv[1:]
    # debug
    # arg = ['set_domains_https', 'cert-hmvcprmp5hcu']
    bdcdn = CdnClient()
    if arg[0] == "-h":
        print(":list_domains   打印domains")
        print(":set_domain_https [domain] [certId] 设置制定domain的https证书")
        print(":set_domains_https [certId]   设置所有domains的https证书")
    elif arg[0] == "list_domains":
        # print(arg)
        bdcdn.list_domains()
    elif arg[0] == "set_domain_https":
        # print(arg)
        if len(arg) != 3:
            print("arg error")
            return
        domain, certId = arg[1], arg[2]
        bdcdn.set_domain_https(domain, certId)
    elif arg[0] == "set_domains_https":
        # print(arg)
        if len(arg) != 2:
            print("arg error")
            return
        certId = arg[1]
        bdcdn.set_domains_https(certId)
    else:
        print("~.~")


if __name__ == '__main__':
    main()
