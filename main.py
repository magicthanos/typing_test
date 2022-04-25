from tkinter import *
import time


def get_text():
    with open('sentences.txt', 'r') as f:
        import random
        input_text = f.readlines()
        return input_text[random.randint(0, len(input_text) - 1)]


#main variables
text_to_write = list(get_text())
root = Tk()
root.title('Typing Test by magicthanos')
text_box = Entry(root, font=('JetBrains Mono', 15), width=50)

word_count = text_to_write.count(' ') + 1  #the count of words
space_count = 0  #the count of spaces
input_text = []  #the text we input
on_first_entry = False
start_timer = 0
t = time


def read_char(entry, end_timer=0):

    global word_count, space_count, text_box, input_text, text_to_write, on_first_entry, start_timer  #global variables

    if not on_first_entry:  #start timer
        start_timer = t.time()
        on_first_entry = True

    #' ' is space
    if entry == ' ':
        space_count += 1

    #if space_count == word_count then we "finished" typing the text
    #if the length of the two lists is the same we are "finished"
    #the last value of the input text has to be 'space' to end, so we can correct any  mistake
    if space_count == word_count or len(input_text) == len(
            text_to_write) and input_text[-1] == ' ':
        text_box.config(state='disabled')
        text_box.unbind('<KeyPress>')
        end_timer = t.time()

        (gross, net, acc) = calculate_wpm(start_timer, end_timer, input_text,
                                          text_to_write)
        wpm_label = Label(
            root,
            text=
            f'Gross WPM: {gross} \nNet WPM: {net} \nTime: {end_timer-start_timer} \nAccuracy: {acc}%',
            font=('JetBrains Mono', 10))
        wpm_label.grid(row=1, column=0)
        return

    if entry == '\x08':  #\x08 is backspace. If backspace is pressed we pop the last item of the list(if there is one)
        try:
            popped_text = input_text.pop()  #we save the popped value
            if popped_text == ' ':  #if the popped value is a space we decrease the space_count by one
                space_count -= 1
        except:
            pass
        return  #return so "\x08" is not added to the list

    if entry in ['', '\r']:  #used to ignore shift key and enter key
        return

    input_text.append(entry)  #add the input to the list


def calculate_wpm(start_time, end_time, input_text, text_to_write):
    time = (end_time - start_time) / 60
    gross_wpm = (len(input_text) / 5) / time
    errors = [c for c in text_to_write if c not in input_text]
    net_wpm = gross_wpm - (len(errors) / 5) / time
    accuracy = (len(input_text) - len(errors)) / len(input_text) * 100
    return (gross_wpm, net_wpm, accuracy)


text_box.grid(row=2, column=0)
text_box.bind('<KeyPress>', lambda e: read_char(e.char))

text_display = Label(root,
                     text=''.join(text_to_write),
                     font=('JetBrains Mono', 20))
text_display.grid(row=0, column=0)

mainloop()