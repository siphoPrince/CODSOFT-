import tkinter as tk
from tkinter import *
import speech_recognition as sr

recognizer = sr.Recognizer()

# screen
root=tk.Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#D3D3D3")

#lable for display
label_screen= Label(root,width=25,height=2, text=" ", font=("arial",30))
label_screen.pack()

# Function to handle voice input
def handle_voice_input():
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        voice_input = recognizer.recognize_google(audio)
        label_screen["text"] += " " + voice_input
        evaluate_expression()
    except sr.UnknownValueError:
        label_screen["text"] = "Voice recognition could not understand audio"
    except sr.RequestError as e:
        label_screen["text"] = "Could not request results from Google Speech Recognition service; {0}".format(e)

def evaluate_expression():
    current_text = label_screen["text"].replace("plus", "+").replace("minus", "-").replace("times", "*").replace("divided by", "/")

    try:
        result = eval(current_text)
        label_screen["text"] = str(result)
    except Exception as e:
        label_screen["text"] = "Error"


def on_button_click(value):
    current_text = label_screen["text"]
    
    # If the button clicked is "=" then evaluate the expression
    if value == "=":
        try:
            result = eval(current_text)
            label_screen["text"] = str(result)
        except Exception as e:
            label_screen["text"] = "Error"
    # If the button clicked is "C" then clear the display
    elif value == "C":
        label_screen["text"] = ""
    # For other buttons, append the clicked value to the current text
    else:
        label_screen["text"] += str(value)

        
# buttons
Button(root,text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="#3697f5", command=lambda: on_button_click("C")).place(x=10, y=100)
Button(root,text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("/")).place(x=150, y=100)
Button(root,text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("%")).place(x=290, y=100)
Button(root,text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("*")).place(x=430, y=100)
 
Button(root,text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("7")).place(x=10, y=200)
Button(root,text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("8")).place(x=150, y=200)
Button(root,text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("9")).place(x=290, y=200)
Button(root,text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("-")).place(x=430, y=200)

Button(root,text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("4")).place(x=10, y=300)
Button(root,text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("5")).place(x=150, y=300)
Button(root,text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("6")).place(x=290, y=300)
Button(root,text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("+")).place(x=430, y=300)

Button(root,text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("1")).place(x=10, y=400)
Button(root,text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("2")).place(x=150, y=400)
Button(root,text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("3")).place(x=290, y=400)
Button(root,text="0", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click("0")).place(x=10, y=500)

Button(root,text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="black", command=lambda: on_button_click(".")).place(x=430, y=400)
Button(root,text="=", width=16, height=1, font=("arial", 30, "bold"), bd=1,fg="#fff",bg="grey", command=lambda: on_button_click("=")).place(x=150, y=500)


Button(root, text="Voice", width=10, height=1, font=("arial", 20, "bold"), bd=1, fg="#fff", bg="green", command=handle_voice_input).place(x=10, y=550)


root.mainloop()
