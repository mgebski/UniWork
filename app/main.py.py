#-*-coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

import hashlib


Config.set('graphics', 'width', '1440')
Config.set('graphics', 'height', '2960')

def hash_password(password, salt):
    
    b_password = password.encode('utf8')
    b_salt = salt.encode('utf8')
    dk = hashlib.pbkdf2_hmac('sha512', b_password, b_salt, 10000)
    return dk.hex()



class MainWindow(Screen):
    
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def btn(self):
        
        email=self.email.text
        password=self.password.text
        
        hashed_password=hash_password(password,"1")
        
        self.email.text=""
        self.password.text=""
        

    
  


class SecondWindow(Screen):
    
    def btn(self):
        print("hello")

class ThirdWindow(Screen):
    
    pass

class FourthWindow(Screen):
    pass


class FifthWindow(Screen):
    
    searchbar = ObjectProperty(None)
    
        
    def btn1(self):
        def btn():
            print("hello")
        self.ids.grid.clear_widgets()
        searchbar = self.searchbar.text
        
        result=[]
        if searchbar!="":
            
            result.append(searchbar)
        x=0
        for i in range(len(result)): 
            button = Button(text=result[x],
                            background_color =(0, 0, 0, 0.7),
                            size_hint=(None,None),
                            width=(400),
                            )
        
            self.ids.grid.add_widget(button)
            x=x+1
    
            
           
    
class SixthWindow(Screen):
    pass
class SeventhWindow(Screen):
    pass
class EigthWindow(Screen):
    pass
class NinthWindow(Screen):
    email = ObjectProperty(None)
    username =  ObjectProperty(None)
    password = ObjectProperty(None)
    con_password = ObjectProperty(None)
    dob = ObjectProperty(None)
    
    def btn(self):
        
        email=self.email.text
        username=self.username.text
        password=self.password.text
        con_password=self.con_password.text
        dob=self.dob.text
        if password==con_password:
            hashed_password=hash_password(password,"1")
            
        else:
            self.password.text=""
            self.con_password.text=""
        
        
        
        

class ImageButton(ButtonBehavior, Image):
    def on_press(self):  
        print ('pressed')

class WindowManager(ScreenManager):
    pass





kv = Builder.load_file('my.kv')
class MyApp(App):
      
    def build(self):
        
        return kv
    
  
MyApp().run()
 
 
