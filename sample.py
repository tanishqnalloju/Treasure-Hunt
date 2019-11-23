import time
from tkinter import *
import PySimpleGUI as sg

def start():
    menu_op = ['1dnidbibi', '2jnoiib', '3uhoih']
    
    menu_box = [sg.Listbox(values = menu_op, bind_return_key = True, size = (50, 20))]

    layout = [[sg.Text('Menu')], menu_box,  [sg.Exit()]]
    window = sg.Window('Game').Layout(layout)

    
    choice, eflag = None, None
    try:
        while True:      
            event, values = window.Read()  
            loading_gif = Image(filename = None, data = "PGh0bWwgbGFuZz0idWsiPjxoZWFkPjxtZXRhIGh0dHAtZXF1aXY9IkNvbnRlbnQtVHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PUlTTy04ODU5LTEiPjx0aXRsZT4mIzEwNTU7JiMxMDg2OyYjMTA4NzsmIzEwNzc7JiMxMDg4OyYjMTA3NzsmIzEwNzY7JiMxMDc4OyYjMTA3NzsmIzEwODU7JiMxMDg1OyYjMTEwMzsgJiMxMDg3OyYjMTA4ODsmIzEwODY7ICYjMTA4NzsmIzEwNzc7JiMxMDg4OyYjMTA3NzsmIzEwNzI7JiMxMDc2OyYjMTA4ODsmIzEwNzc7JiMxMDg5OyYjMTA5MTsmIzEwNzQ7JiMxMDcyOyYjMTA4NTsmIzEwODU7JiMxMTAzOzwvdGl0bGU+PHN0eWxlPmJvZHksZGl2LGF7Zm9udC1mYW1pbHk6Um9ib3RvLEhlbHZldGljYU5ldWUsQXJpYWwsc2Fucy1zZXJpZn1ib2R5e2JhY2tncm91bmQtY29sb3I6I2ZmZjttYXJnaW4tdG9wOjNweH1kaXZ7Y29sb3I6IzAwMH1hOmxpbmt7Y29sb3I6IzAwY31hOnZpc2l0ZWR7Y29sb3I6IzU1MWE4Yn1hOmFjdGl2ZXtjb2xvcjpyZWR9ZGl2Lm15bUdve2JvcmRlci10b3A6MXB4IHNvbGlkICNiYmI7Ym9yZGVyLWJvdHRvbToxcHggc29saWQgI2JiYjtiYWNrZ3JvdW5kOiNmMmYyZjI7bWFyZ2luLXRvcDoxZW07d2lkdGg6MTAwJX1kaXYuYVhnYUdie3BhZGRpbmc6MC41ZW0gMDttYXJnaW4tbGVmdDoxMHB4fWRpdi5mVGs3dmR7bWFyZ2luLWxlZnQ6MzVweDttYXJnaW4tdG9wOjM1cHh9PC9zdHlsZT48c2NyaXB0IG5vbmNlPSJKUnZSYzVEZ0ExWFI5dHFMZmgzamdnPT0iPmZ1bmN0aW9uIGdvX2JhY2soKXt3aW5kb3cuaGlzdG9yeS5nbygtMSk7cmV0dXJuIGZhbHNlO30KCmZ1bmN0aW9uIGN0dShvaSxjdCl7dmFyIGxpbmsgPSBkb2N1bWVudCAmJiBkb2N1bWVudC5yZWZlcnJlcjt2YXIgZXNjX2xpbmsgPSAiIjt2YXIgZSA9IHdpbmRvdyAmJiB3aW5kb3cuZW5jb2RlVVJJQ29tcG9uZW50ID9lbmNvZGVVUklDb21wb25lbnQgOmVzY2FwZTtpZiAobGluayl7ZXNjX2xpbmsgPSBlKGxpbmspO30KbmV3IEltYWdlKCkuc3JjID0gIi91cmw/c2E9VCZ1cmw9IiArIGVzY19saW5rICsgIiZvaT0iICsgZShvaSkrICImY3Q9IiArIGUoY3QpO3JldHVybiBmYWxzZTt9Cjwvc2NyaXB0PjwvaGVhZD48Ym9keT48ZGl2IGNsYXNzPSJteW1HbyI+PGRpdiBjbGFzcz0iYVhnYUdiIj48Zm9udCBzdHlsZT0iZm9udC1zaXplOmxhcmdlciI+PGI+JiMxMDU1OyYjMTA4NjsmIzEwODc7JiMxMDc3OyYjMTA4ODsmIzEwNzc7JiMxMDc2OyYjMTA3ODsmIzEwNzc7JiMxMDg1OyYjMTA4NTsmIzExMDM7ICYjMTA4NzsmIzEwODg7JiMxMDg2OyAmIzEwODc7JiMxMDc3OyYjMTA4ODsmIzEwNzc7JiMxMDcyOyYjMTA3NjsmIzEwODg7JiMxMDc3OyYjMTA4OTsmIzEwOTE7JiMxMDc0OyYjMTA3MjsmIzEwODU7JiMxMDg1OyYjMTEwMzs8L2I+PC9mb250PjwvZGl2PjwvZGl2PjxkaXYgY2xhc3M9ImZUazd2ZCI+Jm5ic3A7JiMxMDU3OyYjMTA5MDsmIzEwODY7JiMxMDg4OyYjMTExMDsmIzEwODU7JiMxMDgyOyYjMTA3MjssICYjMTA4NTsmIzEwNzI7ICYjMTEwMzsmIzEwODI7JiMxMTEwOyYjMTA4MTsgJiMxMDc0OyYjMTA4MDsgJiMxMDg3OyYjMTA3NzsmIzEwODg7JiMxMDc3OyYjMTA3MzsmIzEwOTE7JiMxMDc0OyYjMTA3MjsmIzEwODM7JiMxMDgwOywgJiMxMDg1OyYjMTA3MjsmIzEwODQ7JiMxMDcyOyYjMTA3NTsmIzEwNzI7JiMxMTA4OyYjMTA5MDsmIzExMDA7JiMxMDg5OyYjMTEwMzsgJiMxMDg5OyYjMTA4MjsmIzEwNzc7JiMxMDg4OyYjMTA5MTsmIzEwNzQ7JiMxMDcyOyYjMTA5MDsmIzEwODA7ICYjMTA3NDsmIzEwNzI7JiMxMDg5OyAmIzEwODU7JiMxMDcyOyAmIzEwNzI7JiMxMDc2OyYjMTA4ODsmIzEwNzc7JiMxMDg5OyYjMTA5MTsgPGEgaHJlZj0iaHR0cHM6Ly91eHBsYW5ldC5vcmcvdXNpbmctbG9hZGluZy1hbmltYXRpb24tb24td2Vic2l0ZXMtYW5kLWFwcHMtZXhhbXBsZXMtYW5kLXNuaXBwZXRzLXRvLXVzZS1jYWIwMDk3YmU5ZjEiPmh0dHBzOi8vdXhwbGFuZXQub3JnL3VzaW5nLWxvYWRpbmctYW5pbWF0aW9uLW9uLXdlYnNpdGVzLWFuZC1hcHBzLWV4YW1wbGVzLWFuZC1zbmlwcGV0cy10by11c2UtY2FiMDA5N2JlOWYxPC9hPi48YnI+PGJyPiZuYnNwOyYjMTA3MTsmIzEwODI7JiMxMDk3OyYjMTA4NjsgJiMxMDc0OyYjMTA4MDsgJiMxMDg1OyYjMTA3NzsgJiMxMDczOyYjMTA3MjsmIzEwNzg7JiMxMDcyOyYjMTEwODsmIzEwOTA7JiMxMDc3OyAmIzEwNzk7JiMxMDcyOyYjMTA5MzsmIzEwODY7JiMxMDc2OyYjMTA4MDsmIzEwOTA7JiMxMDgwOyAmIzEwODU7JiMxMDcyOyAmIzEwOTQ7JiMxMTAyOyAmIzEwODk7JiMxMDkwOyYjMTA4NjsmIzEwODg7JiMxMTEwOyYjMTA4NTsmIzEwODI7JiMxMDkxOywgJiMxMDc0OyYjMTA4MDsgJiMxMDg0OyYjMTA4NjsmIzEwNzg7JiMxMDc3OyYjMTA5MDsmIzEwNzc7IDxhIGhyZWY9IiMiIGRhdGEtY3Q9Im9yaWdpbmxpbmsiIGRhdGEtb2k9InVuYXV0aG9yaXplZHJlZGlyZWN0IiBvbmNsaWNrPSJyZXR1cm4gZ29fYmFjaygpOyIgb25tb3VzZWRvd249ImN0dSh0aGlzLmdldEF0dHJpYnV0ZSgnZGF0YS1vaScpLHRoaXMuZ2V0QXR0cmlidXRlKCdkYXRhLWN0JykpOyI+JiMxMDg3OyYjMTA4NjsmIzEwNzQ7JiMxMDc3OyYjMTA4ODsmIzEwODU7JiMxMDkxOyYjMTA5MDsmIzEwODA7JiMxMDg5OyYjMTEwMzsgJiMxMDg1OyYjMTA3MjsgJiMxMDg3OyYjMTA4NjsmIzEwODc7JiMxMDc3OyYjMTA4ODsmIzEwNzc7JiMxMDc2OyYjMTA4NTsmIzExMDI7PC9hPi48YnI+PGJyPjxicj48L2Rpdj48L2JvZHk+PC9odG1sPg==", size = (50, 50), visible = True)
            loading_gif.show()
            UpdateAnimation( loading_gif, time_between_frames=0) 
            #print(event, values)   
            if event == 'Exit':
                eflag = True
                break
            else:
                choice = values[0][0][0]
            break

    except Exception as e:
        print(e)
    except Error as ae:
        print(ae)
        sg.PopupAutoClose('Hostel Management', 'Error encountered while working forwarding to Login Page')
        #LoginPage()
    finally:
        if eflag:
            window.Close()
            exit()
        if choice == '1':
            alloc_dealloc()
        elif choice == '2':
            reportgen()
        elif choice == '3':
            update_details()


if __name__ == "__main__":
    start()