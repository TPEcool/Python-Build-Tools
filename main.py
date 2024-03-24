from ttkbootstrap import *
from file_explorer import init
win = Window('Python Build Tools', 'darkly_bgdark', size=(900, 600))

tabs = Notebook(win)
explorertab = Frame(tabs)
explorer_frame = Frame(explorertab)
explorer_frame.pack(side=BOTTOM, expand=True, fill=BOTH)
tabs.add(explorertab, text='Asset explorer', sticky=N)
tabs.pack(side=TOP, expand=True, fill=BOTH, anchor=N)

explorer_menu = Menu(explorer_frame)
explorer_filemenu = Menu(explorer_menu)
explorer_menu.add_cascade(menu = explorer_filemenu, label='File')

Menubutton(explorertab, menu=explorer_filemenu, text='File', style=LIGHT+OUTLINE).pack(side=TOP, anchor=NW, expand=True)

init(explorertab, explorer_filemenu)

win.mainloop()