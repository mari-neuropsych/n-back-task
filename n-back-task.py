import tkinter as tk
import random
import time

class NBackTask:
    def __init__(self, master, n=2, sequence_length=20):
        self.master = master
        self.n = n
        self.sequence_length = sequence_length
        self.sequence = []
        self.current_index = 0
        self.user_responses = []
        self.start_time = None

        self.label = tk.Label(master, text="", font=("Arial", 48))
        self.label.pack(padx=20, pady=20)
        self.info_label = tk.Label(master, text=f"Press SPACE if current matches {self.n}-back", font=("Arial", 14))
        self.info_label.pack()
        master.bind("<space>", self.record_response)

        self.generate_sequence()
        self.show_next_stimulus()

    def generate_sequence(self):
        self.sequence = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(self.sequence_length)]

    def show_next_stimulus(self):
        if self.current_index < self.sequence_length:
            self.label.config(text=self.sequence[self.current_index])
            self.start_time = time.time()
            self.master.after(1000, self.evaluate_stimulus)
        else:
            self.show_results()

    def record_response(self, event):
        reaction_time = time.time() - self.start_time
        self.user_responses.append((self.current_index, reaction_time))

    def evaluate_stimulus(self):
        self.current_index += 1
        self.show_next_stimulus()

    def show_results(self):
        correct = 0
        for index, _ in self.user_responses:
            if index >= self.n and self.sequence[index] == self.sequence[index - self.n]:
                correct += 1
        total_responses = len(self.user_responses)
        accuracy = (correct / max(total_responses,1)) * 100
        self.label.config(text=f"Task Complete!\nAccuracy: {accuracy:.1f}%")
        print(f"User responses: {self.user_responses}")
        print(f"Accuracy: {accuracy:.1f}%")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("N-Back Task")
    app = NBackTask(root)
    root.mainloop()
