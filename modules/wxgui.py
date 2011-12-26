# -*- coding: utf-8 -*-

from wx import *
'''
Created on 23.12.2011
wx Class for main frame
@author: maksim
'''

class MainFrame(Frame):
    '''
    classdocs
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        Frame.__init__(self, parent, -1, 'Iptv_creator')
        
        self.InitUI()
        self.text = StaticText(self, -1,'Пакеты.', (10, 40))
        self.cb1 = CheckBox(self, -1, 'Социальный',(10, 90))
        self.cb1.SetValue(False)
        self.text = StaticText(self, -1,'колличество: ', (10, 130))
        TextCtrl(self, pos=(120, 120), size=(40, 30))
        
        self.cb1 = CheckBox(self, -1, 'Базовый',(10, 90))
        self.cb1.SetValue(False)
        self.text = StaticText(self, -1,'колличество: ', (10, 130))
        TextCtrl(self, pos=(120, 120), size=(40, 30))
        
        self.cb1 = CheckBox(self, -1, 'Полный',(10, 90))
        self.cb1.SetValue(False)
        self.text = StaticText(self, -1,'колличество: ', (10, 130))
        TextCtrl(self, pos=(120, 120), size=(40, 30))
        
        button = Button(self, -1, '+', (10, 10))
        
        
        TextCtrl(self, pos=(300, 400), size=(250, 150))
        
        self.Bind(EVT_BUTTON, self.Gen, id=button.GetId())
        
        EVT_CHECKBOX(self, self.cb1.GetId(), self.SetCb1)
        
        self.SetSize((800, 600))
        self.Centre()
        
    def InitUI(self):    

        menubar = MenuBar()
        fileMenu = Menu()
        fitem = fileMenu.Append(ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        
        self.SetMenuBar(menubar)
        
        self.Bind(EVT_MENU, self.OnQuit, fitem)
        
    def SetCb1(self, event):
        if self.cb1.GetValue():
            self.setcb1 = True
        else: self.setcb1 = False
        
    def OnQuit(self, e):
        self.Close()
        
    def Gen(self):
        pass
        
        
        
class MainApp(App):

    def OnInit(self):
        frame = MainFrame(None)
        frame.Show()
        
        return True
  
def main():

    application = MainApp()
    application.MainLoop()
    
if __name__ == '__main__':
    main()