# -*- coding: utf-8 -*-

# Created by Hitesh Tiwari.

# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org  --no-cache-dir snowflake

# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org  --no-cache-dir pymysql


import tkinter

from tkinter import ttk

from tkinter import StringVar

from tkinter import messagebox

from tkinter.simpledialog import askstring

import tkinter as tk

import pyodbc

import snowflake.connector

import xlsxwriter

import logging

import datetime

import time

import webbrowser

import os

import csv

Teradata_Fields = ['username_tb', 'pwd_tb', 'db_nm_tb']

AEDL_Fields = 'HAID', 'Password', 'Env'

timestamp = time.strftime("%Y%m%d%H%M%S")


def welcome_formdesign():
    global InitVar

    global MasterFrame

    if InitVar == 1:
        MasterFrame.destroy()

        # print('Resetting The Form')

    root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    # root.geometry("1310x890")

    # Master PaneWindow which holds all the other panes.

    MasterFrame = ttk.Frame(root, padding='0.1i')

    MasterFrame.configure(height=1000, width=1000)

    MasterFrame.grid(row=0, column=0)

    InitVar = 1

    LLK_username_lbl = ttk.Label(master=MasterFrame, text='Welcome To Integrity!', font=160,
                                 foreground='#0a0a0a')  # '#007FFF')

    LLK_username_lbl.grid(row=0, column=0, sticky='nswe')

    # Credit_lbl=ttk.Label(master = MasterFrame, text='Designed by Hitesh Tiwari',font=10,foreground='#007FFF')

    # Credit_lbl.grid(row=10,column=10,sticky='se')

    update_progress('Welcome Form Rendering Completed', 'None')


def llk_formdesign():
    global InitVar

    global MasterFrame, dri_tree, progressbar

    if InitVar == 1:
        MasterFrame.destroy()

        # print('Resetting The Form')

    # Master PaneWindow which holds all the other panes.

    MasterFrame = tkinter.PanedWindow(root, orient='vertical', handlepad=5, sashpad=5, showhandle='true')

    MasterFrame.pack(expand=1, fill='both')

    InitVar = 1

    LLK_username_lbl = tkinter.Label(master=MasterFrame, text='LLK Form Design')

    MasterFrame.add(LLK_username_lbl)

    update_progress('LLK Form Rendering Completed', 'None')


