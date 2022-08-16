import tkinter as tk
from PIL import ImageTk,Image
import cv2 as cv
import numpy as np
from skimage.feature import local_binary_pattern
import matplotlib.pyplot as plt

class GUI:
    def __init__(self, radius, n_points, METHOD):
        self.radius = radius
        self.n_points = n_points
        self.METHOD = METHOD
        
        self.ctr=""
        # Set root
        self.root = tk.Tk()
        self.root.title("Identifikasi Nominal Mata Uang Rupiah")
        
        # Set frame
        self.frame = tk.LabelFrame(self.root, width=900, height=550, bd=0, bg="blue")
        self.frame.pack(padx=0, pady=0)
        
        self.setNav()
        self.setHome()
        self.setImageList()
        self.root.geometry("900x550")
        self.root.eval('tk::PlaceWindow . center')
        self.root.overrideredirect(1)
        self.root.mainloop()
        
    def setNav(self):
        self.nav_img = ImageTk.PhotoImage(Image.open("UI/Nav.jpg"))
        self.nav = tk.Canvas(self.frame, width=900, height=100, bd=0, highlightthickness=0)
        self.nav.create_image(0, 0, anchor=tk.NW, image=self.nav_img)
        self.nav.place(x=0, y=0, width=900, height=100)
        
        # set button
        self.btnHome = tk.Button(self.nav, text="Home", width=100, height=25, font=("Roboto",11), bg="#EEFCFD", bd=0, command=lambda:self.setButtonMenu(0))
        self.btnDataset = tk.Button(self.nav, text="Dataset", width=100, height=25, font=("Roboto",11), bg="#EEFCFD", bd=0, command=lambda:self.setButtonMenu(1))
        self.btnPlot = tk.Button(self.nav, text="Plot", width=100, height=25, font=("Roboto",11), bg="#EEFCFD", bd=0, command=lambda:self.setButtonMenu(2))
        self.btnExit = tk.Button(self.nav, text="Exit", width=100, height=25, font=("Roboto", 11), bg="#088292", bd=0, fg="white", command=self.root.destroy)
        self.btnHome.place(x=457, y=35, width=80, height=25)
        self.btnDataset.place(x=567, y=35, width=80, height=25)
        self.btnPlot.place(x=677, y=35, width=80, height=25)
        self.btnExit.place(x=787, y=35, width=80, height=25)
        
    def setHome(self):
        self.home_img = ImageTk.PhotoImage(Image.open("UI/Home.jpg"))
        self.home = tk.Canvas(self.frame, width=900, height=450, bd=0, highlightthickness=0)
        self.home.create_image(0, 0, anchor=tk.NW, image=self.home_img)
        self.home.place(x=0, y=100, width=900, height=450)
        
        self.btnIden = tk.Button(self.home, text="Identifikasi", width=105, height=40, bd=0, bg="#088292", font=("Roboto",13), fg="white", command=self.setBtnIden)
        self.btnIden.place(x=546, y=10, width=105, height=40)
        
        self.url = tk.Entry(self.home, width=287, borderwidth=0)
        self.url.place(x=248, y=11, width=287, height=38)

    def setDataset(self):
        self.dataNo=0
        self.dataset_img = ImageTk.PhotoImage(Image.open("UI/Dataset.jpg"))
        self.dataset = tk.Canvas(self.frame, width=900, height=500, bd=0, highlightthickness=0)
        self.dataset.create_image(0, 0, anchor=tk.NW, image=self.dataset_img)
        self.dataset.place(x=0, y=100, width=900, height=500)
        
        # set tampilan image
        self.img_label= tk.Label(self.dataset, image=self.image_list[0][0])
        self.img_label.place(x=272, y=74, width=470, height=200)
        
        # set nama file image
        self.img_name = tk.Label(self.dataset, text="Image "+str(1)+".jpg", font=("Roboto", 11), bd=0, bg="#F9E3FF", anchor=tk.E)
        self.img_name.place(x=272, y=274, width=470, height=30)
        
        # set button nominal uang
        self.btn1 = tk.Button(self.dataset, text="1.000", bd=0, bg="#088292", font=("Roboto",10), fg="white", command=lambda:self.setBtnDataset(0))
        self.btn2 = tk.Button(self.dataset, text="2.000", bd=0, bg="#088292", font=("Roboto",10), fg="white", command=lambda:self.setBtnDataset(1))
        self.btn5 = tk.Button(self.dataset, text="5.000", bd=0, bg="#088292", font=("Roboto",10), fg="white", command=lambda:self.setBtnDataset(2))
        self.btn10 = tk.Button(self.dataset, text="10.000", bd=0, bg="#088292", font=("Roboto",10), fg="white", command=lambda:self.setBtnDataset(3))
        self.btn20 = tk.Button(self.dataset, text="20.000", bd=0, bg="#088292", font=("Roboto",10), fg="white", command=lambda:self.setBtnDataset(4))
        self.btn50 = tk.Button(self.dataset, text="50.000", bd=0, bg="#088292", font=("Roboto",10), fg="white", command=lambda:self.setBtnDataset(5))
        self.btn75 = tk.Button(self.dataset, text="75.000", bd=0, bg="#088292", font=("Roboto",10), fg="white", command=lambda:self.setBtnDataset(6))
        self.btn100 = tk.Button(self.dataset, text="100.000", bd=0, bg="#088292", font=("Roboto",10), fg="white", command=lambda:self.setBtnDataset(7))
        self.btnNext = tk.Button(self.dataset, text=">>", bd=0, bg="#088292", font=("Roboto",12), fg="white", command=lambda:self.setBtnNext(1))
        self.btnBack = tk.Button(self.dataset, text="<<", bd=0, bg="#088292", font=("Roboto",12), fg="white", state=tk.DISABLED)
        self.btn1.place(x=82, y=37, width=70, height=25)
        self.btn2.place(x=82, y=77, width=70, height=25)
        self.btn5.place(x=82, y=117, width=70, height=25)
        self.btn10.place(x=82, y=157, width=70, height=25)
        self.btn20.place(x=82, y=197, width=70, height=25)
        self.btn50.place(x=82, y=237, width=70, height=25)
        self.btn75.place(x=82, y=277, width=70, height=25)
        self.btn100.place(x=82, y=317, width=70, height=25)
        self.btnNext.place(x=522, y=371, width=100, height=40)
        self.btnBack.place(x=392, y=371, width=100, height=40)    
        
    def setPlot(self):
        self.plot_img = ImageTk.PhotoImage(Image.open("UI/Plot.jpg"))
        self.plot = tk.Canvas(self.frame, width=900, height=450, bd=0, highlightthickness=0)
        self.plot.create_image(0, 0, anchor=tk.NW, image=self.plot_img)
        self.plot.place(x=0, y=100, width=900, height=450)
        # set plot image
        out_plot = Image.open("plotData.jpg")
        out_plot = out_plot.resize((458,290), Image.ANTIALIAS)
        self.plt_img = ImageTk.PhotoImage(out_plot)
        self.showPlt = tk.Canvas(self.plot, width=425, height=290, bd=0, highlightthickness=0, bg="red")
        self.showPlt.create_image(0, 0, anchor=tk.NW, image=self.plt_img)
        self.showPlt.place(x=82, y=60, width=425, height=290)
        #self.plt_label= tk.Label(self.plot, image=self.plt_img)
        #self.plt_label.place(x=82, y=60, width=458, height=290)
        
        # label akurasi
        akurasi = tk.Label(self.plot, text=": "+str(self.akurasi), font=("Roboto",10), fg="#088292", bg="#EEFCFD")
        akurasi.place(x=662, y=295, width=40, height=15)
        
    def setButtonMenu(self, x):
        if x==0:
            self.setHome()
        elif x==1:
            self.setDataset()
        elif x==2:
            self.setPlot()
            
    def setImageList(self):
        self.image_list=[]
        self.image_hist=[]
        self.kelas=""
        for i in range(0,8):
            if i==0:kelas="1RIBU"
            elif i==1:kelas="2RIBU"
            elif i==2:kelas="5RIBU"
            elif i==3:kelas="10RIBU"
            elif i==4:kelas="20RIBU"
            elif i==5:kelas="50RIBU"
            elif i==6:kelas="75RIBU"
            elif i==7:kelas="100RIBU"
            else:continue
            list_1 = []
            for j in range(0,15):
                file = "DATASET_UANG/"+kelas+"/"+str(j+1)+".jpg"
                image = Image.open(file)
                image = image.resize((470,200), Image.ANTIALIAS)
                list_1.append(ImageTk.PhotoImage(image))
                
                # lbp
                img = cv.imread(file, cv.IMREAD_GRAYSCALE)
                lbp = local_binary_pattern(img, self.n_points, self.radius, self.METHOD)
                hist, bins = np.histogram(lbp.ravel(),256,[0,256])
                histt = np.transpose(hist[0:256,np.newaxis])
                self.image_hist.append(histt)
            self.image_list.append(list_1)
            
        self.datasetUang = np.concatenate((self.image_hist), axis=0).astype(np.float32)
        self.kelasUang = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                   3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                                   5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
                                   7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]).astype(np.float32)
        self.getAkurasi()
        
        # plot
        sred = self.datasetUang[self.kelasUang.ravel()==1]
        plt.scatter(sred[:,0],sred[:,1],80,'r','*')
        sblue = self.datasetUang[self.kelasUang.ravel()==2]
        plt.scatter(sblue[:,0],sblue[:,1],80,'b','*')    
        smagenta = self.datasetUang[self.kelasUang.ravel()==3]
        plt.scatter(smagenta[:,0],smagenta[:,1],80,'m','*')    
        sblack = self.datasetUang[self.kelasUang.ravel()==4]
        plt.scatter(sblack[:,0],sblack[:,1],80,'#E91E63','*')    
        spink = self.datasetUang[self.kelasUang.ravel()==5]
        plt.scatter(spink[:,0],spink[:,1],80,'c','*')    
        sgr = self.datasetUang[self.kelasUang.ravel()==6]
        plt.scatter(sgr[:,0],sgr[:,1],80,'g','*')    
        syl = self.datasetUang[self.kelasUang.ravel()==7]
        plt.scatter(syl[:,0],syl[:,1],80,'y','*')
        bl = self.datasetUang[self.kelasUang.ravel()==8]
        plt.scatter(bl[:,0],bl[:,1],80,'#FFA500','*')
        # save plot
        plt.savefig('plotData.jpg')
        
    def getAkurasi(self):
        # cek akurasi 
        # naive bayes
        print("\n======================================")
        print("    KLASIFIKASI DENGAN NAIVE BAYES    ")
        print("======================================")
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(self.datasetUang, self.kelasUang, test_size=0.20, random_state=0, stratify=self.kelasUang)
        from sklearn.naive_bayes import GaussianNB
        model_gnb = GaussianNB()
        model_gnb.fit(X_train, y_train) # latih        
        # K-Fold Cross Validation
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import accuracy_score
        from sklearn.model_selection import StratifiedKFold
        skf_nb = StratifiedKFold(n_splits=5)
        i=1
        for train, test in skf_nb.split(self.datasetUang,self.kelasUang):
            X_latih_nb, X_uji_nb, y_latih_nb, y_uji_nb = self.datasetUang[train], self.datasetUang[test], self.kelasUang[train], self.kelasUang[test]
            model_gnb.fit(X_latih_nb, y_latih_nb)
            y_pred_nb = model_gnb.predict(X_uji_nb)
            print("ITERASI KE-",i)
            print("> Akurasi :",accuracy_score(y_uji_nb,y_pred_nb))
            print("> Confusion Matrix :\n",confusion_matrix(y_uji_nb, y_pred_nb, labels=[1, 2, 3, 4, 5, 6, 7, 8]))
            i=i+1
            print("--------------------------------------")
        from sklearn.model_selection import cross_val_score
        score_nb= cross_val_score(model_gnb, self.datasetUang, self.kelasUang, cv=5, scoring='accuracy')
        self.akurasi = score_nb.mean()
        print("RATA-RATA AKURASI :", self.akurasi)
        print("======================================")
            
    def setBtnIden(self):
        self.ctr = self.url.get()
        self.url.delete(0, tk.END)
        cimg = cv.imread(self.ctr, cv.IMREAD_GRAYSCALE)
        clbp = local_binary_pattern(cimg, self.n_points, self.radius, self.METHOD)
        chist, cbins = np.histogram(clbp.ravel(),256,[0,256])
        chistt = np.transpose(chist[0:256,np.newaxis])
        testData = chistt
        plt.scatter(testData[:,0],testData[:,1],80,'k','o')
        # Naive Bayes
        from sklearn.naive_bayes import GaussianNB
        model_gnb = GaussianNB()
        model_gnb.fit(self.datasetUang, self.kelasUang)
        res = model_gnb.predict(testData)       
        # set hasil
        if res==1:
            out = "1.000"
        elif res==2:
            out = "2.000"
        elif res==3:
            out = "5.000"
        elif res==4:
            out = "10.000"            
        elif res==5:
            out = "20.000"
        elif res==6:
            out = "50.000"
        elif res==7:
            out = "75.000"
        elif res==8:
            out = "100.000" 
        self.hasil = tk.Label(self.home, text="Hasil = "+out, font=("Roboto", 15, 'bold'), bd=0, bg="#AFAFBE", fg="white")
        self.hasil.place(x=467, y=340, width=356, height=47)
        # set tampilan citra uang
        img = Image.open(self.ctr)
        img = img.resize((235,100), Image.ANTIALIAS)
        self.ctr_img = ImageTk.PhotoImage(img)
        self.ctr_label= tk.Label(self.home, image=self.ctr_img)
        self.ctr_label.place(x=116, y=199, width=235, height=100)
        # set tampilan plot
        plt.savefig('plotPred.jpg') 
        pimg = Image.open("plotPred.jpg")
        pimg = pimg.resize((300,190), Image.ANTIALIAS)
        self.p_img = ImageTk.PhotoImage(pimg)
        self.p_label= tk.Label(self.home, image=self.p_img)
        self.p_label.place(x=496, y=134, width=300, height=190)
            
    def setBtnDataset(self, x):
        self.dataNo=x
        self.img_label.config(image=self.image_list[x][0])
        self.btnNext = tk.Button(self.dataset, text=">>", bd=0, bg="#088292", font=("Roboto",12), fg="white", command=lambda:self.setBtnNext(1))
        self.btnBack = tk.Button(self.dataset, text="<<", bd=0, bg="#088292", font=("Roboto",12), fg="white", state=tk.DISABLED)
        self.img_name = tk.Label(self.dataset, text="Image "+str(1)+".jpg", font=("Roboto", 11), bd=0, bg="#F9E3FF", anchor=tk.E)
        self.img_label.place(x=272, y=74, width=470, height=200)
        self.btnNext.place(x=522, y=371, width=100, height=40)
        self.btnBack.place(x=392, y=371, width=100, height=40)  
        self.img_name.place(x=272, y=274, width=470, height=30)
        
    def setBtnBack(self, image_number):
        self.img_label.config(image=self.image_list[self.dataNo][image_number])
        self.btnNext = tk.Button(self.dataset, text=">>", bd=0, bg="#088292", font=("Roboto",12), fg="white", command=lambda:self.setBtnNext(image_number+1))
        self.btnBack = tk.Button(self.dataset, text="<<", bd=0, bg="#088292", font=("Roboto",12), fg="white", command=lambda:self.setBtnBack(image_number-1))
        self.img_name = tk.Label(self.dataset, text="Image "+str(image_number+1)+".jpg", font=("Roboto", 11), bd=0, bg="#F9E3FF", anchor=tk.E)
        if image_number == 0:
            self.btnBack = tk.Button(self.dataset, text="<<", bd=0, bg="#088292", font=("Roboto",12), state=tk.DISABLED)
        self.img_label.place(x=272, y=74, width=470, height=200)
        self.btnNext.place(x=522, y=371, width=100, height=40)
        self.btnBack.place(x=392, y=371, width=100, height=40)  
        self.img_name.place(x=272, y=274, width=470, height=30)
        
    def setBtnNext(self, image_number):
        self.img_label.config(image=self.image_list[self.dataNo][image_number])
        self.btnNext = tk.Button(self.dataset, text=">>", bd=0, bg="#088292", font=("Roboto",12), fg="white", command=lambda:self.setBtnNext(image_number+1))
        self.btnBack = tk.Button(self.dataset, text="<<", bd=0, bg="#088292", font=("Roboto",12), fg="white", command=lambda:self.setBtnBack(image_number-1))
        self.img_name = tk.Label(self.dataset, text="Image "+str(image_number+1)+".jpg", font=("Roboto", 11), bd=0, bg="#F9E3FF", anchor=tk.E)
        if image_number == 14:
            self.btnNext = tk.Button(self.dataset, text=">>", bd=0, bg="#088292", font=("Roboto",12), state=tk.DISABLED)
        self.img_label.place(x=272, y=74, width=470, height=200)
        self.btnNext.place(x=522, y=371, width=100, height=40)
        self.btnBack.place(x=392, y=371, width=100, height=40)  
        self.img_name.place(x=272, y=274, width=470, height=30)

# settings for LBP
r = 2
n = 4*r
m = 'default'
gui = GUI(r, n, m)

"""
Berikut adalah directory/path dari foto uang untuk dicoba diidentifikasi pada menu home
FOTO_UANG/UANG1.jpg
FOTO_UANG/UANG2.jpg
FOTO_UANG/UANG3.jpg
FOTO_UANG/UANG4.jpg
FOTO_UANG/UANG5.jpg
FOTO_UANG/UANG6.jpg
FOTO_UANG/UANG7.jpg
FOTO_UANG/UANG8.jpg
"""