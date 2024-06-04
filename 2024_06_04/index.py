from pprint import pprint
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tools
from tkinter import messagebox
from tkinter.simpledialog import Dialog

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('AQI顯示')
        #定義style的名稱
        style = ttk.Style()
        style.configure('Top.TFrame')
        style.configure('Top.TLabel',font=('Helvetica',25,'bold'))

        title_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=2,relief='groove')
        ttk.Label(title_frame,text='全台空氣品質指標(AQI)',style='Top.TLabel').pack(expand=True,fill='y')
        title_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

        func_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=1,relief='groove')
        ttk.Button(func_frame,text="AQI品質最好的5個",command=self.click1).pack(side='left',expand=True)
        ttk.Button(func_frame,text="AQI品質最差的5個",command=self.click2).pack(side='left',expand=True)
        ttk.Button(func_frame,text="pm2.5品質最好的5個",command=self.click3).pack(side='left',expand=True)
        ttk.Button(func_frame,text="pm2.5品質最好的5個",command=self.click4).pack(side='left',expand=True)
        func_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)
    
    def click1(self):
        messagebox.showinfo("information","Infomative message")
    
    def click2(self):
        messagebox.showerror("Error","Error message")

    def click3(self):
        messagebox.showwarning("Warning","Warning message")
    
    def click4(self):
        ShowInfo(parent=self,title="這是Dialog")

class ShowInfo(Dialog):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def body(self, master):
        text = tk.Text(self,height=8,font=('Helvetica',30),width=40)
        text.pack(padx=10,pady=10)
        text.insert(tk.INSERT,'kkura')
        text.configure(state='disabled')
        return None
        
def main():
    '''
    try:
        all_data:dict[any] = tools.download_json()
    except Exception as error:
        print(error)
    else:        
        data:list[dict] = tools.get_data(all_data)
        pprint(data)
    '''

    window = Window(theme="itft1")
    window.mainloop()

if __name__ == '__main__':
    main()