def dri_formdesign():
    global InitVar

    global autofill_btn

    global MasterFrame, dri_tree, progressbar, info

    # root.geometry("")

    root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    # The below block of code helps with resetting the form.

    if InitVar == 1:
        MasterFrame.destroy()

        # print('Resetting The Form')

    # Master Frame which holds all the other widgets.

    MasterFrame = ttk.Frame(root, padding='0.1i')

    MasterFrame.grid(row=0, column=0)

    InitVar = 1

    # This LabledFrame holds Teradata Connection Items.

    TeraCred_LF = ttk.LabelFrame(master=MasterFrame, text="Step 1: Teradata Configurations", relief='raised',
                                 padding='0.2i')

    TeraCred_LF.grid(row=0, column=0, padx=10, sticky='nw')

    int_pady = 13

    username_lbl = ttk.Label(master=TeraCred_LF, text='User Name').grid(row=0, column=0, padx=0, pady=int_pady,
                                                                        sticky='w')

    username_tb = ttk.Entry(master=TeraCred_LF, textvariable=tUserName).grid(row=0, column=1, padx=20, pady=int_pady,
                                                                             sticky='nw')

    pwd_lbl = ttk.Label(master=TeraCred_LF, text='Password', anchor='w').grid(row=1, column=0, padx=0, pady=int_pady,
                                                                              sticky='w')

    pwd_tb = ttk.Entry(master=TeraCred_LF, show="*", textvariable=tPassword).grid(row=1, column=1, padx=20,
                                                                                  pady=int_pady, sticky='nw')

    tserver_init.set("Select the server")  # initial value

    # print("tserver_init: ",tserver_init.get())

    # tserver_list=["Select the server","DWDEVCOP1.CORP.ANTHEM.COM", "DWTEST2COP1.CORP.ANTHEM.COM", "DWTEST1COP1.CORP.ANTHEM.COM", "DWPROD2COP1.CORP.ANTHEM.COM"]

    odbc_lbl = ttk.Label(master=TeraCred_LF, text='Teradata Server').grid(row=2, column=0, padx=0, pady=int_pady,
                                                                          sticky='w')

    odbc_optmenu = ttk.OptionMenu(TeraCred_LF, tserver_init, tserver_init.get(), *tserver).grid(row=2, column=1,
                                                                                                padx=20, pady=int_pady,
                                                                                                sticky='nw')

    db_nm_lbl = ttk.Label(master=TeraCred_LF, text='Database Name').grid(row=3, column=0, padx=0, pady=int_pady,
                                                                         sticky='w')

    db_nm_tb = ttk.Entry(master=TeraCred_LF, textvariable=tdbname).grid(row=3, column=1, padx=20, pady=int_pady,
                                                                        sticky='nw')

    testCon_btn = ttk.Button(MasterFrame, text="Test Connection", style="Accent.TButton", command=lambda: TestConn())

    testCon_btn.grid(row=1, column=0, padx=25, pady=10, sticky="nsew")

    # This button exits the applciation. Need to figure out where to place this button.

    # cancel_btn = ttk.Button(MasterFrame,text="Cancel", style="Accent.TButton",command=root.destroy)

    # cancel_btn.grid(row=1, column=1, padx=25, pady=10, sticky="nsew")

    # This Frame holds the DRI configuration options.

    dri_lbl_frm = ttk.LabelFrame(master=MasterFrame, text="Step 2: Provide DRI Detail (Atleast 1)", relief='raised',
                                 padding='0.2i')

    dri_lbl_frm.grid(row=0, column=1, padx=10, sticky='nw')

    ipt_lbl = ttk.Label(master=dri_lbl_frm, text='IPT_NBR').grid(row=0, column=0, padx=0, pady=int_pady, sticky='w')

    ipt_tb = ttk.Entry(master=dri_lbl_frm, textvariable=iptnum).grid(row=0, column=1, padx=20, pady=int_pady,
                                                                     sticky='nw')

    CLLK_lbl = ttk.Label(master=dri_lbl_frm, text='CRCTD_LLK').grid(row=1, column=0, padx=0, pady=int_pady, sticky='w')

    CLLK_tb = ttk.Entry(master=dri_lbl_frm, textvariable=cllk).grid(row=1, column=1, padx=20, pady=int_pady,
                                                                    sticky='nw')

    tbl_nm_lbl = ttk.Label(master=dri_lbl_frm, text='Table Name').grid(row=3, column=0, padx=0, pady=int_pady,
                                                                       sticky='w')

    tbl_nm_tb = ttk.Entry(master=dri_lbl_frm, textvariable=tbl_nm).grid(row=3, column=1, padx=20, pady=int_pady,
                                                                        sticky='nw')

    filler_lbl = ttk.Label(master=dri_lbl_frm, text=' ').grid(row=4, column=0, padx=0, pady=20, sticky='w')

    dri_rtrv_btn = ttk.Button(MasterFrame, text="Retrieve DRI Details", style="Accent.TButton",
                              command=lambda: DRI_Retrieve())

    dri_rtrv_btn.grid(row=1, column=1, padx=25, pady=10, sticky="nsew")

    # This Frame holds the AEDL configuration options.

    aedl_lbl_frm = ttk.LabelFrame(master=MasterFrame, text="Step 4: AEDL Configurations", relief='raised',
                                  padding=('0.2i'))

    aedl_lbl_frm.grid(row=0, column=2, padx=10, sticky='nw')

    HAID_lbl = ttk.Label(master=aedl_lbl_frm, text='Heightend Account ID').grid(row=0, column=0, padx=0, pady=int_pady,
                                                                                sticky='w')

    HAID_tb = ttk.Entry(master=aedl_lbl_frm, textvariable=ha_id).grid(row=0, column=1, padx=20, pady=int_pady,
                                                                      sticky='nw')

    aedl_pwd_lbl = ttk.Label(master=aedl_lbl_frm, text='DB.Schema').grid(row=1, column=0, padx=0, pady=int_pady,
                                                                         sticky='w')

    aedl_pwd_tb = ttk.Entry(master=aedl_lbl_frm, textvariable=sDBName_SchemaName).grid(row=1, column=1, padx=20,
                                                                                       pady=int_pady, sticky='nw')

    aedl_server_init.set("Select the server")  # initial value

    # aedl_server=["Select the server","carelon-edaprod1.privatelink","carelon-eda_nonprod.privatelink"]

    aedl_env_lbl = ttk.Label(master=aedl_lbl_frm, text='Snowflake Server').grid(row=2, column=0, padx=0, pady=int_pady,
                                                                                sticky='w')

    aedl_optmenu = ttk.OptionMenu(aedl_lbl_frm, aedl_server_init, aedl_server_init.get(), *aedl_server).grid(row=2,
                                                                                                             column=1,
                                                                                                             padx=20,
                                                                                                             pady=int_pady,
                                                                                                             sticky='nw')

    aedl_warehouse = ttk.Label(master=aedl_lbl_frm, text='Snowflake Warehouse').grid(row=4, column=0, padx=0,
                                                                                     pady=int_pady, sticky='w')

    aedl_warehouse_tb = ttk.Entry(master=aedl_lbl_frm, textvariable=aedl_wh).grid(row=4, column=1, padx=20,
                                                                                  pady=int_pady, sticky='nw')

    aedl_compare_btn = ttk.Button(MasterFrame, text="Begin Compare", style="Accent.TButton",
                                  command=lambda: begin_compare())

    aedl_compare_btn.grid(row=1, column=2, padx=25, pady=10, sticky="nsew")

    # output_pane = ttk.PanedWindow(MasterFrame)

    # output_pane.config(bg='pink')

    # output_pane.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew", rowspan=13)

    # MasterFrame.grid_columnconfigure(0,weight=1)

    # MasterFrame.grid_rowconfigure(3,weight=1)

    output_lbl_frm = ttk.LabelFrame(master=MasterFrame, text="Step 3: Make A Selection", relief='raised',
                                    padding=('0.2i'), width=100, height=490)

    # output_lbl_frm.grid(row=0,column=0,sticky="nsew")

    output_lbl_frm.grid(row=2, column=0, columnspan=3, rowspan=25, padx=10, sticky="nsew")

    output_lbl_frm.pack_propagate(False)

    # dri_columns=('IPT_NBR','SOR_CD','TBL_NM','KEY_CLMN_NM','CRCTN_CLMN_NM','LOAD_LOG_KEY','RCRD_CRCTN_TYPE_CD','CRCTN_EXECTN_DTM')

    dri_columns = (
    'TBL_NM', 'KEY_CLMN_NM', 'CRCTN_CLMN_NM', 'SOR_CD', 'LOAD_LOG_KEY', 'CRCTN_EXECTN_DTM', 'RCRD_CRCTN_TYPE_CD',
    'IPT_NBR', 'LOAD_LOG_KEY_TYPE_CD')

    dri_tree = ttk.Treeview(output_lbl_frm, columns=dri_columns, show='headings')

    dri_tree.pack(fill='both', expand='true')

    # dri_tree.grid(row=0, column=0, pady=10, sticky="ew")

    dri_vert_scrollbar = ttk.Scrollbar(dri_tree, orient='vertical', command=dri_tree.yview)

    dri_tree.config(yscroll=dri_vert_scrollbar.set)

    dri_vert_scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    dri_hori_scrollbar = ttk.Scrollbar(dri_tree, orient='horizontal', command=dri_tree.xview)

    dri_tree.configure(xscrollcommand=dri_hori_scrollbar.set)

    dri_hori_scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')

    dri_tree.bind('<Double-1>', (lambda event: on_double_click(output_lbl_frm, dri_tree, event)))

    for clmn in dri_columns:
        dri_tree.column(clmn, anchor='w', stretch=False)

        dri_tree.heading(clmn, text=clmn)

    # for i in range(1,100):

    #   dri_tree.insert('','end',values=i)

    EasyOfUseFrame = ttk.LabelFrame(master=MasterFrame, text="Ease Of Use Configurations", relief='raised',
                                    padding=('0.2i'))

    EasyOfUseFrame.grid(row=0, column=4, rowspan=27, padx=5, sticky='ne')

    launch_btn = ttk.Button(EasyOfUseFrame, text="Launch CyberArk", style="Accent.TButton",
                            command=lambda: launch_cyberark()).grid(row=0, column=0, columnspan=2, padx=5,
                                                                    pady=int_pady, sticky='nsew')

    openlogfile_btn = ttk.Button(EasyOfUseFrame, text="Open Log File", style="Accent.TButton",
                                 command=lambda: os.startfile('Integrity_log')).grid(row=1, column=0, columnspan=2,
                                                                                     padx=5, pady=int_pady,
                                                                                     sticky='nsew')

    autofill_btn = ttk.Button(EasyOfUseFrame, text="Auto Fill", style="Accent.TButton",
                              command=lambda: autofill_window_design()).grid(row=2, column=0, columnspan=2, padx=5,
                                                                             pady=int_pady, sticky='nsew')

    switch = ttk.Checkbutton(EasyOfUseFrame, text="Theme Switch", style="Switch", command=lambda: theme_switch())

    switch.grid(row=3, column=0, padx=5, pady=19, sticky="nsew")

    never_disable_frm = ttk.Frame(master=MasterFrame)

    never_disable_frm.grid(row=30, column=0, columnspan=5, padx=5, pady=10, sticky="nsew")

    never_disable_frm.columnconfigure(0, weight=8)

    never_disable_frm.columnconfigure(4, weight=1)

    never_disable_frm.columnconfigure(5, weight=1)

    info_text = 'Progress Information Is Displayed Here...'

    info = ttk.Label(master=never_disable_frm, text=info_text, relief='sunken', foreground='darkgreen')

    info.grid(row=0, column=0, columnspan=3, sticky='we')

    progressbar = ttk.Progressbar(never_disable_frm, mode="indeterminate")

    progressbar.grid(row=0, column=4, padx=10, sticky='w')

    # info.pack(side='left',padx=5)

    # Sizegrip

    sizegrip = ttk.Sizegrip(never_disable_frm)

    sizegrip.grid(row=0, column=5, sticky='se')

    update_progress('DRI Form Rendering Completed', 'None')


