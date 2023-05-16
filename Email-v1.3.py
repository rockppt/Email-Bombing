import tkinter as tk
import requests

API_URL = "https://v.api.aa1.cn/api/qqemail/new/?to={0}&subject={1}&message={2}&from_mail={3}"

root = tk.Tk()
root.geometry("530x400")
root.title("Send Email")

# create labels and entry boxes
to_label = tk.Label(root, text="收件人:")
to_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
to_entry = tk.Entry(root, width=50)
to_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="we")

subject_label = tk.Label(root, text="主题:")
subject_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
subject_entry = tk.Entry(root, width=50)
subject_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="we")

message_label = tk.Label(root, text="内容:")
message_label.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
message_entry = tk.Text(root, height=10, width=60, wrap="word")
message_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="we")

from_label = tk.Label(root, text="发件人:")
from_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
from_entry = tk.Entry(root, width=50)
from_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="we")

count_label = tk.Label(root, text="发送次数:")
count_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
count_spinbox = tk.Spinbox(root, from_=1, to=1000, width=10)
count_spinbox.grid(row=4, column=1, padx=5, pady=5, sticky="w")

status_label = tk.Label(root, text="现况: ")
status_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
status_entry = tk.Entry(root, state="readonly", width=50)
status_entry.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="we")


def send_email():
    # get input values
    to = to_entry.get()
    subject = subject_entry.get()
    message = message_entry.get("1.0", tk.END)
    from_mail = from_entry.get()
    count = count_spinbox.get()

    # validate input values
    if not to or not subject or not message or not from_mail:
        status_entry.config(state="normal")
        status_entry.delete(0, tk.END)
        status_entry.insert(0, "请填写所有字段。")
        status_entry.config(state="readonly")
        return

    # send email
    try:
        for i in range(int(count)):
            response = requests.get(API_URL.format(to, subject, message, from_mail))
            if response.status_code == 200:
                status_entry.config(state="normal")
                status_entry.delete(0, tk.END)
                status_entry.insert(0, "Email发送成功。")
                status_entry.config(state="readonly")
            else:
                status_entry.config(state="normal")
                status_entry.delete(0, tk.END)
                status_entry.insert(0, "Email发送失败：{}".format(response.text))
                status_entry.config(state="readonly")
    except Exception as e:
        status_entry.config(state="normal")
        status_entry.delete(0, tk.END)
        status_entry.insert(0, "Email发送失败：{}".format(str(e)))
        status_entry.config(state="readonly")


# create button for sending email
send_button = tk.Button(root, text="发送Email", command=send_email)
send_button.grid(row=6, column=1, padx=5, pady=5, sticky="we")

root.mainloop()

# Download：https://github.com/rockppt/Email-Bombing.git