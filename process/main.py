import os
import tkinter
from tkinter import *
import tkinter as Tk
import imutils
import cv2
from PIL import Image, ImageTk
from tensorboard.plugins.image.summary_v2 import image

from process.gui.image_paths import ImagePaths
from process.database.config import DataBasePaths
from process.gui.setup.images.login_button import login_button_image_path

from process.face_processing.face_signup import FaceSignUp

#from process.face_processing.face_login import FacialLogin
#from process.com_interface.serial_com import SerialComunication

class CustomFrame(Tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=Tk.BOTH, expand=True)

class GraphicalUserInterface:
    def __init__(self, root):
        self.main_window = root
        self.main_window.title('face access control')
        self.main_window.geometry('1280x720')
        self.frame = CustomFrame(self.main_window)

        # config stream
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,1280)
        self.cap.set(4,720)

        # signup window
        self.signup_window = None
        self.input_name = None
        self.input_user_code = None
        self.name = None
        self.user_code = None
        self.user_list = None
        # face capture
        self.face_signup_window = None
        self.signup_video = None
        self.user_codes = []
        self.data = []

        #modules
        self.images = ImagePaths()
        self.database = DataBasePaths()
        self.face_sign_up = FaceSignUp()

        #process
        self.main()
        pass

    def gui_login(self):
        print("Acceso Facial")

    def facial_sign_up(self):
        if self.cap:
            ret, frame_bgr = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
                # process
                check_face, face_info = self.face_sign_up.process(frame, '123')
                print(check_face, face_info)
                # config video
                frame = imutils.resize(frame, width=1280)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)

                # show frames
                self.signup_video.configure(image=img)
                self.signup_video.image = img
                self.signup_video.after(10, self.facial_sign_up)
        else:
            self.cap.release()

    def data_sign_up(self):
        # extract data
        self.name, self.user_code = self.input_name.get(), self.input_user_code.get()
        #print(f'name: {self.name} user code: {self.user_code}')
        # check data
        if len(self.name) == 0 or len(self.user_code) == 0:
            print('¡Formulary incomplete!')
        else:
            # check users
            self.user_list = os.listdir(self.database.check_users)
            for u_list in self.user_list:
                user = u_list
                user = user.split('.')
                self.user_codes.append(user[0])
            if self.user_code in self.user_codes:
                print('¡Previously registered user!')
            else:
                # save data
                self.data.append(self.name)
                self.data.append(self.user_code)

                file = open(f"{self.database.users}/{self.user_code}.txt", 'w')
                file.writelines(self.name + ',')
                file.writelines(self.user_code + ',')
                file.close()

                # clear
                self.input_name.delete(0,END)
                self.input_user_code.delete(0,END)

                # face register
                self.face_signup_window = Toplevel()
                self.face_signup_window.title('face capture')
                self.face_signup_window.geometry('1280x720')

                self.signup_video = Label(self.face_signup_window)
                self.signup_video.place(x=0, y=0)
                self.signup_window.destroy()
                self.facial_sign_up()

    def gui_signup(self):
        self.signup_window = Toplevel(self.frame)
        self.signup_window.title('facial signup')
        self.signup_window.geometry('1280x720')

        # background
        background_signup_img = PhotoImage(file=self.images.gui_signup_img)
        background_signup = Label(self.signup_window, image=background_signup_img)
        background_signup.image = background_signup_img
        background_signup.place(x=0, y=0)

        # input data
        self.input_name = Entry(self.signup_window)
        self.input_name.place(x=585, y=320)
        self.input_user_code = Entry(self.signup_window)
        self.input_user_code.place(x=585,y=475)

        # button
        register_button_img = PhotoImage(file=self.images.register_img)
        register_button = Button(self.signup_window, image=register_button_img, height="40", width="200",
                                 command=self.data_sign_up)
        register_button.image = register_button_img
        register_button.place(x=1005, y=565)

    def main(self):
        # background
        background_img = PhotoImage(file=self.images.init_img)
        background = Label(self.frame, image=background_img, text='back')
        background.image = background_img
        background.place(x=0, y=0, relwidth=1, relheight= 1)

        # buttons
        login_button_img = PhotoImage(file=self.images.login_img)
        login_button = Button(self.frame, image=login_button_img, height="40", width="200", command=self.gui_login)
        login_button.image = login_button_img
        login_button.place(x=980, y=325)

        signup_button_img = PhotoImage(file=self.images.signup_img)
        signup_button = Button(self.frame, image=signup_button_img, height="40", width="200", command=self.gui_signup)
        signup_button.image = signup_button_img
        signup_button.place(x=980, y=578)