def theme_switch():
    global ThemeInt

    if (ThemeInt % 2) == 0:
        ttk.Style().theme_use('forest-light')

        print('Change To Light')

        ThemeInt = ThemeInt + 1

        return

    ttk.Style().theme_use('forest-dark')

    print('Change To Dark')

    ThemeInt = ThemeInt + 1

    update_progress('Theme Load Completed.', 'None')


def autofill_window_design():
    global autofill_window, autofill_btn, autofill_tree

    autofill_window = tk.Toplevel()

    autofill_window.title('Auto Fill Configurations')

    autofill_window.geometry('1000x600')

    # ttk.Style().theme_use('forest-light')

    # if os.path.exists('Integrity_AutoFill.parm') == True:

    #   param = open('Integrity_AutoFill.parm','r+')

    # wip_lbl=ttk.Label(master = autofill_window, text='Work In Progress.').grid(row=1,column=0,sticky='nsew')

    autofill_columns = ('ATTRIBUTE NAME', 'VALUE')

    autofill_tree = ttk.Treeview(autofill_window, columns=autofill_columns, show='headings')

    autofill_tree.pack(fill='both', expand='true')

    # dri_tree.grid(row=0, column=0, pady=10, sticky="ew")

    autofill_tree.column("ATTRIBUTE NAME", width=70)

    autofill_tree.column("VALUE", anchor="w", width=120)

    autofill_vert_scrollbar = ttk.Scrollbar(autofill_tree, orient='vertical', command=autofill_tree.yview)

    autofill_tree.config(yscroll=autofill_vert_scrollbar.set)

    autofill_vert_scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    autofill_hori_scrollbar = ttk.Scrollbar(autofill_tree, orient='horizontal', command=autofill_tree.xview)

    autofill_tree.configure(xscrollcommand=autofill_hori_scrollbar.set)

    autofill_hori_scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')

    for clmn in autofill_columns:
        # autofill_tree.column(clmn,anchor='w',stretch=False)

        autofill_tree.heading(clmn, text=clmn)

    populate_autofill_tree()

    # autofill_populate()

    action_frm = ttk.Frame(master=autofill_window)

    autofill_save = ttk.Button(action_frm, text="Save Changes", style="Accent.TButton",
                               command=lambda: autofill_flush(autofill_window, autofill_tree))

    autofill_close = ttk.Button(action_frm, text="Close Without Saving", style="Accent.TButton",
                                command=(lambda event: autofill_window.destroy()))

    autofill_save.pack(fill='both', expand='true', side='left')

    autofill_close.pack(fill='both', expand='true', side='right')

    action_frm.pack(fill='both', expand='true')

    autofill_tree.bind('<Double-1>', (lambda event: on_double_click(autofill_window, autofill_tree, event)))

    # autofill_window.protocol("WM_DELETE_WINDOW", autofill_flush(autofill_window,autofill_tree))


# parm_file = open('Integrity_AutoFill.parm','r+')


def autofill_flush(autofill_window, autofill_tree):
    userchoice = tkinter.messagebox.askquestion('Save Changes', 'Save Changes Made To AutoFill Options Before Closing?')

    # print("UserChoice: ",userchoice)

    if userchoice == "yes":

        parm_file = open('Integrity_AutoFill.parm', 'w')

        for itemid in autofill_tree.get_children():
            # print(str(autofill_tree.item(itemid)['values'][0]) + "::" + str(autofill_tree.item(itemid)['values'][1]))

            parm_file.writelines(
                str(autofill_tree.item(itemid)['values'][0]) + "::" + str(autofill_tree.item(itemid)['values'][1]))

        autofill_window.destroy()

        autofill_populate()

    else:

        print("AutoFill: No Changes")


def on_double_click(tgt_window, tgt_tree, event):
    # global autofill_window

    region_clicked = tgt_tree.identify_region(event.x, event.y)

    if region_clicked not in ("tree", "cell"):
        return

    column_clicked = tgt_tree.identify_column(event.x)

    if column_clicked == "#2":
        # print("Column 2 Double Clicked")

        selected_iid = tgt_tree.focus()

        selected_values = tgt_tree.item(selected_iid)

        selected_values_values = selected_values.get("values")

        column_box = tgt_tree.bbox(selected_iid, 1)

        # print('x=',column_box[0],'y=',column_box[1],'w=',column_box[2],'h=',column_box[3],'selected_values_values',selected_values_values)

        entry_edit = ttk.Entry(tgt_window, width=column_box[2])

        entry_edit.place(x=column_box[0], y=column_box[1], w=column_box[2], h=column_box[3] + 10)

        entry_edit.editing_item_iid = selected_iid

        entry_edit.insert(0, selected_values_values[1])

        entry_edit.select_range(0, 'end')

        entry_edit.focus()

        entry_edit.bind('<FocusOut>', (lambda event: on_done_edit(tgt_tree, event)))

        entry_edit.bind('<Return>', (lambda event: on_done_edit(tgt_tree, event)))

        entry_edit.bind('<Escape>', (lambda event: entry_edit.destroy()))


def on_done_edit(tgt_tree, event):
    new_value = str(event.widget.get()) + "\n"

    current_values = tgt_tree.item(event.widget.editing_item_iid).get("values")

    current_values[1] = new_value

    tgt_tree.item(event.widget.editing_item_iid, values=current_values)

    event.widget.destroy()


