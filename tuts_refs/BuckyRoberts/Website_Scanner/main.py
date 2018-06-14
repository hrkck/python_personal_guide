from domain_name import *
from general import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = 'website_targets'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    print("Gathered domain name")

    ip_address = get_ip_address(domain_name)
    print("Gathered ip adress")

    nmap = get_nmap('-F', ip_address)
    print("Gathered nmap")

    robots_txt = get_robots_txt(url)
    print("Gathered robots.txt")

    whois = get_whois(domain_name)
    print("Gathered whois info")

    create_report(name, url, domain_name, nmap, robots_txt, whois)
    print("Creating the report...")


def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots_txt.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)


gather_info('bobisnothing', 'http://www.bobisnothing.com/')
