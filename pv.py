#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import time
import sys

#sys.setrecursionlimit(200000)

var = 1
root = tk.Tk()
list_label = []
list_text = []
list_time = []
list_starttime = []
list_endtime = []

list_time_start = []
list_time_stop = []
start_Button = tk.Button()
stop_Button = tk.Button()
after_id_list = []

#タイマーの更新頻度[ms]
INTERVAL = 10

def getText(event):
    #global var
    #print(var)
    #var = var_text.get()
    print(event)
    index_num = list_time.index(event)
    print(index_num)
    startButtonClick(index_num)
    

def startButtonClick(start_button):
    print("start")
    global list_time_start   
    #print(list_time_start)
    #print(len(list_time_start))
    #list_index = list_time_start.index(start_button)
    #print(str(list_time[start_button].cget("text")) + " " + "okkkkkkkkkkkkkkk")
    if(list_time[start_button].cget("text") == "0.00"):
        list_index = start_button
        start_time = time.time()
        list_starttime[start_button] = start_time
        #print(list_index)
        #print(start_time)
        update_time(list_index, start_time)
        #root.after(INTERVAL, update_time(list_index, start_time))
    elif(list_time[start_button].cget("text") == list_endtime[start_button]):
        list_index = start_button
        start_time = list_starttime[start_button]
        #print(list_index)
        #print(start_time)
        update_time(list_index, start_time)
        #root.after(INTERVAL, update_time(list_index, start_time))

def stopButtonClick(stop_button):
    print("stop")
    index_num = list_time.index(stop_button)
    root.after_cancel(after_id_list[index_num])
    list_endtime[index_num] = list_time[index_num].cget("text")
    print("stop " + list_endtime[index_num])

def update_time(Index, st_time):
    global list_time
    print(Index)
    print(st_time)
    after_id_list[Index] = root.after(50, lambda: update_time(Index, st_time))
    now_time = time.time()
    elapsed_time = now_time - st_time
    #print(str(elapsed_time) + " " + " " + str(now_time) + " " + " " + str(st_time))
    #elapsed_time_str = "{:4.2f}".format(elapsed_time)
    #elapsed_time_str = '{:.2f}'.format(elapsed_time)
    #list_time[Index].config(text=elapsed_time_str)
    elapsed_time_str = "{:.2f}".format(elapsed_time)
    list_time[Index].configure(text=elapsed_time_str)   
    #list_time[Index] = elapsed_time_str
   
    """
    while True:
        now_time = time.time()
        elapsed_time = now_time - st_time
        print(str(elapsed_time) + " " + " " + str(now_time) + " " + " " + str(st_time))
        #elapsed_time_str = "{:4.2f}".format(elapsed_time)
        #elapsed_time_str = '{:.2f}'.format(elapsed_time)
        #list_time[Index].config(text=elapsed_time_str)
        print(type(elapsed_time))
        elapsed_time_str = "{:.2f}".format(elapsed_time)
        print(type(elapsed_time_str))
        list_time[Index].configure(text=elapsed_time_str)   
        #list_time[Index] = elapsed_time_str
     """  

def inc_command():
    global var
    
    if(int(var) <= 6):
        label = tk.Label(root, text='変数' + str(var))
        list_label.append(label)
        label.place(x=40, y=30 + (var * 50 ))
        text = tk.Entry(root)
        if(var == 1):
            text.insert(tk.END, '(作業全体時間)')
        else:
            text.insert(tk.END, 'ex twitter')
        
        list_text.append(text)
        text.place(x=40, y=30 + (var * 50 ) + 20)

        #ストップウォッチの描画
        label_time = tk.Label(root, text="0.00", width=6,font=("", 25, "bold"),)
        label_time.place(x=200, y=25 + (var * 50) + 20)
        list_time.append(label_time)
        after_id_list.append(0)
        list_starttime.append("0.00")
        list_endtime.append("0.00")

        start_Button = tk.Button(root, text='START', command=lambda: getText(label_time))
        #start_Button.bind("<Button-1>", startButtonClick(list_time_start))
        start_Button.place(x=300, y=25 + (var * 50) + 20)
        list_time_start.append(start_Button)
        #startButtonClick(start_Button)

        stop_Button = tk.Button(root, text='STOP', command=lambda: stopButtonClick(label_time))
        #stop_Button.bind("<Button-1>", stopButtonClick(label_time))
        stop_Button.place(x=350, y=25 + (var * 50) + 20)   
        list_time_stop.append(stop_Button)

        
        #となりにストップウォッチの配置
        var = var + 1
    else:
        print("変数は6つまで")

def dec_command():
    global var
    global list_label
    global list_text
    global list_time
    global list_time_start
    global list_time_stop
    if(len(list_label) != 0):       
        list_label[var-2].destroy()
        list_text[var-2].destroy()
        list_time[var-2].destroy()
        list_time_start[var-2].destroy()
        list_time_stop[var-2].destroy()
        del list_label[var-2]
        del list_text[var-2] 
        del list_time[var-2]
        del list_time_start[var-2]
        del list_time_stop[var-2]

        var = var - 1
    else:
        print("リストが空")

def output():
    print("結果の出力")

# メイン
if __name__ == '__main__':
    #global start_Button
    #global stop_Button
    try:
        while True:
            root.title("環境係数による生産性の測定")
            root.geometry("700x400")

            #割り込みを行う変数入力
            var1 = tk.Label(text='変数の数')
            var1.place(x=30, y=5)
            var_text = tk.Entry(width=5)
            var_text.place(x=90,y=5)

            #変数増加ボタン
            inc_Button = tk.Button(root, text='増やす', command=inc_command)
            inc_Button.place(x=190, y=5)
    
            #変数減少ボタン
            dec_Button = tk.Button(root, text='減らす', command=dec_command)
            dec_Button.place(x=290, y=5)

            #結果のアウトプットボタン
            out_Button = tk.Button(root, text='出力', command=output)
            out_Button.place(x=390, y=5)

            #list_time_start[var].bind("<Button-1>", callback)
            #print(start_Button)
            #start_Button.bind("<Button-1>", callback(start_Button))

            root.mainloop()

    except KeyboardInterrupt:
        print("get Ctrl + C")
        sys.exit()
