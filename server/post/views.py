from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

import requests as rq
from bs4 import BeautifulSoup as bsp
from pprint import pprint

# from post_g import post_


def index(request):
    l = post_()
    return JsonResponse(l,safe=False)
    # return HttpResponse("Hello, world. You're at the polls index.")

def post_():


    url = 'https://aastik.in/'


    data = []
    post ={
        'title':'',
        'purl':'',
        'topic':'',
        'author':'',
        'date':'',
        'des':'',
        'imgurl':''
        }


    resp = rq.get(url).text

    bs = bsp(resp , "lxml")

    # a = bs.find_all("div" , class_='td-block-span12')
    # print(art.find('div',class_="td-module-thumb").a["title"])


    # pprint(len(a))
    # art = bs.div
    for art in bs.find_all("div" , class_='td-block-span12'):

        # pprint(len(art) == len(a))
        try:

            post['purl'] = art.find('div',class_="td-module-thumb").a["href"] 
            post['title'] = art.find('div',class_="item-details").h3.a.text  
            post['topic'] = art.find('div',class_="td-module-meta-info").a.text

            post['author'] = art.find('span',class_="td-post-author-name").text
            post['date'] = art.find('span',class_="td-post-date").text

            post['des'] = art.find('div',class_="td-excerpt").text
            post['imgurl'] = art.find('div',class_="td-module-thumb").a.img['data-lazy-src']
            data.append(post)
            # print(len(data))
        except :
            print('not done')
        dic = {"sa":data}
    return dic
    # if len(data) ==4 :
    #     break


    # pprint(data)
    # print(art.find('div',class_="td-module-thumb").a["title"])
    # print(len(art))

    