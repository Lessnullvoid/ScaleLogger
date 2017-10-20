#/Estrutura:
# - Un archivo por codigo
# - 39 posiciones en formato de row
# - 39 archivos en formato indivdual >> depende del modelo que se seleccione
# - datos datetime + serial en la ultima posicion de la lista save
# selecionar nombre de lista con raw_input
# if seleciona el archivo para abrir y el archivo de escritura
# escribir valor desde el puerto serial en la celda siguiente
# raw_input selecionar otro usuario, ingresar otro dato, guardar


import datetime
import csv
import os
import sys, termios, tty
import serial as ser
import string
from time import sleep
import pandas as pd
import pygame.locals import *

disp_w = 1000
disp_h = 600
pygame.init()
screen = pygame.display.set_mode((disp_w, disp_h))
pygame.display.set_caption('[Scale:Logger]')

# in the case of using just one file to add data per row
with open('autumn.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

input = raw_input ('Enter your number:')

while True:

    if (input == "1"):
        print 'position row1'
        dinamic_name = '45E.csv'
        break

with open('45E.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
        #add date and weight to the selected row + cell

    if (input  == "2"):
        print 'position row2'
        #add date and weight to the selected row + cell

    if (input  == "3"):
        print 'position row3'
        #add date and weight to the selected row + cell

    if (input  == "4"):
        print 'position row4'
        #add date and weight to the selected row + cell


def saveLine(tobj, line, loc, name):
    fname = loc + tobj.strftime(name)
    with (open(fname, 'a+')) as f:
        f.write(line)

class serialDevice:
    def __init__(self, device, baud=9600, delim='\r\n', loc='~/', name='autumn.csv'):
        self.allowed = set(string.printable)
        self.buf     = str()
        self.delim   = delim
        self.loc     = loc
        self.name    = name
        self.s       = ser.Serial(device, baud)

    def read(self):
        while self.delim not in self.buf:
            sleep(0.05)
            self.buf = self.buf + self.s.read(self.s.inWaiting())
        tcol  = datetime.datetime.now()
        parts = self.buf.partition(self.delim)
        line  = parts[0].replace('\r', '').replace('\n', '')
        line  = filter(lambda x: x in self.allowed, line)
        self.buf = parts[2]
        save = ','.join([str(tcol), line]) + '\n'
        saveLine(tcol, save, self.loc, self.name)
        print(save)
        input = raw_input ('Enter your number:')

    def end(self):
        print('\n\nStopping data collection...\n\n')
        self.s.flush()
        self.s.close()



if __name__ == '__main__':
    device = '/dev/tty.usbserial-DN02G2ES'
    baud   = 9600
    delim  = '\r\n'
    loc    = './'
    name   = dinamic_name
    dev = serialDevice(device, baud, delim, loc, name)
    while True:
        try:
            dev.read()
        except (KeyboardInterrupt, SystemExit):
            raise


dev.end()
