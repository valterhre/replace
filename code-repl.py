
import keyboard
o=[]
# k= keyboard.record('esc')
li=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
 ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', ' ']
cy=['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д',
    'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.', ' ']
cyr=[]
def la():
    while True:
        events = keyboard.record('shift')
        o.append(list(keyboard.get_typed_strings(events))[0])

        print(cyr)

        for r in o[0]:
            if r in li:
                print('en')
                cyr.append(cy[li.index(r)])
            if r in cy:
                print('rut')
                cyr.append(li[cy.index(r)])
        def presed():
            print(cyr)
            for i in range(len(o[0])):
                keyboard.press_and_release('backspace')
            keyboard.write(''.join(cyr))
            o.clear()
            cyr.clear()
        if keyboard.read_key()=='shift':
            if bool(o[0]):
                presed()
                print(o)
                if '' in o:
                    o.remove('')
            else:
                if '' in o:
                    o.remove('')
        if not o:
            break
def de():
    while True:
        keyboard.wait('shift')
        la()

de()

