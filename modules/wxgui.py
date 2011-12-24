# -*- coding: utf-8 -*-

from wx import App, Frame, StaticText, Button, EVT_BUTTON

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
        self.text = StaticText(self, -1,'0', (120, 40))
        button1 = Button(self, -1, '+', (10, 10))
        button2 = Button(self, -1, '-', (10, 60))
        
        self.Bind(EVT_BUTTON, self.OnPlus, id=button1.GetId())
        self.Bind(EVT_BUTTON, self.OnMinus, id=button2.GetId())
        
        self.Centre()
        
    def OnPlus(self, event):
        value = int(self.text.GetLabel())
        value = value + 1
        self.text.SetLabel(str(value))
        
    def OnMinus(self, event):
        value = int(self.text.GetLabel())
        value = value - 1
        self.text.SetLabel(str(value))
        
        
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