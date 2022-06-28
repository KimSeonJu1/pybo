import json
import os
import sys
import urllib.request

def naver_blog(keyword):
    client_id = "upXcyouzvQpvKfaW5K6Y"
    client_secret = "JAbFrQqXQj"

    encText = urllib.parse.quote(keyword)

    url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        response_json = json.loads(response_body)
        blog_list = response_json['items']

        title_list = []
        for tmp in blog_list:
            title_list.append(tmp['title'])
    else:
        print("Error Code:" + rescode)

    return title_list
