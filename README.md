# Bypassing-Bot-Detection-Systems

When web scraping with packages BeautifulSoup and Selenium every programmer will be met with this WAF response similar to this.

![Cloudflare response](https://user-images.githubusercontent.com/92893340/191365938-33fc8827-fd66-4621-a32e-cca75e020696.JPG)

But not to fear, because unless you're sending hundreds of requests a minute the solution is quite simple. For this example I will be using 'https://offerup.com/'. OfferUp doesnt want robots all over their site for obvious reasons, so please dont abuse this infromation. This post is solely for edicational purposes. 

The WAF looks at request headers to authenticate a user. So why dont we try a replay attack with the headers we send legitimately via web browser?

(P.S.) I personally recomend using BeautifulSoup over Selenium. I have found Selenuim much harder to create custom content. But this is a personal opnion. Feel free to use whatever library fits your personal needs.

# Step one: 
Head to the site you want to scrape. Wait for it to load and press f12 (or right click and to to inspect).

# Step Two: 
Once you are in the developer tools on the site you want to scrape head to the networking tab. 

![Networking Tab](https://user-images.githubusercontent.com/92893340/191372115-629c74ad-bb33-415a-b095-2a41117dd83a.JPG)

Hit 'Ctrl + r' to reload the page and click of the packet with the domain name of the site you are scraping. 

![packets](https://user-images.githubusercontent.com/92893340/191372797-feb28247-7a0f-40dc-96af-9640e9ffccb3.JPG)

# Step Three:
When you click on the correct packet move to the 'headers' tab. Under this tab you should see 'Request Headers'. These specs are going to be the payload in our replay attack. 

![request_headers_page](https://user-images.githubusercontent.com/92893340/191373933-25df8b23-9fd7-48c7-8fe9-678f65de32d6.JPG)

# Step four:
Its time to write some python! Start by importing the requests module and your web scraping library of choice. I will be using BeautifulSoup.
Next, build a dictionary and name it whatever you want. This dictionary is where we will be putting the request headers we just retreved in our browser. 

The keys of this dictionary are going to be the dark grey color independent clauses before the colon in our request headers. 

(these values will be the keys in your dictionary) 
![Independent clauses](https://user-images.githubusercontent.com/92893340/191376504-b2ca4ee5-8841-4fab-818e-7fa36d8ef514.JPG)

the values in our dictionary will be represented by the values following each Colon in our request headers.

![Dictionary values](https://user-images.githubusercontent.com/92893340/191377863-dcaaed9b-6e3a-4597-952e-6ab5679287d8.JPG)

Little side note: When building this dictionary make sure it is letter for letter! if one letter is wrong this will not work. I know from personal experence that building this dictionary is a tedious task. But the end result is rewarding!

In the end it should look something like this (These values vary for each client)
```
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
```
# Step five
Its finally time to send a request with our headers attached. 
```
request = request.get(<'your url here'>, headers=incert name of dictionary with headers here)

soup = BeautifulSoup(request.text, 'html.parser')

for i in soup.find_all('a'):
    print(i)
```
As shown below I can now retreve HTML from the page! Mission complete!

![returned links](https://user-images.githubusercontent.com/92893340/191571733-3d63a1ee-eb4a-461a-98b9-f819859e1eca.JPG)

# Keep in mind 
If you are going to be sending traffic that is out of the oridnary in any way be sure to cover your tracks. A large number of requests could get you IP blocked. If you are wanting to build a scalping bot or any script that will send lots of reqauests implement user-agent rotation and proxy rotation. 




