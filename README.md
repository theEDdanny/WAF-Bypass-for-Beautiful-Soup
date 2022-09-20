# Bypassing-Bot-Detection-Systems\

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

Little side note: Each Key and value in our dictionary is going to be a string datatype.



