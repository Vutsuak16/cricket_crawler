__author__ = 'kaustuv'
import wx
import vutsuak
import SQL
import wx.lib.agw.hyperlink as hl


class MainPanel(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Cricket ", size=(1300,700))
        panel = wx.Panel(self)
        image_file = '/home/kaustuv/Desktop/app_background.jpeg'


        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(panel, -1, bmp1, (0, 0))
        button1 = wx.Button(panel, label="Player", pos=(100, 200), size=(220, 50))
        button2 = wx.Button(panel, label="Country", pos=(100, 275), size=(220, 50))
        button3 = wx.Button(panel, label="Role", pos=(100, 350), size=(220, 50))
        button4 = wx.Button(panel, label="Batsmen", pos=(100, 425), size=(220, 50))
        button5 = wx.Button(panel, label="Bowlers", pos=(100, 500), size=(220, 50))
        button6 = wx.Button(panel, label="Exit", pos=(1050, 600), size=(220, 50))
        button7 = wx.Button(panel, label="Crawl", pos=(1050, 300), size=(220, 50))
        button1.SetBackgroundColour('LIGHTGREEN')
        button2.SetBackgroundColour('LIGHTGREEN')
        button3.SetBackgroundColour('LIGHTGREEN')
        button4.SetBackgroundColour('LIGHTGREEN')
        button5.SetBackgroundColour('LIGHTGREEN')
        button6.SetBackgroundColour('LIGHTGREEN')
        button7.SetBackgroundColour('LIGHTGREEN')

        self.Bind(wx.EVT_BUTTON, self.run_player, button1)
        self.Bind(wx.EVT_BUTTON, self.run_country, button2)
        self.Bind(wx.EVT_BUTTON, self.run_role, button3)
        self.Bind(wx.EVT_BUTTON, self.run_batsmen, button4)
        self.Bind(wx.EVT_BUTTON, self.run_bowlers, button5)
        self.Bind(wx.EVT_BUTTON, self.closebutton, button6)
        self.Bind(wx.EVT_BUTTON, self.run_crawler, button7)


    def closebutton(self, event):
        self.Close(True)
        exit(0)

    def run_crawler(self, event):
        box = wx.TextEntryDialog(None, "Enter the name of the Player", "Cricket")
        box.SetBackgroundColour('light grey')
        if box.ShowModal() == wx.ID_OK:
            player = box.GetValue()
            vutsuak.imp_funct(player)
            data=vutsuak.retdata()[0]
            crawler_links=vutsuak.retdata()[1]
            pos=15
            ct=0
            for i in crawler_links:
                text1=hl.HyperLinkCtrl(self,-1,label=i,pos=(350,pos),URL="")
                text1.AutoBrowse(True)
                text1.SetColours("BLUE", "BLUE", "BLUE")
                text1.EnableRollover(True)
                text1.SetUnderlines(False, False, True)
                text1.SetBold(True)
                text1.OpenInSameWindow(True)
                text1.SetToolTip(wx.ToolTip("LINK!!!!!"))
                text1.UpdateLink()

                pos += 15
                ct+=1
                if ct>50:
                    break
            SQL.insert_db(data)


        else:

            text=wx.TextCtrl(self,-1,"You have cancelled the Application",size=(675,550),pos=(350,100))
            text.SetBackgroundColour('light grey')
            font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
            text.SetFont(font)

    def run_player(self, event):

        box = wx.TextEntryDialog(None, "Enter the name of the Player", "Cricket")
        box.SetBackgroundColour('light grey')
        if box.ShowModal() == wx.ID_OK:
            player = box.GetValue()
            disp=SQL.showall_db(arg1="pname",arg2="%"+player+"%",arg3="check")
            text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
            text.SetBackgroundColour('light grey')

            font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
            text.SetFont(font)

            checks = ['Country','Born','Current Age','Major Teams','Profile', 'Images', 'All Info']
            modal = wx.SingleChoiceDialog(None, "", "CHOICES", checks)
            if modal.ShowModal() == wx.ID_OK:
                choice= modal.GetStringSelection()
                disp=SQL.showall_db(arg1="pname",arg2="%"+player+"%",arg3=choice)
                text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
                text.SetBackgroundColour('light grey')
                font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
                text.SetFont(font)

        else:

            text=wx.TextCtrl(self,-1,"You have cancelled the Application",size=(675,550),pos=(350,100))
            text.SetBackgroundColour('light grey')
            font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
            text.SetFont(font)


    def run_country(self, event):
        box = wx.TextEntryDialog(None, "Enter the name of the Country", "Cricket")
        box.SetBackgroundColour('light grey')
        if box.ShowModal() == wx.ID_OK:
            country = box.GetValue()
            disp=SQL.showall_db(arg1="pcountry",arg2="%"+country+"%",arg3="check")
            text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
            text.SetBackgroundColour('light grey')
            font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
            text.SetFont(font)

            checks = ['Player Name','Images', 'All Info']
            modal = wx.SingleChoiceDialog(None, "", "CHOICES", checks)
            if modal.ShowModal() == wx.ID_OK:
                choice= modal.GetStringSelection()
                disp=SQL.showall_db(arg1="pcountry",arg2="%"+country+"%",arg3=choice)
                text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
                text.SetBackgroundColour('light grey')
                font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
                text.SetFont(font)

            else:
                text=wx.TextCtrl(self,-1,"You have cancelled the Application",size=(675,550),pos=(350,100))
                text.SetBackgroundColour('light grey')
                font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
                text.SetFont(font)

    def run_role(self, event):
        box = wx.TextEntryDialog(None, "Enter the Role of Player", "Cricket")
        box.SetBackgroundColour('light grey')
        if box.ShowModal() == wx.ID_OK:
            role = box.GetValue()
            disp=SQL.showall_db(arg1="prole",arg2="%"+role+"%",arg3="check")
            text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
            text.SetBackgroundColour('light grey')
            font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
            text.SetFont(font)

            checks = ['Player Name','Country','All Info']
            modal = wx.SingleChoiceDialog(None, "", "CHOICES", checks)
            if modal.ShowModal() == wx.ID_OK:
                choice= modal.GetStringSelection()
                disp=SQL.showall_db(arg1="prole",arg2="%"+role+"%",arg3=choice)
                text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
                text.SetBackgroundColour('light grey')
                font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
                text.SetFont(font)

            else:
                text=wx.TextCtrl(self,-1,"You have cancelled the Application",size=(675,550),pos=(350,100))
                text.SetBackgroundColour('light grey')
                font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
                text.SetFont(font)

    def run_batsmen(self, event):
        box = wx.TextEntryDialog(None, "Enter Batting Style", "Cricket")
        box.SetBackgroundColour('light grey')
        if box.ShowModal() == wx.ID_OK:
            batsmen = box.GetValue()
            disp=SQL.showall_db(arg1="pbatt",arg2="%"+batsmen+"%",arg3="check")
            text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
            text.SetBackgroundColour('light grey')
            font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
            text.SetFont(font)

            checks = ['Player Name','Country','All Info']
            modal = wx.SingleChoiceDialog(None, "", "CHOICES", checks)
            if modal.ShowModal() == wx.ID_OK:
                choice= modal.GetStringSelection()
                disp=SQL.showall_db(arg1="pbatt",arg2="%"+batsmen+"%",arg3=choice)
                text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
                text.SetBackgroundColour('light grey')
                font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
                text.SetFont(font)

            else:
                text=wx.TextCtrl(self,-1,"You have cancelled the Application",size=(675,550),pos=(350,100))
                text.SetBackgroundColour('light grey')
                font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
                text.SetFont(font)

    def run_bowlers(self, event):
        box = wx.TextEntryDialog(None, "Enter Bowling Style", "Cricket")
        box.SetBackgroundColour('light grey')
        if box.ShowModal() == wx.ID_OK:
            bowlers = box.GetValue()
            disp=SQL.showall_db(arg1="pbowl",arg2="%"+bowlers+"%",arg3="check")
            text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
            text.SetBackgroundColour('light grey')
            font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
            text.SetFont(font)

            checks = ['Player Name','Country','All Info']
            modal = wx.SingleChoiceDialog(None, "", "CHOICES", checks)
            if modal.ShowModal() == wx.ID_OK:
                choice= modal.GetStringSelection()
                disp=SQL.showall_db(arg1="pbowl",arg2="%"+bowlers+"%",arg3=choice)
                text=wx.TextCtrl(self,-1,disp,size=(675,550),pos=(350,100))
                text.SetBackgroundColour('light grey')
                font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
                text.SetFont(font)

            else:
                text=wx.TextCtrl(self,-1,"You have cancelled the Application",size=(675,550),pos=(350,100))
                text.SetBackgroundColour('light grey')
                font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
                text.SetFont(font)


if __author__ == 'kaustuv':
    app = wx.PySimpleApp()
    frame = MainPanel(parent=None, id=1)
    frame.Show()
    app.MainLoop()