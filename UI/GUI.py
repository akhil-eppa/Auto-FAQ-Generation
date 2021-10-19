# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:51:03 2021

@author: Akhil
"""
import csv
import PySimpleGUI as sg
import os.path
from os import path
import time
import datetime
import requests
import json
import threading
def get_faqs(context,limit,window):
    headers = {'content-type': 'application/json'}
    print("Before API Call")
    response = requests.post('https://faq-generator.loca.lt/api', timeout=1000, json = {"context":context,"limit":limit})
    print(response)
    t=response.text
    print("After API Call")
    t = json.loads(response.text)
    #print(t)
    faqs=[]
    for i in t:
        print(i["question"])
        print(i["answer"])
        faqs.append(i["question"])
        faqs.append(i["answer"])
    faq_window(faqs)
    '''
    time.sleep(3)
    faqs=["1","2","3"]
    faq_window(faqs)
    '''
    window.write_event_value('-THREAD-', '** DONE **')
#sg.theme('DarkAmber')
def feedback_window():
    layout=[[sg.Text("Enter Name"),sg.Input()],
            [sg.Text("Provide Feedback",justification='center',size=(300,1))],
            [sg.Multiline(size=(80, 10), key='textbox')],
            [sg.Button("Submit",key="-SUBMIT-",size=(22,1)),sg.Button("Clear",key="-CLEAR-",size=(22,1))]
            ]
    window=sg.Window("Feedback",layout,size=(400,300),modal=True)
    while True:
        event,values=window.read()
        if event=='Exit' or event==sg.WIN_CLOSED:
            break
        if event=='-SUBMIT-':
            name=values[0]
            p=values['textbox']
            if len(name)!=1 and len(p)!=1 and p!='':
                header=0
                if not(path.exists('feed.csv')):
                    header=1
                with open("feed.csv",mode='a',newline='') as file:
                    fieldnames=['name','feedback','time']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    if header:
                        writer.writeheader()
                    today=datetime.datetime.now()
                    writer.writerow({'name':name,'feedback':p,'time':today})
                    window.close()
            else:
                caution_window()
        if event=='-CLEAR-':
            print("clear")
            window['textbox']('')
    window.close()
def manual_window():
    layout=[[sg.Text('This software takes in a summarized text and',justification='center',size=(400,1))],
            [sg.Text('generates relevent Frequently Asked Questions',justification='center',size=(400,1))],
            [sg.Text('from the given text.',justification='center',size=(400,1))],
            [sg.Text('Enter passage into text area and hit the',justification='center',size=(400,1))],
            [sg.Text('Generate Button to get the FAQs.',justification='center',size=(400,1))]]
    window=sg.Window("About",layout,size=(300,200),modal=True)
    while True:
        event,values=window.read()
        if event=='Exit' or event==sg.WIN_CLOSED:
            break
    window.close()
def about_window():
    layout=[[sg.Text('About the Product : Version 1.0',justification='center',size=(400,1))],
            [sg.Text('Developed at PES University, Bengaluru, India',justification='center',size=(400,1))],
            [sg.Text('Developers:',justification='center',size=(400,1))],
            [sg.Text('Punit Koujalgi',justification='center',size=(400,1))],
            [sg.Text('Santosh Vasisht',justification='center',size=(400,1))],
            [sg.Text('Akhil Eppa',justification='center',size=(400,1))],
            [sg.Text('Varun Tirthani',justification='center',size=(400,1))],
            [sg.Text('-----Developed Using Python 3.8------',justification='center',size=(400,1))]]
    window=sg.Window("About",layout,size=(300,250),modal=True)
    while True:
        event,values=window.read()
        if event=='Exit' or event==sg.WIN_CLOSED:
            break
    window.close()
def caution_window():
    layout=[[sg.Text('Kindly input passage into text area!',justification='center',size=(400,200))]]
    window=sg.Window("Caution",layout,size=(300,100),modal=True)
    while True:
        event,values=window.read()
        if event=='Exit' or event==sg.WIN_CLOSED:
            break
    window.close()

def caution_window2():
    layout=[[sg.Text('Kindly input numerical value for number of FAQs!',justification='center',size=(400,200))]]
    window=sg.Window("Caution",layout,size=(300,100),modal=True)
    while True:
        event,values=window.read()
        if event=='Exit' or event==sg.WIN_CLOSED:
            break
    window.close()

def faq_window(faqs):
    layout=[[sg.Listbox(values=faqs, enable_events=False, size=(600, 30), key='FAQ_List')]]
    window=sg.Window("FAQs",layout,size=(600,400),modal=True)
    while True:
        event,values=window.read()
        if event=="Exit" or event==sg.WIN_CLOSED:
            break
    window.close()
def check(x):
    if len(x)<1:
        return False
    try:
        x=int(x)
        return True
    except:
        return False
def main():
    menu_def = [['&Support', '&Feedback'],
                ['&Help',['&Manual','&About']]]
    layout=[[sg.Menu(menu_def, tearoff=False)],
            [sg.Text('Auto FAQ Generator',justification='center',size=(600,1),font=("Arial",20),text_color="lightblue")],
            [sg.Text("Enter text summary/Passage",justification='center',font=("Arial",14),size=(600,1))],
            [sg.Multiline(size=(80, 20), key='textbox')],
            [sg.Text('Number of FAQS :', justification='right'),sg.Input(justification='center',key='limit',size=(10,1))],
            [sg.Button('Generate',size=(200,1),key='-GENERATE-')],
            [sg.Button('Clear',size=(35,1),key='-CLEAR-'),sg.Button('Exit',size=(35,1))]]
    window=sg.Window('AutoFAQGen',layout,size=(600,500),element_justification='c')

    while True:
        event, values = window.read()
        
        
        if event in (None, 'Exit'):
            break
        elif event=="About":
            about_window()
            #sg.popup('Developed at PES University in ','Collaboration with Dr. Ramamoorthy Srinath')
            print('about')
        elif event=="Manual":
            manual_window()
            print('manual')
        elif event=="Feedback":
            feedback_window()
            print("feedback")
        elif event == '-GENERATE-':
            print("Asked to generate")
            context=values['textbox']
            limit=values['limit']

            if len(context)!=1 and context!=' ' and context!=None:
                if check(limit):    
                    #faqs=[str(i)+". ------------------------\n" for i in range(10)]
                    #faq_window(faqs)
                    threading.Thread(target=get_faqs, args=(context, limit, window), daemon=True).start()
                    layout=[[sg.Text('FAQs are being Generated....',justification='center',size=(400,200))]]
                    load=sg.Window("Caution",layout,size=(300,100),modal=True)
                    while True:
                        event,values=load.read()
                        if event=="Exit" or event=="Alarm" or event==sg.WIN_CLOSED:
                            break
                    
                    #get_faqs(context,limit)
                else:
                    caution_window2()
            else:
                caution_window()
        elif event == '-CLEAR-':
            print("clear")
            window['textbox']('')
            window['limit']('')
            #window.FindElement('-CLEAR-').Update('')
        elif event == '-THREAD-':
            load.close()
            print("Done with API Call")
    window.close()

if __name__=="__main__":
    main()
    