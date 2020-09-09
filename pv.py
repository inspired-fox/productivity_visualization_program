#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import matplotlib as plt
#import numpy as np
import time
import sys;print(sys.version);print(sys.path)
#import sys

#sys.setrecursionlimit(200000)

var = 1
sum = 0
root = tk.Tk()
list_label = []
list_text = []
list_time = []
list_starttime = []
list_endtime = []
flag_list = []
elapsed_time_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

list_time_start = []
list_time_stop = []
start_Button = tk.Button()
stop_Button = tk.Button()
after_id_list = []

#タイマーの更新頻度[ms]
INTERVAL = 10

def getText(event):
    #print(event)
    index_num = list_time.index(event)
    startButtonClick(index_num)
    

def startButtonClick(Index):
    print("start")
    global list_time_start
    global flag_list   
    #print(list_time_start)
   
    if(elapsed_time_list[Index] == 0.0):
        #初回動作c
        start_time = time.time()
        flag_list[Index] = 1
        list_starttime[Index] = start_time
        update_time(Index, start_time)
    else:
        if(flag_list[Index] == 0):
            start_time = time.time()
            list_starttime[Index] = start_time
            update_time(Index, start_time)
        else:
            start_time = list_starttime[Index]
            update_time(Index, start_time)

def stopButtonClick(stop_button):
    global flag_list
    global elapsed_time_list
    global sum
    index_num = list_time.index(stop_button)

    print("stop")
    index_num = list_time.index(stop_button)
    root.after_cancel(after_id_list[index_num])
    list_endtime[index_num] = list_time[index_num].cget("text")
    print("stop " + list_endtime[index_num])
    flag_list[index_num] = 0
    elapsed_time_list[index_num] = sum
    print(elapsed_time_list)

def update_time(Index, st_time):
    global list_time
    global flag_list
    global elapsed_time_list
    global sum

    Hour = 0
    Min = 0
    Sec = 0.0

    #print(st_time)
    after_id_list[Index] = root.after(50, lambda: update_time(Index, st_time))
    
    now_time = time.time()
    #elapsed_time_list[Index] = now_time - st_time
    if(elapsed_time_list[Index] != 0.0):
        #前回のタイマー結果を加算
        #if(flag_list[Index] == 0):
        #タイマーが再開された時
        '''
        print("-----")
        print(elapsed_time_list[Index])
        print(now_time - st_time)
        print("----")
        '''
        sum = elapsed_time_list[Index] + now_time - st_time
        Hour = int((sum / 60) / 60)
        Min = int(sum / 60)
        Sec = sum % 60
        flag_list[Index] = 1


    else:
        #初めてのタイマー起動
        elapsed_time_list[Index] = now_time - st_time
        Hour = int((elapsed_time_list[Index] / 60) / 60)
        Min = int(elapsed_time_list[Index] / 60)
        Sec = elapsed_time_list[Index] % 60
        flag_list[Index] = 1

    elapsed_time_str = str(Hour) + ":" + str(Min) + ":" + format(Sec, '.1f')
    #elapsed_time_str = "{0}:{1}:{2:.2f}".format(Hour, Min, Sec)
    list_time[Index].configure(text=elapsed_time_str)


    
 

def inc_command():
    global var
    
    if(int(var) <= 6):
        label = tk.Label(root, text='変数' + str(var))
        list_label.append(label)
        label.place(x=40, y=30 + (var * 50 ))
        text = tk.Entry(root)
        if(var == 1):
            text.insert(tk.END, '作業全体時間')
        else:
            text.insert(tk.END, 'ex twitter')
        
        list_text.append(text)
        text.place(x=40, y=30 + (var * 50 ) + 20, width =100)

        #ストップウォッチの描画
        label_time = tk.Label(root, text="0.00", width=10,font=("", 25, "bold"),)
        label_time.place(x=200, y=25 + (var * 50) + 20)
        list_time.append(label_time)
        after_id_list.append(0)
        list_starttime.append("0.00")
        list_endtime.append("0.00")
        flag_list.append(0)
        #elapsed_time_list.append(0.0)

        start_Button = tk.Button(root, text='START', command=lambda: getText(label_time))
        #start_Button.bind("<Button-1>", startButtonClick(list_time_start))
        start_Button.place(x=400, y=25 + (var * 50) + 20)
        list_time_start.append(start_Button)
        #startButtonClick(start_Button)

        stop_Button = tk.Button(root, text='STOP', command=lambda: stopButtonClick(label_time))
        #stop_Button.bind("<Button-1>", stopButtonClick(label_time))
        stop_Button.place(x=450, y=25 + (var * 50) + 20)   
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
    global elapsed_time_list

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
        elapsed_time_list[var-2] = 0.0

        var = var - 1
    else:
        print("リストが空")

def output():
    print("結果の出力")
    global list_time
    global elapsed_time_list
    index_num = 0
    split_list = []
    Hour = 0
    Min = 0
    Sec = 0.0
    r = 0.0
    sum = 0.0

    WWT = 0 #作業全体時間
    OTV = [] #その他の変数時間
    

    for i in list_time:
        stopButtonClick(i)
        split_list = ((list_time[index_num].cget("text")).split(":"))
        Hour = int(split_list[0])
        Min = int(split_list[1])
        Sec = split_list[2]
        #print(split_list)
        if (index_num == 0):
            #WWT = format((Hour * 60.0 * 60.0 + Min * 60.0 + Sec), '.1f')
            WWT = float(Hour) * 60.0 * 60.0 + float(Min) * 60.0 + float(Sec)
        else:
            #torino = format((Hour * 60.0 * 60.0 + Min * 60.0 + Sec), '.1f') 
            OTV.append(float(Hour) * 60.0 * 60.0 + float(Min) * 60.0 + float(Sec))

        index_num += 1

    print("作業効率:")

    for i in OTV:
        sum = sum + i

    print(WWT / sum)
    r = WWT / sum

    ans = tk.Label(text='今日の作業効率は' + format(r, '.1f'),font=("", 15, "bold"),)
    ans.place(x=450, y=5)
    mapplot(ans)

def mapplot(ans_num):
    #描画領域
    fig, ax = plt.subplots(1, 1)

    #y軸方向の描画幅を指定
    ax.set_ylim((-1.1, 1.1))

    #x軸ー時刻
    x = np.arange(0, 24, 1)

    #y軸-作業効率
    y = ans_num

    #グラフの描画
    ax.plot(x, y, color='green')
    plt.show()



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