def populate_autofill_tree():
    global autofill_tree

    if (os.path.exists('Integrity_AutoFill.parm') == True and os.path.getsize('Integrity_AutoFill.parm') > 0):

        parm_file = open('Integrity_AutoFill.parm', 'r+')

        # print('Integrity_AutoFill.parm Exists')

        for line in parm_file.readlines():

            if line.startswith('--') == False:

                line_item = line.split('::')

                if line_item[0].rstrip() == "":

                    # elif line_item[0].rstrip() != "" and line_item[1].rstrip() == "" and line_item[0][:1]=="m":

                    print("Mandatory Attribute: ", line_item, " Has Not Been Set")

                else:

                    line_item0 = line_item[0].rstrip()

                    line_item1 = line_item[1].rstrip()

                    # print(line_item)

                    autofill_tree.insert(parent="", index=tk.END, values=(line_item))

                    # dri_tree.insert('','end',values=tuple(row))

        parm_file.close()


def menubar_design():
    menubar = tkinter.Menu(root)

    filemenu = tkinter.Menu(menubar, tearoff=0)

    filemenu.add_command(label="LLK Based Integrity Check", accelerator="Ctrl+L", command=lambda: llk_formdesign())

    filemenu.add_command(label="DRI Integrity Check", accelerator="Ctrl+D", command=lambda: dri_formdesign())

    filemenu.add_separator()

    filemenu.add_command(label="Exit", accelerator="Ctrl+Q", command=lambda: quit_root())

    menubar.add_cascade(label="Validation", menu=filemenu, underline=1)

    helpmenu = tkinter.Menu(menubar, tearoff=0)

    helpmenu.add_command(label="Help Index")

    helpmenu.add_command(label="About...")

    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    update_progress('MenuBar Redering Completed.', 'None')


def main():
    # Global Configuration Variables.

    global output_dir, log_dir, val_report_dir

    # Global Variables.

    global root, pane1

    global tDriverName, tUserName, tPassword, tserver_init, tserver, tdbname, mCyberArkLink, ha_id, ha_pwd, aedl_wh, aedl_server, aedl_server_init, sDBName_SchemaName, aedl_role, iptnum, cllk, tbl_nm, SampleCount, sor_cd_user_choice_v

    global InitVar, ThemeInt

    # Global Widgets

    global dir_tree, progressbar

    output_dir = os.getcwd() + '\\tera_out'

    # print(output_dir)

    log_dir = os.getcwd() + '\\log'

    # print(log_dir)

    val_report_dir = os.getcwd() + '\\val_out'

    root = tk.Tk()

    update_progress('Main Block Initiated.', 'None')

    root.tk.call('source', 'forest-dark.tcl')

    root.tk.call('source', 'forest-light.tcl')

    ttk.Style().theme_use('forest-light')

    tDriverName = StringVar(root)

    tUserName = StringVar(root)

    tPassword = StringVar(root)

    tdbname = StringVar(root)

    # tserver = StringVar(root)

    tserver = []

    tserver_init = StringVar(root)

    SampleCount = StringVar(root)

    mCyberArkLink = StringVar(root)

    ha_id = StringVar(root)

    ha_pwd = StringVar(root)

    aedl_wh = StringVar(root)

    aedl_role = StringVar(root)

    aedl_server = []

    aedl_server_init = StringVar(root)

    sDBName_SchemaName = StringVar(root)

    # aedl_server = StringVar(root)

    iptnum = StringVar(root)

    cllk = StringVar(root)

    tbl_nm = StringVar(root)

    sor_cd_user_choice_v = StringVar(root)

    InitVar = int(0)

    ThemeInt = int(1)

    root.title("Integrity")

    # root.geometry("1310x890")

    root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    # root.attributes('-fullscreen', True)

    root.option_add('*Foreground', '#007FFF')

    root.bind_all('<Control-w>', (lambda event: welcome_formdesign()))

    root.bind_all('<Control-W>', (lambda event: welcome_formdesign()))

    root.bind_all('<Control-l>', (lambda event: llk_formdesign()))

    root.bind_all('<Control-L>', (lambda event: llk_formdesign()))

    root.bind_all('<Control-d>', (lambda event: dri_formdesign()))

    root.bind_all('<Control-D>', (lambda event: dri_formdesign()))

    root.bind_all('<Control-q>', (lambda event: quit_root()))

    root.bind_all('<Control-Q>', (lambda event: quit_root()))

    autofill_populate()

    menubar_design()

    welcome_formdesign()

    root.columnconfigure(0, weight=3)

    root.rowconfigure(0, weight=1)

    root.columnconfigure(0, weight=3)

    # root.rowconfigure(0,weight=1)

    root.columnconfigure(0, weight=3)

    # root.rowconfigure(0,weight=1)

    root.columnconfigure(0, weight=1)

    # root.rowconfigure(0,weight=1)

    # root.resizable(True,False)

    update_progress('Awaiting User Inputs.', 'None')

    root.mainloop()


def quit_root():
    try:

        tera_connect.close()

        print('Teradata Connection Closed')



    except(pyodbc.Error, pyodbc.OperationalError) as ex:

        log.error(ex)

    except Exception as ex:

        log.error(ex)

    except NameError as ex:

        log.error(ex)

    except RuntimeError as ex:

        log.error(ex)

    snowflake_connection_close

    root.destroy()

    print('Bye!')


def launch_cyberark():
    global mCyberArkLink

    new = 1

    url = mCyberArkLink.get();

    webbrowser.open(url, new=new)


