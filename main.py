import requests
from bs4 import BeautifulSoup

url = "https://www.offerup.com/"

offerup_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/'
                      'webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
                      '/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'DX=web-94b375acbffc0c9b4a2d126b102a65b8080fc614e522cf8e0a7a14b5; '
                      '_sim_uuid=058BA461-A25C-4687-80FD-510C6F3E8B10; _ga=GA1.1.615373648.1663002800;'
                      ' __gads=ID=d5de5260502ec397-22bc08297ad500cb:T=1663002799:S=ALNI_MaIduokf07hshvcOKvyuukwwhAK9w;'
                      ' afUserId=744fd4c7-fec9-417f-b9b3-4375028a662a-p; AF_SYNC=1663002801992; ou.ftue=1;'
                      ' ou.color-mode=light; ou.similityDeviceId=a239bf3eff8b9da5a923d09a0cb1a84d;'
                      ' _sim_si=9E1EFC1C-7169-4B97-B284-90160EBFF5E6;'
                      ' ou.location={%22city%22:%22Laurel%22%2C%22state%22:%22MT%22%2C%22zipCode%22:'
                      '%2259044%22%2C%22longitude%22:-108.7682%2C%22latitude%22:45.6753%2C%22source%22:%22ip%22};'
                      ' OU.USER_CONTEXT_COOKIE={%22device_id%22:%22web-94b375acbffc0c9b4a2d126b102a65b8080fc614e522cf8e0a7'
                      'a14b5%22%2C%22user_agent%22:%22Mozilla/5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)'
                      '%20AppleWebKit/537.36%20(KHTML%2C%20like%20Gecko)%20Chrome/'
                      '105.0.0.0%20Safari/537.36%22%2C%22device_platform%22:%22web%22};'
                      ' _sim_cr=eyJkZXZpY2VfaWQiOiJhMjM5YmYzZWZmOGI5ZGE1YTkyM2QwOWEwY2IxYTg0ZCIsIn'
                      'MiOiI5RTFFRkMxQy03MTY5LTRCOTctQjI4NC05MDE2MEVCRkY1RTYiLCJlIjoxNjYzMzY2NzExM'
                      'DU5fQ==; _ga_JPXV0F18DW=GS1.1.1663193911.3.0.1663193911.0.0.0; tatari-cookie'
                      '-test=31701101; tatari-session-cookie=42a633b6-60e5-6bfd-c018-ff51ec1cae39;'
                      ' __gpi=UID=000008bea14a4c4c:T=1663002799:RT=1663193911:S=ALNI_MaG2AzQ5nRIs1'
                      '_qqHj6l2m2mgNC1w; _dd_s=rum=0&expire=1663195110476; __cf_bm=RKonqAH8F7PtWd2c'
                      'XYU3O1mzsfcpkxmEwKbtg9L9CUY-1663194221-0-AeowObn3z5M39f/n47uveCroGw1zppkMJQ'
                      'tPUd4DoGbAXIeMNE6PGU8FHqxl/guLk/Sy98KIZJCbvrzgswxLMXg=',
            'Host': 'offerup.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit'
                          '/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }


def without_headers():
    request = requests.get(url)

    print(request.text)

    soup = BeautifulSoup(request.text, 'html.parser')

    for i in soup.find_all('a'):
        print(i)


def with_headers():
    request = requests.get(url, headers=offerup_headers)

    soup = BeautifulSoup(request.text, 'html.parser')

    for i in soup.find_all('a'):
        print(i)


with_headers()