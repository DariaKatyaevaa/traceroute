import argparse
import subprocess
import re
from pandas import DataFrame


def routing(ip):
    traceroute = subprocess.run(["tracert", ip], stdout=subprocess.PIPE, encoding='cp1251').stdout
    ips = re.findall(r'\d+\.\d+\.\d+\.\d+', traceroute)
    asns = []
    print('поиск автономных систем')
    for ip in ips:
        result = subprocess.run(["curl", "http://api.whois.vu/?q=" + ip],
                                stdout=subprocess.PIPE, encoding='utf-8').stdout
        asn = re.findall(r'AS\d+', result)
        if asn:
            asn = asn[0]
        else:
            asn = ""
        asns.append(asn)
    print("\n\n\nРезультат")
    table = DataFrame({'IP': ips, 'AS': asns})
    table.index += 1
    print(table)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Трассировка автономных систем.'
                                                 'Катяева Дарья КН-202 (МЕН280207)')
    parser.add_argument('-d', '--domain', type=str, help='ip or domain for tracing')
    args = parser.parse_args()
    routing(args.domain)
