import simulator

# Helper to define how letters should be printed.
byte_alphabet = [
  [ 0x00, 0x00, 0x00, 0x00, 0x00 ],  # space  (0x20)
  [ 0x00, 0x00, 0x2F, 0x00, 0x00 ],  # !
  [ 0x00, 0x07, 0x05, 0x07, 0x00 ],  # " but will display °
  [ 0x14, 0x7F, 0x14, 0x7F, 0x14 ],  # #
  [ 0x24, 0x2A, 0x7F, 0x2A, 0x12 ],  # $
  [ 0x23, 0x13, 0x08, 0x64, 0x62 ],  # %
  [ 0x36, 0x49, 0x55, 0x22, 0x50 ],  # &amp;
  [ 0x00, 0x05, 0x03, 0x00, 0x00 ],  # '
  [ 0x00, 0x1C, 0x22, 0x41, 0x00 ],  # (
  [ 0x00, 0x41, 0x22, 0x1C, 0x00 ],  # (
  [ 0x14, 0x08, 0x3E, 0x08, 0x14 ],  # *
  [ 0x08, 0x08, 0x3E, 0x08, 0x08 ],  # +
  [ 0x00, 0x50, 0x30, 0x00, 0x00 ],  # ,
  [ 0x08, 0x08, 0x08, 0x08, 0x08 ],  # -
  [ 0x00, 0x30, 0x30, 0x00, 0x00 ],  # .
  [ 0x20, 0x10, 0x08, 0x04, 0x02 ],  # /
  
  [ 0x3E, 0x51, 0x49, 0x45, 0x3E ], # 0  (0x30)
  [ 0x00, 0x42, 0x7F, 0x40, 0x00 ], # 1
  [ 0x42, 0x61, 0x51, 0x49, 0x46 ], # 2
  [ 0x21, 0x41, 0x45, 0x4B, 0x31 ], # 3
  [ 0x18, 0x14, 0x12, 0x7F, 0x10 ], # 4
  [ 0x27, 0x45, 0x45, 0x45, 0x39 ], # 5
  [ 0x3C, 0x4A, 0x49, 0x49, 0x30 ], # 6
  [ 0x01, 0x71, 0x09, 0x05, 0x03 ], # 7
  [ 0x36, 0x49, 0x49, 0x49, 0x36 ], # 8
  [ 0x06, 0x49, 0x49, 0x29, 0x1E ], # 9
  [ 0x00, 0x36, 0x36, 0x00, 0x00 ], # :
  [ 0x00, 0x56, 0x36, 0x00, 0x00 ], # ;
  [ 0x08, 0x14, 0x22, 0x41, 0x00 ], # &lt;
  [ 0x14, 0x14, 0x14, 0x14, 0x14 ], # =
  [ 0x00, 0x41, 0x22, 0x14, 0x08 ], # &gt;
  [ 0x02, 0x01, 0x51, 0x09, 0x06 ], # ?
                                
  [ 0x32, 0x49, 0x79, 0x41, 0x3E ], # @  (0x40)
  [ 0x7E, 0x11, 0x11, 0x11, 0x7E ], # A
  [ 0x7F, 0x49, 0x49, 0x49, 0x36 ], # B
  [ 0x3E, 0x41, 0x41, 0x41, 0x22 ], # C
  [ 0x7F, 0x41, 0x41, 0x22, 0x1C ], # D
  [ 0x7F, 0x49, 0x49, 0x49, 0x41 ], # E
  [ 0x7F, 0x09, 0x09, 0x09, 0x01 ], # F
  [ 0x3E, 0x41, 0x49, 0x49, 0x7A ], # G
  [ 0x7F, 0x08, 0x08, 0x08, 0x7F ], # H
  [ 0x00, 0x41, 0x7F, 0x41, 0x00 ], # I
  [ 0x20, 0x40, 0x41, 0x3F, 0x01 ], # J
  [ 0x7F, 0x08, 0x14, 0x22, 0x41 ], # K
  [ 0x7F, 0x40, 0x40, 0x40, 0x40 ], # L
  [ 0x7F, 0x02, 0x0C, 0x02, 0x7F ], # M
  [ 0x7F, 0x04, 0x08, 0x10, 0x7F ], # N
  [ 0x3E, 0x41, 0x41, 0x41, 0x3E ], # O
                                 
  [ 0x7F, 0x09, 0x09, 0x09, 0x06 ], # P  (0x50) //edited - replace 0x3F with 0x7F
  [ 0x3E, 0x41, 0x51, 0x21, 0x5E ], # Q
  [ 0x7F, 0x09, 0x19, 0x29, 0x46 ], # R
  [ 0x46, 0x49, 0x49, 0x49, 0x31 ], # S
  [ 0x01, 0x01, 0x7F, 0x01, 0x01 ], # T
  [ 0x3F, 0x40, 0x40, 0x40, 0x3F ], # U
  [ 0x1F, 0x20, 0x40, 0x20, 0x1F ], # V
  [ 0x3F, 0x40, 0x30, 0x40, 0x3F ], # W
  [ 0x63, 0x14, 0x08, 0x14, 0x63 ], # X
  [ 0x07, 0x08, 0x70, 0x08, 0x07 ], # Y
  [ 0x61, 0x51, 0x49, 0x45, 0x43 ], # Z
  [ 0x00, 0x7F, 0x41, 0x41, 0x00 ], # [
  [ 0x02, 0x04, 0x08, 0x10, 0x20 ], # backslash
  [ 0x00, 0x41, 0x41, 0x7F, 0x00 ], # ]
  [ 0x04, 0x02, 0x01, 0x02, 0x04 ], # ^
  [ 0x40, 0x40, 0x40, 0x40, 0x40 ], # _
                                 
  [ 0x00, 0x01, 0x02, 0x04, 0x00 ], # `  (0x60)
  [ 0x20, 0x54, 0x54, 0x54, 0x78 ], # a
  [ 0x7F, 0x50, 0x48, 0x48, 0x30 ], # b
  [ 0x38, 0x44, 0x44, 0x44, 0x20 ], # c
  [ 0x38, 0x44, 0x44, 0x48, 0x7F ], # d
  [ 0x38, 0x54, 0x54, 0x54, 0x18 ], # e
  [ 0x08, 0x7E, 0x09, 0x01, 0x02 ], # f
  [ 0x0C, 0x52, 0x52, 0x52, 0x3E ], # g
  [ 0x7F, 0x08, 0x04, 0x04, 0x78 ], # h
  [ 0x00, 0x44, 0x7D, 0x40, 0x00 ], # i
  [ 0x20, 0x40, 0x44, 0x3D, 0x00 ], # j
  [ 0x7F, 0x10, 0x28, 0x44, 0x00 ], # k
  [ 0x00, 0x41, 0x7F, 0x40, 0x00 ], # l
  [ 0x7C, 0x04, 0x18, 0x04, 0x78 ], # m
  [ 0x7C, 0x08, 0x04, 0x04, 0x78 ], # n
  [ 0x38, 0x44, 0x44, 0x44, 0x38 ], # o
                                 
  [ 0x7C, 0x14, 0x14, 0x14, 0x08 ], # p  (0x70)
  [ 0x08, 0x14, 0x14, 0x08, 0x7C ], # q
  [ 0x7C, 0x08, 0x04, 0x04, 0x08 ], # r
  [ 0x48, 0x54, 0x54, 0x54, 0x20 ], # s
  [ 0x04, 0x3F, 0x44, 0x40, 0x20 ], # t
  [ 0x3C, 0x40, 0x40, 0x20, 0x7C ], # u
  [ 0x1C, 0x20, 0x40, 0x20, 0x1C ], # v
  [ 0x3C, 0x40, 0x30, 0x40, 0x3C ], # w
  [ 0x44, 0x28, 0x10, 0x28, 0x44 ], # x
  [ 0x0C, 0x50, 0x50, 0x50, 0x3C ], # y
  [ 0x44, 0x64, 0x54, 0x4C, 0x44 ], # z
  [ 0x00, 0x08, 0x36, 0x41, 0x00 ], # {
  [ 0x00, 0x00, 0x7F, 0x00, 0x00 ], # |
  [ 0x00, 0x41, 0x36, 0x08, 0x00 ], # }
  [ 0x30, 0x08, 0x10, 0x20, 0x18 ], # ~
  [ 0x7F, 0x55, 0x49, 0x55, 0x7F ]  # unknown char (0x7F)  
]

