import keyboard
import pyperclip
o=[]
# k= keyboard.record('esc')
li=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
 ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', ' ']
cy=['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д',
    'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.', ' ']

def repl():
    keyboard.press('ctrl+c')
    buff=pyperclip.paste()
    for b in buff:
        if b in li:
            o.append(cy[li.index(b)])
    print(o)
    keyboard.write(''.join(o))
    o.clear()
keyboard.add_hotkey('ctrl+o',repl)
keyboard.wait('esc')
