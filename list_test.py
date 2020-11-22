import tkinter as tk
import wes as w
import analytics as a

root = tk.Tk()
root.title("test")
root.geometry("500x500")

search_bar = tk.Entry(root)
search_bar.pack()

def uf():
    label1 = tk.Label(root, text="User found")
    label1.pack()

def src_fn():

    x = search_bar.get()
    if x in w.followerslist:
        uf()    
    else:
        label2 = tk.Label(root, text="User not found")
        label2.pack()

var = search_bar.get()
def an_fn():
    t_id = a.t_id
    t_uname = a.t_un
    t_sname = a.t_sn
    t_des = a.t_desc
    t_fc = a.t_fc
    tid = tk.Label(root,text="Twitter Id = "+str(t_id))
    tid.pack()
    tun = tk.Label(root,text="UserName = "+t_uname)
    tun.pack()
    tsn = tk.Label(root,text="ScreenName = "+t_sname)
    tsn.pack()
    tdes = tk.Label(root,text="Description = "+t_des)
    tdes.pack()
    tfc = tk.Label(root,text="Followers Count = "+str(t_fc))
    tfc.pack()

search_btn = tk.Button(root, text="Search", command=src_fn)
search_btn.pack()

an_btn = tk.Button(root, text="Get Analytics", command=an_fn)
an_btn.pack()
frame = tk.Frame(root)
scbar = tk.Scrollbar(frame, orient = "vertical")


followers_list_box = tk.Listbox(frame, yscrollcommand = scbar.set)
scbar.config(command=followers_list_box.yview)
scbar.pack(side="right", fill="y")
frame.pack()
followers_list_box.pack(pady=15)

for i in w.followerslist:
    followers_list_box.insert(0,i)



root.mainloop()
