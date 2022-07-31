from itertools import count
import requests
from bs4 import BeautifulSoup
import re

pageCounter=0
jobs = []
while(pageCounter!=14):
    urlResult = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=php&start={pageCounter}")
    #they have jobs with noexperience that i couldnot solve (entry levels)
    if(pageCounter==9 or pageCounter==13 or pageCounter==12):
        pageCounter+=1
        continue
    markup = urlResult.content
    # take object from beautiful soup
    bs = BeautifulSoup(markup , 'lxml')

    # find h2 from markup
    jobHeadings = bs.find_all('h2' , {"class" : "css-m604qf"})
    jobAnchors = bs.find_all('a' , {"class" : "css-o171kl"})
    jobLocation = bs.find_all('span' , {"class" : "css-5wys0k"})
    experienceYears = bs.find_all('span' , {"class" : '' })
    jobType=bs.find_all('span' , {"class" : 'css-1ve4b75 eoyjyou0' })

    experienceYrs=[]
    for i in range(len(experienceYears)):
        experienceYrs.append(re.findall(r"^.*Yrs.*$", experienceYears[i].text)) 
    #remove null values   
    experienceYrs = list(filter(None, experienceYrs))
    # print(pageCounter)
    # print(len(experienceYrs))
    # print(len(jobHeadings))
    # experiencecount=0
    for i in range(len(jobHeadings)):
        jobs.append(jobHeadings[i].text)
        jobs.append(jobLocation[i].text)
        # if(jobType[i].text=="Internship"or"Freelance / Project"):
        #     continue
        jobs.append(str(experienceYrs[i]))
        # experiencecount+=1
    pageCounter+=1







print(jobs)

# #print(jobs)
# Write into file 
with open('jobs.txt' , 'w') as jobsFile:
    for job in jobs:
        jobsFile.write(job)
    print('Jobs Added Successfully ')

# Read Jobs

with open('jobs.txt' , 'r') as jobsFile:
    print(jobsFile.read())