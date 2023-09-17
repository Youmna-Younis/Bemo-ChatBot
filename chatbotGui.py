from tkinter import *
from chat_with_bot import get_reponse


#Define colors

#color dark  blue "#6fa5b1"  ,  green "#4e6b9f"
BG_COLOR  ="#220e24"

BG_GRAY="#e6dae2"
TEXT_COLOR = "#634258"
purple='#581845'
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApp:
    def __init__(self):
        self.window=Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()
    def _setup_main_window(self):
        self.window.title('chat')
        #self.window.resizable(width=False, height=False)
        self.window.configure(width=770, height=650,bg=BG_COLOR)
        #head label
        head_label=Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,text='ChatBot', font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)


        #divider
        line=Label(self.window,width=450,bg=TEXT_COLOR)
        line.place(relwidth=1, rely=0.07, relheight=0.012)


        #text
        self.text_widget=Text(self.window,width=20,height=2,bg=BG_COLOR,fg=TEXT_COLOR, font=FONT_BOLD, pady=5,padx=5)
        self.text_widget.place(relwidth=1, rely=0.08, relheight=0.745)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        #scrolbar
        scrolbar=Scrollbar(self.text_widget)
        scrolbar.place(relheight=1,relx=0.974)
        scrolbar.configure(command=self.text_widget.yview)

        # #bottom
        # bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        # bottom_label.place(relwidth=1, rely=0.825)
        # #send button
        # send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=purple,
        #                      command=lambda: self._on_enter_pressed(None))
        # # send_button.place(relheight=0.06,relwidth=0.22, rely=0.008,relx=0.77)
        # send_button.place (relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        bottom_label = Label(self.window, bg=BG_COLOR, height=40,fg=BG_COLOR)
        bottom_label.place(relwidth=1, rely=0.900)

        # Create the "Send" button with a distinct background color
        send_button = Button(
            bottom_label,
            text="Send",
            font=FONT_BOLD,
            width=20,
            bg=TEXT_COLOR,  # Change the background color to something noticeable
            command=lambda: self._on_enter_pressed(None)

        )
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


        #message box
        self.msg_entry=Entry(bottom_label,bg=BG_GRAY,fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>",self._on_enter_pressed)

    #in case enter is pressed without write any message
    def _insert_message(self,msg,sender):
          if not msg:
                     return
          self.msg_entry.delete(0,END)
          msg1=f"{sender}:{msg}\n\n"
          self.text_widget.configure(state=NORMAL)
          self.text_widget.insert(END,msg1)
          self.text_widget.configure(state=DISABLED)


          msg2=f"{'Bemo'} : {get_reponse(msg)}\n\n"
          self.text_widget.configure(state=NORMAL)
          self.text_widget.insert(END, msg2)
          self.text_widget.configure(state=DISABLED)

          self.text_widget.see(END)

    def _on_enter_pressed(self,event):
            msg=self.msg_entry.get()
            self._insert_message(msg,'you')
    #send button




if __name__=="__main__":
     app=ChatApp()
     app.run()