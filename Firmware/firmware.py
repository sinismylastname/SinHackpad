import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros


keyboard = KMKKeyboard()
macros = Macros()

undo = Macros(Tap(KC.LCTL), Tap(KC.Z))
redo = Macros(Tap(KC.LCTL), Tap(KC.Y))

copy = Macros(Tap(KC.LCTL), Tap(KC.C))
paste = Macros(Tap(KC.LCTL), Tap(KC.V))

keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [undo, redo, copy, paste]
]

if __name__ == '__main__':
    keyboard.go()