# Helper to shift all LEDs to the left.
def allStripsMoveLeft(leds):
    ledsPerStrip = len(leds) // 8
    for i in range(8):
        for j in range(ledsPerStrip - 1):
            leds[i * ledsPerStrip + j] = leds[i * ledsPerStrip + j + 1]

# Helper to scroll a given text using given colors.
def scrollText(leds, text, textColor, backColor, delay):
    isOn = False
    for i in range(len(text)):
        alphabetIndex = max(0, ord(text[i]) - ord(' '))
        for j in range(6): # columns
            for k in range(8): # rows
                isOn = byte_alphabet[alphabetIndex][j] & (1 << (7 - k)) if j < 5 else False
                leds[(len(leds) // 8) * (8 - k) - 1] = textColor if isOn else backColor
            simulator.show(leds)
            simulator.delay(delay)
            allStripsMoveLeft(leds)

def scrollingTextProgram(leds):
    BLUE  = [0, 0, 255]
    RED   = [255, 0, 0]
    YELLOW = [255, 255, 0]
    PAUSE = 40 # milliseconds
    scrollText(leds, " EASY LED PANEL ", RED, BLUE, PAUSE)
    scrollText(leds, " EASY LED PANEL ", YELLOW, RED, PAUSE)
    scrollText(leds, " EASY LED PANEL ", BLUE, YELLOW, PAUSE)

if __name__ == "__main__":
    # Call your program here
    simulator.loop(scrollingTextProgram)