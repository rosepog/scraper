"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from datetime import datetime
from django.db import IntegrityError
from app.models import*
import re
import json
import time
import requests

def home(request):
    if request.method == "POST":
        try:
            r= requests.get('http://www.ricercaimprese.com/')
            req=r.text
            req2=json.dumps(req)
            splitcont = re.findall(r'<h2>Regioni(.*?)</ul>', req2)
            for item in splitcont:
            #    print (item)
                splitcont2 = re.findall(r'<a href=(.*?)>', item)
                for item2 in splitcont2:
                    #print(item2)
                    sub2 = re.sub(r'\\"', '', item2)
                    link = 'http://www.ricercaimprese.com/' + sub2
                    #print (link)
                    scrape2(link)
                    page= requests.get(link)
                    page2=page.text
                    page3=json.dumps(page2)
                    getlastpage = re.findall(r'Vai a pagina:(.*?)Vai all', page3)
                    for getlastpage in getlastpage:
                        getlastpage2 = re.findall(r'href=(.*?)title=', getlastpage)
                        for getlastpage2 in getlastpage2:
                            sub3 = re.sub(r'\\"', '', getlastpage2)
                            link2 = 'http://www.ricercaimprese.com/' + sub3
                            #print (link2)
                            getlastpage3 = re.findall(r'-(.*?).htm', sub3)
                            for getlastpage3 in getlastpage3:
                                finalnum = getlastpage3
                    finalink = re.sub(r'.htm', '', sub2)
                    #scrape(finalnum)
                    for x in range(2, int(finalnum)):
                        finallink2 = 'http://www.ricercaimprese.com/' + finalink + '-' + str(x) + '.htm'
                        scrape2(finallink2)
                    #time.sleep(3)
        except requests.ConnectionError as e:
            print (e)
        return HttpResponseRedirect(reverse('explorer/1.html'))
    return render(request, 'app/index.html')

def scrape2(link):
    
    #print(link)
    rpage = requests.get(link)
    rpage2 = rpage.text
    rpage3 = json.dumps(rpage2)
    splitconti = re.findall(r'titoloh1(.*?)Ultime aziende inserite', rpage3)
    for itemconti in splitconti:
        splitcont3 = re.findall(r'box_aziende_inteno(.*?)</a>', itemconti)
        for item3 in splitcont3:
                    splitcont4 = re.findall(r'<a href=(.*?)>', item3)
                    for item4 in splitcont4:
                        sub3 = re.sub(r'\\"', '', item4)
                        link2 = 'http://www.ricercaimprese.com/' + sub3
                        #print (link2)
                        link2page = requests.get(link2)
                        link2page2 = link2page.text
                        link2page3 = json.dumps(link2page2)
                        actname = re.findall(r'alt=(.*?)/><h1>', link2page3)
                        for actname in actname:
                            actsub = re.sub(r'\\"', '', actname)
                            actsub2 = re.sub(r'\\n', '', actsub)
                            #print (actsub2)
                        email = re.findall(r'email: (.*?)<br', link2page3)
                        email3 = ""
                        for email in email:
                            if email != '':
                                email3 = email
                            else:
                                email3 = ""
                        website = re.findall(r'Url:</b>(.*?)</span>', link2page3)
                        websub2 = ""
                        for website in website:
                            if website != '':
                                websub = re.sub(r"<span class='girandola'>","",website)
                                websub2 = websub [::-1]
                        tel = re.findall(r'tel: (.*?)<br', link2page3)
                        tel3 = ""
                        for tel in tel:
                            if tel != '':
                                tel3 = tel
                            else:
                                tel3 = ""
                        prov = re.findall(r'Provincia:</b> (.*?)<br', link2page3)
                        for prov in prov:
                            prov = prov
                        city = re.findall(r'Comune:</b>  (.*?)<br', link2page3)
                        for city in city:
                            city = city
                        category = re.findall(r'Categorie che potrebbero interessarti:(.*?)</ul>', link2page3)
                        catsub2 = ""
                        for category in category:
                            if category != '':
                                category2 = re.findall(r'html(.*?)</a>', category)
                                for category2 in category2:
                                    catsub = re.sub(r'">', '', category2)
                                    catsub3 = re.sub(r'\\', '', catsub)
                                    catsub2 = catsub3 + ',' + catsub2
                        desc = re.findall(r'</h1><p>(.*?)</p>', link2page3)
                        for desc in desc:
                            if desc != '':
                                descsub = re.sub(r'<br />', '', desc)
                                decsub2 = descsub.encode('utf-16', 'surrogatepass').decode('utf-16')
                                decsub3 = json.loads('"%s"'%(decsub2))
                                decsub3 = decsub3
                        try:
                            scrapeob=Scrape.objects.create(ActivityName=actsub2, Email=email3, Website=websub2, Phone=tel3, Province=prov, City=city, Category=catsub2, Description=decsub3)
                            scrapeob.save()
                        except IntegrityError as e:
                            context={'error': e}

def scrape(request):
    if request.method == "POST":
        return render(request, 'app/user_activated.html')