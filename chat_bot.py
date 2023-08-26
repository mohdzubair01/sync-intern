import tkinter as tk
from tkinter import messagebox

class AdmissionChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Admission Query Chatbot")
        self.create_widgets()
        self.user_info = {}

    def create_widgets(self):
        self.chat_area = tk.Text(self.root, wrap=tk.WORD)
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.insert(tk.END, "Chatbot: Welcome! Please provide the following information for admission:\n")
        self.chat_area.configure(state=tk.DISABLED)

        self.user_input = tk.Entry(self.root, width=50)
        self.user_input.pack(padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.process_input)
        self.submit_button.pack(pady=10)

        self.finish_button = tk.Button(self.root, text="Finish", command=self.display_final_report, state=tk.DISABLED)
        self.finish_button.pack(pady=10)

    def process_input(self):
        user_message = self.user_input.get()
        self.add_message("You: " + user_message)

        if "name" not in self.user_info:
            self.user_info["name"] = user_message
            self.add_message("Chatbot: Hi, {}. What's your age?".format(user_message))
        elif "age" not in self.user_info:
            try:
                age = int(user_message)
                self.user_info["age"] = age
                self.add_message("Chatbot: Great! What's your desired course?")
            except ValueError:
                self.add_message("Chatbot: Please enter a valid age.")
        elif "course" not in self.user_info:
            self.user_info["course"] = user_message
            self.add_message("Chatbot: Thanks! What's your previous GPA?")
        elif "gpa" not in self.user_info:
            try:
                gpa = float(user_message)
                self.user_info["gpa"] = gpa
                self.add_message("Chatbot: What's your preferred mode of study? (Full-time / Part-time)")
            except ValueError:
                self.add_message("Chatbot: Please enter a valid GPA.")
        elif "study_mode" not in self.user_info:
            self.user_info["study_mode"] = user_message
            self.add_message("Chatbot: Do you have any specific question or concern about the admission process?")
        else:
            # Handle additional steps here if needed.
            self.add_message("Chatbot: Thank you! If you have more questions, feel free to ask.")
        
        if len(self.user_info) == 5:  # Number of steps to collect information
            self.finish_button.config(state=tk.NORMAL)

        self.user_input.delete(0, tk.END)

    def display_final_report(self):
        self.add_message("Chatbot: Here is the final report of the collected data:\n")
        for key, value in self.user_info.items():
            self.add_message("{}: {}".format(key.capitalize(), value))
        self.add_message("Chatbot: Your application will be processed. If you need any further assistance, please let us know.")
        self.finish_button.config(state=tk.DISABLED)

    def add_message(self, message):
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.insert(tk.END, "\n" + message)
        self.chat_area.configure(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = AdmissionChatbot(root)
    root.mainloop()
