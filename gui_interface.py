import tkinter as tk
from voting_system import VoteManager

class GUIInterface(tk.Frame):
    def __init__(self, manager, master=None):
        super().__init__(master, bg='white')
        self.manager = manager
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.create_id_entry()
        self.create_candidate_selection()
        self.create_submit_button()
        self.create_message_label()
        self.create_results_display()

    def create_id_entry(self):
        id_frame = tk.Frame(self, bg='white')
        id_frame.pack(pady=(10, 5), padx=10, fill='x')
        tk.Label(id_frame, text="ID:", bg='white').pack(side=tk.LEFT)
        self.id_entry = tk.Entry(id_frame, bd=2, width=30)
        self.id_entry.pack(side=tk.RIGHT, expand=True, fill='x')

    def create_candidate_selection(self):
        tk.Label(self, text="CANDIDATES", bg='white').pack(pady=(10, 2))
        self.selected_candidate = tk.StringVar()
        self.candidates = self.manager.get_candidate_names()
        for candidate in self.candidates:
            tk.Radiobutton(self, text=candidate, variable=self.selected_candidate, value=candidate, bg='white').pack()

    def create_submit_button(self):
        self.submit_button = tk.Button(self, text="SUBMIT VOTE", command=self.vote, bg='lightgrey', fg='black')
        self.submit_button.pack(pady=10)

    def create_message_label(self):
        self.message_label = tk.Label(self, text="", bg='white')
        self.message_label.pack()

    def create_results_display(self):
        self.results_label = tk.Label(self, text="", bg='white', fg="black")
        self.results_label.pack()

    def vote(self):
        voter_id = self.id_entry.get()
        candidate = self.selected_candidate.get()
        try:
            if self.manager.vote(candidate, voter_id):
                self.update_results()
                self.message_label.config(text="Vote Recorded", fg="green")
            else:
                self.message_label.config(text="Duplicate vote or invalid ID", fg="red")
        except ValueError as e:
            self.message_label.config(text=str(e), fg="red")

    def update_results(self):
        results = self.manager.get_results()
        results_text = "\n".join(f"{candidate}: {votes}" for candidate, votes in results.items())
        self.results_label.config(text=results_text)
        self.manager.save_voting_record_to_csv()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIInterface(VoteManager(), master=root)
    app.mainloop()
