import requests
import urllib3
import random


def create_conn(proxy):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    return urllib3.ProxyManager(proxy,
                                 cert_reqs='CERT_NONE',
                                 num_pools=10,
                                 maxsize=10,
                                 retries=False,
                                 timeout=10)


def change_ip(url):
    response = requests.get(url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=DE')
    if response.status_code == 200:
        # print(response.text)
        # return False
        proxies = response.text.split('\n')
        random_proxy = random.choice(proxies)
        http_proxy = "http://{}".format(random_proxy)
        print('Changing IP to: ', random_proxy)

        with create_conn(http_proxy) as conn:
            r = conn.request('GET', url)
            return r.data


if __name__ == "__main__":
    url = 'http://ipinfo.io'
    data = change_ip(url)
    print(data)
