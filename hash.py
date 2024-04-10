import math
from tkinter import *
from tkinter import messagebox

def sha224(text):
    # Initialize variables
    h0 = 0xc1059ed8
    h1 = 0x367cd507
    h2 = 0x3070dd17
    h3 = 0xf70e5939
    h4 = 0xffc00b31
    h5 = 0x68581511
    h6 = 0x64f98fa7
    h7 = 0xbefa4fa4

    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # Rest of the code remains the same
    # Insert the k values above this line



    # Pre-processing
    original_length = len(text)
    original_bit_length = original_length * 8
    text += chr(0x80)
    while (len(text) * 8) % 512 != 448:
        text += chr(0)

    text += chr((original_bit_length >> 56) & 0xff)
    text += chr((original_bit_length >> 48) & 0xff)
    text += chr((original_bit_length >> 40) & 0xff)
    text += chr((original_bit_length >> 32) & 0xff)
    text += chr((original_bit_length >> 24) & 0xff)
    text += chr((original_bit_length >> 16) & 0xff)
    text += chr((original_bit_length >> 8) & 0xff)
    text += chr(original_bit_length & 0xff)

    # Main loop
    for i in range(0, len(text), 64):
        chunk = text[i:i + 64]
        w = [0] * 64
        for j in range(16):
            w[j] = ord(chunk[j * 4]) << 24 | ord(chunk[j * 4 + 1]) << 16 | ord(chunk[j * 4 + 2]) << 8 | ord(
                chunk[j * 4 + 3])

        for j in range(16, 64):
            s0 = (w[j - 15] >> 7 | w[j - 15] << 25) ^ (w[j - 15] >> 18 | w[j - 15] << 14) ^ (w[j - 15] >> 3)
            s1 = (w[j - 2] >> 17 | w[j - 2] << 15) ^ (w[j - 2] >> 19 | w[j - 2] << 13) ^ (w[j - 2] >> 10)
            w[j] = (w[j - 16] + s0 + w[j - 7] + s1) & 0xffffffff

        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        for j in range(64):
            s0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = s0 + maj
            s1 = (e >> 6 | e << 26) ^ (e >> 11 | e << 21) ^ (e >> 25 | e << 7)
            ch = (e & f) ^ (~e & g)
            t1 = h + s1 + ch + k[j] + w[j]

            h = g
            g = f
            f = e
            e = (d + t1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xffffffff

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
        h5 = (h5 + f) & 0xffffffff
        h6 = (h6 + g) & 0xffffffff
        h7 = (h7 + h) & 0xffffffff

    # Final hash
    hash_result = '%08x%08x%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4, h5, h6)
    return hash_result




def calculate_main():
    text = weight_tf.get()
    result = sha224(text)

    messagebox.showinfo('hello', f'Hash функция: {result}')

window = Tk()
window.title('Генератор чисел')
window.geometry('500x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

height_lb = Label(
    frame,
    text="Введите текст"
)
height_lb.grid(row=4, column=1)


weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
    frame,
    text='Сгенерировать hash функцию',
    command=calculate_main
)
cal_btn.grid(row=5, column=2)



window.mainloop()