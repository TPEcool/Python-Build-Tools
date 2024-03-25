from ttkbootstrap import *
from file_explorer import init
win = Window('Python Build Tools', 'darkly_bgdark', size=(625, 600), resizable=(False, False))

tabs = Notebook(win)
explorertab = Frame(tabs)
explorer_menuframe = Frame(explorertab, height=50)  # Fixed-size region of height 50
explorer_menuframe.pack(side=TOP, fill=BOTH)

explorer_frame = Frame(explorertab)
explorer_frame.pack(expand=True, fill=BOTH)  # Adjusted packing options to expand vertically

tabs.pack(side=TOP, expand=True, fill=BOTH, anchor=N)

explorer_menu = Menu(explorer_frame)
explorer_filemenu = Menu(explorer_menu)
explorer_menu.add_cascade(menu=explorer_filemenu, label='File')

Menubutton(explorer_menuframe, menu=explorer_filemenu, text='File', style=(LIGHT, OUTLINE)).pack(side=TOP, anchor=NW, expand=True)

init(explorer_frame, explorer_filemenu)

builder_tab = Frame(tabs)

tabs.add(builder_tab, text='Executable builder', sticky='nsew')  # Adjusted sticky parameter
tabs.add(explorertab, text='Asset explorer', sticky='nsew')  # Adjusted sticky parameter



win.mainloop()