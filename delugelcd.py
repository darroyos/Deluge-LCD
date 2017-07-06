#!/usr/bin/python
import time
import I2C_LCD_driver


class Torrent:

    def __init__(self, title, size=0):
        self.__title = title
        self.__size = size

    def setSize(self, size):
        self.__size = size

    def getTitle(self):
        return self.__title

    def getSize(self):
        return self.__size


def parseDelugeOutput(file):
    torrents = []
    index = 0
    newTorrent = True

    for line in file:
        line = line.strip()  # remove initial whitespaces

        "Make sure it isn't the first line"
        if len(line) != 0:

            if line.startswith("Name: "):
                parsedName = line.split("Name: ")
                torrents.append(Torrent(parsedName[1]))
                newTorrent = True

            elif line.startswith("State: ") and not line.startswith("State: Downloading"):
                "Delete the last element if it isn't in a downlading state"
                if newTorrent:
                    torrents.pop()
                    newTorrent = False

            elif newTorrent and line.startswith("Size: "):
                parsedSize = line.split("Ratio: ")[0].split("Size: ")[1]
                torrents[index].setSize(parsedSize)
                index += 1

    return torrents


def printLCD(lcd, torrent):
    str_pad = " " * 16
    my_long_string = str_pad + torrent.getTitle()

    lcd.lcd_display_string(torrent.getSize(), 2)

    for i in range(0, len(my_long_string)):
        lcd_text = my_long_string[i:(i + 16)]
        lcd.lcd_display_string(lcd_text, 1)
        time.sleep(0.3)
        lcd.lcd_display_string(str_pad, 1)


def main():
    file = open("output.txt", "r")
    torrents = parseDelugeOutput(file)

    mylcd = I2C_LCD_driver.lcd()

    print "Currently downloading..."
    for torrent in torrents:
        printLCD(mylcd, torrent)
        print "Title: " + torrent.getTitle()
        print "Size: " + torrent.getSize()


if __name__ == "__main__":
    main()
