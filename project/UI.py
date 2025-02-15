"""
UI.py
This module creates a graphical user interface (GUI) for sentiment analysis using Tkinter. 
It loads pre-trained machine learning models and allows users to input text reviews, 
which are then analyzed to predict the sentiment (positive or negative) using three different models:
Logistic Regression, Naive Bayes, and Support Vector Classifier.
Constants:
    LOGISTIC_MODEL_PATH (str): Path to the logistic regression model file.
    NAIVE_BAYES_MODEL_PATH (str): Path to the naive bayes model file.
    SVC_MODEL_PATH (str): Path to the support vector classifier model file.
    BG_COLOR (str): Background color for the GUI.
    FONT (tuple): Font settings for the GUI.
Functions:
    predict_sentiment(): Retrieves the text from the input box, uses the loaded models to predict sentiment, 
                         and displays the results in a message box.
Main:
    Creates and configures the main window, styles, and widgets for the GUI, and runs the Tkinter main loop.
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import joblib

# Constants
LOGISTIC_MODEL_PATH = r'.\models\logistic_regression_model.pkl'
NAIVE_BAYES_MODEL_PATH = r'.\models\naive_bayes_model.pkl'
SVC_MODEL_PATH = r'.\models\support_vector_classifier.pkl'
BG_COLOR = '#add8e6'
FONT = ('Helvetica', 12)

# Load the models
logistic_regression_model = joblib.load(LOGISTIC_MODEL_PATH)
naive_bayes_model = joblib.load(NAIVE_BAYES_MODEL_PATH)
support_vector_classifier_model = joblib.load(SVC_MODEL_PATH)

def predict_sentiment():
    review = entry.get("1.0", tk.END)
    results = []

    for model, name in [(logistic_regression_model, "Logistic Regression"), 
                        (naive_bayes_model, "Naive Bayes"), 
                        (support_vector_classifier_model, "Support Vector Classifier")]:
        prediction = model.predict([review])
        sentiment = "Positive" if prediction == 1 else "Negative"
        results.append(f"{name} Sentiment: {sentiment}")

    messagebox.showinfo("Sentiment Analysis Results", "\n".join(results))

# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis App")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Style configuration
style = ttk.Style()
style.configure('TButton', font=FONT, padding=10)
style.configure('TLabel', font=FONT, background=BG_COLOR)
style.configure('TText', font=FONT, background='#ffffff', foreground='#000000')

# Create a frame
frame = ttk.Frame(root, padding="10 10 10 10", style='My.TFrame')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add custom style for the frame
style.configure('My.TFrame', background=BG_COLOR)

# Create a label
label = ttk.Label(frame, text="Enter your review:")
label.grid(row=0, column=0, pady=10, sticky=(tk.W, tk.E))

# Create a text box
entry = tk.Text(frame, height=10, width=50, font=FONT)
entry.grid(row=1, column=0, pady=10, sticky=(tk.W, tk.E))

# Create a submit button
submit_button = ttk.Button(frame, text="Submit", command=predict_sentiment, style='My.TButton')
submit_button.grid(row=2, column=0, pady=10)

# Add custom style for the button
style.map('My.TButton', background=[('active', '#32cd32'), ('!active', '#90ee90')])

# Configure resizing behavior
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

# +



# Run the application
root.mainloop()
# -



# +








# +










# +



# -


# +




# -






# +








# -











# +



# -










































