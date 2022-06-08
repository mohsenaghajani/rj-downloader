import requests
import re
import os
from termcolor import colored
os.system('cls')

def wellcom():
    print('\n wellcom to' ,colored('rj downloader','red'),'\n')
    print('-'*20)

def get_response(url):
    try:
        r=requests.get(url)
        while r.status_code !=200:
            r=requests.get(url)
        return r.text
    except:
        print('link is invalid')

def video_quality():
    while True:
        print('-'*20)
        quality=input('choice quality betwin (4k 1080 720 480):  ')
        print('-'*20)
        if quality in ['4k','1080','720','480']: 
            if quality=='4k':
                return quality
            elif quality=='1080':
                return 'hd'
            elif quality=='720':
                return 'hl'
            else:
                return 'lq'
        print('input invalid try again')    


def quality_choice(type):
    while True:
        if type in ['mp3','podcast']:
            print('-'*20)
            quality=input('choice quality betwin (320 256):  ')
            print('-'*20)
            if quality in ['320','256']: 
                return quality
        else:
            return video_quality()
        print('input invalid try again') 

def format_file(type):
    if type in ['mp3','podcast']:
        return 'mp3'
    return 'mp4'

def link_generate(type,link_music):
    quality=quality_choice(type)
    format=format_file(type)
    if type in['mp3','podcast']:
        print('-'*10,colored('linkdownload','green'),'-'*10)
        print(f'https://host2.rj-mw1.com/media/{type}/{format}-{quality}/{link_music[0]}.{format}')
        print('-'*20)
        return
    print('-'*10,colored('linkdownload','green'),'-'*10)
    print(f'https://host2.rj-mw1.com/media/music_video/{quality}/{link_music[0]}.{format}')
    print('-'*20)
    return


def get_link():
    wellcom()
    url=input(' enter link of radio javan:')
    response=get_response(url)
    for type in ['mp3','podcast','video']:
        
        link_music=re.findall(f'href="https://www.radiojavan.com/{type}s/{type}/([^"]+)"',response)
        
        if link_music:
            link_generate(type,link_music)
            return    
    print('-'*20)
    print('link is invalid')
    print('please try again')
    print('-'*20)

try:
    get_link()
except:
    print('link is invalid')
