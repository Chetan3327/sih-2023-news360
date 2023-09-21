from . import tool
from django.shortcuts import render, redirect
from .models import * 
from pprint import pprint
from . import tools
from django.conf import settings

# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# save_path = str(settings.BASE_DIR)  + '\sihpredict\\new_model'
# print("==================================")
# print(save_path)

# tokenizer = AutoTokenizer.from_pretrained(save_path)
# model = AutoModelForSequenceClassification.from_pretrained(save_path)


# import torch
# inputs = tokenizer("""india won asia cup""", return_tensors="pt")
# with torch.no_grad():
#     logits = model(**inputs).logits

# predicted_class_id = logits.argmax().item()
# print(model.config.id2label[predicted_class_id])
print("==================================")


print(tool.get_sentiment("india won the asia cup."))
print(tool.get_sentiment("india not won the asia cup "))
print(tool.get_sentiment("The government's decision to build a new parliament building has been criticized by many, who argue that it is a waste of money and resources"))
# print(tools.get_sentiment("hello how are you"))
# print(tools.get_sentiment("Amid diplomatic row over Khalistani separatist death, MEA issues travel advisory for Indians in Canada: Exercise utmost caution"))




from .youtube import get_captions
captions,latest_video_id = get_captions()
print(captions)
videos = []
for statement in captions:
    sentement = tools.get_sentiment(statement["sentence"])
    if sentement == "negative":
        videos.append({"url":f"https://www.youtube.com/embed/{latest_video_id}?start={int(statement['s'])}&end={int(statement['e'])+1}",
                       "statement":statement["sentence"]})

from .web import get_news_data 
news_data = get_news_data()
# heading, content, article_url
print(news_data)
print("==================================")


link = []
link.append("".join(i for i in news_data['article_url']).replace("\n",""))
# link += ["https://indianexpress.com/article/india/india-canada-travel-advisory-diplomatic-tension-8948339/",
#         "https://indianexpress.com/article/political-pulse/chill-nitish-india-ties-grows-boycott-tv-anchors-coordination-rjd-minister-row-8947883/",
#         "https://indianexpress.com/article/india/hardeep-singh-nijjar-terrorist-cracking-down-gangs-khalistan-movement-8947895/",
#         "https://indianexpress.com/article/india/uzair-khan-electrician-turned-militant-jk-police-kashmir-encounter-8947313/",
#         "https://www.thequint.com/news/india/thirteen-booked-for-sloganeering-during-friday-prayers-in-kashmirs-jamia-masjid-psa-charges-likely",
#         "https://www.thehindu.com/news/national/karnataka/hc-rejects-petition-of-two-minor-pakistani-nationals-for-grant-of-citizenship-through-their-indian-mother/article66703295.ece",
#         "https://www.thehindu.com/news/national/passenger-tries-to-open-emergency-exit-door-cover-onboard-indigos-delhi-chennai-flight/article67326056.ece",
#         "https://www.thehindu.com/news/national/secular-socialist-missing-from-copies-of-constitution-given-to-lawmakers-adhir/article67325930.ece",
#         "https://www.thehindu.com/news/national/1984-anti-sikh-riots-delhi-court-acquits-former-congress-mp-sajjan-kumar/article67326388.ece",
#         "https://economictimes.indiatimes.com/news/politics-and-nation/punjab-congress-leader-shot-dead-in-moga-canadian-based-gangster-claimed-responsibility/videoshow/103780195.cms"]

sources = []
sources.append("".join(i for i in news_data['source_newspaper']).replace("\n",""))
# sources += ["The Indian Express",
#             "The Indian Express",
#             "The Indian Express",
#             "The Indian Express",
#             "The Quint",
#             "The Hindu",
#             "The Hindu",
#             "The Hindu",
#             "The Hindu",
#             "The Economics Times"]

