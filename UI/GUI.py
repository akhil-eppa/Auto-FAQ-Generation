# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:51:03 2021

@author: Akhil
"""
import csv
import PySimpleGUI as sg
import os.path
from os import path
import datetime

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

def faq_window(faqs):
    layout=[[sg.Listbox(values=faqs, enable_events=False, size=(600, 30), key='FAQ_List')]]
    window=sg.Window("FAQs",layout,size=(600,400),modal=True)
    while True:
        event,values=window.read()
        if event=="Exit" or event==sg.WIN_CLOSED:
            break
    window.close()
def main():
    menu_def = [['&Support', '&Feedback'],
                ['&Help',['&Manual','&About']]]
    layout=[[sg.Menu(menu_def, tearoff=False)],
            [sg.Text('Auto FAQ Generator',justification='center',size=(600,1),font=("Arial",20),text_color="lightblue")],
            [sg.Text("Enter Text Summary/Passage",justification='center',font=("Arial",14),size=(600,1))],
            [sg.Multiline(size=(80, 20), key='textbox')],
            [sg.Button('Generate',size=(200,1),key='-GENERATE-')],
            [sg.Button('Clear',size=(35,1),key='-CLEAR-'),sg.Button('Exit',size=(35,1))]]
    window=sg.Window('AutoFAQGen',layout,size=(600,500))

    while True:
        event, values = window.read()
        
        
        if event in (None, 'Exit'):
            break
        if event=="About":
            about_window()
            #sg.popup('Developed at PES University in ','Collaboration with Dr. Ramamoorthy Srinath')
            print('about')
        if event=="Manual":
            manual_window()
            print('manual')
        if event=="Feedback":
            feedback_window()
            print("feedback")
        if event == '-GENERATE-':
            print("Asked to generate")
            p=values['textbox']
            
            if len(p)!=1 and p!=' ' and p!=None:
                faqs=[str(i)+". ------------------------\n" for i in range(10)]
                faq_window(faqs)
            else:
                caution_window()
        if event == '-CLEAR-':
            print("clear")
            window['textbox']('')
            #window.FindElement('-CLEAR-').Update('')
    window.close()

if __name__=="__main__":
    main()
    