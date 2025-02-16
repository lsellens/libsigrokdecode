##
## This file is part of the libsigrokdecode project.
##
## Copyright (C) 2014 Uwe Hermann <uwe@hermann-uwe.de>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
##

# Addresses/devices. Items that are not listed are reserved/unknown.
address = {
    0x00: 'Joy-it SBC-IRC01',
    0x40: 'Matsui TV',
    0xEA41: 'Unknown LED Panel',
    0x04: 'LG TV',
}

digits = {
    0: ['0', '0'],
    1: ['1', '1'],
    2: ['2', '2'],
    3: ['3', '3'],
    4: ['4', '4'],
    5: ['5', '5'],
    6: ['6', '6'],
    7: ['7', '7'],
    8: ['8', '8'],
    9: ['9', '9'],
}

# Commands. Items that are not listed are reserved/unknown.
command = {
    0x40: dict(list(digits.items()) + list({
        11: ['-/--', '-/--'],
        16: ['Mute', 'M'],
        18: ['Standby', 'StBy'],
        26: ['Volume up', 'Vol+'],
        27: ['Program up', 'P+'],
        30: ['Volume down', 'Vol-'],
        31: ['Program down', 'P-'],
        68: ['AV', 'AV'],
    }.items())),

    # This is most likely a generic remote control. The PCB
    # has space for 16 buttons total, of which not all are
    # connected. The PCB is marked "JSY", "XSK-5462", and
    # "2014-6-12 JW". It consists of only a single IC, marked
    # "BJEC107BNE" or similar. The following buttons are
    # marked for the remote control of a LED panel this was
    # found in.
    0xEA41: {
        0x10: ['Warmer', 'T+'],
        0x11: ['Colder', 'T-'],
        0x12: ['Brighter', '+'],
        0x13: ['Darker', '-'],
        0x14: ['Off', 'O'],
        0x15: ['On', 'I'],
        0x41: ['Min Brightness', 'Min'],
        0x48: ['Max Brightness', 'Max'],
    },
    0x00: {
        0x45: ['Volume down', 'Vol-'],
        0x46: ['Play/Pause', 'P/P'],
        0x47: ['Volume up', 'Vol+'],
        0x44: ['Setup', 'Set'],
        0x40: ['Up', 'U'],
        0x43: ['Stop / Mode', 'S/M'],
        0x07: ['Left', 'L'],
        0x15: ['Enter', 'E'],
        0x09: ['Right', 'R'],
        0x16: ['0 / 10+', '0'],
        0x19: ['Down', 'D'],
        0x0D: ['Back', 'B'],
        0x0C: ['1', '1'],
        0x18: ['2', '2'],
        0x5E: ['3', '3'],
        0x08: ['4', '4'],
        0x1C: ['5', '5'],
        0x5A: ['6', '6'],
        0x42: ['7', '7'],
        0x52: ['8', '8'],
        0x4A: ['9', '9'],
    },
    0x04: {  # LG TV Remote Commands
        0x08: ['Power', 'Pwr'],
        0xF0: ['TV Radio', 'TvRad'],
        0x0B: ['Input', 'Inp'],
        0x43: ['Q.Menu', 'QMn'],
        0x79: ['Aspect Ratio', 'Ratio'],
        0x39: ['Subtitles', 'Subttl'],
        0x11: ['1', '1'],
        0x12: ['2', '2'],
        0x13: ['3', '3'],
        0x14: ['4', '4'],
        0x15: ['5', '5'],
        0x16: ['6', '6'],
        0x17: ['7', '7'],
        0x18: ['8', '8'],
        0x19: ['9', '9'],
        0xAB: ['Guide', 'Gd'],
        0x10: ['0', '0'],
        0x1A: ['Q.View', 'QVw'],
        0x02: ['Volume Up', 'Vol+'],
        0x03: ['Volume Down', 'Vol-'],
        0x1E: ['Favorites', 'Fav'],
        0xAA: ['Info', 'Info'],
        0x09: ['Mute', 'M'],
        0x00: ['Channel Up', 'Ch+'],
        0x01: ['Channel Down', 'Ch-'],
        0x9F: ['App', 'App'],
        0x7C: ['Home', 'Home'],
        0x42: ['My Apps', 'Apps'],
        0x20: ['Text', 'Txt'],
        0x21: ['T. Options', 'TOpt'],
        0x40: ['Up', 'Up'],
        0x41: ['Down', 'Down'],
        0x07: ['Left', 'Left'],
        0x06: ['Right', 'Right'],
        0x44: ['OK', 'OK'],
        0x28: ['Back', 'Back'],
        0x5B: ['Exit', 'Exit'],
        0x91: ['AD', 'AD'],
        0x53: ['List', 'List'],
        0xB1: ['Stop', 'Stop'],
        0x8F: ['Rewind', 'Rew'],
        0xB0: ['Play', 'Play'],
        0xBA: ['Pause', 'Pause'],
        0x8E: ['Fast Forward', 'Fwd'],
        0x72: ['Red', 'Red'],
        0x71: ['Green', 'Green'],
        0x63: ['Yellow', 'Yellow'],
        0x61: ['Blue', 'Blue'],
    }
}