content = []
content.append("".join(i for i in news_data['content']).replace("\n",""))
# content += ["With India and Canada in the middle of a diplomatic face-off over the killing of Khalistani separatist Hardeep Singh Nijjar, the Ministry of External Affairs on Wednesday issued an advisory urging Indian nationals and students in Canada to “exercise utmost caution”. “In view of growing anti-India activities and politically-condoned hate crimes and criminal violence in Canada, all Indian nationals there and those contemplating travel are urged to exercise utmost caution,” the advisory reads. “Recently, threats have particularly targeted Indian diplomats and sections of the Indian community who oppose the anti-India agenda. Indian nationals are therefore advised to avoid travelling to regions and potential venues in Canada that have seen such incidents.” This comes after Canada, alleging potential links between the Indian government and the killing of the pro-Khalistan leader, expelled a top Indian diplomat. In a tit-for-tat move, India responded by ousting a senior Canadian diplomat in Delhi.",
#                 "While Bihar Chief Minister and Janata Dal (United) supremo Nitish Kumar has said he was ready for an early Lok Sabha election, he seems to be increasingly out of sync with the Opposition alliance INDIA or his senior partner in Bihar's ruling Mahagathbandhan (grand alliance), the RJD, on various issues.Among other issues, Nitish is said to be uncomfortable with the RJDs alleged bid to sharpen “backward versus forward” politics by not reining in its Education Minister Chandra Shekhar, who continues to criticise Ramcharitmanas.",
#                 "It was on July 1, 2020, when the Centre for the first time took a strong decision against the Khalistan Tiger Force (KTF) chief Hardeep Singh Nijjar, who was killed in June this year, and eight others, designating them as “terrorists” for actively running a secessionist campaign against India from abroad and motivating Sikh youth from Punjab to join militant ranks.In February this year, the Centre had notified KTF as a “terrorist organisation” under the Unlawful Activities Prevention Act (UAPA). Giving reasons for declaring KTF as a terror organisation, the Union Ministry of Home Affairs (MHA) said, “It is a militant outfit and it aims to revive terrorism in Punjab and challenges the territorial integrity, unity, national security and sovereignty of India and promotes various acts of terrorism, including targeted killings in Punjab”.",
#                 "In the Valley, Jammu and Kashmir police keep a profile of every local militant  his age, educational and family background, ideological inclination and military expertise. While profiling underground militants, police categorise them as A, A+, A++,or B. There are several factors taken into account while deciding this  how lethal the militant is, how many attacks or killings he has carried out, his military understanding, his position in the terror outfit, or the potential to emerge as a central figure.For over a year, Uzair Khan was one among the less than 50 local militants on the police radar, categorised in their records as B  relatively less lethal and unlikely to emerge as a central figure.But a day after three top security officers  Col Manpreet Singh and Major Aashish Dhanchok of the Army's 19 Rashtriya Rifles and DSP Himayun Muzamil of J&K Police  were killed in a gunfight inside the dense forests of Gadole in south Kashmir's Kokernag, the spotlight turned to Uzair who, police believe, was behind the killings.",
#                 "The video of the incident went viral on social media on Friday.“After culmination of the prayers about a dozen persons started anti-national and provocative sloganeering, for a while this was joined by a couple of others as well, while most of the gathering remained aloof,Balwal said that the mosque management committee tried to stop the sloganeering which led to an altercation between those who raised the slogans and mosque volunteers.This created a situation of ruckus inside the mosque leading to clashes between them. Later the hooligans were dispersed outside the mosque by volunteers (of Mosque committee)",
#                 "Two minor Pakistani nationals, born to a Pakistani father and an Indian mother in Dubai, will have to wait till they complete 21 years of age to apply for Indian citizenship as the High Court of Karnataka has said that it cannot direct authorities to grant citizenship to them when the Pakistani law does not permit its citizens to give up their citizenship till they turn 21.. | Photo Credit:Two minor Pakistani nationals, born to a Pakistani father and an Indian mother in Dubai, will have to wait till they complete 21 years of age to apply for Indian citizenship as the High Court of Karnataka has said that it cannot direct authorities to grant citizenship to them when the Pakistani law does not permit its citizens to give up their citizenship till they turn 21.“When the law of Pakistan does not permit renunciation of citizenship till the age of 21, the law of India would not permit grant of citizenship till the renunciation of citizenship of another country,” the court observed while pointing out that Indian law prohibits dual citizenship.Justice M. Nagaprasanna passed the order while rejecting a joint petition, filed by the 17-year-old girl and the 14-year-old boy, represented by their mother, Ameena, all residents of Bengaluru.",
#                 "A male passenger onboard an IndiGo flight from the national capital to Chennai tried to open the cover of the emergency exit door prior to take-off on September 19 night.In a statement on September 20, the airline said that as per the standard operating procedure, the passenger was declared unruly by the crew and handed over to the local authorities on arrival at Chennai.The incident happened onboard flight 6E 6341 from Delhi to Chennai. The passenger tried to open the emergency exit door cover prior to take-off. At no point was the safety of the flight compromised, the statement said.",
#                 "Congress leader Adhir Ranjan Chowdhury on September 20 alleged that the words 'secular' and 'socialist' were missing from the Preamble in the copies of the Constitution given to lawmakers on the opening day of the new Parliament building.Congress leader Adhir Ranjan Chowdhury on September 20 alleged that the words 'secular' and 'socialist' were missing from the Preamble in the copies of the Constitution given to lawmakers on the opening day of the new Parliament building.However, Law Minister Arjun Ram Meghwal said the copies carried the original version of the Preamble of the Constitution and that these words were added later to it after constitutional amendments. This is as per the original Preamble. Amendments were made later, he asserted.Terming the matter as serious, Mr. Chowdhury said the words have been 'cleverly removed' and expressed doubts over the intentions of the BJP government.The Preamble of the Constitution in the copy that we carried to the new building does not include the words secular and socialist. They have been cleverly removed...this is a serious matter and we will raise this issue",
#                 "A Delhi court Wednesday (September 20) acquitted former Congress MP Sajjan Kumar in a case related to the killing of a person during the 1984 anti-Sikh riots, giving him the “benefit of doubt”.Special Judge Geetanjli Goel also acquitted two other accused — Ved Prakash Pial and Brahmanand Gupta — holding that the prosecution failed to prove the case of murder and rioting against them. A Sikh man Surjit Singh was killed during the incident in Sultanpuri.",
#                 "Punjab Congress leader Baljinder Singh Balli was fatally shot at his Moga residence. He was lured outside by two unidentified individuals, then shot upon his return. Despite being rushed to the hospital, Balli succumbed to his injuries. The assailants escaped on a motorcycle, and the incident was captured on CCTV. Later, designated terrorist Arshdeep Singh Gill, also known as Arsh Dalla, claimed responsibility, accusing Balli of introducing him to crime and harassing his mother."]

