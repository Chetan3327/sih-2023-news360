import requests
from lxml import html

# article_url = "https://www.thehindu.com/news/national/parliament-special-session-live-updates-september-20-day/article67325075.ece"
# article_url = "https://www.thehindu.com/business/markets/rupee-recovers-from-record-lows-jumps-24-paise-to-end-at-8308-against-us-dollar/article67326016.ece"

# xpath_expression_heading = "/html/body/section[2]/div/div/div[1]/h1"
# xpath_expression_content = "/html/body/section[2]/div/div/div[1]/div[6]/p"



def get_article_data(article_url, xpath_expression_heading, xpath_expression_content, newspaper):
    response = requests.get(article_url)

    if response.status_code == 200:
        parsed_html = html.fromstring(response.text)
        
        heading = parsed_html.xpath(xpath_expression_heading)
        article = parsed_html.xpath(xpath_expression_content)
        
        article_data = {"heading":"",
                        "content":"",
                        "article_url":article_url,
                        }
        if heading:
            heading = heading[0].text
            article_data["heading"] = heading
        else:
            print("heading not found.")
        article_text = ""
        for i in range(len(article)):
            if article[i] != None:
                article_text += str(article[i].text)
                article_text += "\n"
        article_data["content"] = article_text
        article_data['source_newspaper'] = newspaper
        return article_data

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)


# print(get_article_data(article_url , xpath_expression_heading , xpath_expression_content))