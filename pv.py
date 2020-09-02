#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import time

var = 1
root = tk.Tk()
list_label = []
list_text = []

#def input_timer():

"""
def startButtonClick():
    global app
    global start_flag
    global start_time
    global after_id
    global cout

    if not start_flag:
"""

#def resetButtonClick():

#def update():

def inc_command(beta):
    global var
    if(var <= 6):
        label = tk.Label(root, text='変数' + str(var))
        list_label.append(label)
        label.place(x=90, y=30 + (var * 50 ))
        text = tk.Entry(root)
        if(var == 1):
            text.insert(tk.END, '(作業全体時間)')
        else:
            text.insert(tk.END, 'ex twitter')
        
        list_text.append(text)
        text.place(x=90, y=30 + (var * 50 ) + 20)

        #となりにストップウォッチの配置
        var = var + 1
    else:
        print("変数は6つまで")

def dec_command():
    global var
    global list_label
    global list_text
    
    if(len(list_label) != 0):       
        #print(list_label)
        list_label[var-2].destroy()
        #print(list_text)
        list_text[var-2].destroy()
        del list_label[var-2]
        del list_text[var-2] 
        var = var - 1
    else:
        print("リストが空")

def output():
    print("結果の出力")

# メイン
if __name__ == '__main__':
    root.title("環境係数による生産性の測定")
    root.geometry("700x400")

    #割り込みを行う変数入力
    #変数増加ボタン
    inc_Button = tk.Button(root, text='増やす')
    inc_Button.bind("<Button-1>", inc_command)
    inc_Button.place(x=90, y=5)


    #変数減少ボタン
    dec_Button = tk.Button(root, text='減らす', command=dec_command)
    dec_Button.place(x=190, y=5)

    #結果のアウトプットボタン
    out_Button = tk.Button(root, text='出力', command=output)
    out_Button.place(x=390, y=5)

    root.mainloop()