Heading = []
Heading.append("".join(i for i in news_data['heading']).replace("\n",""))
# Heading += ["Amid diplomatic row over Khalistani separatist death, MEA issues travel advisory for Indians in Canada: Exercise utmost caution",
#                 "Chill in Nitish, INDIA ties grows: Boycott of TV anchors to coordination gaps to RJD minister row",
#                 "From declaring Hardeep Singh Nijjar terrorist to cracking down on gangs: How Centre acted against Khalistan movement",
#                 "Uzair Khan, electrician-turned militant who ranked low on J&K police priority, behind killing of Armymen, DSP",
#                 "13 Booked for Sloganeering During Friday Prayers in Kashmir, PSA Charges Likely",
#                 "HC rejects petition of two minor Pakistani nationals for grant of citizenship through their Indian mother",
#                 "Passenger tries to open emergency exit door cover onboard IndiGo's Delhi-Chennai flight",
#                 "'Secular', 'socialist' missing from copies of Constitution given to lawmakers",
#                 "1984 anti-Sikh riots: Delhi court acquits former Congress MP Sajjan Kumar",
#                 "Punjab Congress leader shot dead in Moga; Canadian-based gangster claims responsibility"]

x=len(Heading)
for i in range(0,x):
    news.objects.create(
    heading=Heading[i],
    content=content[i],
    urls=link[i],
    source=sources[i],
    sentiment = tools.get_sentiment(content[i])
    )
AllData=news.objects.order_by('-id')
    
   

def upload(request):
    
    return render(request,"./home/upload.html")

def home(request):
    return render(request, './home/home.html',{'news':AllData, "videos":videos})
    
def about(request):
    return render(request, './home/about.html')