def update_progress(info_text, pb_status):
    global root, info, progressbar

    print(info_text)

    if pb_status == 'Start':

        info.config(text=info_text)

        progressbar.start()

        root.update_idletasks()

    elif pb_status == 'Stop':

        info.config(text=info_text)

        progressbar.stop()

        root.update_idletasks()

    elif pb_status == 'ProgressBarStep':

        info.config(text=info_text)

        root.update_idletasks()

        progressbar.step

    else:

        Something = 1

    log.info(info_text + " " + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

    root.update_idletasks()


def TestConn():
    global root, tUserName, tPassword, tserver, tDriverName, tserver_init, tdbname, ausername, apassword, iptnum, cllk, tbl_nm, info, progressbar, tera_connect

    update_progress('Testing Connection To Teradata Using The Credentials Provided...', 'Start')

    try:

        link = 'DRIVER={DRIVERNAME};DBCNAME={hostname};MechanismName=LDAP;Database={DBName};UID={uid};PWD={pwd}'.format(

            DRIVERNAME=tDriverName.get(), hostname=tserver_init.get(), DBName=tdbname.get(),

            uid=tUserName.get(), pwd='Welcome@1')  # pwd=tPassword.get())

        with pyodbc.connect(link, autocommit=True) as tera_connect:

            log.info("Teradata connection successful:" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

            tkinter.messagebox.showinfo(title="Hurray", message="Teradata Connection Successful!")

            snowflake_connect()

            tkinter.messagebox.showinfo(title="Hurray", message="Snowflake Connection Successful!")

            update_progress("Teradata and Snowflake Connections Successful. Proceed With Next Step.", 'Stop')

    except(pyodbc.Error, pyodbc.OperationalError) as ex:

        log.error(ex)

        update_progress('Teradata Or Snowflake Connection Failed. Check Logs.', 'Stop')

        tkinter.messagebox.showerror(title="Alas!", message="Connection Failed!")

        logging.shutdown()

    except Exception as ex:

        log.error(ex)

        update_progress('Teradata Or Snowflake Connection Failed. Check Logs.', 'Stop')

        tkinter.messagebox.showerror(title="Alas!", message="Connection Failed!")

        logging.shutdown()

    except RuntimeError as ex:

        log.error(ex)

        update_progress('Teradata Or Snowflake Connection Failed. Check Logs.', 'Stop')

        tkinter.messagebox.showerror(title="Alas!", message="Connection Failed!")

        logging.shutdown()


def tera_execute(query, callingblock):
    print('Executing Query:' + query)

    try:

        with tera_connect.cursor() as cur:

            cur.execute(query)

            rows = cur.fetchall()

            return (rows)

    except(pyodbc.Error, pyodbc.OperationalError) as ex:

        log.error(ex)

        update_progress('Error During Query Execution. Check Logs. Calling Block' + callingblock, 'Stop')

        tkinter.messagebox.showerror(title="Alas!", message="Query Execution Failed!")

        logging.shutdown()

    except Exception as ex:

        log.error(ex)

        update_progress('Error During Query Execution. Check Logs. Calling Block' + callingblock, 'Stop')

        tkinter.messagebox.showerror(title="Alas!", message="Query Execution Failed!")

        logging.shutdown()

    except RuntimeError as ex:

        log.error(ex)

        update_progress('Error During Query Execution. Check Logs. Calling Block' + callingblock, 'Stop')

        tkinter.messagebox.showerror(title="Alas!", message="Query Execution Failed!")

        logging.shutdown()


def clear_tree_view():
    global dri_tree

    for item in dri_tree.get_children():
        dri_tree.delete(item)


def DRI_Retrieve():
    global root, tUserName, tPassword, tserver, tdbname, ausername, apassword, iptnum, cllk, tbl_nm, dri_tree, progressbar, tera_connect

    update_progress('Retriving Data From DB...', 'Start')

    query = "SELECT TBL_NM,KEY_CLMN_NM,CRCTN_CLMN_NM,SOR_CD,LOAD_LOG_KEY,to_char(CRCTN_EXECTN_DTM,'YYYY-MM-DD HH24:MI:SS') CRCTN_EXECTN_DTM,RCRD_CRCTN_TYPE_CD,IPT_NBR,LOAD_LOG_KEY_TYPE_CD FROM " + tdbname.get() + ".DRI_INPT_LOAD_TRKR WHERE "

    Check = 0

    if iptnum.get() != "":
        query = query + "IPT_NBR LIKE '%" + iptnum.get() + "%'"

        Check = 1

    if tbl_nm.get() != "":

        if Check == 1:

            query = query + " AND TBL_NM LIKE '%" + tbl_nm.get() + "%'"

        else:

            query = query + " TBL_NM LIKE '%" + tbl_nm.get() + "%'"

            Check = 1

    if cllk.get() != "":

        if Check == 1:

            query = query + " AND LOAD_LOG_KEY = " + cllk.get()

        else:

            query = query + " LOAD_LOG_KEY = " + cllk.get()

            Check = 1

    query = query + " ORDER BY CRCTN_EXECTN_DTM DESC;"

    if Check == 1:

        rows = tera_execute(query, 'DRI_Retrieve')

        update_progress('Data Retrieved From DB...', 'ProgressBarStep')

        update_progress('Clearing Any Old Tree View Entries...', 'ProgressBarStep')

        clear_tree_view()

        update_progress('Populating Tree View...', 'ProgressBarStep')

        for row in rows:
            dri_tree.insert('', 'end', values=tuple(row))

        update_progress('Proceed With Next Step...', 'Stop')

    else:

        print("Step2: No Input Provided")

        update_progress('Make a selection.', 'Stop')


def begin_compare():
    global root, tUserName, tPassword, tserver, tdbname, ausername, apassword, iptnum, cllk, tbl_nm, dri_tree, progressbar

    global item_values, item_details, item_values

    global dri_tbl_nm, dri_key_clmn, dri_impctd_clmn, dri_cllk, dri_sorcd, dri_llk_type, dri_rcrd_crctn_type, dri_ipt_nbr

    global edw_data_extrct_query, edw_aedl_comp_query

    update_progress('Begin Compare Called...', 'Start')

    if dri_tree.selection():

        for item_iid in dri_tree.selection():

            # print(item_iid)

            # item_iid=dri_tree.selection()

            item_details = dri_tree.item(item_iid)

            item_values = item_details.get("values")

            dri_tbl_nm = str(item_values[0])

            dri_key_clmn = str(item_values[1])

            dri_impctd_clmn = str(item_values[2])

            dri_sorcd = item_values[3]

            dri_cllk = str(item_values[4])

            dri_rcrd_crctn_type = str(item_values[6])

            dri_ipt_nbr = str(item_values[7])

            dri_llk_type = str(item_values[8])

            if dri_impctd_clmn.upper() == "ALL":

                print("ALL COLUMNS UPDATED AS PART OF THIS IPT_NBR")

                print(output_dir)

                output_file_nm = output_dir + '\\' + dri_tbl_nm + '.csv'

                build_queries()

            else:

                print("SELECTED COLUMN(S) UPDATED AS PART OF THIS IPT_NBR")

                print(output_dir)

                output_file_nm = output_dir + '\\' + dri_tbl_nm + '.csv'

                build_queries()

            # Based on selection made, extracting data from teradata.

            tera_data_write(edw_data_extrct_query, output_file_nm)

            snowflake_file_copy_and_comp(output_file_nm)

    else:

        # print('Nothing Is Selected')

        update_progress('Make A Selection...', 'Stop')


def build_queries():
    global item_values, item_details, item_values, SampleCount

    global dri_tbl_nm, dri_key_clmn, dri_impctd_clmn, dri_cllk, dri_sorcd, dri_llk_type, dri_rcrd_crctn_type, dri_ipt_nbr, join_cond

    global edw_data_extrct_query, edw_aedl_comp_query, aedl_data_extract_query

    update_progress('Deriving Validation Queries...', 'None')

    # Preparing EDW to AEDL Join Condition

    join_cols = ['EDW.$' + str(index) + '=' 'AEDL.' + columns.strip() for index, columns in
                 enumerate(dri_key_clmn.split(","), start=1)]

    key_cols = ['EDW.$' + str(index) for index, columns in enumerate(dri_key_clmn.split(","), start=1)]

    join_cond = " AND ".join(join_cols)

    key_cols_all = ",".join(key_cols)

    # join_cond=join_cond[0:-4] #Removing the extra AND clause from the end.

    key_col_count = dri_key_clmn.count(",") + 1

    # Initial Values

    userchoice = ""

    sor_cd_check = ""

    q2c_edw_cllk_count = ""

    q2c_edw_dri_dtl_count = ""

    edw_data_extrct_query_part1 = "SELECT " + dri_key_clmn

    edw_data_extrct_query_part2 = "\n FROM " + dri_tbl_nm + "\n WHERE CRCTD_LOAD_LOG_KEY=" + dri_cllk

    edw_aedl_comp_query = "SELECT COUNT(*) \n FROM P01_EDL.EDL." + dri_tbl_nm + " AEDL \n INNER JOIN @~/" + dri_tbl_nm + '.csv' + " (file_format=>'CSV_READ_REPLACE_INVALID_CHAR') EDW \n ON " + join_cond + " \n AND AEDL.CRCTD_LOAD_LOG_KEY=" + dri_cllk

    if dri_impctd_clmn.strip().upper() == "ALL":

        aedl_data_extract_query_edw_part = "SELECT CAST('EDW RECORD' AS VARCHAR(15)) Row_Type,"

    else:

        aedl_data_extract_query_edw_part = "SELECT CAST('EDW RECORD' AS VARCHAR(15)) Row_Type," + key_cols_all + ","

    aedl_data_extract_query_aedl_part = "SELECT CAST('AEDL RECORD' AS VARCHAR(15)) Row_Type," + dri_key_clmn + ","

    aedl_data_extract_query_predicate = "\n FROM P01_EDL.EDL." + dri_tbl_nm + " AEDL \n INNER JOIN @~/" + dri_tbl_nm + '.csv' + " (file_format=>'CSV_READ_REPLACE_INVALID_CHAR') EDW \n ON " + join_cond + " \n AND AEDL.CRCTD_LOAD_LOG_KEY=" + dri_cllk

    # Query To Fetch All Column Names From Teradata.

    col_extrct_query = "SELECT DISTINCT COLUMNNAME,COLUMNID,COLUMNTYPE FROM DBC.COLUMNSV C INNER JOIN DBC.TABLESV T ON C.DATABASENAME = T.DATABASENAME AND C.TABLENAME =T.TABLENAME WHERE T.TABLEKIND IN ('T','O') AND T.TABLENAME ='" + dri_tbl_nm + "' AND T.DATABASENAME = 'EDW_V20' ORDER BY COLUMNID"

    # Query To Fetch All SOR_CD Column Names From Teradata.

    sorcd_extrct_query = "SELECT DISTINCT COLUMNNAME,COLUMNID,COLUMNTYPE FROM DBC.COLUMNSV C INNER JOIN DBC.TABLESV T ON C.DATABASENAME = T.DATABASENAME AND C.TABLENAME =T.TABLENAME WHERE T.TABLEKIND IN ('T','O') AND T.TABLENAME ='" + dri_tbl_nm + "' AND T.DATABASENAME LIKE 'EDW%' AND T.DATABASE/NAME <> 'EDW_DR' AND C.COLUMNNAME LIKE '%SOR_CD%' ORDER BY COLUMNID"

    # Build query to extract data from teradata and a query for EDW-AEDL comparison query.

    if str(dri_sorcd).strip().upper() != "ALL":

        rows = tera_execute(sorcd_extrct_query, 'Build_Queries')

        all_sorcd_cols = ''

        if len(rows) > 1:

            for row in rows:
                all_sorcd_cols = all_sorcd_cols + row[0] + ","

            all_sorcd_cols = all_sorcd_cols[0:-1]

            msg = 'For Validating Data In ' + dri_tbl_nm + ', which of these SOR_CD column should to be used? \n'

            msg = msg + all_sorcd_cols + '\n'

            Check = -1

            while Check == -1:

                userchoice = askstring('Which SOR_CD to Use?', msg)

                if all_sorcd_cols.find(userchoice) >= 0:
                    Check = 0

            sor_cd_check = " AND " + userchoice + "='" + str(dri_sorcd) + "'"

        else:

            sor_cd_check = " AND " + str(rows[0][0]) + "='" + str(dri_sorcd) + "'"

    else:

        sor_cd_check = "/* Checking For All SOR_CDs */"

    edw_aedl_comp_query = edw_aedl_comp_query + "\n" + sor_cd_check + "\n AND ("

    aedl_data_extract_query_predicate = aedl_data_extract_query_predicate + "\n" + sor_cd_check + "\n AND ("

    edw_data_extrct_query_part2 = edw_data_extrct_query_part2 + "\n" + sor_cd_check + "\n" + " SAMPLE " + SampleCount.get()

    rows = tera_execute(col_extrct_query, 'Build_Queries')

    # EDW CLLK Count Check.

    if dri_llk_type.strip() == "C":

        print("dri_rcrd_crctn_type:" + dri_rcrd_crctn_type[0])

        if dri_rcrd_crctn_type[0] == "I" or dri_rcrd_crctn_type[0] == "U":

            q2c_edw_cllk_count = "SELECT COUNT(*) \n FROM " + dri_tbl_nm + "\n WHERE CRCTD_LOAD_LOG_KEY=" + dri_cllk

            q2c_edw_dri_dtl_count = "SELECT COUNT(*) \n FROM DRI_DTL \n WHERE IPT_NBR='" + dri_ipt_nbr.strip() + dri_rcrd_crctn_type.strip() + "' \n AND TBL_NM='" + dri_tbl_nm + "'"

            if userchoice != "":
                q2c_edw_cllk_count = q2c_edw_cllk_count + "\n" + sor_cd_check

        if dri_rcrd_crctn_type[0] == "P" or dri_rcrd_crctn_type[0] == "D":

            q2c_edw_cllk_count = "SELECT COUNT(*) \n FROM " + dri_tbl_nm + " TBL \n INNER JOIN DRI_DTL DD \n ON DD.KEY_CLMN_VAL_TXT = TBL." + dri_key_clmn

            if userchoice != "":
                q2c_edw_cllk_count = q2c_edw_cllk_count + " \n AND DD.SOR_CD=TBL." + userchoice

            q2c_edw_cllk_count = q2c_edw_cllk_count + " \n AND DD.IPT_NBR='" + dri_ipt_nbr.strip() + dri_rcrd_crctn_type.strip() + "' \n AND TBL_NM='" + dri_tbl_nm + "' \n AND TBL.CRCTD_LOAD_LOG_KEY=" + dri_cllk

            q2c_edw_dri_dtl_count = "SELECT COUNT(*) \n FROM DRI_DTL \n WHERE IPT_NBR='" + dri_ipt_nbr.strip() + dri_rcrd_crctn_type.strip() + "' \n AND TBL_NM='" + dri_tbl_nm + "'"

    q2c_edw_cllk_count_rows = tera_execute(q2c_edw_cllk_count, 'Build_Queries')

    q2c_edw_dri_dtl_count_rows = tera_execute(q2c_edw_dri_dtl_count, 'Build_Queries')

    print("q2c_edw_cllk_count: " + q2c_edw_cllk_count + "\n Result: " + str(q2c_edw_cllk_count_rows))

    print("q2c_edw_dri_dtl_count: " + q2c_edw_dri_dtl_count + "\n Result: " + str(q2c_edw_dri_dtl_count_rows))

    noskip_cnt = 1

    i = key_col_count + 1

    for row in rows:

        index = dri_key_clmn.find(row[0])

        if dri_impctd_clmn.strip().upper() == "ALL":

            aedl_data_extract_query_edw_part = aedl_data_extract_query_edw_part + "\n EDW.$" + str(noskip_cnt) + ","

            if index == -1:
                edw_aedl_comp_query = edw_aedl_comp_query + "AEDL." + row[0] + " <> EDW.$" + str(i) + "\n  OR "

                aedl_data_extract_query_aedl_part = aedl_data_extract_query_aedl_part + "AEDL." + row[0] + ","

                aedl_data_extract_query_predicate = aedl_data_extract_query_predicate + "AEDL." + row[
                    0] + " <> EDW.$" + str(i) + "\n  OR "

            if row[2] == 'DA' or row[2] == 'TS':

                edw_data_extrct_query_part1 = edw_data_extrct_query_part1 + ",CAST(" + row[0] + " AS VARCHAR(100))"

            elif row[2] == 'CF':

                edw_data_extrct_query_part1 = edw_data_extrct_query_part1 + ",TRIM(" + row[0] + ")"

            else:

                edw_data_extrct_query_part1 = edw_data_extrct_query_part1 + "," + row[0]

            i += 1

        if dri_impctd_clmn.strip().upper() != "ALL" and dri_impctd_clmn.strip().find(row[0]) == 0:

            aedl_data_extract_query_edw_part = aedl_data_extract_query_edw_part + " EDW.$" + str(i) + ","

            if index == -1:
                edw_aedl_comp_query = edw_aedl_comp_query + " AEDL." + row[0] + " <> EDW.$" + str(
                    key_col_count + 1) + "\n  OR "

                aedl_data_extract_query_aedl_part = aedl_data_extract_query_aedl_part + "AEDL." + row[0] + ","

                aedl_data_extract_query_predicate = aedl_data_extract_query_predicate + "AEDL." + row[
                    0] + " <> EDW.$" + str(key_col_count + 1) + "\n  OR "

            if row[2] == 'DA' or row[2] == 'TS':

                edw_data_extrct_query_part1 = edw_data_extrct_query_part1 + ",CAST(" + row[0] + " AS VARCHAR(100))"

            elif row[2] == 'CF':

                edw_data_extrct_query_part1 = edw_data_extrct_query_part1 + ",TRIM(" + row[0] + ")"

            else:

                edw_data_extrct_query_part1 = edw_data_extrct_query_part1 + "," + row[0]

            i += 1

        noskip_cnt += 1

    edw_aedl_comp_query = edw_aedl_comp_query[0:-4] + ')'

    edw_data_extrct_query = edw_data_extrct_query_part1 + edw_data_extrct_query_part2

    aedl_data_extract_query = aedl_data_extract_query_aedl_part[0:-1] + aedl_data_extract_query_predicate[
                                                                        0:-4] + ')\n UNION ALL \n' + aedl_data_extract_query_edw_part[
                                                                                                     0:-1] + aedl_data_extract_query_predicate[
                                                                                                             0:-4] + ') ORDER BY ' + dri_key_clmn + ',ROW_TYPE \n'

    print("edw_data_extrct_query", edw_data_extrct_query + "\n");

    print("edw_aedl_comp_query", edw_aedl_comp_query + "\n");

    print("aedl_data_extract_query:", aedl_data_extract_query + "\n");


def tera_data_write(tera_query, write_to):
    global root, tUserName, tPassword, tserver, tdbname, ausername, apassword, iptnum, cllk, tbl_nm, dri_tree, progressbar, tera_connect

    global output_dir, log_dir

    global item_values

    update_progress('tera_data_write Called...', 'ProgressBarStep')

    rows = tera_execute(tera_query, 'Tera_Data_Write')

    print('Writing to ', write_to)

    tera_filename = str(item_values[1]) + '.csv'

    # tera_out_file = open(write_to,"w")

    update_progress('Writing Output To File', 'ProgressBarStep')

    # of = open(write_to+ '.txt','w+')

    # of2 = open(write_to+ '2.txt','w+')

    with open(write_to, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # writer.writerow([x[0] for x in crsr.description])  # column headers

        for row in rows:
            row_str = str(row)

            row_str.encode('UTF-8', errors='replace')

            # print(row_str)

            # of.writelines(row_str)

            # of2.writelines(row_str)

            writer.writerow(row)

    csvfile.close()

    # for row in rows:

    #   row_text=str(row)

    #   row_text=row_text[1:]

    #   row_text=row_text[:-1]

    #   tera_out_file.write(row_text + '\n')

    # tera_out_file.close()

    update_progress('File Ready.', 'Stop')


def snowflake_connect():
    global ha_id, ha_pwd, aedl_wh, aedl_server

    global item_values, item_details, item_values

    global snow_con, snow_cur

    # print ('1',ha_id.get())

    # print ('2',ha_pwd.get())

    # print ('3',aedl_wh.get())

    # print ('4',aedl_server_init.get())

    update_progress('Establishing Connection With Snowflake...', 'Start')

    # snow_conn_strng= "user='{username}',password='{password}',account='{server}',warehouse='{warehouse}',database='P01_EDL',schema='EDL'".format(username=ha_id.get(),password=ha_pwd.get(),server=aedl_server.get(),warehouse=aedl_wh.get())

    # print('SNOW_CONN_STRNG: ',snow_conn_strng)

    snow_con = snowflake.connector.connect(user='AN941372AD', authenticator='externalbrowser',
                                           account='carelon-edaprod1.privatelink', warehouse='P01_EDL_ADHOC_WH',
                                           database='P01_EDL', schema='EDL')

    snow_cur = snow_con.cursor()

    update_progress('Connected To SnowFlake.', 'Stop')


def snowflake_connection_close():
    global snow_con, snow_cur

    if snow_cur:
        snow_cur.close()

    if snow_con:
        snow_con.close()

        print('Snowflake Connection Closed')


def snowflake_file_copy_and_comp(output_file_nm):
    global item_values, item_details, item_values

    global snow_cur

    global edw_aedl_comp_query, aedl_data_extract_query

    output_file_nm = output_file_nm.replace("\\", "/")

    remove_sql = "REMOVE @~/" + str(item_values[0]) + '.csv'

    # print(remove_sql)

    snow_cur.execute(remove_sql)

    put_sql = "put 'file://" + output_file_nm + "' @~/" + str(item_values[0]) + '.csv'

    # print(put_sql)

    snow_cur.execute(put_sql)

    update_progress('File Uploaded To Snowflake.', 'Stop')

    ff_sql = """CREATE OR REPLACE TEMPORARY FILE FORMAT CSV_READ_REPLACE_INVALID_CHAR

                COMPRESSION = 'AUTO'

                FIELD_DELIMITER = ','

                RECORD_DELIMITER = '\n'

                SKIP_HEADER = 0

                FIELD_OPTIONALLY_ENCLOSED_BY = '"'

                TRIM_SPACE = FALSE

                REPLACE_INVALID_CHARACTERS = TRUE

                ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE

                ESCAPE = 'NONE'

                ESCAPE_UNENCLOSED_FIELD=NONE

                DATE_FORMAT = 'yyyy-mm-dd'

                TIMESTAMP_FORMAT = 'AUTO'

                NULL_IF = ('NULL', 'null')

                COMMENT = 'Integrity Parse Comma-Delimited, Double-Quoted CSV Files';"""

    snow_cur.execute(ff_sql)

    update_progress('Validation Started.', 'Start')

    snow_cur.execute(edw_aedl_comp_query)

    resultset = snow_cur.fetchall()

    print('Count Query Executed Successfully.')

    print(resultset)

    print(resultset[0][0])

    if resultset[0][0] == 0:

        print(item_values[0] + " Data Synced Successfully!")

    else:

        print(item_values[0] + " Issue With Data Sync! Trying To Extract Data From Snowflake")

        snow_cur.execute(aedl_data_extract_query)

        resultset = snow_cur.fetchall()

        columns = [column[0] for column in snow_cur.description]

        write_to_excel(columns, resultset)

        # print(resultset)

    remove_sql = "REMOVE @~/" + str(item_values[0]) + '.csv'


def write_to_excel(columns, resultset):
    global root, tUserName, tPassword, tserver, tdbname, ausername, apassword, iptnum, cllk, tbl_nm, dri_tree, progressbar

    global val_report_dir

    excel_file_timestamp = time.strftime("%Y%m%d%H%M%S")

    tUserName = 'AF62123'

    # val_report_dir=os.getcwd() + '\\val_out'

    val_output_file_nm = val_report_dir + "\\" + tUserName + "_Validation_Report_" + excel_file_timestamp + ".xlsx"

    workbook = xlsxwriter.Workbook(val_output_file_nm)

    worksheet = workbook.add_worksheet("Testing")

    # Light red fill with dark red text.

    red_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})

    # Blue Fill with white text

    heading_format = workbook.add_format({'bg_color': '#3399FF', 'font_color': '#FFFFFF'})

    data_format = workbook.add_format()

    data_format.set_num_format('@')  # @ - This is text format in excel

    worksheet.write_row(0, 0, columns, data_format)

    rownum = 1

    for row in resultset:
        worksheet.write_row(rownum, 0, row, data_format)

        rownum += 1

    cf = 1

    while cf <= rownum:

        if cf % 2 > 0:
            worksheet.conditional_format(cf, 1, cf + 1, 300, {'type': 'unique',

                                                              'format': red_format})

        cf += 1

    workbook.close()

    print("Data Extracted From Snowflake. Please proceed with manual validation.")


# This function is called as the first process to load

def autofill_populate():
    global root, tDriverName, tUserName, tserver, tdbname, ha_id, aedl_wh, aedl_server, aedl_role, mCyberArkLink, sDBName_SchemaName, SampleCount

    global iptnum

    tserver = []

    aedl_server = []

    if (os.path.exists('Integrity_AutoFill.parm') == True and os.path.getsize('Integrity_AutoFill.parm') > 0):

        parm_file = open('Integrity_AutoFill.parm', 'r+')

        print('Integrity_AutoFill.parm Exists')

        for line in parm_file.readlines():

            if line.startswith('--') == False:

                line_item = line.split('::')

                if line_item[0].rstrip() == "":

                    print("Blank Line Skipped")

                elif line_item[0].rstrip() != "" and line_item[1].rstrip() == "" and line_item[0][:1] == "m":

                    print("Mandatory Attribute: ", line_item, " Has Not Been Set")

                else:

                    line_item0 = line_item[0].rstrip()

                    line_item1 = line_item[1].rstrip()

                    if line_item0 == "tDriverName":

                        tDriverName.set(line_item1)

                    elif line_item0 == "tUserName":

                        tUserName.set(line_item1)

                    elif line_item0 == "mServerNames":

                        tserver = tuple(line_item1.split(','))

                    elif line_item0 == "tDatabaseName":

                        tdbname.set(line_item1)

                    elif line_item0 == "mCyberArkLink":

                        mCyberArkLink.set(line_item1)

                    elif line_item0 == "sHeightend_Account_ID":

                        ha_id.set(line_item1)

                    elif line_item0 == "mAccountName":

                        aedl_server = tuple(line_item1.split(','))

                    elif line_item0 == "sDBName.SchemaName":

                        sDBName_SchemaName.set(line_item1)

                    elif line_item0 == "sWarehouseName":

                        aedl_wh.set(line_item1)

                    elif line_item0 == "sRoleName":

                        aedl_role.set(line_item1)

                    elif line_item0 == "oSampleCount":

                        SampleCount.set(line_item1)

                    elif line_item0 == "iptnum":

                        iptnum.set(line_item1)

    else:

        print('Integrity_AutoFill.parm Does Not Exists')

    parm_file.close()


if __name__ == '__main__':
    # logging.basicConfig(filename='Integrity_'+timestamp, level=logging.DEBUG, filemode='w')

    logging.basicConfig(filename='Integrity_log', level=logging.DEBUG, filemode='w')

    # logging.setlevel(logging.INFO)

    log = logging.getLogger(__name__)

    main()
