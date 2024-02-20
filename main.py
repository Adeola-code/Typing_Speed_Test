import tkinter as tk
import random
import time


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Adeola's Typing Speed Test App")

        self.words = ["python", "programming", "tkinter", "hello", "backend", "developer", "keyboard", "mississippi",
                      "application", "django"]
        self.current_word = ""
        self.start_time = None

        self.create_widgets()

    def create_widgets(self):
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Helvetica", 18))
        self.entry.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.result_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

    def start_test(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
        self.start_time = time.time()
        self.entry.bind("<Return>", self.check_result)

    def check_result(self, event):
        user_input = self.entry.get().strip()
        end_time = time.time()

        if user_input == self.current_word:
            elapsed_time = end_time - self.start_time
            words_per_minute = int((len(self.current_word) / 5) / (elapsed_time / 60))
            self.result_label.config(text=f"Your typing speed: {words_per_minute} words per minute")
        else:
            self.result_label.config(text="Incorrect. Try again.")

        self.entry.unbind("<Return>")
        self.start_button.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
