import requests
from lxml import html
from .article import get_article_data

main_data = {
    "the_hindu":{"url":"https://www.thehindu.com/",
              "latest_news":"/html/body/section[2]/div/div[1]/div[3]/div[1]/ul/li[1]/a",
              "article_heading":"/html/body/section[2]/div/div/div[1]/h1",
              "article_content":"/html/body/section[2]/div/div/div[1]/div[6]/p",
              },
    # "mint":{"url":"https://www.livemint.com/latest-news",
    #           "latest_news":"/html/body/a",
    #           "article_heading":"/html/body/section/section/section/article/div/a[1]/h1",
    #           "article_content":"/html/body/section/section/section/div[4]//p",
    #           },
    # "indian_express":{"url":"https://indianexpress.com/latest-news/",
    #           "latest_news":"/html/body/div[2]/div[5]/div/div/div[1]/div[3]/div[1]/div[2]/div[2]/h2/a",
    #           "article_heading":"/html/body/div[2]/div[5]/div/div[1]/div/h1",
    #           "article_content":"/html/body/div[2]/div[5]/div/div[2]/div/div[1]/div/div[1]/p",
    #           },
    # "ndtv":{"url":"https://www.ndtv.com/latest",
    #           "latest_news":"//h2[@class='newsHdng']/a",
    #           "article_heading":"//h2[@class='sp-ttl']",
    #           "article_content":"/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/p",
    #           },
    "indiatoday":{"url":"https://www.indiatoday.in/news.html",
              "latest_news":"/html/body/div[1]/div[3]/div/div/div[2]/main/div/div[2]/div/div[2]/ul/li[1]/h3/a",
              "article_heading":"/html/body/div[1]/div[3]/div/div/div[2]/main/div/div[1]/h1",
              "article_content":"/html/body/div[1]/div[3]/div/div/div[2]/main/div/div[1]/div[6]/div[1]/p",
              },
}

def get_news_data(newspaper="the_hindu"):
    response = requests.get(main_data[newspaper]["url"])

    if response.status_code == 200:
        parsed_html = html.fromstring(response.text)
        # with open("j.html","w") as f:
        #     f.write(str(response.text))
        xpath_expression = main_data[newspaper]["latest_news"]
        element = parsed_html.xpath(xpath_expression)
        print(parsed_html)
        if element:
            article_url = element[0].get("href")
            if newspaper == "indiatoday":
                article_url= 'https://indiatoday.in' +str(article_url)
            # print("href:", article_url)
            return (get_article_data(article_url, main_data[newspaper]["article_heading"], main_data[newspaper]["article_content"], newspaper))

        else:
            print("News article not found.")
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)
