"""
TEST GUI
"""

from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
    """Displays a label"""
    """Sets up the window and the label"""
    def __init__(self):
         EasyFrame.__init__(self,title = "Label Demo")
         self.label1 = self.addLabel(text = "Label 1", row = 1,column = 0)
         self.label2 = self.addLabel(text = "Label 2", row = 2,column = 0)
         self.addButton(text = "This is a Button One", row = 3,column = 0,command = self.buttonOne)
         self.addButton(text = "This is a Button Two", row = 3,column = 25,command = self.buttonTwo)
    def buttonOne(self):
            """Handles the button one event"""
            self.label1["text"] = "You pressed button one."
    def buttonTwo(self):
            """Handles the button two event"""
            self.label2["text"] = "You pressed button two."
def main():
         """Instantiates and pops up the window"""
         LabelDemo().mainloop()
if __name__ == "__main__":
       main()