from tkinter import *
import time

#main variables
text_to_write = list('Hello guys!')
print(text_to_write)
root = Tk()
text_box = Entry(root)

word_count = text_to_write.count(' ') + 1  #the count of words
space_count = 0  #the count of spaces
input_text = []  #the text we input
on_first_entry = False
start_timer = 0
end_timer = 0


def read_char(entry):

    global word_count, space_count, text_box, input_text, text_to_write, on_first_entry, start_timer, end_timer  #global variables

    if not on_first_entry:  #start timer
        start_timer = time.time()
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
        end_timer = time.time()
        print(end_timer - start_timer)
        return

    if entry == '\x08':  #\x08 is backspace. If backspace is pressed we pop the last item of the list(if there is one)
        try:
            popped_text = input_text.pop()  #we save the popped value
            if popped_text == ' ':  #if the popped value is a space we decrease the space_count by one
                space_count -= 1
        except:
            pass
        return  #return so "\x08" is not added to the list

    if entry == '':  #used to ignore shift key
        return

    input_text.append(entry)
    print(input_text)


text_box.grid(row=0, column=0)
text_box.bind('<KeyPress>', lambda e: read_char(e.char))

mainloop()