from tkinter import ttk

def config_style():
    '''introduit des styles pour tkinter'''
    s=ttk.Style()
    s.theme_use("clam")
    s.configure("TFrame",background="#BCD5EA")
    s.configure("TButton", padding=5, relief="flat",
    background="#D3E1ED")
    s.configure("TLabel",background="#BCD5EA")
 