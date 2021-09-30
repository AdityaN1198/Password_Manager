import pickle
import tkinter as tk
from data_saving import load_data

users_dict = load_data()

login_signup_win = tk.Tk()
login_signup_win.geometry('200x100')
login_signup_win.eval('tk::PlaceWindow . center')
login_signup_win.title('Password Manager')

def dest_win():
    login_signup_win.destroy()
    window = tk.Tk()
    window.geometry('600x400')
    window.title('Password Manager')

    welcome_text = tk.Label(window,
                            text='hi please enter your username and password below, to see your passwords')
    welcome_text.pack()

    username_text = tk.Label(window,
                             text='Username')

    username_text.pack()
    username_text_field = tk.Entry(window)
    username_text_field.pack()

    password_text = tk.Label(window,
                             text='Password')
    password_text.pack()
    password_text_field = tk.Entry(window,
                                   show='*')
    password_text_field.pack()

    def check_auth():
        username = username_text_field.get()
        if username not in users_dict:
            win = tk.Toplevel()
            win.wm_title("Wrong Credentials")

            l = tk.Label(win, text="The credentials do not match, please enter check your credentials")
            l.grid(row=0, column=0)

            b = tk.Button(win, text="Okay", command=win.destroy)
            b.grid(row=1, column=0)

        else:
            password = password_text_field.get()
            if users_dict[username]['password'] != password:
                win = tk.Toplevel()
                win.wm_title("Wrong Credentials")

                l = tk.Label(win, text="The credentials do not match, please enter check your credentials")
                l.grid(row=0, column=0)

                b = tk.Button(win, text="Okay", command=win.destroy)
                b.grid(row=1, column=0)

            else:
                window.destroy()

                def show_pass():
                    choice_win.withdraw()
                    second_win = tk.Tk()
                    second_win.geometry('500x100')
                    second_win.title('Passwords')

                    def display_passwords():
                        whole_pass = 'Platform             Password \n'
                        for i in users_dict[username]:
                            if i != 'password':
                                whole_pass += i + "           " + users_dict[username][i] + '\n'

                        return whole_pass

                    def go_back():
                        second_win.destroy()
                        choice_win.deiconify()

                    show_pass = tk.Label(second_win,
                                         text=display_passwords())

                    show_pass.pack()

                    back_button = tk.Button(second_win,
                                            text='Done',
                                            command=go_back)
                    back_button.pack()

                    second_win.mainloop()

                def add_pass():

                    def go_back():
                        add_pass_win.destroy()
                        choice_win.deiconify()

                    def add_to_dict():
                        plat = platform.get()
                        new_pass = new_password.get()

                        users_dict[username][plat] = new_pass

                        with open('user_data', 'wb') as f:
                            pickle.dump(users_dict, f)

                        go_back()

                    choice_win.withdraw()

                    add_pass_win = tk.Tk()
                    add_pass_win.geometry('500x200')
                    add_pass_win.eval('tk::PlaceWindow . center')

                    platform_text = tk.Label(add_pass_win,
                                             text='Name of Platform')
                    platform_text.pack()

                    platform = tk.Entry(add_pass_win)
                    platform.pack()

                    new_password_text = tk.Label(add_pass_win,
                                                 text='Password')
                    new_password_text.pack()

                    new_password = tk.Entry(add_pass_win)
                    new_password.pack()

                    add_pass = tk.Button(add_pass_win,
                                         text='Add Password',
                                         command=add_to_dict)
                    add_pass.pack()
                    add_pass_win.mainloop()

                choice_win = tk.Tk()
                choice_win.geometry('500x100')
                choice_win.eval('tk::PlaceWindow . center')
                choice_win.title('Password Manager')

                see_pass = tk.Button(choice_win,
                                     text='Show my Passwords',
                                     command=show_pass)
                see_pass.pack()

                add_new_pass = tk.Button(choice_win,
                                         text='Add a new Password',
                                         command=add_pass)
                add_new_pass.pack()


                choice_win.mainloop()

    submit_button = tk.Button(window,
                              text='Log In',
                              command=check_auth)
    submit_button.pack()

    window.mainloop()

log_in = tk.Button(login_signup_win,
                   text='Log In',
                   command=dest_win)
log_in.pack()

def make_new_acct():
    global users_dict

    new_acct_win = tk.Toplevel()
    new_acct_win.geometry('500x300')

    new_user_name_text = tk.Label(new_acct_win,
                                  text='New Username')
    new_user_name_text.pack()


    new_user_name = tk.Entry(new_acct_win)
    new_user_name.pack()

    new_acct_pass_text = tk.Label(new_acct_win,
                                  text='Password')
    new_acct_pass_text.pack()

    new_acct_pass = tk.Entry(new_acct_win,
                             show="*")
    new_acct_pass.pack()

    confirm_pass_text = tk.Label(new_acct_win,
                                  text='Confirm Password')
    confirm_pass_text.pack()

    confirm_pass = tk.Entry(new_acct_win,
                            show="*")
    confirm_pass.pack()

    def add_acct():


        new_user = new_user_name.get()
        new_pass = new_acct_pass.get()
        confirm_new_pass = confirm_pass.get()

        if new_pass != confirm_new_pass:
            win = tk.Toplevel()
            win.wm_title("Error")

            l = tk.Label(win, text="Passwords do not match")
            l.grid(row=0, column=0)

            b = tk.Button(win, text="Okay", command=win.destroy)
            b.grid(row=1, column=0)

        elif len(new_pass) <4:
            win = tk.Toplevel()
            win.wm_title("Error")

            l = tk.Label(win, text="Password should be longer than 4 Chars")
            l.grid(row=0, column=0)

            b = tk.Button(win, text="Okay", command=win.destroy)
            b.grid(row=1, column=0)


        elif new_user in users_dict:
            win = tk.Toplevel()
            win.wm_title("Wrong Credentials")

            l = tk.Label(win, text="Username Not available")
            l.grid(row=0, column=0)

            b = tk.Button(win, text="Okay", command=win.destroy)
            b.grid(row=1, column=0)

        else:
            users_dict[new_user] = {'password':new_pass}
            with open('user_data', 'wb') as f:
                pickle.dump(users_dict,f)

            new_acct_win.destroy()
            login_signup_win.deiconify()


    add_new_acct = tk.Button(new_acct_win,
                             text='Add New Account',
                             command=add_acct)
    add_new_acct.pack()




create_new_acc = tk.Button(login_signup_win,
                           text='Add New Account',
                           command=make_new_acct)
create_new_acc.pack()


login_signup_win.mainloop()

