import pyautogui

t = 2

for count in range(t * 60, 1, -1):
    if count > 60:
        m = int(round(count / 60, 2))
        s = count % 60
        print(f'{m}m:{s}s')
    else:
        print(count, 's')

    pyautogui.sleep(1)
