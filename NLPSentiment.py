import tkinter as tk
from tkinter import ttk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment(sentence):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(sentence)

    if sentiment_scores['compound'] >= 0.05:
        sentiment = "Positive"
        color = "#00ff00"  # Green
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "Negative"
        color = "#ff0000"  # Red
    else:
        sentiment = "Neutral"
        color = "#cccccc"  # Grey

    explanation = f"Compound Score: {sentiment_scores['compound']:.2f}\n" \
                  f"Sentiment: {sentiment}"

    return explanation, color

def analyze_button_clicked():
    sentence = sentence_entry.get()
    result, background_color = analyze_sentiment(sentence)
    result_var.set(result)
    frame.configure(bg=background_color)

# Create main window
window = tk.Tk()
window.title("Sentiment Analysis GUI")
window.configure(background="#333")  # Set initial background color

# Create frame
frame = tk.Frame(window, background="#333", padx=20, pady=20)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create widgets
label = ttk.Label(frame, text="Enter a sentence:")
sentence_entry = ttk.Entry(frame, width=40)
analyze_button = ttk.Button(frame, text="Analyze Sentiment", command=analyze_button_clicked)
result_var = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_var)

# Grading explanation label
grading_label = ttk.Label(frame, text="Sentiment Grading:\nPositive: compound score >= 0.05\nNegative: compound score <= -0.05\nNeutral: -0.05 < compound score < 0.05", font=('Helvetica', 10), justify=tk.LEFT)

# Place widgets in the frame
label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
sentence_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10))
analyze_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))
result_label.grid(row=3, column=0, columnspan=2, pady=(0, 10))
grading_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Start the GUI
window.mainloop()
