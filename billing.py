from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Softwore")
        bg_color="#074463"
        title=Label(self.root,text="Billing Softwore",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,'bold')).pack(fill=X)
        #........variable....#
        self.soap=IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.gell= IntVar()
        self.loshan = IntVar()
        #.......#
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        #........#
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbs_up = IntVar()
        self.limca = IntVar()
        self.sprite= IntVar()
        #....total product..#
        self.cosmetic_price=StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()
        #.....customer...#
        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 99999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


        f1=LabelFrame(self.root,text="Customer Details",bd=12,relief=GROOVE,font=("times new roman",15,'bold'),bg=bg_color,fg="gold")
        f1.place(x=0,y=80,relwidth=1)
        cname=Label(f1,text="Customer Name",font=("times new roman",20,'bold'),bg=bg_color,fg="white").grid(row=0,column=0)
        cname=Entry(f1,font="arial 15",textvariable=self.c_name,width=20,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)
        phono=Label(f1,text="Phone No",font=("times new roman",20,'bold'),bg=bg_color,fg="white").grid(row=0,column=2)
        phono=Entry(f1,font="arial 15",textvariable=self.c_phone,width=20,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)
        billno = Label(f1, text="Bill No", font=("times new roman", 20, 'bold'), bg=bg_color, fg="white").grid(row=0, column=4)
        billno = Entry(f1, font="arial 15",textvariable=self.search_bill, width=20, bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10, pady=10)
        btn=Button(f1,text="search",command=self.find_bill,bd=7,fg="black",width=10,font=("times new roman",15, 'bold')).grid(row=0, column=6,padx=10,pady=10)
        #....COSMATICES....#

        f2=LabelFrame(self.root,text="Cosmatics ",bd=10,relief=GROOVE,font=("times new roman",15,'bold'),bg=bg_color,fg="gold")
        f2.place(x=5,y=180,width=325,height=380)
        bath_lb=Label(f2,text="Bath Soap ",font=("times new roman",15,'bold'),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(f2,font="arial 15",textvariable=self.soap,width=10,bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        face_lb = Label(f2, text="Face Cream ", font=("times new roman", 15, 'bold'), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        face_txt = Entry(f2, font="arial 15",textvariable=self.face_cream, width=10, bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        facew_lb = Label(f2, text="Face Wash", font=("times new roman", 15, 'bold'), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        facew_txt = Entry(f2, font="arial 15",textvariable=self.face_wash, width=10, bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        hairsp_lb = Label(f2, text="Hair Spray ", font=("times new roman", 15, 'bold'), bg=bg_color, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky='w')
        hairsp_txt = Entry(f2, font="arial 15",textvariable=self.hair_spray, width=10, bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        hairg_lb = Label(f2, text="Hair Gell ", font=("times new roman", 15, 'bold'), bg=bg_color, fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky='w')
        hairg_txt = Entry(f2, font="arial 15",textvariable=self.gell, width=10, bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        bodyw_lb = Label(f2, text="Body Loshan ", font=("times new roman", 15, 'bold'), bg=bg_color, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky='w')
        bodyw_txt = Entry(f2, font="arial 15", width=10,textvariable=self.loshan, bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)
        #...grocery...#
        f3 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 15, 'bold'),
                        bg=bg_color, fg="gold")
        f3.place(x=340, y=180, width=325, height=380)
        rice_lb = Label(f3, text="Rice", font=("times new roman", 15, 'bold'), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        rice_txt = Entry(f3, font="arial 15",textvariable=self.rice, width=10, bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        foodoil_lb = Label(f3, text="Food Oil ", font=("times new roman", 15, 'bold'), bg=bg_color,
                        fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        foodoil_txt = Entry(f3, font="arial 15",textvariable=self.food_oil, width=10, bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        daal_lb = Label(f3, text="Daal", font=("times new roman", 15, 'bold'), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        daal_txt = Entry(f3, font="arial 15", width=10,textvariable=self.daal, bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        wheat_lb = Label(f3, text="Wheat ", font=("times new roman", 15, 'bold'), bg=bg_color,
                          fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky='w')
        wheat_txt = Entry(f3, font="arial 15", width=10, textvariable=self.wheat,bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        sugar_lb = Label(f3, text="Sugar ", font=("times new roman", 15, 'bold'), bg=bg_color,
                         fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky='w')
        sugar_txt = Entry(f3, font="arial 15", width=10,textvariable=self.sugar, bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        tea_lb = Label(f3, text="Tea", font=("times new roman", 15, 'bold'), bg=bg_color,
                         fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky='w')
        tea_txt = Entry(f3, font="arial 15",textvariable=self.tea, width=10, bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)
        # ...cold drink....#

        f4 = LabelFrame(self.root, text="Cold Drink", bd=10, relief=GROOVE, font=("times new roman", 15, 'bold'),
                        bg=bg_color, fg="gold")
        f4.place(x=675, y=180, width=325, height=380)
        maza_lb = Label(f4, text="Maza",font=("times new roman", 15, 'bold'), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        maza_txt = Entry(f4, font="arial 15",textvariable=self.maza , width=10, bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        cock_lb = Label(f4, text="Cock", font=("times new roman", 15, 'bold'), bg=bg_color,
                        fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        cock_txt = Entry(f4, font="arial 15",textvariable=self.cock , width=10, bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        frooti_lb = Label(f4, text="Frooti", font=("times new roman", 15, 'bold'), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        frooti_txt = Entry(f4, font="arial 15", width=10,textvariable=self.frooti , bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        thumbsup_lb = Label(f4, text="Thumbs Up", font=("times new roman", 15, 'bold'), bg=bg_color,
                          fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky='w')
        thumbsup_txt = Entry(f4, font="arial 15", width=10,textvariable=self.thumbs_up , bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        limca_lb = Label(f4, text="Limca ", font=("times new roman", 15, 'bold'), bg=bg_color,
                         fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky='w')
        limca_txt = Entry(f4, font="arial 15", width=10,textvariable=self.limca , bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        sprite_lb = Label(f4, text="Sprite ", font=("times new roman", 15, 'bold'), bg=bg_color,
                         fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky='w')
        sprite_txt = Entry(f4, font="arial 15", width=10,textvariable=self.sprite , bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)
        # ...bills area...#
        f5 =Frame(self.root,  bd=10, relief=GROOVE )

        f5.place(x=1010, y=180, width=340, height=380)
        bill_title=Label(f5,text='Bill Area',font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_bar=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scrol_bar.set)
        scrol_bar.pack(side=RIGHT,fill=Y)
        scrol_bar.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # .... button frame....#
        f6= LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, 'bold'),
                        bg=bg_color, fg="gold")
        f6.place(x=0,y=560, relwidth=1, height=140)
        m1=Label(f6,text='Total Cosmetic price',bg="#074463",fg='white',font=("times new roman", 14, 'bold')).grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_txt=Entry(f6,width=18,textvariable=self.cosmetic_price ,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        m2=Label(f6,text='Total Grocery price',bg="#074463",fg='white',font=("times new roman", 14, 'bold')).grid(row=1,column=0,padx=20,pady=1,sticky='w')
        m2_txt=Entry(f6,width=18,font="arial 10 bold",textvariable=self.grocery_price ,bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        m3=Label(f6,text='Total Cold Drinks  price',bg="#074463",fg='white',font=("times new roman", 14, 'bold')).grid(row=2,column=0,padx=20,pady=1,sticky='w')
        m3_txt=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.cold_drink_price ,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        m4=Label(f6,text='Cosmetic Tax',bg="#074463",fg='white',font=("times new roman", 14, 'bold')).grid(row=0,column=2,padx=20,pady=1,sticky='w')
        m4_txt=Entry(f6,width=18,font="arial 10 bold",textvariable=self.cosmetic_tax ,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        m5=Label(f6,text='Grocery Tax',bg="#074463",fg='white',font=("times new roman", 14, 'bold')).grid(row=1,column=2,padx=20,pady=1,sticky='w')
        m5_txt=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.grocery_tax ,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        m6=Label(f6,text='Cold Drinks Tax',bg="#074463",fg='white',font=("times new roman", 14, 'bold')).grid(row=2,column=2,padx=20,pady=1,sticky='w')
        m6_txt=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.cold_drink_tax ,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_frame=Frame(f6,bd=7,relief=GROOVE)
        btn_frame.place(x=750,width=580,height=105)
        total_btn=Button(btn_frame,command=self.total,text='Total',bg='cadetblue',fg='white',width=11,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=25)
        gbill_btn=Button(btn_frame,command=self.bill_area,text='Generate Bill',bg='cadetblue',fg='white',width=14,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=25)
        clear_btn=Button(btn_frame,text='Clear',command=self.clear_data,bg='cadetblue',fg='white',width=11,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=25)
        exit_btn=Button(btn_frame,command=self.exit_app,text='Exit',bg='cadetblue',fg='white',width=11,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=25)
        self.welcome_bill()
    def total(self):
        self.so=self.soap.get()*40
        self.f_c=self.face_cream.get() * 120
        self.f_w=self.face_wash.get() * 60
        self.h_s=self.hair_spray.get() * 180
        self.g=self.gell.get() * 140
        self.l=self.loshan.get() * 180
        self.total_cosmetic_price=float(
            self.so+
            self.f_c +
            self.f_w +
            self.h_s +
            self.g +
            self.l
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        self.r = self.rice.get() * 50
        self.f_o = self.food_oil.get() * 110
        self.d = self.daal.get() * 120
        self.w =self.wheat.get() * 30
        self.s = self.sugar.get() * 45
        self.t =self.tea.get() * 200
        self.total_grocery_price = float(
            self.r +
            self.f_o +
            self.d+
            self.w +
            self.s +
            self.t
        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.04),2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))
        self.m = self.maza.get() *60
        self.co = self.cock.get() *70
        self.fr = self.frooti.get() * 58
        self.tu =self.thumbs_up.get() * 72
        self.li =self.limca.get() * 70
        self.sp = self.sprite.get() * 64
        self.total_cold_price = float(
            self.m +
            self.co +
            self.fr +
            self.tu+
            self.li +
            self.sp
        )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_price))
        self.d_tax=round((self.total_cold_price * 0.025),2)
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))
        self.total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_price+
                              self.c_tax+
                              self.g_tax+
                              self.d_tax
                              )
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Webcode Reatil")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number:  {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n ====================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\tprice")
        self.txtarea.insert(END, f"\n ====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","plz enter any product")
        else:
            self.welcome_bill()
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\tRs.{self.so}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\tRs.{self.f_c}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\tRs.{self.f_w}")
            if self.hair_spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spary\t\t{self.hair_spray.get()}\tRs.{self.h_s}")
            if self.gell.get() != 0:
                self.txtarea.insert(END, f"\n Gell\t\t{self.gell.get()}\tRs.{self.g}")
            if self.loshan.get() != 0:
                self.txtarea.insert(END, f"\n Loshan\t\t{self.loshan.get()}\tRs.{self.l}")

            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\tRs.{self.r}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\tRs.{self.f_o}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\tRs.{self.d}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\tRs.{self.w}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\tRs.{self.s}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\tRs.{self.t}")

            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\tRs.{self.m}")
            if self.cock.get()!=0:
                self.txtarea.insert(END,f"\n Cock\t\t{self.cock.get()}\tRs.{self.co}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\tRs.{self.fr}")
            if self.thumbs_up.get() != 0:
                self.txtarea.insert(END, f"\n Thumbs Up\t\t{self.thumbs_up.get()}\tRs.{self.tu}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\tRs.{self.li}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\tRs.{self.sp}")
            self.txtarea.insert(END, f"\n --------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmatic Tax:\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax:\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmatic Tax:\t\t\t{self.cold_drink_tax.get()}")
            self.txtarea.insert(END,f"\n Total Bill:\t\t\tRs. {round((self.total_bill),2)}")
            self.txtarea.insert(END, f"\n ----------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do yoy want to save the bill?")
        if op>0:

           self.bill_data=self.txtarea.get('1.0',END)
           f1=open("C:/users/paresh/bills/"+str(self.bill_no.get())+".txt","w")
           f1.write(self.bill_data)
           f1.close()
           messagebox.showinfo("saved","bill saved successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("C:/bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"C:/bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                   self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","invalid Bill no")
    def clear_data(self):
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.hair_spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)
        # .......#
        self.rice.set(0)
        self.food_oil .set(0)
        self.daal .set(0)
        self.wheat.set(0)
        self.sugar .set(0)
        self.tea.set(0)
        # ........#
        self.maza .set(0)
        self.cock.set(0)
        self.frooti .set(0)
        self.thumbs_up.set(0)
        self.limca .set(0)
        self.sprite.set(0)
        # ....total product..#
        self.cosmetic_price .set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")
        # .....customer...#
        self.c_name.set("")
        self.c_phone .set("")

        self.bill_no.set("")
        x = random.randint(1000, 99999)
        self.bill_no.set(str(x))
        self.search_bill .set("")
        self.welcome_bill()
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do You really Want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()