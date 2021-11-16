import numpy as np
import soundfile as sf
import cv2

width, height = 1264, 1264


def ppwave(screen, xs, ys, title="os", gain=100):
    screen *= 0

    ys = width / 2 + (ys * gain)
    xs = height / 2 + (xs * gain)

    pts = np.array(list(zip(xs, ys))).astype(np.int32)

    cv2.polylines(screen, [pts], False, (0, 225, 0))
    cv2.imshow(title, screen)


def main():
    screen = np.zeros((height, width, 3), dtype=np.uint8)
    xs = np.arange(width).astype(np.int32)
    mode = 'wave'
    rate = 44100
    T = 1
    f = 10.0
    ff = 10.0

    t = np.linspace(0, T, T * rate, endpoint=True)
    x = np.sin(2 * np.pi * f * t)
    y = np.cos(2 * np.pi * ff * t)

    print(x.shape)

    while (True):

        if(mode == 'file'):
            for block in sf.blocks('sounds/sound2.wav', blocksize=1024, overlap=128):
                ppwave(screen, block[:, 0], block[:, 1] * -1)
        else:
            dx = np.array_split(x, 10)
            dy = np.array_split(y, 10)

            for a, b in zip(dx, dy):
                ppwave(screen, a, b * -1, gain = 150)

        key = cv2.waitKey(2) & 0xFF


        f -= 0.001
        x = np.sin(2 * np.pi * f * t)

        ff += 0.001
        y = np.sin(2 * np.pi * ff * t)
        if (ord('j') == key):
            print(ff)
            ff += 4
            y = np.sin(2 * np.pi * ff * t)

        if (ord('h') == key):
            print(ff)
            ff -= 4
            y = np.sin(2 * np.pi * ff * t)

        if (ord('f') == key):
            print(f)
            f += 4
            x = np.sin(2 * np.pi * f * t)

        if (ord('d') == key):
            print(f)
            f -= 4
            x = np.sin(2 * np.pi * f * t)

        if (ord('m') == key):
            break;


if __name__ == "__main__":
    main()
