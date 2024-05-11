import tkinter as tk
from gui_interface import GUIInterface
from voting_system import VoteManager

"""
Main execution module for the Voting Application.

This script initializes the main components of the application
and starts the GUI interface for user interactions.
"""

def main():
    """Entry point for the Voting Application."""
    root = tk.Tk()
    app = GUIInterface(VoteManager(), master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
