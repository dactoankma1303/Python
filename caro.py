# -*- encoding: utf-8 -*-
import os
import time
import random
    
def menu():
        time.sleep(4)
        print u'\n\t\t\t\t\t\t\t     CHÀO MỪNG BẠN ĐẾN VỚI TRÒ CHƠI CARO < / PHIÊN BẢN 1.0 >'
        time.sleep(3)
        print u'\n\t\t\t\t\t\t\t     Luật Chơi : '
        time.sleep(3)
        print u'\n\t\t\t\t\t\t\t     Người Chiến Thắng Là Người Tạo Được Đường Thẳng Theo Chiều'
        print u'\n\t\t\t\t\t\t\t     Dọc / Ngang / Chéo với chính xác 5 quân cờ của mình .'
        time.sleep(3)
        print u'\n\t\t\t\t\t\t\t     1.Player - Computer'
        time.sleep(3)
        print u'\n\t\t\t\t\t\t\t     2.Player - Player'

def player_computer():

    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def print_board():
        print u'\n\t\t\t\t\t\t\t\t\t\t       VỊ TRÍ CÁC QUÂN CỜ : '
        time.sleep(1)
        print ('x'*61)
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t        1 |  2 |  3 |  4 | 5 | 6  |  7 |  8 |  9 | 10 | 11  | 12 | 13 | 14 | 15 '  %(board[1],  board[2],  board[3],  board[4],  board[5],  board[6],  board[7],  board[8],  board[9], board[10],  board[11],  board[12],  board[13],  board[14],  board[15]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 '  %(board[16],  board[17],  board[18],  board[19],  board[20],  board[21],  board[22],  board[23],  board[24], board[25],  board[26],  board[27],  board[28],  board[29],  board[30]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 '  %(board[31],  board[32],  board[33],  board[34],  board[35],  board[36],  board[37],  board[38],  board[39], board[40],  board[41],  board[42],  board[43],  board[44],  board[45]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 '  %(board[46],  board[47],  board[48],  board[49],  board[50],  board[51],  board[52],  board[53],  board[54], board[55],  board[56],  board[57],  board[58],  board[59],  board[60]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 | 72 | 73 | 74 | 75  ' %(board[61],  board[62],  board[63],  board[64],  board[65],  board[66],  board[67],  board[68],  board[69], board[70],  board[71],  board[72],  board[73],  board[74],  board[75]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90  ' %(board[76],  board[77],  board[78],  board[79],  board[80],  board[81],  board[82],  board[83],  board[84], board[85],  board[86],  board[87],  board[88],  board[89],  board[90]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100| 101| 102| 103| 104| 105 ' %(board[91],  board[92],  board[93],  board[94],  board[95],  board[96],  board[97],  board[98],  board[99], board[100],  board[101],  board[102],  board[103],  board[104],  board[105]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       106| 107| 108| 109| 110| 111| 112| 113| 114| 115| 116| 117| 118| 119| 120 ' %(board[106],  board[107],  board[108],  board[109],  board[110],  board[111],  board[112],  board[113],  board[114], board[115],  board[116],  board[117],  board[118],  board[119],  board[120]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       121| 122| 123| 124| 125| 126| 127| 128| 129| 130| 131| 132| 133| 134| 135 ' %(board[121],  board[122],  board[123],  board[124],  board[125],  board[126],  board[127],  board[128],  board[129], board[130],  board[131],  board[132],  board[133],  board[134],  board[135]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       136| 137| 138| 139| 140| 141| 142| 143| 144| 145| 146| 147| 148| 149| 150 ' %(board[136],  board[137],  board[138],  board[139],  board[140],  board[141],  board[142],  board[143],  board[144], board[145],  board[146],  board[147],  board[148],  board[149],  board[150]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       151| 152| 153| 154| 155| 156| 157| 158| 159| 160| 161| 162| 163| 164| 165 ' %(board[151],  board[152],  board[153],  board[154],  board[155],  board[156],  board[157],  board[158],  board[159], board[160],  board[161],  board[162],  board[163],  board[164],  board[165]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       166| 167| 168| 169| 170| 171| 172| 173| 174| 175| 176| 177| 178| 179| 180 ' %(board[166],  board[167],  board[168],  board[169],  board[170],  board[171],  board[172],  board[173],  board[174], board[175],  board[176],  board[177],  board[178],  board[179],  board[180]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       181| 182| 183| 184| 185| 186| 187| 188| 189| 190| 191| 192| 193| 194| 195 ' %(board[181],  board[182],  board[183],  board[184],  board[185],  board[186],  board[187],  board[188],  board[189], board[190],  board[191],  board[192],  board[193],  board[194],  board[195]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       196| 197| 198| 199| 200| 201| 202| 203| 204| 205| 206| 207| 208| 209| 210 ' %(board[196],  board[197],  board[198],  board[199],  board[200],  board[201],  board[202],  board[203],  board[204], board[205],  board[206],  board[207],  board[208],  board[209],  board[210]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       211| 212| 213| 214| 215| 216| 217| 218| 219| 220| 221| 222| 223| 224| 225 ' %(board[211],  board[212],  board[213],  board[214],  board[215],  board[216],  board[217],  board[218],  board[219], board[220],  board[221],  board[222],  board[223],  board[224],  board[225]))
        print ('x'*61)
    def is_winner(board, player):
        if (board[1]== player and board[2] == player and board[3] == player and board[4] == player and board[5] == player)or \
            (board[2]== player and board[3] == player and board[4] == player and board[5] == player and board[6] == player) or \
            (board[3]== player and board[4] == player and board[5] == player and board[6] == player and board[7] == player) or \
            (board[4]== player and board[5] == player and board[6] == player and board[7] == player and board[8] == player) or \
            (board[5]== player and board[6] == player and board[7] == player and board[8] == player and board[9] == player) or \
            (board[6]== player and board[7] == player and board[8] == player and board[9] == player and board[10] == player) or \
            (board[7]== player and board[8] == player and board[9] == player and board[10] == player and board[11] == player) or \
            (board[8]== player and board[9] == player and board[10] == player and board[11] == player and board[12] == player) or \
            (board[9]== player and board[10] == player and board[11] == player and board[12] == player and board[13] == player) or \
            (board[10]== player and board[11] == player and board[12] == player and board[13] == player and board[14] == player) or \
            (board[11]== player and board[12] == player and board[13] == player and board[14] == player and board[15] == player) or \
            (board[16]== player and board[17] == player and board[18] == player and board[19] == player and board[20] == player) or \
            (board[17]== player and board[18] == player and board[19] == player and board[20] == player and board[21] == player) or \
            (board[18]== player and board[19] == player and board[20] == player and board[21] == player and board[22] == player) or \
            (board[19]== player and board[20] == player and board[21] == player and board[22] == player and board[23] == player) or \
            (board[20]== player and board[21] == player and board[22] == player and board[23] == player and board[24] == player) or \
            (board[21]== player and board[22] == player and board[23] == player and board[24] == player and board[25] == player) or \
            (board[22]== player and board[23] == player and board[24] == player and board[25] == player and board[26] == player) or \
            (board[23]== player and board[24] == player and board[25] == player and board[26] == player and board[27] == player) or \
            (board[24]== player and board[25] == player and board[26] == player and board[27] == player and board[28] == player) or \
            (board[25]== player and board[26] == player and board[27] == player and board[28] == player and board[29] == player) or \
            (board[26]== player and board[27] == player and board[28] == player and board[29] == player and board[30] == player) or \
            (board[31]== player and board[32] == player and board[33] == player and board[34] == player and board[35] == player) or \
            (board[32]== player and board[33] == player and board[34] == player and board[35] == player and board[36] == player) or \
            (board[33]== player and board[34] == player and board[35] == player and board[36] == player and board[37] == player) or \
            (board[34]== player and board[35] == player and board[36] == player and board[37] == player and board[38] == player) or \
            (board[35]== player and board[36] == player and board[37] == player and board[38] == player and board[39] == player) or \
            (board[36]== player and board[37] == player and board[38] == player and board[39] == player and board[40] == player) or \
            (board[37]== player and board[38] == player and board[39] == player and board[40] == player and board[41] == player) or \
            (board[38]== player and board[39] == player and board[40] == player and board[41] == player and board[42] == player) or \
            (board[39]== player and board[40] == player and board[41] == player and board[42] == player and board[43] == player) or \
            (board[40]== player and board[41] == player and board[42] == player and board[43] == player and board[44] == player) or \
            (board[41]== player and board[42] == player and board[43] == player and board[44] == player and board[45] == player) or \
            (board[46]== player and board[47] == player and board[48] == player and board[49] == player and board[50] == player) or \
            (board[47]== player and board[48] == player and board[49] == player and board[50] == player and board[51] == player) or \
            (board[48]== player and board[49] == player and board[50] == player and board[51] == player and board[52] == player) or \
            (board[49]== player and board[50] == player and board[51] == player and board[52] == player and board[53] == player) or \
            (board[50]== player and board[51] == player and board[52] == player and board[53] == player and board[54] == player) or \
            (board[51]== player and board[52] == player and board[53] == player and board[54] == player and board[55] == player) or \
            (board[52]== player and board[53] == player and board[54] == player and board[55] == player and board[56] == player) or \
            (board[53]== player and board[54] == player and board[55] == player and board[56] == player and board[57] == player) or \
            (board[54]== player and board[55] == player and board[56] == player and board[57] == player and board[58] == player) or \
            (board[55]== player and board[56] == player and board[57] == player and board[58] == player and board[59] == player) or \
            (board[56]== player and board[57] == player and board[58] == player and board[59] == player and board[60] == player) or \
            (board[61]== player and board[62] == player and board[63] == player and board[64] == player and board[65] == player) or \
            (board[62]== player and board[63] == player and board[64] == player and board[65] == player and board[66] == player) or \
            (board[63]== player and board[64] == player and board[65] == player and board[66] == player and board[67] == player) or \
            (board[64]== player and board[65] == player and board[66] == player and board[67] == player and board[68] == player) or \
            (board[65]== player and board[66] == player and board[67] == player and board[68] == player and board[69] == player) or \
            (board[66]== player and board[67] == player and board[68] == player and board[69] == player and board[70] == player) or \
            (board[67]== player and board[68] == player and board[69] == player and board[70] == player and board[71] == player) or \
            (board[68]== player and board[69] == player and board[70] == player and board[71] == player and board[72] == player) or \
            (board[69]== player and board[70] == player and board[71] == player and board[72] == player and board[73] == player) or \
            (board[70]== player and board[71] == player and board[72] == player and board[73] == player and board[74] == player) or \
            (board[71]== player and board[72] == player and board[73] == player and board[74] == player and board[75] == player) or \
            (board[76]== player and board[77] == player and board[78] == player and board[79] == player and board[80] == player) or \
            (board[77]== player and board[78] == player and board[79] == player and board[80] == player and board[81] == player) or \
            (board[78]== player and board[79] == player and board[80] == player and board[81] == player and board[82] == player) or \
            (board[79]== player and board[80] == player and board[81] == player and board[82] == player and board[83] == player) or \
            (board[80]== player and board[81] == player and board[82] == player and board[83] == player and board[84] == player) or \
            (board[81]== player and board[82] == player and board[83] == player and board[84] == player and board[85] == player) or \
            (board[82]== player and board[83] == player and board[84] == player and board[85] == player and board[86] == player) or \
            (board[83]== player and board[84] == player and board[85] == player and board[86] == player and board[87] == player) or \
            (board[84]== player and board[85] == player and board[86] == player and board[87] == player and board[88] == player) or \
            (board[85]== player and board[86] == player and board[87] == player and board[88] == player and board[89] == player) or \
            (board[86]== player and board[87] == player and board[88] == player and board[89] == player and board[90] == player) or \
            (board[91]== player and board[92] == player and board[93] == player and board[94] == player and board[95] == player) or \
            (board[92]== player and board[93] == player and board[94] == player and board[95] == player and board[96] == player) or \
            (board[93]== player and board[94] == player and board[95] == player and board[96] == player and board[97] == player) or \
            (board[94]== player and board[95] == player and board[96] == player and board[97] == player and board[98] == player) or \
            (board[95]== player and board[96] == player and board[97] == player and board[98] == player and board[99] == player) or \
            (board[96]== player and board[97] == player and board[98] == player and board[99] == player and board[100] == player) or \
            (board[97]== player and board[98] == player and board[99] == player and board[100] == player and board[101] == player) or \
            (board[98]== player and board[99] == player and board[100] == player and board[101] == player and board[102] == player) or \
            (board[99]== player and board[100] == player and board[101] == player and board[102] == player and board[103] == player) or \
            (board[100]== player and board[101] == player and board[102] == player and board[103] == player and board[104] == player) or \
            (board[101]== player and board[102] == player and board[103] == player and board[104] == player and board[105] == player) or \
            (board[106]== player and board[107] == player and board[108] == player and board[109] == player and board[110] == player) or \
            (board[107]== player and board[108] == player and board[109] == player and board[110] == player and board[111] == player) or \
            (board[108]== player and board[109] == player and board[110] == player and board[111] == player and board[112] == player) or \
            (board[109]== player and board[110] == player and board[111] == player and board[112] == player and board[113] == player) or \
            (board[110]== player and board[111] == player and board[112] == player and board[113] == player and board[114] == player) or \
            (board[111]== player and board[112] == player and board[113] == player and board[114] == player and board[115] == player) or \
            (board[112]== player and board[113] == player and board[114] == player and board[115] == player and board[116] == player) or \
            (board[113]== player and board[114] == player and board[115] == player and board[116] == player and board[117] == player) or \
            (board[114]== player and board[115] == player and board[116] == player and board[117] == player and board[118] == player) or \
            (board[115]== player and board[116] == player and board[117] == player and board[118] == player and board[119] == player) or \
            (board[116]== player and board[117] == player and board[118] == player and board[119] == player and board[120] == player) or \
            (board[121]== player and board[122] == player and board[123] == player and board[124] == player and board[125] == player) or \
            (board[122]== player and board[123] == player and board[124] == player and board[125] == player and board[126] == player) or \
            (board[123]== player and board[124] == player and board[125] == player and board[126] == player and board[127] == player) or \
            (board[124]== player and board[125] == player and board[126] == player and board[127] == player and board[128] == player) or \
            (board[125]== player and board[126] == player and board[127] == player and board[128] == player and board[129] == player) or \
            (board[126]== player and board[127] == player and board[128] == player and board[129] == player and board[130] == player) or \
            (board[127]== player and board[128] == player and board[129] == player and board[130] == player and board[131] == player) or \
            (board[128]== player and board[129] == player and board[130] == player and board[131] == player and board[132] == player) or \
            (board[129]== player and board[130] == player and board[131] == player and board[132] == player and board[133] == player) or \
            (board[130]== player and board[131] == player and board[132] == player and board[133] == player and board[134] == player) or \
            (board[131]== player and board[132] == player and board[133] == player and board[134] == player and board[135] == player) or \
            (board[136]== player and board[137] == player and board[138] == player and board[139] == player and board[140] == player) or \
            (board[137]== player and board[138] == player and board[139] == player and board[140] == player and board[141] == player) or \
            (board[138]== player and board[139] == player and board[140] == player and board[141] == player and board[142] == player) or \
            (board[139]== player and board[140] == player and board[141] == player and board[142] == player and board[143] == player) or \
            (board[140]== player and board[141] == player and board[142] == player and board[143] == player and board[144] == player) or \
            (board[141]== player and board[142] == player and board[143] == player and board[144] == player and board[145] == player) or \
            (board[142]== player and board[143] == player and board[144] == player and board[145] == player and board[146] == player) or \
            (board[143]== player and board[144] == player and board[145] == player and board[146] == player and board[147] == player) or \
            (board[144]== player and board[145] == player and board[146] == player and board[147] == player and board[148] == player) or \
            (board[145]== player and board[146] == player and board[147] == player and board[148] == player and board[149] == player) or \
            (board[146]== player and board[147] == player and board[148] == player and board[149] == player and board[150] == player) or \
            (board[151]== player and board[152] == player and board[153] == player and board[154] == player and board[155] == player) or \
            (board[152]== player and board[153] == player and board[154] == player and board[155] == player and board[156] == player) or \
            (board[153]== player and board[154] == player and board[155] == player and board[156] == player and board[157] == player) or \
            (board[154]== player and board[155] == player and board[156] == player and board[157] == player and board[158] == player) or \
            (board[155]== player and board[156] == player and board[157] == player and board[158] == player and board[159] == player) or \
            (board[156]== player and board[157] == player and board[158] == player and board[159] == player and board[160] == player) or \
            (board[157]== player and board[158] == player and board[159] == player and board[160] == player and board[161] == player) or \
            (board[158]== player and board[159] == player and board[160] == player and board[161] == player and board[162] == player) or \
            (board[159]== player and board[160] == player and board[161] == player and board[162] == player and board[163] == player) or \
            (board[160]== player and board[161] == player and board[162] == player and board[163] == player and board[164] == player) or \
            (board[161]== player and board[162] == player and board[163] == player and board[164] == player and board[165] == player) or \
            (board[166]== player and board[167] == player and board[168] == player and board[169] == player and board[170] == player) or \
            (board[167]== player and board[168] == player and board[169] == player and board[170] == player and board[171] == player) or \
            (board[168]== player and board[169] == player and board[170] == player and board[171] == player and board[172] == player) or \
            (board[169]== player and board[170] == player and board[171] == player and board[172] == player and board[173] == player) or \
            (board[170]== player and board[171] == player and board[172] == player and board[173] == player and board[174] == player) or \
            (board[171]== player and board[172] == player and board[173] == player and board[174] == player and board[175] == player) or \
            (board[172]== player and board[173] == player and board[174] == player and board[175] == player and board[176] == player) or \
            (board[173]== player and board[174] == player and board[175] == player and board[176] == player and board[177] == player) or \
            (board[174]== player and board[175] == player and board[176] == player and board[177] == player and board[178] == player) or \
            (board[175]== player and board[176] == player and board[177] == player and board[178] == player and board[179] == player) or \
            (board[176]== player and board[177] == player and board[178] == player and board[179] == player and board[180] == player) or \
            (board[181]== player and board[182] == player and board[183] == player and board[184] == player and board[185] == player) or \
            (board[182]== player and board[183] == player and board[184] == player and board[185] == player and board[186] == player) or \
            (board[183]== player and board[184] == player and board[185] == player and board[186] == player and board[187] == player) or \
            (board[184]== player and board[185] == player and board[186] == player and board[187] == player and board[188] == player) or \
            (board[185]== player and board[186] == player and board[187] == player and board[188] == player and board[189] == player) or \
            (board[186]== player and board[187] == player and board[188] == player and board[189] == player and board[190] == player) or \
            (board[187]== player and board[188] == player and board[189] == player and board[190] == player and board[191] == player) or \
            (board[188]== player and board[189] == player and board[190] == player and board[191] == player and board[192] == player) or \
            (board[189]== player and board[190] == player and board[191] == player and board[192] == player and board[193] == player) or \
            (board[190]== player and board[191] == player and board[192] == player and board[193] == player and board[194] == player) or \
            (board[191]== player and board[192] == player and board[193] == player and board[194] == player and board[195] == player) or \
            (board[196]== player and board[197] == player and board[198] == player and board[199] == player and board[200] == player) or \
            (board[197]== player and board[198] == player and board[199] == player and board[200] == player and board[201] == player) or \
            (board[198]== player and board[199] == player and board[200] == player and board[201] == player and board[202] == player) or \
            (board[199]== player and board[200] == player and board[201] == player and board[202] == player and board[203] == player) or \
            (board[200]== player and board[201] == player and board[202] == player and board[203] == player and board[204] == player) or \
            (board[201]== player and board[202] == player and board[203] == player and board[204] == player and board[205] == player) or \
            (board[202]== player and board[203] == player and board[204] == player and board[205] == player and board[206] == player) or \
            (board[203]== player and board[204] == player and board[205] == player and board[206] == player and board[207] == player) or \
            (board[204]== player and board[205] == player and board[206] == player and board[207] == player and board[208] == player) or \
            (board[205]== player and board[206] == player and board[207] == player and board[208] == player and board[209] == player) or \
            (board[206]== player and board[207] == player and board[208] == player and board[209] == player and board[210] == player) or \
            (board[211]== player and board[212] == player and board[213] == player and board[214] == player and board[215] == player) or \
            (board[212]== player and board[213] == player and board[214] == player and board[215] == player and board[216] == player) or \
            (board[213]== player and board[214] == player and board[215] == player and board[216] == player and board[217] == player) or \
            (board[214]== player and board[215] == player and board[216] == player and board[217] == player and board[218] == player) or \
            (board[215]== player and board[216] == player and board[217] == player and board[218] == player and board[219] == player) or \
            (board[216]== player and board[217] == player and board[218] == player and board[219] == player and board[220] == player) or \
            (board[217]== player and board[218] == player and board[219] == player and board[220] == player and board[221] == player) or \
            (board[218]== player and board[219] == player and board[220] == player and board[221] == player and board[222] == player) or \
            (board[219]== player and board[220] == player and board[221] == player and board[222] == player and board[223] == player) or \
            (board[220]== player and board[221] == player and board[222] == player and board[223] == player and board[224] == player) or \
            (board[221]== player and board[222] == player and board[223] == player and board[224] == player and board[225] == player) or \
            (board[1]== player and board[16] == player and board[31] == player and board[46] == player and board[61] == player) or \
            (board[16]== player and board[31] == player and board[46] == player and board[61] == player and board[76] == player) or \
            (board[31]== player and board[46] == player and board[61] == player and board[76] == player and board[91] == player) or \
            (board[46]== player and board[61] == player and board[76] == player and board[91] == player and board[106] == player) or \
            (board[61]== player and board[76] == player and board[91] == player and board[106] == player and board[121] == player) or \
            (board[76]== player and board[91] == player and board[106] == player and board[121] == player and board[136] == player) or \
            (board[91]== player and board[106] == player and board[121] == player and board[136] == player and board[151] == player) or \
            (board[106]== player and board[121] == player and board[136] == player and board[151] == player and board[166] == player) or \
            (board[121]== player and board[136] == player and board[151] == player and board[166] == player and board[181] == player) or \
            (board[136]== player and board[151] == player and board[166] == player and board[181] == player and board[196] == player) or \
            (board[151]== player and board[166] == player and board[181] == player and board[196] == player and board[211] == player) or \
            (board[2]== player and board[17] == player and board[32] == player and board[47] == player and board[62] == player) or \
            (board[17]== player and board[32] == player and board[47] == player and board[62] == player and board[77] == player) or \
            (board[32]== player and board[47] == player and board[62] == player and board[77] == player and board[92] == player) or \
            (board[47]== player and board[62] == player and board[77] == player and board[92] == player and board[107] == player) or \
            (board[62]== player and board[77] == player and board[92] == player and board[107] == player and board[122] == player) or \
            (board[77]== player and board[92] == player and board[107] == player and board[122] == player and board[137] == player) or \
            (board[92]== player and board[107] == player and board[122] == player and board[137] == player and board[152] == player) or \
            (board[107]== player and board[122] == player and board[137] == player and board[152] == player and board[167] == player) or \
            (board[122]== player and board[137] == player and board[152] == player and board[167] == player and board[182] == player) or \
            (board[137]== player and board[152] == player and board[167] == player and board[182] == player and board[197] == player) or \
            (board[152]== player and board[167] == player and board[182] == player and board[197] == player and board[212] == player) or \
            (board[3]== player and board[18] == player and board[33] == player and board[48] == player and board[63] == player) or \
            (board[18]== player and board[33] == player and board[48] == player and board[63] == player and board[78] == player) or \
            (board[33]== player and board[48] == player and board[63] == player and board[78] == player and board[93] == player) or \
            (board[48]== player and board[63] == player and board[78] == player and board[93] == player and board[108] == player) or \
            (board[63]== player and board[78] == player and board[93] == player and board[108] == player and board[123] == player) or \
            (board[78]== player and board[93] == player and board[108] == player and board[123] == player and board[138] == player) or \
            (board[93]== player and board[108] == player and board[123] == player and board[138] == player and board[153] == player) or \
            (board[108]== player and board[123] == player and board[138] == player and board[153] == player and board[168] == player) or \
            (board[123]== player and board[138] == player and board[153] == player and board[168] == player and board[183] == player) or \
            (board[138]== player and board[153] == player and board[168] == player and board[183] == player and board[198] == player) or \
            (board[153]== player and board[168] == player and board[183] == player and board[198] == player and board[213] == player) or \
            (board[4]== player and board[19] == player and board[34] == player and board[49] == player and board[64] == player) or \
            (board[19]== player and board[34] == player and board[49] == player and board[64] == player and board[79] == player) or \
            (board[34]== player and board[49] == player and board[64] == player and board[79] == player and board[94] == player) or \
            (board[49]== player and board[64] == player and board[79] == player and board[94] == player and board[109] == player) or \
            (board[64]== player and board[79] == player and board[94] == player and board[109] == player and board[124] == player) or \
            (board[79]== player and board[94] == player and board[109] == player and board[124] == player and board[139] == player) or \
            (board[94]== player and board[109] == player and board[124] == player and board[139] == player and board[154] == player) or \
            (board[109]== player and board[124] == player and board[139] == player and board[154] == player and board[169] == player) or \
            (board[124]== player and board[139] == player and board[154] == player and board[169] == player and board[184] == player) or \
            (board[139]== player and board[154] == player and board[169] == player and board[184] == player and board[199] == player) or \
            (board[154]== player and board[169] == player and board[184] == player and board[199] == player and board[214] == player) or \
            (board[5]== player and board[20] == player and board[35] == player and board[50] == player and board[65] == player) or \
            (board[20]== player and board[35] == player and board[50] == player and board[65] == player and board[80] == player) or \
            (board[35]== player and board[50] == player and board[65] == player and board[80] == player and board[95] == player) or \
            (board[50]== player and board[65] == player and board[80] == player and board[95] == player and board[110] == player) or \
            (board[65]== player and board[80] == player and board[95] == player and board[110] == player and board[125] == player) or \
            (board[80]== player and board[95] == player and board[110] == player and board[125] == player and board[140] == player) or \
            (board[95]== player and board[110] == player and board[125] == player and board[140] == player and board[155] == player) or \
            (board[110]== player and board[125] == player and board[140] == player and board[155] == player and board[170] == player) or \
            (board[125]== player and board[140] == player and board[155] == player and board[170] == player and board[185] == player) or \
            (board[140]== player and board[155] == player and board[170] == player and board[185] == player and board[200] == player) or \
            (board[155]== player and board[170] == player and board[185] == player and board[200] == player and board[215] == player) or \
            (board[6]== player and board[21] == player and board[36] == player and board[51] == player and board[66] == player) or \
            (board[21]== player and board[36] == player and board[51] == player and board[66] == player and board[81] == player) or \
            (board[36]== player and board[51] == player and board[66] == player and board[81] == player and board[96] == player) or \
            (board[51]== player and board[66] == player and board[81] == player and board[96] == player and board[111] == player) or \
            (board[66]== player and board[81] == player and board[96] == player and board[111] == player and board[126] == player) or \
            (board[81]== player and board[96] == player and board[111] == player and board[126] == player and board[141] == player) or \
            (board[96]== player and board[111] == player and board[126] == player and board[141] == player and board[156] == player) or \
            (board[111]== player and board[126] == player and board[141] == player and board[156] == player and board[171] == player) or \
            (board[126]== player and board[141] == player and board[156] == player and board[171] == player and board[186] == player) or \
            (board[141]== player and board[156] == player and board[171] == player and board[186] == player and board[201] == player) or \
            (board[156]== player and board[171] == player and board[186] == player and board[201] == player and board[216] == player) or \
            (board[7]== player and board[22] == player and board[37] == player and board[52] == player and board[67] == player) or \
            (board[22]== player and board[37] == player and board[52] == player and board[67] == player and board[82] == player) or \
            (board[37]== player and board[52] == player and board[67] == player and board[82] == player and board[97] == player) or \
            (board[52]== player and board[67] == player and board[82] == player and board[97] == player and board[112] == player) or \
            (board[67]== player and board[82] == player and board[97] == player and board[112] == player and board[127] == player) or \
            (board[82]== player and board[97] == player and board[112] == player and board[127] == player and board[142] == player) or \
            (board[97]== player and board[112] == player and board[127] == player and board[142] == player and board[157] == player) or \
            (board[112]== player and board[127] == player and board[142] == player and board[157] == player and board[172] == player) or \
            (board[127]== player and board[142] == player and board[157] == player and board[172] == player and board[187] == player) or \
            (board[142]== player and board[157] == player and board[172] == player and board[187] == player and board[202] == player) or \
            (board[157]== player and board[172] == player and board[187] == player and board[202] == player and board[217] == player) or \
            (board[8]== player and board[23] == player and board[38] == player and board[53] == player and board[68] == player) or \
            (board[23]== player and board[38] == player and board[53] == player and board[68] == player and board[83] == player) or \
            (board[38]== player and board[53] == player and board[68] == player and board[83] == player and board[98] == player) or \
            (board[53]== player and board[68] == player and board[83] == player and board[98] == player and board[113] == player) or \
            (board[68]== player and board[83] == player and board[98] == player and board[113] == player and board[128] == player) or \
            (board[83]== player and board[98] == player and board[113] == player and board[128] == player and board[143] == player) or \
            (board[98]== player and board[113] == player and board[128] == player and board[143] == player and board[158] == player) or \
            (board[113]== player and board[128] == player and board[143] == player and board[158] == player and board[173] == player) or \
            (board[128]== player and board[143] == player and board[158] == player and board[173] == player and board[188] == player) or \
            (board[143]== player and board[158] == player and board[173] == player and board[188] == player and board[203] == player) or \
            (board[158]== player and board[173] == player and board[188] == player and board[203] == player and board[218] == player) or \
            (board[9]== player and board[24] == player and board[39] == player and board[54] == player and board[69] == player) or \
            (board[24]== player and board[39] == player and board[54] == player and board[69] == player and board[84] == player) or \
            (board[39]== player and board[54] == player and board[69] == player and board[84] == player and board[99] == player) or \
            (board[54]== player and board[69] == player and board[84] == player and board[99] == player and board[114] == player) or \
            (board[69]== player and board[84] == player and board[99] == player and board[114] == player and board[129] == player) or \
            (board[84]== player and board[99] == player and board[114] == player and board[129] == player and board[144] == player) or \
            (board[99]== player and board[114] == player and board[129] == player and board[144] == player and board[159] == player) or \
            (board[114]== player and board[129] == player and board[144] == player and board[159] == player and board[174] == player) or \
            (board[129]== player and board[144] == player and board[159] == player and board[174] == player and board[189] == player) or \
            (board[144]== player and board[159] == player and board[174] == player and board[189] == player and board[204] == player) or \
            (board[159]== player and board[174] == player and board[189] == player and board[204] == player and board[219] == player) or \
            (board[10]== player and board[25] == player and board[40] == player and board[55] == player and board[70] == player) or \
            (board[25]== player and board[40] == player and board[55] == player and board[70] == player and board[85] == player) or \
            (board[40]== player and board[55] == player and board[70] == player and board[85] == player and board[100] == player) or \
            (board[55]== player and board[70] == player and board[85] == player and board[100] == player and board[115] == player) or \
            (board[70]== player and board[85] == player and board[100] == player and board[115] == player and board[130] == player) or \
            (board[85]== player and board[100] == player and board[115] == player and board[130] == player and board[145] == player) or \
            (board[100]== player and board[115] == player and board[130] == player and board[145] == player and board[160] == player) or \
            (board[115]== player and board[130] == player and board[145] == player and board[160] == player and board[175] == player) or \
            (board[130]== player and board[145] == player and board[160] == player and board[175] == player and board[190] == player) or \
            (board[145]== player and board[160] == player and board[175] == player and board[190] == player and board[205] == player) or \
            (board[160]== player and board[175] == player and board[190] == player and board[205] == player and board[220] == player) or \
            (board[11]== player and board[26] == player and board[41] == player and board[56] == player and board[71] == player) or \
            (board[26]== player and board[41] == player and board[56] == player and board[71] == player and board[86] == player) or \
            (board[41]== player and board[56] == player and board[71] == player and board[86] == player and board[101] == player) or \
            (board[56]== player and board[71] == player and board[86] == player and board[101] == player and board[116] == player) or \
            (board[71]== player and board[86] == player and board[101] == player and board[116] == player and board[131] == player) or \
            (board[86]== player and board[101] == player and board[116] == player and board[131] == player and board[146] == player) or \
            (board[101]== player and board[116] == player and board[131] == player and board[146] == player and board[161] == player) or \
            (board[116]== player and board[131] == player and board[146] == player and board[161] == player and board[176] == player) or \
            (board[131]== player and board[146] == player and board[161] == player and board[176] == player and board[191] == player) or \
            (board[146]== player and board[161] == player and board[176] == player and board[191] == player and board[206] == player) or \
            (board[161]== player and board[176] == player and board[191] == player and board[206] == player and board[221] == player) or \
            (board[12]== player and board[27] == player and board[42] == player and board[57] == player and board[72] == player) or \
            (board[27]== player and board[42] == player and board[57] == player and board[72] == player and board[87] == player) or \
            (board[42]== player and board[57] == player and board[72] == player and board[87] == player and board[102] == player) or \
            (board[57]== player and board[72] == player and board[87] == player and board[102] == player and board[117] == player) or \
            (board[72]== player and board[87] == player and board[102] == player and board[117] == player and board[132] == player) or \
            (board[87]== player and board[102] == player and board[117] == player and board[132] == player and board[147] == player) or \
            (board[102]== player and board[117] == player and board[132] == player and board[147] == player and board[162] == player) or \
            (board[117]== player and board[132] == player and board[147] == player and board[162] == player and board[177] == player) or \
            (board[132]== player and board[147] == player and board[162] == player and board[177] == player and board[192] == player) or \
            (board[147]== player and board[162] == player and board[177] == player and board[192] == player and board[207] == player) or \
            (board[162]== player and board[177] == player and board[192] == player and board[207] == player and board[222] == player) or \
            (board[13]== player and board[28] == player and board[43] == player and board[58] == player and board[73] == player) or \
            (board[28]== player and board[43] == player and board[58] == player and board[73] == player and board[88] == player) or \
            (board[43]== player and board[58] == player and board[73] == player and board[88] == player and board[103] == player) or \
            (board[58]== player and board[73] == player and board[88] == player and board[103] == player and board[118] == player) or \
            (board[73]== player and board[88] == player and board[103] == player and board[118] == player and board[133] == player) or \
            (board[88]== player and board[103] == player and board[118] == player and board[133] == player and board[148] == player) or \
            (board[103]== player and board[118] == player and board[133] == player and board[148] == player and board[163] == player) or \
            (board[118]== player and board[133] == player and board[148] == player and board[163] == player and board[178] == player) or \
            (board[133]== player and board[148] == player and board[163] == player and board[178] == player and board[193] == player) or \
            (board[148]== player and board[163] == player and board[178] == player and board[193] == player and board[208] == player) or \
            (board[163]== player and board[178] == player and board[193] == player and board[208] == player and board[223] == player) or \
            (board[14]== player and board[29] == player and board[44] == player and board[59] == player and board[74] == player) or \
            (board[29]== player and board[44] == player and board[59] == player and board[74] == player and board[89] == player) or \
            (board[44]== player and board[59] == player and board[74] == player and board[89] == player and board[104] == player) or \
            (board[59]== player and board[74] == player and board[89] == player and board[104] == player and board[119] == player) or \
            (board[74]== player and board[89] == player and board[104] == player and board[119] == player and board[134] == player) or \
            (board[89]== player and board[104] == player and board[119] == player and board[134] == player and board[149] == player) or \
            (board[104]== player and board[119] == player and board[134] == player and board[149] == player and board[164] == player) or \
            (board[119]== player and board[134] == player and board[149] == player and board[164] == player and board[179] == player) or \
            (board[134]== player and board[149] == player and board[164] == player and board[179] == player and board[194] == player) or \
            (board[149]== player and board[164] == player and board[179] == player and board[194] == player and board[209] == player) or \
            (board[164]== player and board[179] == player and board[194] == player and board[209] == player and board[224] == player) or \
            (board[15]== player and board[30] == player and board[45] == player and board[60] == player and board[75] == player) or \
            (board[30]== player and board[45] == player and board[60] == player and board[75] == player and board[90] == player) or \
            (board[45]== player and board[60] == player and board[75] == player and board[90] == player and board[105] == player) or \
            (board[60]== player and board[75] == player and board[90] == player and board[105] == player and board[120] == player) or \
            (board[75]== player and board[90] == player and board[105] == player and board[120] == player and board[135] == player) or \
            (board[90]== player and board[105] == player and board[120] == player and board[135] == player and board[150] == player) or \
            (board[105]== player and board[120] == player and board[135] == player and board[150] == player and board[165] == player) or \
            (board[120]== player and board[135] == player and board[150] == player and board[165] == player and board[180] == player) or \
            (board[135]== player and board[150] == player and board[165] == player and board[180] == player and board[195] == player) or \
            (board[150]== player and board[165] == player and board[180] == player and board[195] == player and board[210] == player) or \
            (board[165]== player and board[180] == player and board[195] == player and board[210] == player and board[222] == player) or \
            (board[1]== player and board[17] == player and board[33] == player and board[49] == player and board[65] == player) or \
            (board[17]== player and board[33] == player and board[49] == player and board[65] == player and board[81] == player) or \
            (board[33]== player and board[49] == player and board[65] == player and board[81] == player and board[97] == player) or \
            (board[49]== player and board[65] == player and board[81] == player and board[97] == player and board[113] == player) or \
            (board[65]== player and board[81] == player and board[97] == player and board[113] == player and board[129] == player) or \
            (board[81]== player and board[97] == player and board[113] == player and board[129] == player and board[145] == player) or \
            (board[97]== player and board[113] == player and board[129] == player and board[145] == player and board[161] == player) or \
            (board[113]== player and board[129] == player and board[145] == player and board[161] == player and board[177] == player) or \
            (board[129]== player and board[145] == player and board[161] == player and board[177] == player and board[193] == player) or \
            (board[145]== player and board[161] == player and board[177] == player and board[193] == player and board[209] == player) or \
            (board[161]== player and board[177] == player and board[193] == player and board[209] == player and board[225] == player)or \
            (board[16]== player and board[32] == player and board[48] == player and board[64] == player and board[80] == player) or \
            (board[32]== player and board[48] == player and board[64] == player and board[80] == player and board[96] == player) or \
            (board[48]== player and board[64] == player and board[80] == player and board[96] == player and board[112] == player) or \
            (board[64]== player and board[80] == player and board[96] == player and board[112] == player and board[128] == player) or \
            (board[80]== player and board[96] == player and board[112] == player and board[128] == player and board[144] == player) or \
            (board[96]== player and board[112] == player and board[128] == player and board[144] == player and board[160] == player) or \
            (board[112]== player and board[128] == player and board[144] == player and board[160] == player and board[176] == player) or \
            (board[128]== player and board[144] == player and board[160] == player and board[176] == player and board[192] == player) or \
            (board[144]== player and board[160] == player and board[176] == player and board[192] == player and board[208] == player) or \
            (board[160]== player and board[176] == player and board[192] == player and board[208] == player and board[224] == player)or \
            (board[31]== player and board[47] == player and board[63] == player and board[79] == player and board[95] == player) or \
            (board[47]== player and board[63] == player and board[79] == player and board[95] == player and board[111] == player) or \
            (board[63]== player and board[79] == player and board[95] == player and board[111] == player and board[127] == player) or \
            (board[79]== player and board[95] == player and board[111] == player and board[127] == player and board[143] == player) or \
            (board[95]== player and board[111] == player and board[127] == player and board[143] == player and board[159] == player) or \
            (board[111]== player and board[127] == player and board[143] == player and board[159] == player and board[175] == player) or \
            (board[127]== player and board[143] == player and board[159] == player and board[175] == player and board[191] == player) or \
            (board[143]== player and board[159] == player and board[175] == player and board[191] == player and board[207] == player) or \
            (board[159]== player and board[175] == player and board[191] == player and board[207] == player and board[223] == player) or \
            (board[46]== player and board[62] == player and board[78] == player and board[94] == player and board[110] == player) or \
            (board[62]== player and board[78] == player and board[94] == player and board[110] == player and board[126] == player) or \
            (board[78]== player and board[94] == player and board[110] == player and board[126] == player and board[142] == player) or \
            (board[94]== player and board[110] == player and board[126] == player and board[142] == player and board[158] == player) or \
            (board[110]== player and board[126] == player and board[142] == player and board[158] == player and board[174] == player) or \
            (board[126]== player and board[142] == player and board[158] == player and board[174] == player and board[190] == player) or \
            (board[142]== player and board[158] == player and board[174] == player and board[190] == player and board[206] == player) or \
            (board[158]== player and board[174] == player and board[190] == player and board[206] == player and board[222] == player) or \
            (board[61]== player and board[77] == player and board[93] == player and board[109] == player and board[125] == player) or \
            (board[77]== player and board[93] == player and board[109] == player and board[125] == player and board[141] == player) or \
            (board[93]== player and board[109] == player and board[125] == player and board[141] == player and board[157] == player) or \
            (board[109]== player and board[125] == player and board[141] == player and board[157] == player and board[173] == player) or \
            (board[125]== player and board[141] == player and board[157] == player and board[173] == player and board[189] == player) or \
            (board[141]== player and board[157] == player and board[173] == player and board[189] == player and board[205] == player) or \
            (board[157]== player and board[173] == player and board[189] == player and board[205] == player and board[221] == player) or \
            (board[76]== player and board[92] == player and board[108] == player and board[124] == player and board[140] == player) or \
            (board[92]== player and board[108] == player and board[124] == player and board[140] == player and board[156] == player) or \
            (board[108]== player and board[124] == player and board[140] == player and board[156] == player and board[172] == player) or \
            (board[124]== player and board[140] == player and board[156] == player and board[172] == player and board[188] == player) or \
            (board[140]== player and board[156] == player and board[172] == player and board[188] == player and board[204] == player) or \
            (board[156]== player and board[172] == player and board[188] == player and board[204] == player and board[220] == player) or \
            (board[91]== player and board[107] == player and board[123] == player and board[139] == player and board[155] == player) or \
            (board[107]== player and board[123] == player and board[139] == player and board[155] == player and board[171] == player) or \
            (board[123]== player and board[139] == player and board[155] == player and board[171] == player and board[187] == player) or \
            (board[139]== player and board[155] == player and board[171] == player and board[187] == player and board[203] == player) or \
            (board[155]== player and board[171] == player and board[187] == player and board[203] == player and board[219] == player) or \
            (board[106]== player and board[122] == player and board[138] == player and board[154] == player and board[170] == player) or \
            (board[122]== player and board[138] == player and board[154] == player and board[170] == player and board[186] == player) or \
            (board[138]== player and board[154] == player and board[170] == player and board[186] == player and board[202] == player) or \
            (board[154]== player and board[170] == player and board[186] == player and board[202] == player and board[218] == player) or \
            (board[121]== player and board[137] == player and board[153] == player and board[169] == player and board[185] == player) or \
            (board[137]== player and board[153] == player and board[169] == player and board[185] == player and board[201] == player) or \
            (board[153]== player and board[169] == player and board[185] == player and board[201] == player and board[217] == player) or \
            (board[136]== player and board[152] == player and board[168] == player and board[184] == player and board[200] == player) or \
            (board[152]== player and board[168] == player and board[184] == player and board[200] == player and board[216] == player) or \
            (board[151]== player and board[167] == player and board[183] == player and board[199] == player and board[215] == player) or\
            (board[2]== player and board[18] == player and board[34] == player and board[50] == player and board[66] == player) or \
            (board[18]== player and board[34] == player and board[50] == player and board[66] == player and board[82] == player) or \
            (board[34]== player and board[50] == player and board[66] == player and board[82] == player and board[98] == player) or \
            (board[50]== player and board[66] == player and board[82] == player and board[98] == player and board[114] == player) or \
            (board[66]== player and board[82] == player and board[98] == player and board[114] == player and board[130] == player) or \
            (board[82]== player and board[98] == player and board[114] == player and board[130] == player and board[146] == player) or \
            (board[98]== player and board[114] == player and board[130] == player and board[144] == player and board[162] == player) or \
            (board[114]== player and board[130] == player and board[146] == player and board[162] == player and board[178] == player) or \
            (board[130]== player and board[146] == player and board[162] == player and board[178] == player and board[194] == player) or \
            (board[146]== player and board[162] == player and board[178] == player and board[194] == player and board[210] == player) or \
            (board[3]== player and board[19] == player and board[35] == player and board[51] == player and board[67] == player) or \
            (board[19]== player and board[35] == player and board[51] == player and board[67] == player and board[83] == player) or \
            (board[35]== player and board[51] == player and board[67] == player and board[83] == player and board[99] == player) or \
            (board[51]== player and board[67] == player and board[83] == player and board[99] == player and board[115] == player) or \
            (board[67]== player and board[83] == player and board[99] == player and board[115] == player and board[131] == player) or \
            (board[83]== player and board[99] == player and board[115] == player and board[131] == player and board[147] == player) or \
            (board[99]== player and board[115] == player and board[131] == player and board[145] == player and board[163] == player) or \
            (board[115]== player and board[131] == player and board[147] == player and board[163] == player and board[179] == player) or \
            (board[131]== player and board[147] == player and board[163] == player and board[179] == player and board[195] == player) or \
            (board[4]== player and board[20] == player and board[36] == player and board[52] == player and board[68] == player) or \
            (board[20]== player and board[36] == player and board[52] == player and board[68] == player and board[84] == player) or \
            (board[36]== player and board[52] == player and board[68] == player and board[84] == player and board[100] == player) or \
            (board[52]== player and board[68] == player and board[84] == player and board[100] == player and board[116] == player) or \
            (board[68]== player and board[84] == player and board[100] == player and board[116] == player and board[132] == player) or \
            (board[84]== player and board[100] == player and board[116] == player and board[132] == player and board[148] == player) or \
            (board[100]== player and board[116] == player and board[132] == player and board[146] == player and board[164] == player) or \
            (board[116]== player and board[132] == player and board[148] == player and board[164] == player and board[180] == player) or \
            (board[5]== player and board[21] == player and board[37] == player and board[53] == player and board[69] == player) or \
            (board[21]== player and board[37] == player and board[53] == player and board[69] == player and board[85] == player) or \
            (board[37]== player and board[53] == player and board[69] == player and board[85] == player and board[101] == player) or \
            (board[53]== player and board[69] == player and board[85] == player and board[101] == player and board[117] == player) or \
            (board[69]== player and board[85] == player and board[101] == player and board[117] == player and board[133] == player) or \
            (board[85]== player and board[101] == player and board[117] == player and board[133] == player and board[149] == player) or \
            (board[101]== player and board[117] == player and board[133] == player and board[147] == player and board[165] == player) or \
            (board[6]== player and board[22] == player and board[38] == player and board[54] == player and board[70] == player) or \
            (board[22]== player and board[38] == player and board[54] == player and board[70] == player and board[86] == player) or \
            (board[38]== player and board[54] == player and board[70] == player and board[86] == player and board[102] == player) or \
            (board[54]== player and board[70] == player and board[86] == player and board[102] == player and board[118] == player) or \
            (board[70]== player and board[86] == player and board[102] == player and board[118] == player and board[134] == player) or \
            (board[86]== player and board[102] == player and board[118] == player and board[134] == player and board[150] == player) or\
            (board[7]== player and board[23] == player and board[39] == player and board[55] == player and board[71] == player) or \
            (board[23]== player and board[39] == player and board[55] == player and board[71] == player and board[87] == player) or \
            (board[39]== player and board[55] == player and board[71] == player and board[87] == player and board[103] == player) or \
            (board[55]== player and board[71] == player and board[87] == player and board[103] == player and board[119] == player) or \
            (board[71]== player and board[87] == player and board[103] == player and board[119] == player and board[135] == player) or \
            (board[8]== player and board[24] == player and board[40] == player and board[56] == player and board[72] == player) or \
            (board[24]== player and board[40] == player and board[56] == player and board[72] == player and board[88] == player) or \
            (board[40]== player and board[56] == player and board[72] == player and board[88] == player and board[104] == player) or \
            (board[56]== player and board[72] == player and board[88] == player and board[104] == player and board[120] == player) or \
            (board[9]== player and board[25] == player and board[41] == player and board[57] == player and board[73] == player) or \
            (board[25]== player and board[41] == player and board[57] == player and board[73] == player and board[89] == player) or \
            (board[41]== player and board[57] == player and board[73] == player and board[89] == player and board[105] == player) or \
            (board[10]== player and board[26] == player and board[42] == player and board[58] == player and board[74] == player) or \
            (board[26]== player and board[42] == player and board[58] == player and board[74] == player and board[90] == player) or \
            (board[11]== player and board[27] == player and board[43] == player and board[59] == player and board[75] == player) or \
            (board[211]== player and board[197] == player and board[183] == player and board[169] == player and board[155] == player) or \
            (board[197]== player and board[183] == player and board[169] == player and board[155] == player and board[141] == player) or \
            (board[183]== player and board[169] == player and board[155] == player and board[141] == player and board[127] == player) or \
            (board[169]== player and board[155] == player and board[141] == player and board[127] == player and board[113] == player) or \
            (board[155]== player and board[141] == player and board[127] == player and board[113] == player and board[99] == player) or \
            (board[141]== player and board[127] == player and board[113] == player and board[99] == player and board[85] == player) or \
            (board[127]== player and board[113] == player and board[99] == player and board[85] == player and board[71] == player) or \
            (board[113]== player and board[99] == player and board[85] == player and board[71] == player and board[57] == player) or \
            (board[99]== player and board[85] == player and board[71] == player and board[57] == player and board[43] == player) or \
            (board[85]== player and board[71] == player and board[57] == player and board[43] == player and board[29] == player) or \
            (board[71]== player and board[57] == player and board[43] == player and board[29] == player and board[15] == player) or \
            (board[212]== player and board[198] == player and board[184] == player and board[170] == player and board[156] == player) or \
            (board[198]== player and board[184] == player and board[170] == player and board[156] == player and board[142] == player) or \
            (board[184]== player and board[170] == player and board[156] == player and board[142] == player and board[128] == player) or \
            (board[170]== player and board[156] == player and board[142] == player and board[128] == player and board[114] == player) or \
            (board[156]== player and board[142] == player and board[128] == player and board[114] == player and board[100] == player) or \
            (board[142]== player and board[128] == player and board[114] == player and board[100] == player and board[86] == player) or \
            (board[128]== player and board[114] == player and board[100] == player and board[86] == player and board[72] == player) or \
            (board[114]== player and board[100] == player and board[86] == player and board[72] == player and board[58] == player) or \
            (board[100]== player and board[86] == player and board[72] == player and board[58] == player and board[44] == player) or \
            (board[86]== player and board[72] == player and board[58] == player and board[44] == player and board[30] == player) or \
            (board[213]== player and board[199] == player and board[185] == player and board[171] == player and board[157] == player) or \
            (board[199]== player and board[185] == player and board[171] == player and board[157] == player and board[143] == player) or \
            (board[185]== player and board[171] == player and board[157] == player and board[143] == player and board[129] == player) or \
            (board[171]== player and board[157] == player and board[143] == player and board[129] == player and board[115] == player) or \
            (board[157]== player and board[143] == player and board[129] == player and board[115] == player and board[101] == player) or \
            (board[143]== player and board[129] == player and board[115] == player and board[101] == player and board[87] == player) or \
            (board[129]== player and board[115] == player and board[101] == player and board[87] == player and board[73] == player) or \
            (board[115]== player and board[101] == player and board[87] == player and board[73] == player and board[59] == player) or \
            (board[101]== player and board[87] == player and board[73] == player and board[59] == player and board[45] == player) or \
            (board[214]== player and board[200] == player and board[186] == player and board[172] == player and board[158] == player) or \
            (board[200]== player and board[186] == player and board[172] == player and board[158] == player and board[144] == player) or \
            (board[186]== player and board[172] == player and board[158] == player and board[144] == player and board[130] == player) or \
            (board[172]== player and board[158] == player and board[144] == player and board[130] == player and board[116] == player) or \
            (board[158]== player and board[144] == player and board[130] == player and board[116] == player and board[102] == player) or \
            (board[144]== player and board[130] == player and board[116] == player and board[102] == player and board[88] == player) or \
            (board[130]== player and board[116] == player and board[102] == player and board[88] == player and board[74] == player) or \
            (board[116]== player and board[102] == player and board[88] == player and board[74] == player and board[60] == player) or \
            (board[215]== player and board[201] == player and board[187] == player and board[173] == player and board[159] == player) or \
            (board[201]== player and board[187] == player and board[173] == player and board[159] == player and board[145] == player) or \
            (board[187]== player and board[173] == player and board[159] == player and board[145] == player and board[131] == player) or \
            (board[173]== player and board[159] == player and board[145] == player and board[131] == player and board[117] == player) or \
            (board[159]== player and board[145] == player and board[131] == player and board[117] == player and board[103] == player) or \
            (board[145]== player and board[131] == player and board[117] == player and board[103] == player and board[89] == player) or \
            (board[131]== player and board[117] == player and board[103] == player and board[89] == player and board[75] == player) or \
            (board[216]== player and board[202] == player and board[188] == player and board[174] == player and board[160] == player) or \
            (board[202]== player and board[188] == player and board[174] == player and board[160] == player and board[146] == player) or \
            (board[188]== player and board[174] == player and board[160] == player and board[146] == player and board[132] == player) or \
            (board[174]== player and board[160] == player and board[146] == player and board[132] == player and board[118] == player) or \
            (board[160]== player and board[146] == player and board[132] == player and board[118] == player and board[104] == player) or \
            (board[146]== player and board[132] == player and board[118] == player and board[104] == player and board[90] == player) or \
            (board[217]== player and board[203] == player and board[189] == player and board[175] == player and board[161] == player) or \
            (board[203]== player and board[189] == player and board[175] == player and board[161] == player and board[147] == player) or \
            (board[189]== player and board[175] == player and board[161] == player and board[147] == player and board[133] == player) or \
            (board[175]== player and board[161] == player and board[147] == player and board[133] == player and board[119] == player) or \
            (board[161]== player and board[147] == player and board[133] == player and board[119] == player and board[105] == player) or \
            (board[218]== player and board[204] == player and board[190] == player and board[176] == player and board[162] == player) or \
            (board[204]== player and board[190] == player and board[176] == player and board[162] == player and board[148] == player) or \
            (board[190]== player and board[176] == player and board[162] == player and board[148] == player and board[134] == player) or \
            (board[176]== player and board[162] == player and board[148] == player and board[134] == player and board[120] == player) or \
            (board[219]== player and board[205] == player and board[191] == player and board[177] == player and board[163] == player) or \
            (board[204]== player and board[191] == player and board[177] == player and board[163] == player and board[149] == player) or \
            (board[191]== player and board[177] == player and board[163] == player and board[149] == player and board[135] == player) or \
            (board[220]== player and board[206] == player and board[192] == player and board[178] == player and board[164] == player) or \
            (board[205]== player and board[192] == player and board[178] == player and board[164] == player and board[150] == player) or \
            (board[221]== player and board[207] == player and board[193] == player and board[179] == player and board[165] == player) or\
            (board[196]== player and board[182] == player and board[168] == player and board[154] == player and board[140] == player) or \
            (board[182]== player and board[168] == player and board[154] == player and board[140] == player and board[126] == player) or \
            (board[168]== player and board[154] == player and board[140] == player and board[126] == player and board[112] == player) or \
            (board[154]== player and board[140] == player and board[126] == player and board[112] == player and board[98] == player) or \
            (board[140]== player and board[126] == player and board[112] == player and board[98] == player and board[84] == player) or \
            (board[126]== player and board[112] == player and board[98] == player and board[84] == player and board[70] == player) or \
            (board[112]== player and board[98] == player and board[84] == player and board[70] == player and board[56] == player) or \
            (board[98]== player and board[84] == player and board[70] == player and board[56] == player and board[42] == player) or \
            (board[84]== player and board[70] == player and board[56] == player and board[42] == player and board[28] == player) or \
            (board[70]== player and board[56] == player and board[42] == player and board[28] == player and board[14] == player) or \
            (board[181]== player and board[167] == player and board[153] == player and board[139] == player and board[125] == player) or \
            (board[167]== player and board[153] == player and board[139] == player and board[125] == player and board[111] == player) or \
            (board[153]== player and board[139] == player and board[125] == player and board[111] == player and board[97] == player) or \
            (board[139]== player and board[125] == player and board[111] == player and board[97] == player and board[83] == player) or \
            (board[125]== player and board[111] == player and board[97] == player and board[83] == player and board[69] == player) or \
            (board[111]== player and board[97] == player and board[83] == player and board[69] == player and board[55] == player) or \
            (board[97]== player and board[83] == player and board[69] == player and board[55] == player and board[41] == player) or \
            (board[83]== player and board[69] == player and board[55] == player and board[41] == player and board[27] == player) or \
            (board[69]== player and board[55] == player and board[41] == player and board[27] == player and board[13] == player) or \
            (board[166]== player and board[152] == player and board[138] == player and board[124] == player and board[110] == player) or \
            (board[152]== player and board[138] == player and board[124] == player and board[110] == player and board[96] == player) or \
            (board[138]== player and board[124] == player and board[110] == player and board[96] == player and board[82] == player) or \
            (board[124]== player and board[110] == player and board[96] == player and board[82] == player and board[68] == player) or \
            (board[110]== player and board[96] == player and board[82] == player and board[68] == player and board[54] == player) or \
            (board[96]== player and board[82] == player and board[68] == player and board[54] == player and board[40] == player) or \
            (board[82]== player and board[68] == player and board[54] == player and board[40] == player and board[26] == player) or \
            (board[68]== player and board[54] == player and board[40] == player and board[26] == player and board[12] == player) or \
            (board[151]== player and board[137] == player and board[123] == player and board[109] == player and board[95] == player) or \
            (board[137]== player and board[123] == player and board[109] == player and board[95] == player and board[81] == player) or \
            (board[123]== player and board[109] == player and board[95] == player and board[81] == player and board[67] == player) or \
            (board[109]== player and board[95] == player and board[81] == player and board[67] == player and board[53] == player) or \
            (board[95]== player and board[81] == player and board[67] == player and board[53] == player and board[39] == player) or \
            (board[81]== player and board[67] == player and board[53] == player and board[39] == player and board[25] == player) or \
            (board[67]== player and board[53] == player and board[39] == player and board[25] == player and board[11] == player) or \
            (board[136]== player and board[122] == player and board[108] == player and board[94] == player and board[80] == player) or \
            (board[122]== player and board[108] == player and board[94] == player and board[80] == player and board[66] == player) or \
            (board[108]== player and board[94] == player and board[80] == player and board[66] == player and board[52] == player) or \
            (board[94]== player and board[80] == player and board[66] == player and board[52] == player and board[38] == player) or \
            (board[80]== player and board[66] == player and board[52] == player and board[38] == player and board[24] == player) or \
            (board[66]== player and board[52] == player and board[38] == player and board[24] == player and board[10] == player) or \
            (board[121]== player and board[107] == player and board[93] == player and board[79] == player and board[65] == player) or \
            (board[107]== player and board[93] == player and board[79] == player and board[65] == player and board[51] == player) or \
            (board[93]== player and board[79] == player and board[65] == player and board[51] == player and board[37] == player) or \
            (board[79]== player and board[65] == player and board[51] == player and board[37] == player and board[23] == player) or \
            (board[65]== player and board[51] == player and board[37] == player and board[23] == player and board[9] == player) or \
            (board[106]== player and board[92] == player and board[78] == player and board[64] == player and board[50] == player) or \
            (board[92]== player and board[78] == player and board[64] == player and board[50] == player and board[36] == player) or \
            (board[78]== player and board[64] == player and board[50] == player and board[36] == player and board[22] == player) or \
            (board[64]== player and board[50] == player and board[36] == player and board[22] == player and board[8] == player) or \
            (board[91]== player and board[77] == player and board[63] == player and board[49] == player and board[35] == player) or \
            (board[77]== player and board[63] == player and board[49] == player and board[35] == player and board[21] == player) or \
            (board[63]== player and board[49] == player and board[35] == player and board[21] == player and board[7] == player) or \
            (board[76]== player and board[62] == player and board[48] == player and board[34] == player and board[20] == player) or \
            (board[62]== player and board[48] == player and board[34] == player and board[20] == player and board[6] == player) or \
            (board[61]== player and board[47] == player and board[33] == player and board[19] == player and board[5] == player) :
            return True
        else: 
            return False

    def is_board_full(board):
	    if ' ' in board:
		    return False
	    else:
		    return True

    def get_computer_move(board, player):
	    if board[10] == ' ':
		    return 10

	    while True:
		    move = random.randint(1,225)
		    if board[move] == ' ':
		           return move
		           break	
	    return 10

    while True:

	    print_board()
            #Player X Input
	    time.sleep(0.5)
	    choice = int(raw_input(u'\n\t\t     Mời Bạn ( X ) Chọn Vị Trí Từ 1 -> 225 >> '))

	    #Check space
	    if board[choice] == ' ':
		    board[choice] = 'X'
	    else:
		    print u'\n\t\t     Vị Trí Này Không Còn Trống , Lượt Computer Chọn !'
		    time.sleep(1)
	    #Check X win
	    if is_winner(board, 'X'):
	        
	        print_board()
	        print u'\n\t\t     Người Chơi ( X ) Thắng ! '
	        break
	
            #Check hoa
	    if is_board_full(board):
		    print u'\n\t\t     Trận Đấu Hòa !'
		    break

            #Player O Input
	    choice = get_computer_move(board,  'O')

	    #Check space
	    if board[choice] == ' ':
		    board[choice] = 'O'
	    else:
		    print u'\n\t\t     Vị Trí Này Không Còn Trống , Lượt Bạn Chọn !'
		    time.sleep(1)

           #Check O win
	    if is_winner(board, 'O'):
		
		    print_board()
		    print u'\n\t\t     Computer (O) Thắng ! '
		    break

            #Check hoa
	    if is_board_full(board):
		    print u'\n\t\t     Trận Đấu Hòa !'
		    break

def player_player():

    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def print_board():
        print u'\n\t\t\t\t\t\t\t\t\t\t\t\t     VỊ TRÍ CÁC QUÂN CỜ :                       '
        time.sleep(1)
        print ('x'*61)
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t        1 |  2 |  3 |  4 | 5 | 6  |  7 |  8 |  9 | 10 | 11  | 12 | 13 | 14 | 15 '  %(board[1],  board[2],  board[3],  board[4],  board[5],  board[6],  board[7],  board[8],  board[9], board[10],  board[11],  board[12],  board[13],  board[14],  board[15]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 '  %(board[16],  board[17],  board[18],  board[19],  board[20],  board[21],  board[22],  board[23],  board[24], board[25],  board[26],  board[27],  board[28],  board[29],  board[30]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 '  %(board[31],  board[32],  board[33],  board[34],  board[35],  board[36],  board[37],  board[38],  board[39], board[40],  board[41],  board[42],  board[43],  board[44],  board[45]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 '  %(board[46],  board[47],  board[48],  board[49],  board[50],  board[51],  board[52],  board[53],  board[54], board[55],  board[56],  board[57],  board[58],  board[59],  board[60]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 | 72 | 73 | 74 | 75  ' %(board[61],  board[62],  board[63],  board[64],  board[65],  board[66],  board[67],  board[68],  board[69], board[70],  board[71],  board[72],  board[73],  board[74],  board[75]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90  ' %(board[76],  board[77],  board[78],  board[79],  board[80],  board[81],  board[82],  board[83],  board[84], board[85],  board[86],  board[87],  board[88],  board[89],  board[90]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100| 101| 102| 103| 104| 105 ' %(board[91],  board[92],  board[93],  board[94],  board[95],  board[96],  board[97],  board[98],  board[99], board[100],  board[101],  board[102],  board[103],  board[104],  board[105]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       106| 107| 108| 109| 110| 111| 112| 113| 114| 115| 116| 117| 118| 119| 120 ' %(board[106],  board[107],  board[108],  board[109],  board[110],  board[111],  board[112],  board[113],  board[114], board[115],  board[116],  board[117],  board[118],  board[119],  board[120]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       121| 122| 123| 124| 125| 126| 127| 128| 129| 130| 131| 132| 133| 134| 135 ' %(board[121],  board[122],  board[123],  board[124],  board[125],  board[126],  board[127],  board[128],  board[129], board[130],  board[131],  board[132],  board[133],  board[134],  board[135]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       136| 137| 138| 139| 140| 141| 142| 143| 144| 145| 146| 147| 148| 149| 150 ' %(board[136],  board[137],  board[138],  board[139],  board[140],  board[141],  board[142],  board[143],  board[144], board[145],  board[146],  board[147],  board[148],  board[149],  board[150]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       151| 152| 153| 154| 155| 156| 157| 158| 159| 160| 161| 162| 163| 164| 165 ' %(board[151],  board[152],  board[153],  board[154],  board[155],  board[156],  board[157],  board[158],  board[159], board[160],  board[161],  board[162],  board[163],  board[164],  board[165]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       166| 167| 168| 169| 170| 171| 172| 173| 174| 175| 176| 177| 178| 179| 180 ' %(board[166],  board[167],  board[168],  board[169],  board[170],  board[171],  board[172],  board[173],  board[174], board[175],  board[176],  board[177],  board[178],  board[179],  board[180]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       181| 182| 183| 184| 185| 186| 187| 188| 189| 190| 191| 192| 193| 194| 195 ' %(board[181],  board[182],  board[183],  board[184],  board[185],  board[186],  board[187],  board[188],  board[189], board[190],  board[191],  board[192],  board[193],  board[194],  board[195]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       196| 197| 198| 199| 200| 201| 202| 203| 204| 205| 206| 207| 208| 209| 210 ' %(board[196],  board[197],  board[198],  board[199],  board[200],  board[201],  board[202],  board[203],  board[204], board[205],  board[206],  board[207],  board[208],  board[209],  board[210]))
        print ('[-----------------------------------------------------------]')
        print ('[ %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s ]\t\t\t       211| 212| 213| 214| 215| 216| 217| 218| 219| 220| 221| 222| 223| 224| 225 ' %(board[211],  board[212],  board[213],  board[214],  board[215],  board[216],  board[217],  board[218],  board[219], board[220],  board[221],  board[222],  board[223],  board[224],  board[225]))
        print ('x'*61)

    def is_winner(board, player):
        if (board[1]== player and board[2] == player and board[3] == player and board[4] == player and board[5] == player)or \
            (board[2]== player and board[3] == player and board[4] == player and board[5] == player and board[6] == player) or \
            (board[3]== player and board[4] == player and board[5] == player and board[6] == player and board[7] == player) or \
            (board[4]== player and board[5] == player and board[6] == player and board[7] == player and board[8] == player) or \
            (board[5]== player and board[6] == player and board[7] == player and board[8] == player and board[9] == player) or \
            (board[6]== player and board[7] == player and board[8] == player and board[9] == player and board[10] == player) or \
            (board[7]== player and board[8] == player and board[9] == player and board[10] == player and board[11] == player) or \
            (board[8]== player and board[9] == player and board[10] == player and board[11] == player and board[12] == player) or \
            (board[9]== player and board[10] == player and board[11] == player and board[12] == player and board[13] == player) or \
            (board[10]== player and board[11] == player and board[12] == player and board[13] == player and board[14] == player) or \
            (board[11]== player and board[12] == player and board[13] == player and board[14] == player and board[15] == player) or \
            (board[16]== player and board[17] == player and board[18] == player and board[19] == player and board[20] == player) or \
            (board[17]== player and board[18] == player and board[19] == player and board[20] == player and board[21] == player) or \
            (board[18]== player and board[19] == player and board[20] == player and board[21] == player and board[22] == player) or \
            (board[19]== player and board[20] == player and board[21] == player and board[22] == player and board[23] == player) or \
            (board[20]== player and board[21] == player and board[22] == player and board[23] == player and board[24] == player) or \
            (board[21]== player and board[22] == player and board[23] == player and board[24] == player and board[25] == player) or \
            (board[22]== player and board[23] == player and board[24] == player and board[25] == player and board[26] == player) or \
            (board[23]== player and board[24] == player and board[25] == player and board[26] == player and board[27] == player) or \
            (board[24]== player and board[25] == player and board[26] == player and board[27] == player and board[28] == player) or \
            (board[25]== player and board[26] == player and board[27] == player and board[28] == player and board[29] == player) or \
            (board[26]== player and board[27] == player and board[28] == player and board[29] == player and board[30] == player) or \
            (board[31]== player and board[32] == player and board[33] == player and board[34] == player and board[35] == player) or \
            (board[32]== player and board[33] == player and board[34] == player and board[35] == player and board[36] == player) or \
            (board[33]== player and board[34] == player and board[35] == player and board[36] == player and board[37] == player) or \
            (board[34]== player and board[35] == player and board[36] == player and board[37] == player and board[38] == player) or \
            (board[35]== player and board[36] == player and board[37] == player and board[38] == player and board[39] == player) or \
            (board[36]== player and board[37] == player and board[38] == player and board[39] == player and board[40] == player) or \
            (board[37]== player and board[38] == player and board[39] == player and board[40] == player and board[41] == player) or \
            (board[38]== player and board[39] == player and board[40] == player and board[41] == player and board[42] == player) or \
            (board[39]== player and board[40] == player and board[41] == player and board[42] == player and board[43] == player) or \
            (board[40]== player and board[41] == player and board[42] == player and board[43] == player and board[44] == player) or \
            (board[41]== player and board[42] == player and board[43] == player and board[44] == player and board[45] == player) or \
            (board[46]== player and board[47] == player and board[48] == player and board[49] == player and board[50] == player) or \
            (board[47]== player and board[48] == player and board[49] == player and board[50] == player and board[51] == player) or \
            (board[48]== player and board[49] == player and board[50] == player and board[51] == player and board[52] == player) or \
            (board[49]== player and board[50] == player and board[51] == player and board[52] == player and board[53] == player) or \
            (board[50]== player and board[51] == player and board[52] == player and board[53] == player and board[54] == player) or \
            (board[51]== player and board[52] == player and board[53] == player and board[54] == player and board[55] == player) or \
            (board[52]== player and board[53] == player and board[54] == player and board[55] == player and board[56] == player) or \
            (board[53]== player and board[54] == player and board[55] == player and board[56] == player and board[57] == player) or \
            (board[54]== player and board[55] == player and board[56] == player and board[57] == player and board[58] == player) or \
            (board[55]== player and board[56] == player and board[57] == player and board[58] == player and board[59] == player) or \
            (board[56]== player and board[57] == player and board[58] == player and board[59] == player and board[60] == player) or \
            (board[61]== player and board[62] == player and board[63] == player and board[64] == player and board[65] == player) or \
            (board[62]== player and board[63] == player and board[64] == player and board[65] == player and board[66] == player) or \
            (board[63]== player and board[64] == player and board[65] == player and board[66] == player and board[67] == player) or \
            (board[64]== player and board[65] == player and board[66] == player and board[67] == player and board[68] == player) or \
            (board[65]== player and board[66] == player and board[67] == player and board[68] == player and board[69] == player) or \
            (board[66]== player and board[67] == player and board[68] == player and board[69] == player and board[70] == player) or \
            (board[67]== player and board[68] == player and board[69] == player and board[70] == player and board[71] == player) or \
            (board[68]== player and board[69] == player and board[70] == player and board[71] == player and board[72] == player) or \
            (board[69]== player and board[70] == player and board[71] == player and board[72] == player and board[73] == player) or \
            (board[70]== player and board[71] == player and board[72] == player and board[73] == player and board[74] == player) or \
            (board[71]== player and board[72] == player and board[73] == player and board[74] == player and board[75] == player) or \
            (board[76]== player and board[77] == player and board[78] == player and board[79] == player and board[80] == player) or \
            (board[77]== player and board[78] == player and board[79] == player and board[80] == player and board[81] == player) or \
            (board[78]== player and board[79] == player and board[80] == player and board[81] == player and board[82] == player) or \
            (board[79]== player and board[80] == player and board[81] == player and board[82] == player and board[83] == player) or \
            (board[80]== player and board[81] == player and board[82] == player and board[83] == player and board[84] == player) or \
            (board[81]== player and board[82] == player and board[83] == player and board[84] == player and board[85] == player) or \
            (board[82]== player and board[83] == player and board[84] == player and board[85] == player and board[86] == player) or \
            (board[83]== player and board[84] == player and board[85] == player and board[86] == player and board[87] == player) or \
            (board[84]== player and board[85] == player and board[86] == player and board[87] == player and board[88] == player) or \
            (board[85]== player and board[86] == player and board[87] == player and board[88] == player and board[89] == player) or \
            (board[86]== player and board[87] == player and board[88] == player and board[89] == player and board[90] == player) or \
            (board[91]== player and board[92] == player and board[93] == player and board[94] == player and board[95] == player) or \
            (board[92]== player and board[93] == player and board[94] == player and board[95] == player and board[96] == player) or \
            (board[93]== player and board[94] == player and board[95] == player and board[96] == player and board[97] == player) or \
            (board[94]== player and board[95] == player and board[96] == player and board[97] == player and board[98] == player) or \
            (board[95]== player and board[96] == player and board[97] == player and board[98] == player and board[99] == player) or \
            (board[96]== player and board[97] == player and board[98] == player and board[99] == player and board[100] == player) or \
            (board[97]== player and board[98] == player and board[99] == player and board[100] == player and board[101] == player) or \
            (board[98]== player and board[99] == player and board[100] == player and board[101] == player and board[102] == player) or \
            (board[99]== player and board[100] == player and board[101] == player and board[102] == player and board[103] == player) or \
            (board[100]== player and board[101] == player and board[102] == player and board[103] == player and board[104] == player) or \
            (board[101]== player and board[102] == player and board[103] == player and board[104] == player and board[105] == player) or \
            (board[106]== player and board[107] == player and board[108] == player and board[109] == player and board[110] == player) or \
            (board[107]== player and board[108] == player and board[109] == player and board[110] == player and board[111] == player) or \
            (board[108]== player and board[109] == player and board[110] == player and board[111] == player and board[112] == player) or \
            (board[109]== player and board[110] == player and board[111] == player and board[112] == player and board[113] == player) or \
            (board[110]== player and board[111] == player and board[112] == player and board[113] == player and board[114] == player) or \
            (board[111]== player and board[112] == player and board[113] == player and board[114] == player and board[115] == player) or \
            (board[112]== player and board[113] == player and board[114] == player and board[115] == player and board[116] == player) or \
            (board[113]== player and board[114] == player and board[115] == player and board[116] == player and board[117] == player) or \
            (board[114]== player and board[115] == player and board[116] == player and board[117] == player and board[118] == player) or \
            (board[115]== player and board[116] == player and board[117] == player and board[118] == player and board[119] == player) or \
            (board[116]== player and board[117] == player and board[118] == player and board[119] == player and board[120] == player) or \
            (board[121]== player and board[122] == player and board[123] == player and board[124] == player and board[125] == player) or \
            (board[122]== player and board[123] == player and board[124] == player and board[125] == player and board[126] == player) or \
            (board[123]== player and board[124] == player and board[125] == player and board[126] == player and board[127] == player) or \
            (board[124]== player and board[125] == player and board[126] == player and board[127] == player and board[128] == player) or \
            (board[125]== player and board[126] == player and board[127] == player and board[128] == player and board[129] == player) or \
            (board[126]== player and board[127] == player and board[128] == player and board[129] == player and board[130] == player) or \
            (board[127]== player and board[128] == player and board[129] == player and board[130] == player and board[131] == player) or \
            (board[128]== player and board[129] == player and board[130] == player and board[131] == player and board[132] == player) or \
            (board[129]== player and board[130] == player and board[131] == player and board[132] == player and board[133] == player) or \
            (board[130]== player and board[131] == player and board[132] == player and board[133] == player and board[134] == player) or \
            (board[131]== player and board[132] == player and board[133] == player and board[134] == player and board[135] == player) or \
            (board[136]== player and board[137] == player and board[138] == player and board[139] == player and board[140] == player) or \
            (board[137]== player and board[138] == player and board[139] == player and board[140] == player and board[141] == player) or \
            (board[138]== player and board[139] == player and board[140] == player and board[141] == player and board[142] == player) or \
            (board[139]== player and board[140] == player and board[141] == player and board[142] == player and board[143] == player) or \
            (board[140]== player and board[141] == player and board[142] == player and board[143] == player and board[144] == player) or \
            (board[141]== player and board[142] == player and board[143] == player and board[144] == player and board[145] == player) or \
            (board[142]== player and board[143] == player and board[144] == player and board[145] == player and board[146] == player) or \
            (board[143]== player and board[144] == player and board[145] == player and board[146] == player and board[147] == player) or \
            (board[144]== player and board[145] == player and board[146] == player and board[147] == player and board[148] == player) or \
            (board[145]== player and board[146] == player and board[147] == player and board[148] == player and board[149] == player) or \
            (board[146]== player and board[147] == player and board[148] == player and board[149] == player and board[150] == player) or \
            (board[151]== player and board[152] == player and board[153] == player and board[154] == player and board[155] == player) or \
            (board[152]== player and board[153] == player and board[154] == player and board[155] == player and board[156] == player) or \
            (board[153]== player and board[154] == player and board[155] == player and board[156] == player and board[157] == player) or \
            (board[154]== player and board[155] == player and board[156] == player and board[157] == player and board[158] == player) or \
            (board[155]== player and board[156] == player and board[157] == player and board[158] == player and board[159] == player) or \
            (board[156]== player and board[157] == player and board[158] == player and board[159] == player and board[160] == player) or \
            (board[157]== player and board[158] == player and board[159] == player and board[160] == player and board[161] == player) or \
            (board[158]== player and board[159] == player and board[160] == player and board[161] == player and board[162] == player) or \
            (board[159]== player and board[160] == player and board[161] == player and board[162] == player and board[163] == player) or \
            (board[160]== player and board[161] == player and board[162] == player and board[163] == player and board[164] == player) or \
            (board[161]== player and board[162] == player and board[163] == player and board[164] == player and board[165] == player) or \
            (board[166]== player and board[167] == player and board[168] == player and board[169] == player and board[170] == player) or \
            (board[167]== player and board[168] == player and board[169] == player and board[170] == player and board[171] == player) or \
            (board[168]== player and board[169] == player and board[170] == player and board[171] == player and board[172] == player) or \
            (board[169]== player and board[170] == player and board[171] == player and board[172] == player and board[173] == player) or \
            (board[170]== player and board[171] == player and board[172] == player and board[173] == player and board[174] == player) or \
            (board[171]== player and board[172] == player and board[173] == player and board[174] == player and board[175] == player) or \
            (board[172]== player and board[173] == player and board[174] == player and board[175] == player and board[176] == player) or \
            (board[173]== player and board[174] == player and board[175] == player and board[176] == player and board[177] == player) or \
            (board[174]== player and board[175] == player and board[176] == player and board[177] == player and board[178] == player) or \
            (board[175]== player and board[176] == player and board[177] == player and board[178] == player and board[179] == player) or \
            (board[176]== player and board[177] == player and board[178] == player and board[179] == player and board[180] == player) or \
            (board[181]== player and board[182] == player and board[183] == player and board[184] == player and board[185] == player) or \
            (board[182]== player and board[183] == player and board[184] == player and board[185] == player and board[186] == player) or \
            (board[183]== player and board[184] == player and board[185] == player and board[186] == player and board[187] == player) or \
            (board[184]== player and board[185] == player and board[186] == player and board[187] == player and board[188] == player) or \
            (board[185]== player and board[186] == player and board[187] == player and board[188] == player and board[189] == player) or \
            (board[186]== player and board[187] == player and board[188] == player and board[189] == player and board[190] == player) or \
            (board[187]== player and board[188] == player and board[189] == player and board[190] == player and board[191] == player) or \
            (board[188]== player and board[189] == player and board[190] == player and board[191] == player and board[192] == player) or \
            (board[189]== player and board[190] == player and board[191] == player and board[192] == player and board[193] == player) or \
            (board[190]== player and board[191] == player and board[192] == player and board[193] == player and board[194] == player) or \
            (board[191]== player and board[192] == player and board[193] == player and board[194] == player and board[195] == player) or \
            (board[196]== player and board[197] == player and board[198] == player and board[199] == player and board[200] == player) or \
            (board[197]== player and board[198] == player and board[199] == player and board[200] == player and board[201] == player) or \
            (board[198]== player and board[199] == player and board[200] == player and board[201] == player and board[202] == player) or \
            (board[199]== player and board[200] == player and board[201] == player and board[202] == player and board[203] == player) or \
            (board[200]== player and board[201] == player and board[202] == player and board[203] == player and board[204] == player) or \
            (board[201]== player and board[202] == player and board[203] == player and board[204] == player and board[205] == player) or \
            (board[202]== player and board[203] == player and board[204] == player and board[205] == player and board[206] == player) or \
            (board[203]== player and board[204] == player and board[205] == player and board[206] == player and board[207] == player) or \
            (board[204]== player and board[205] == player and board[206] == player and board[207] == player and board[208] == player) or \
            (board[205]== player and board[206] == player and board[207] == player and board[208] == player and board[209] == player) or \
            (board[206]== player and board[207] == player and board[208] == player and board[209] == player and board[210] == player) or \
            (board[211]== player and board[212] == player and board[213] == player and board[214] == player and board[215] == player) or \
            (board[212]== player and board[213] == player and board[214] == player and board[215] == player and board[216] == player) or \
            (board[213]== player and board[214] == player and board[215] == player and board[216] == player and board[217] == player) or \
            (board[214]== player and board[215] == player and board[216] == player and board[217] == player and board[218] == player) or \
            (board[215]== player and board[216] == player and board[217] == player and board[218] == player and board[219] == player) or \
            (board[216]== player and board[217] == player and board[218] == player and board[219] == player and board[220] == player) or \
            (board[217]== player and board[218] == player and board[219] == player and board[220] == player and board[221] == player) or \
            (board[218]== player and board[219] == player and board[220] == player and board[221] == player and board[222] == player) or \
            (board[219]== player and board[220] == player and board[221] == player and board[222] == player and board[223] == player) or \
            (board[220]== player and board[221] == player and board[222] == player and board[223] == player and board[224] == player) or \
            (board[221]== player and board[222] == player and board[223] == player and board[224] == player and board[225] == player) or \
            (board[1]== player and board[16] == player and board[31] == player and board[46] == player and board[61] == player) or \
            (board[16]== player and board[31] == player and board[46] == player and board[61] == player and board[76] == player) or \
            (board[31]== player and board[46] == player and board[61] == player and board[76] == player and board[91] == player) or \
            (board[46]== player and board[61] == player and board[76] == player and board[91] == player and board[106] == player) or \
            (board[61]== player and board[76] == player and board[91] == player and board[106] == player and board[121] == player) or \
            (board[76]== player and board[91] == player and board[106] == player and board[121] == player and board[136] == player) or \
            (board[91]== player and board[106] == player and board[121] == player and board[136] == player and board[151] == player) or \
            (board[106]== player and board[121] == player and board[136] == player and board[151] == player and board[166] == player) or \
            (board[121]== player and board[136] == player and board[151] == player and board[166] == player and board[181] == player) or \
            (board[136]== player and board[151] == player and board[166] == player and board[181] == player and board[196] == player) or \
            (board[151]== player and board[166] == player and board[181] == player and board[196] == player and board[211] == player) or \
            (board[2]== player and board[17] == player and board[32] == player and board[47] == player and board[62] == player) or \
            (board[17]== player and board[32] == player and board[47] == player and board[62] == player and board[77] == player) or \
            (board[32]== player and board[47] == player and board[62] == player and board[77] == player and board[92] == player) or \
            (board[47]== player and board[62] == player and board[77] == player and board[92] == player and board[107] == player) or \
            (board[62]== player and board[77] == player and board[92] == player and board[107] == player and board[122] == player) or \
            (board[77]== player and board[92] == player and board[107] == player and board[122] == player and board[137] == player) or \
            (board[92]== player and board[107] == player and board[122] == player and board[137] == player and board[152] == player) or \
            (board[107]== player and board[122] == player and board[137] == player and board[152] == player and board[167] == player) or \
            (board[122]== player and board[137] == player and board[152] == player and board[167] == player and board[182] == player) or \
            (board[137]== player and board[152] == player and board[167] == player and board[182] == player and board[197] == player) or \
            (board[152]== player and board[167] == player and board[182] == player and board[197] == player and board[212] == player) or \
            (board[3]== player and board[18] == player and board[33] == player and board[48] == player and board[63] == player) or \
            (board[18]== player and board[33] == player and board[48] == player and board[63] == player and board[78] == player) or \
            (board[33]== player and board[48] == player and board[63] == player and board[78] == player and board[93] == player) or \
            (board[48]== player and board[63] == player and board[78] == player and board[93] == player and board[108] == player) or \
            (board[63]== player and board[78] == player and board[93] == player and board[108] == player and board[123] == player) or \
            (board[78]== player and board[93] == player and board[108] == player and board[123] == player and board[138] == player) or \
            (board[93]== player and board[108] == player and board[123] == player and board[138] == player and board[153] == player) or \
            (board[108]== player and board[123] == player and board[138] == player and board[153] == player and board[168] == player) or \
            (board[123]== player and board[138] == player and board[153] == player and board[168] == player and board[183] == player) or \
            (board[138]== player and board[153] == player and board[168] == player and board[183] == player and board[198] == player) or \
            (board[153]== player and board[168] == player and board[183] == player and board[198] == player and board[213] == player) or \
            (board[4]== player and board[19] == player and board[34] == player and board[49] == player and board[64] == player) or \
            (board[19]== player and board[34] == player and board[49] == player and board[64] == player and board[79] == player) or \
            (board[34]== player and board[49] == player and board[64] == player and board[79] == player and board[94] == player) or \
            (board[49]== player and board[64] == player and board[79] == player and board[94] == player and board[109] == player) or \
            (board[64]== player and board[79] == player and board[94] == player and board[109] == player and board[124] == player) or \
            (board[79]== player and board[94] == player and board[109] == player and board[124] == player and board[139] == player) or \
            (board[94]== player and board[109] == player and board[124] == player and board[139] == player and board[154] == player) or \
            (board[109]== player and board[124] == player and board[139] == player and board[154] == player and board[169] == player) or \
            (board[124]== player and board[139] == player and board[154] == player and board[169] == player and board[184] == player) or \
            (board[139]== player and board[154] == player and board[169] == player and board[184] == player and board[199] == player) or \
            (board[154]== player and board[169] == player and board[184] == player and board[199] == player and board[214] == player) or \
            (board[5]== player and board[20] == player and board[35] == player and board[50] == player and board[65] == player) or \
            (board[20]== player and board[35] == player and board[50] == player and board[65] == player and board[80] == player) or \
            (board[35]== player and board[50] == player and board[65] == player and board[80] == player and board[95] == player) or \
            (board[50]== player and board[65] == player and board[80] == player and board[95] == player and board[110] == player) or \
            (board[65]== player and board[80] == player and board[95] == player and board[110] == player and board[125] == player) or \
            (board[80]== player and board[95] == player and board[110] == player and board[125] == player and board[140] == player) or \
            (board[95]== player and board[110] == player and board[125] == player and board[140] == player and board[155] == player) or \
            (board[110]== player and board[125] == player and board[140] == player and board[155] == player and board[170] == player) or \
            (board[125]== player and board[140] == player and board[155] == player and board[170] == player and board[185] == player) or \
            (board[140]== player and board[155] == player and board[170] == player and board[185] == player and board[200] == player) or \
            (board[155]== player and board[170] == player and board[185] == player and board[200] == player and board[215] == player) or \
            (board[6]== player and board[21] == player and board[36] == player and board[51] == player and board[66] == player) or \
            (board[21]== player and board[36] == player and board[51] == player and board[66] == player and board[81] == player) or \
            (board[36]== player and board[51] == player and board[66] == player and board[81] == player and board[96] == player) or \
            (board[51]== player and board[66] == player and board[81] == player and board[96] == player and board[111] == player) or \
            (board[66]== player and board[81] == player and board[96] == player and board[111] == player and board[126] == player) or \
            (board[81]== player and board[96] == player and board[111] == player and board[126] == player and board[141] == player) or \
            (board[96]== player and board[111] == player and board[126] == player and board[141] == player and board[156] == player) or \
            (board[111]== player and board[126] == player and board[141] == player and board[156] == player and board[171] == player) or \
            (board[126]== player and board[141] == player and board[156] == player and board[171] == player and board[186] == player) or \
            (board[141]== player and board[156] == player and board[171] == player and board[186] == player and board[201] == player) or \
            (board[156]== player and board[171] == player and board[186] == player and board[201] == player and board[216] == player) or \
            (board[7]== player and board[22] == player and board[37] == player and board[52] == player and board[67] == player) or \
            (board[22]== player and board[37] == player and board[52] == player and board[67] == player and board[82] == player) or \
            (board[37]== player and board[52] == player and board[67] == player and board[82] == player and board[97] == player) or \
            (board[52]== player and board[67] == player and board[82] == player and board[97] == player and board[112] == player) or \
            (board[67]== player and board[82] == player and board[97] == player and board[112] == player and board[127] == player) or \
            (board[82]== player and board[97] == player and board[112] == player and board[127] == player and board[142] == player) or \
            (board[97]== player and board[112] == player and board[127] == player and board[142] == player and board[157] == player) or \
            (board[112]== player and board[127] == player and board[142] == player and board[157] == player and board[172] == player) or \
            (board[127]== player and board[142] == player and board[157] == player and board[172] == player and board[187] == player) or \
            (board[142]== player and board[157] == player and board[172] == player and board[187] == player and board[202] == player) or \
            (board[157]== player and board[172] == player and board[187] == player and board[202] == player and board[217] == player) or \
            (board[8]== player and board[23] == player and board[38] == player and board[53] == player and board[68] == player) or \
            (board[23]== player and board[38] == player and board[53] == player and board[68] == player and board[83] == player) or \
            (board[38]== player and board[53] == player and board[68] == player and board[83] == player and board[98] == player) or \
            (board[53]== player and board[68] == player and board[83] == player and board[98] == player and board[113] == player) or \
            (board[68]== player and board[83] == player and board[98] == player and board[113] == player and board[128] == player) or \
            (board[83]== player and board[98] == player and board[113] == player and board[128] == player and board[143] == player) or \
            (board[98]== player and board[113] == player and board[128] == player and board[143] == player and board[158] == player) or \
            (board[113]== player and board[128] == player and board[143] == player and board[158] == player and board[173] == player) or \
            (board[128]== player and board[143] == player and board[158] == player and board[173] == player and board[188] == player) or \
            (board[143]== player and board[158] == player and board[173] == player and board[188] == player and board[203] == player) or \
            (board[158]== player and board[173] == player and board[188] == player and board[203] == player and board[218] == player) or \
            (board[9]== player and board[24] == player and board[39] == player and board[54] == player and board[69] == player) or \
            (board[24]== player and board[39] == player and board[54] == player and board[69] == player and board[84] == player) or \
            (board[39]== player and board[54] == player and board[69] == player and board[84] == player and board[99] == player) or \
            (board[54]== player and board[69] == player and board[84] == player and board[99] == player and board[114] == player) or \
            (board[69]== player and board[84] == player and board[99] == player and board[114] == player and board[129] == player) or \
            (board[84]== player and board[99] == player and board[114] == player and board[129] == player and board[144] == player) or \
            (board[99]== player and board[114] == player and board[129] == player and board[144] == player and board[159] == player) or \
            (board[114]== player and board[129] == player and board[144] == player and board[159] == player and board[174] == player) or \
            (board[129]== player and board[144] == player and board[159] == player and board[174] == player and board[189] == player) or \
            (board[144]== player and board[159] == player and board[174] == player and board[189] == player and board[204] == player) or \
            (board[159]== player and board[174] == player and board[189] == player and board[204] == player and board[219] == player) or \
            (board[10]== player and board[25] == player and board[40] == player and board[55] == player and board[70] == player) or \
            (board[25]== player and board[40] == player and board[55] == player and board[70] == player and board[85] == player) or \
            (board[40]== player and board[55] == player and board[70] == player and board[85] == player and board[100] == player) or \
            (board[55]== player and board[70] == player and board[85] == player and board[100] == player and board[115] == player) or \
            (board[70]== player and board[85] == player and board[100] == player and board[115] == player and board[130] == player) or \
            (board[85]== player and board[100] == player and board[115] == player and board[130] == player and board[145] == player) or \
            (board[100]== player and board[115] == player and board[130] == player and board[145] == player and board[160] == player) or \
            (board[115]== player and board[130] == player and board[145] == player and board[160] == player and board[175] == player) or \
            (board[130]== player and board[145] == player and board[160] == player and board[175] == player and board[190] == player) or \
            (board[145]== player and board[160] == player and board[175] == player and board[190] == player and board[205] == player) or \
            (board[160]== player and board[175] == player and board[190] == player and board[205] == player and board[220] == player) or \
            (board[11]== player and board[26] == player and board[41] == player and board[56] == player and board[71] == player) or \
            (board[26]== player and board[41] == player and board[56] == player and board[71] == player and board[86] == player) or \
            (board[41]== player and board[56] == player and board[71] == player and board[86] == player and board[101] == player) or \
            (board[56]== player and board[71] == player and board[86] == player and board[101] == player and board[116] == player) or \
            (board[71]== player and board[86] == player and board[101] == player and board[116] == player and board[131] == player) or \
            (board[86]== player and board[101] == player and board[116] == player and board[131] == player and board[146] == player) or \
            (board[101]== player and board[116] == player and board[131] == player and board[146] == player and board[161] == player) or \
            (board[116]== player and board[131] == player and board[146] == player and board[161] == player and board[176] == player) or \
            (board[131]== player and board[146] == player and board[161] == player and board[176] == player and board[191] == player) or \
            (board[146]== player and board[161] == player and board[176] == player and board[191] == player and board[206] == player) or \
            (board[161]== player and board[176] == player and board[191] == player and board[206] == player and board[221] == player) or \
            (board[12]== player and board[27] == player and board[42] == player and board[57] == player and board[72] == player) or \
            (board[27]== player and board[42] == player and board[57] == player and board[72] == player and board[87] == player) or \
            (board[42]== player and board[57] == player and board[72] == player and board[87] == player and board[102] == player) or \
            (board[57]== player and board[72] == player and board[87] == player and board[102] == player and board[117] == player) or \
            (board[72]== player and board[87] == player and board[102] == player and board[117] == player and board[132] == player) or \
            (board[87]== player and board[102] == player and board[117] == player and board[132] == player and board[147] == player) or \
            (board[102]== player and board[117] == player and board[132] == player and board[147] == player and board[162] == player) or \
            (board[117]== player and board[132] == player and board[147] == player and board[162] == player and board[177] == player) or \
            (board[132]== player and board[147] == player and board[162] == player and board[177] == player and board[192] == player) or \
            (board[147]== player and board[162] == player and board[177] == player and board[192] == player and board[207] == player) or \
            (board[162]== player and board[177] == player and board[192] == player and board[207] == player and board[222] == player) or \
            (board[13]== player and board[28] == player and board[43] == player and board[58] == player and board[73] == player) or \
            (board[28]== player and board[43] == player and board[58] == player and board[73] == player and board[88] == player) or \
            (board[43]== player and board[58] == player and board[73] == player and board[88] == player and board[103] == player) or \
            (board[58]== player and board[73] == player and board[88] == player and board[103] == player and board[118] == player) or \
            (board[73]== player and board[88] == player and board[103] == player and board[118] == player and board[133] == player) or \
            (board[88]== player and board[103] == player and board[118] == player and board[133] == player and board[148] == player) or \
            (board[103]== player and board[118] == player and board[133] == player and board[148] == player and board[163] == player) or \
            (board[118]== player and board[133] == player and board[148] == player and board[163] == player and board[178] == player) or \
            (board[133]== player and board[148] == player and board[163] == player and board[178] == player and board[193] == player) or \
            (board[148]== player and board[163] == player and board[178] == player and board[193] == player and board[208] == player) or \
            (board[163]== player and board[178] == player and board[193] == player and board[208] == player and board[223] == player) or \
            (board[14]== player and board[29] == player and board[44] == player and board[59] == player and board[74] == player) or \
            (board[29]== player and board[44] == player and board[59] == player and board[74] == player and board[89] == player) or \
            (board[44]== player and board[59] == player and board[74] == player and board[89] == player and board[104] == player) or \
            (board[59]== player and board[74] == player and board[89] == player and board[104] == player and board[119] == player) or \
            (board[74]== player and board[89] == player and board[104] == player and board[119] == player and board[134] == player) or \
            (board[89]== player and board[104] == player and board[119] == player and board[134] == player and board[149] == player) or \
            (board[104]== player and board[119] == player and board[134] == player and board[149] == player and board[164] == player) or \
            (board[119]== player and board[134] == player and board[149] == player and board[164] == player and board[179] == player) or \
            (board[134]== player and board[149] == player and board[164] == player and board[179] == player and board[194] == player) or \
            (board[149]== player and board[164] == player and board[179] == player and board[194] == player and board[209] == player) or \
            (board[164]== player and board[179] == player and board[194] == player and board[209] == player and board[224] == player) or \
            (board[15]== player and board[30] == player and board[45] == player and board[60] == player and board[75] == player) or \
            (board[30]== player and board[45] == player and board[60] == player and board[75] == player and board[90] == player) or \
            (board[45]== player and board[60] == player and board[75] == player and board[90] == player and board[105] == player) or \
            (board[60]== player and board[75] == player and board[90] == player and board[105] == player and board[120] == player) or \
            (board[75]== player and board[90] == player and board[105] == player and board[120] == player and board[135] == player) or \
            (board[90]== player and board[105] == player and board[120] == player and board[135] == player and board[150] == player) or \
            (board[105]== player and board[120] == player and board[135] == player and board[150] == player and board[165] == player) or \
            (board[120]== player and board[135] == player and board[150] == player and board[165] == player and board[180] == player) or \
            (board[135]== player and board[150] == player and board[165] == player and board[180] == player and board[195] == player) or \
            (board[150]== player and board[165] == player and board[180] == player and board[195] == player and board[210] == player) or \
            (board[165]== player and board[180] == player and board[195] == player and board[210] == player and board[222] == player) or \
            (board[1]== player and board[17] == player and board[33] == player and board[49] == player and board[65] == player) or \
            (board[17]== player and board[33] == player and board[49] == player and board[65] == player and board[81] == player) or \
            (board[33]== player and board[49] == player and board[65] == player and board[81] == player and board[97] == player) or \
            (board[49]== player and board[65] == player and board[81] == player and board[97] == player and board[113] == player) or \
            (board[65]== player and board[81] == player and board[97] == player and board[113] == player and board[129] == player) or \
            (board[81]== player and board[97] == player and board[113] == player and board[129] == player and board[145] == player) or \
            (board[97]== player and board[113] == player and board[129] == player and board[145] == player and board[161] == player) or \
            (board[113]== player and board[129] == player and board[145] == player and board[161] == player and board[177] == player) or \
            (board[129]== player and board[145] == player and board[161] == player and board[177] == player and board[193] == player) or \
            (board[145]== player and board[161] == player and board[177] == player and board[193] == player and board[209] == player) or \
            (board[161]== player and board[177] == player and board[193] == player and board[209] == player and board[225] == player)or \
            (board[16]== player and board[32] == player and board[48] == player and board[64] == player and board[80] == player) or \
            (board[32]== player and board[48] == player and board[64] == player and board[80] == player and board[96] == player) or \
            (board[48]== player and board[64] == player and board[80] == player and board[96] == player and board[112] == player) or \
            (board[64]== player and board[80] == player and board[96] == player and board[112] == player and board[128] == player) or \
            (board[80]== player and board[96] == player and board[112] == player and board[128] == player and board[144] == player) or \
            (board[96]== player and board[112] == player and board[128] == player and board[144] == player and board[160] == player) or \
            (board[112]== player and board[128] == player and board[144] == player and board[160] == player and board[176] == player) or \
            (board[128]== player and board[144] == player and board[160] == player and board[176] == player and board[192] == player) or \
            (board[144]== player and board[160] == player and board[176] == player and board[192] == player and board[208] == player) or \
            (board[160]== player and board[176] == player and board[192] == player and board[208] == player and board[224] == player)or \
            (board[31]== player and board[47] == player and board[63] == player and board[79] == player and board[95] == player) or \
            (board[47]== player and board[63] == player and board[79] == player and board[95] == player and board[111] == player) or \
            (board[63]== player and board[79] == player and board[95] == player and board[111] == player and board[127] == player) or \
            (board[79]== player and board[95] == player and board[111] == player and board[127] == player and board[143] == player) or \
            (board[95]== player and board[111] == player and board[127] == player and board[143] == player and board[159] == player) or \
            (board[111]== player and board[127] == player and board[143] == player and board[159] == player and board[175] == player) or \
            (board[127]== player and board[143] == player and board[159] == player and board[175] == player and board[191] == player) or \
            (board[143]== player and board[159] == player and board[175] == player and board[191] == player and board[207] == player) or \
            (board[159]== player and board[175] == player and board[191] == player and board[207] == player and board[223] == player) or \
            (board[46]== player and board[62] == player and board[78] == player and board[94] == player and board[110] == player) or \
            (board[62]== player and board[78] == player and board[94] == player and board[110] == player and board[126] == player) or \
            (board[78]== player and board[94] == player and board[110] == player and board[126] == player and board[142] == player) or \
            (board[94]== player and board[110] == player and board[126] == player and board[142] == player and board[158] == player) or \
            (board[110]== player and board[126] == player and board[142] == player and board[158] == player and board[174] == player) or \
            (board[126]== player and board[142] == player and board[158] == player and board[174] == player and board[190] == player) or \
            (board[142]== player and board[158] == player and board[174] == player and board[190] == player and board[206] == player) or \
            (board[158]== player and board[174] == player and board[190] == player and board[206] == player and board[222] == player) or \
            (board[61]== player and board[77] == player and board[93] == player and board[109] == player and board[125] == player) or \
            (board[77]== player and board[93] == player and board[109] == player and board[125] == player and board[141] == player) or \
            (board[93]== player and board[109] == player and board[125] == player and board[141] == player and board[157] == player) or \
            (board[109]== player and board[125] == player and board[141] == player and board[157] == player and board[173] == player) or \
            (board[125]== player and board[141] == player and board[157] == player and board[173] == player and board[189] == player) or \
            (board[141]== player and board[157] == player and board[173] == player and board[189] == player and board[205] == player) or \
            (board[157]== player and board[173] == player and board[189] == player and board[205] == player and board[221] == player) or \
            (board[76]== player and board[92] == player and board[108] == player and board[124] == player and board[140] == player) or \
            (board[92]== player and board[108] == player and board[124] == player and board[140] == player and board[156] == player) or \
            (board[108]== player and board[124] == player and board[140] == player and board[156] == player and board[172] == player) or \
            (board[124]== player and board[140] == player and board[156] == player and board[172] == player and board[188] == player) or \
            (board[140]== player and board[156] == player and board[172] == player and board[188] == player and board[204] == player) or \
            (board[156]== player and board[172] == player and board[188] == player and board[204] == player and board[220] == player) or \
            (board[91]== player and board[107] == player and board[123] == player and board[139] == player and board[155] == player) or \
            (board[107]== player and board[123] == player and board[139] == player and board[155] == player and board[171] == player) or \
            (board[123]== player and board[139] == player and board[155] == player and board[171] == player and board[187] == player) or \
            (board[139]== player and board[155] == player and board[171] == player and board[187] == player and board[203] == player) or \
            (board[155]== player and board[171] == player and board[187] == player and board[203] == player and board[219] == player) or \
            (board[106]== player and board[122] == player and board[138] == player and board[154] == player and board[170] == player) or \
            (board[122]== player and board[138] == player and board[154] == player and board[170] == player and board[186] == player) or \
            (board[138]== player and board[154] == player and board[170] == player and board[186] == player and board[202] == player) or \
            (board[154]== player and board[170] == player and board[186] == player and board[202] == player and board[218] == player) or \
            (board[121]== player and board[137] == player and board[153] == player and board[169] == player and board[185] == player) or \
            (board[137]== player and board[153] == player and board[169] == player and board[185] == player and board[201] == player) or \
            (board[153]== player and board[169] == player and board[185] == player and board[201] == player and board[217] == player) or \
            (board[136]== player and board[152] == player and board[168] == player and board[184] == player and board[200] == player) or \
            (board[152]== player and board[168] == player and board[184] == player and board[200] == player and board[216] == player) or \
            (board[151]== player and board[167] == player and board[183] == player and board[199] == player and board[215] == player) or\
            (board[2]== player and board[18] == player and board[34] == player and board[50] == player and board[66] == player) or \
            (board[18]== player and board[34] == player and board[50] == player and board[66] == player and board[82] == player) or \
            (board[34]== player and board[50] == player and board[66] == player and board[82] == player and board[98] == player) or \
            (board[50]== player and board[66] == player and board[82] == player and board[98] == player and board[114] == player) or \
            (board[66]== player and board[82] == player and board[98] == player and board[114] == player and board[130] == player) or \
            (board[82]== player and board[98] == player and board[114] == player and board[130] == player and board[146] == player) or \
            (board[98]== player and board[114] == player and board[130] == player and board[144] == player and board[162] == player) or \
            (board[114]== player and board[130] == player and board[146] == player and board[162] == player and board[178] == player) or \
            (board[130]== player and board[146] == player and board[162] == player and board[178] == player and board[194] == player) or \
            (board[146]== player and board[162] == player and board[178] == player and board[194] == player and board[210] == player) or \
            (board[3]== player and board[19] == player and board[35] == player and board[51] == player and board[67] == player) or \
            (board[19]== player and board[35] == player and board[51] == player and board[67] == player and board[83] == player) or \
            (board[35]== player and board[51] == player and board[67] == player and board[83] == player and board[99] == player) or \
            (board[51]== player and board[67] == player and board[83] == player and board[99] == player and board[115] == player) or \
            (board[67]== player and board[83] == player and board[99] == player and board[115] == player and board[131] == player) or \
            (board[83]== player and board[99] == player and board[115] == player and board[131] == player and board[147] == player) or \
            (board[99]== player and board[115] == player and board[131] == player and board[145] == player and board[163] == player) or \
            (board[115]== player and board[131] == player and board[147] == player and board[163] == player and board[179] == player) or \
            (board[131]== player and board[147] == player and board[163] == player and board[179] == player and board[195] == player) or \
            (board[4]== player and board[20] == player and board[36] == player and board[52] == player and board[68] == player) or \
            (board[20]== player and board[36] == player and board[52] == player and board[68] == player and board[84] == player) or \
            (board[36]== player and board[52] == player and board[68] == player and board[84] == player and board[100] == player) or \
            (board[52]== player and board[68] == player and board[84] == player and board[100] == player and board[116] == player) or \
            (board[68]== player and board[84] == player and board[100] == player and board[116] == player and board[132] == player) or \
            (board[84]== player and board[100] == player and board[116] == player and board[132] == player and board[148] == player) or \
            (board[100]== player and board[116] == player and board[132] == player and board[146] == player and board[164] == player) or \
            (board[116]== player and board[132] == player and board[148] == player and board[164] == player and board[180] == player) or \
            (board[5]== player and board[21] == player and board[37] == player and board[53] == player and board[69] == player) or \
            (board[21]== player and board[37] == player and board[53] == player and board[69] == player and board[85] == player) or \
            (board[37]== player and board[53] == player and board[69] == player and board[85] == player and board[101] == player) or \
            (board[53]== player and board[69] == player and board[85] == player and board[101] == player and board[117] == player) or \
            (board[69]== player and board[85] == player and board[101] == player and board[117] == player and board[133] == player) or \
            (board[85]== player and board[101] == player and board[117] == player and board[133] == player and board[149] == player) or \
            (board[101]== player and board[117] == player and board[133] == player and board[147] == player and board[165] == player) or \
            (board[6]== player and board[22] == player and board[38] == player and board[54] == player and board[70] == player) or \
            (board[22]== player and board[38] == player and board[54] == player and board[70] == player and board[86] == player) or \
            (board[38]== player and board[54] == player and board[70] == player and board[86] == player and board[102] == player) or \
            (board[54]== player and board[70] == player and board[86] == player and board[102] == player and board[118] == player) or \
            (board[70]== player and board[86] == player and board[102] == player and board[118] == player and board[134] == player) or \
            (board[86]== player and board[102] == player and board[118] == player and board[134] == player and board[150] == player) or\
            (board[7]== player and board[23] == player and board[39] == player and board[55] == player and board[71] == player) or \
            (board[23]== player and board[39] == player and board[55] == player and board[71] == player and board[87] == player) or \
            (board[39]== player and board[55] == player and board[71] == player and board[87] == player and board[103] == player) or \
            (board[55]== player and board[71] == player and board[87] == player and board[103] == player and board[119] == player) or \
            (board[71]== player and board[87] == player and board[103] == player and board[119] == player and board[135] == player) or \
            (board[8]== player and board[24] == player and board[40] == player and board[56] == player and board[72] == player) or \
            (board[24]== player and board[40] == player and board[56] == player and board[72] == player and board[88] == player) or \
            (board[40]== player and board[56] == player and board[72] == player and board[88] == player and board[104] == player) or \
            (board[56]== player and board[72] == player and board[88] == player and board[104] == player and board[120] == player) or \
            (board[9]== player and board[25] == player and board[41] == player and board[57] == player and board[73] == player) or \
            (board[25]== player and board[41] == player and board[57] == player and board[73] == player and board[89] == player) or \
            (board[41]== player and board[57] == player and board[73] == player and board[89] == player and board[105] == player) or \
            (board[10]== player and board[26] == player and board[42] == player and board[58] == player and board[74] == player) or \
            (board[26]== player and board[42] == player and board[58] == player and board[74] == player and board[90] == player) or \
            (board[11]== player and board[27] == player and board[43] == player and board[59] == player and board[75] == player) or \
            (board[211]== player and board[197] == player and board[183] == player and board[169] == player and board[155] == player) or \
            (board[197]== player and board[183] == player and board[169] == player and board[155] == player and board[141] == player) or \
            (board[183]== player and board[169] == player and board[155] == player and board[141] == player and board[127] == player) or \
            (board[169]== player and board[155] == player and board[141] == player and board[127] == player and board[113] == player) or \
            (board[155]== player and board[141] == player and board[127] == player and board[113] == player and board[99] == player) or \
            (board[141]== player and board[127] == player and board[113] == player and board[99] == player and board[85] == player) or \
            (board[127]== player and board[113] == player and board[99] == player and board[85] == player and board[71] == player) or \
            (board[113]== player and board[99] == player and board[85] == player and board[71] == player and board[57] == player) or \
            (board[99]== player and board[85] == player and board[71] == player and board[57] == player and board[43] == player) or \
            (board[85]== player and board[71] == player and board[57] == player and board[43] == player and board[29] == player) or \
            (board[71]== player and board[57] == player and board[43] == player and board[29] == player and board[15] == player) or \
            (board[212]== player and board[198] == player and board[184] == player and board[170] == player and board[156] == player) or \
            (board[198]== player and board[184] == player and board[170] == player and board[156] == player and board[142] == player) or \
            (board[184]== player and board[170] == player and board[156] == player and board[142] == player and board[128] == player) or \
            (board[170]== player and board[156] == player and board[142] == player and board[128] == player and board[114] == player) or \
            (board[156]== player and board[142] == player and board[128] == player and board[114] == player and board[100] == player) or \
            (board[142]== player and board[128] == player and board[114] == player and board[100] == player and board[86] == player) or \
            (board[128]== player and board[114] == player and board[100] == player and board[86] == player and board[72] == player) or \
            (board[114]== player and board[100] == player and board[86] == player and board[72] == player and board[58] == player) or \
            (board[100]== player and board[86] == player and board[72] == player and board[58] == player and board[44] == player) or \
            (board[86]== player and board[72] == player and board[58] == player and board[44] == player and board[30] == player) or \
            (board[213]== player and board[199] == player and board[185] == player and board[171] == player and board[157] == player) or \
            (board[199]== player and board[185] == player and board[171] == player and board[157] == player and board[143] == player) or \
            (board[185]== player and board[171] == player and board[157] == player and board[143] == player and board[129] == player) or \
            (board[171]== player and board[157] == player and board[143] == player and board[129] == player and board[115] == player) or \
            (board[157]== player and board[143] == player and board[129] == player and board[115] == player and board[101] == player) or \
            (board[143]== player and board[129] == player and board[115] == player and board[101] == player and board[87] == player) or \
            (board[129]== player and board[115] == player and board[101] == player and board[87] == player and board[73] == player) or \
            (board[115]== player and board[101] == player and board[87] == player and board[73] == player and board[59] == player) or \
            (board[101]== player and board[87] == player and board[73] == player and board[59] == player and board[45] == player) or \
            (board[214]== player and board[200] == player and board[186] == player and board[172] == player and board[158] == player) or \
            (board[200]== player and board[186] == player and board[172] == player and board[158] == player and board[144] == player) or \
            (board[186]== player and board[172] == player and board[158] == player and board[144] == player and board[130] == player) or \
            (board[172]== player and board[158] == player and board[144] == player and board[130] == player and board[116] == player) or \
            (board[158]== player and board[144] == player and board[130] == player and board[116] == player and board[102] == player) or \
            (board[144]== player and board[130] == player and board[116] == player and board[102] == player and board[88] == player) or \
            (board[130]== player and board[116] == player and board[102] == player and board[88] == player and board[74] == player) or \
            (board[116]== player and board[102] == player and board[88] == player and board[74] == player and board[60] == player) or \
            (board[215]== player and board[201] == player and board[187] == player and board[173] == player and board[159] == player) or \
            (board[201]== player and board[187] == player and board[173] == player and board[159] == player and board[145] == player) or \
            (board[187]== player and board[173] == player and board[159] == player and board[145] == player and board[131] == player) or \
            (board[173]== player and board[159] == player and board[145] == player and board[131] == player and board[117] == player) or \
            (board[159]== player and board[145] == player and board[131] == player and board[117] == player and board[103] == player) or \
            (board[145]== player and board[131] == player and board[117] == player and board[103] == player and board[89] == player) or \
            (board[131]== player and board[117] == player and board[103] == player and board[89] == player and board[75] == player) or \
            (board[216]== player and board[202] == player and board[188] == player and board[174] == player and board[160] == player) or \
            (board[202]== player and board[188] == player and board[174] == player and board[160] == player and board[146] == player) or \
            (board[188]== player and board[174] == player and board[160] == player and board[146] == player and board[132] == player) or \
            (board[174]== player and board[160] == player and board[146] == player and board[132] == player and board[118] == player) or \
            (board[160]== player and board[146] == player and board[132] == player and board[118] == player and board[104] == player) or \
            (board[146]== player and board[132] == player and board[118] == player and board[104] == player and board[90] == player) or \
            (board[217]== player and board[203] == player and board[189] == player and board[175] == player and board[161] == player) or \
            (board[203]== player and board[189] == player and board[175] == player and board[161] == player and board[147] == player) or \
            (board[189]== player and board[175] == player and board[161] == player and board[147] == player and board[133] == player) or \
            (board[175]== player and board[161] == player and board[147] == player and board[133] == player and board[119] == player) or \
            (board[161]== player and board[147] == player and board[133] == player and board[119] == player and board[105] == player) or \
            (board[218]== player and board[204] == player and board[190] == player and board[176] == player and board[162] == player) or \
            (board[204]== player and board[190] == player and board[176] == player and board[162] == player and board[148] == player) or \
            (board[190]== player and board[176] == player and board[162] == player and board[148] == player and board[134] == player) or \
            (board[176]== player and board[162] == player and board[148] == player and board[134] == player and board[120] == player) or \
            (board[219]== player and board[205] == player and board[191] == player and board[177] == player and board[163] == player) or \
            (board[204]== player and board[191] == player and board[177] == player and board[163] == player and board[149] == player) or \
            (board[191]== player and board[177] == player and board[163] == player and board[149] == player and board[135] == player) or \
            (board[220]== player and board[206] == player and board[192] == player and board[178] == player and board[164] == player) or \
            (board[205]== player and board[192] == player and board[178] == player and board[164] == player and board[150] == player) or \
            (board[221]== player and board[207] == player and board[193] == player and board[179] == player and board[165] == player) or\
            (board[196]== player and board[182] == player and board[168] == player and board[154] == player and board[140] == player) or \
            (board[182]== player and board[168] == player and board[154] == player and board[140] == player and board[126] == player) or \
            (board[168]== player and board[154] == player and board[140] == player and board[126] == player and board[112] == player) or \
            (board[154]== player and board[140] == player and board[126] == player and board[112] == player and board[98] == player) or \
            (board[140]== player and board[126] == player and board[112] == player and board[98] == player and board[84] == player) or \
            (board[126]== player and board[112] == player and board[98] == player and board[84] == player and board[70] == player) or \
            (board[112]== player and board[98] == player and board[84] == player and board[70] == player and board[56] == player) or \
            (board[98]== player and board[84] == player and board[70] == player and board[56] == player and board[42] == player) or \
            (board[84]== player and board[70] == player and board[56] == player and board[42] == player and board[28] == player) or \
            (board[70]== player and board[56] == player and board[42] == player and board[28] == player and board[14] == player) or \
            (board[181]== player and board[167] == player and board[153] == player and board[139] == player and board[125] == player) or \
            (board[167]== player and board[153] == player and board[139] == player and board[125] == player and board[111] == player) or \
            (board[153]== player and board[139] == player and board[125] == player and board[111] == player and board[97] == player) or \
            (board[139]== player and board[125] == player and board[111] == player and board[97] == player and board[83] == player) or \
            (board[125]== player and board[111] == player and board[97] == player and board[83] == player and board[69] == player) or \
            (board[111]== player and board[97] == player and board[83] == player and board[69] == player and board[55] == player) or \
            (board[97]== player and board[83] == player and board[69] == player and board[55] == player and board[41] == player) or \
            (board[83]== player and board[69] == player and board[55] == player and board[41] == player and board[27] == player) or \
            (board[69]== player and board[55] == player and board[41] == player and board[27] == player and board[13] == player) or \
            (board[166]== player and board[152] == player and board[138] == player and board[124] == player and board[110] == player) or \
            (board[152]== player and board[138] == player and board[124] == player and board[110] == player and board[96] == player) or \
            (board[138]== player and board[124] == player and board[110] == player and board[96] == player and board[82] == player) or \
            (board[124]== player and board[110] == player and board[96] == player and board[82] == player and board[68] == player) or \
            (board[110]== player and board[96] == player and board[82] == player and board[68] == player and board[54] == player) or \
            (board[96]== player and board[82] == player and board[68] == player and board[54] == player and board[40] == player) or \
            (board[82]== player and board[68] == player and board[54] == player and board[40] == player and board[26] == player) or \
            (board[68]== player and board[54] == player and board[40] == player and board[26] == player and board[12] == player) or \
            (board[151]== player and board[137] == player and board[123] == player and board[109] == player and board[95] == player) or \
            (board[137]== player and board[123] == player and board[109] == player and board[95] == player and board[81] == player) or \
            (board[123]== player and board[109] == player and board[95] == player and board[81] == player and board[67] == player) or \
            (board[109]== player and board[95] == player and board[81] == player and board[67] == player and board[53] == player) or \
            (board[95]== player and board[81] == player and board[67] == player and board[53] == player and board[39] == player) or \
            (board[81]== player and board[67] == player and board[53] == player and board[39] == player and board[25] == player) or \
            (board[67]== player and board[53] == player and board[39] == player and board[25] == player and board[11] == player) or \
            (board[136]== player and board[122] == player and board[108] == player and board[94] == player and board[80] == player) or \
            (board[122]== player and board[108] == player and board[94] == player and board[80] == player and board[66] == player) or \
            (board[108]== player and board[94] == player and board[80] == player and board[66] == player and board[52] == player) or \
            (board[94]== player and board[80] == player and board[66] == player and board[52] == player and board[38] == player) or \
            (board[80]== player and board[66] == player and board[52] == player and board[38] == player and board[24] == player) or \
            (board[66]== player and board[52] == player and board[38] == player and board[24] == player and board[10] == player) or \
            (board[121]== player and board[107] == player and board[93] == player and board[79] == player and board[65] == player) or \
            (board[107]== player and board[93] == player and board[79] == player and board[65] == player and board[51] == player) or \
            (board[93]== player and board[79] == player and board[65] == player and board[51] == player and board[37] == player) or \
            (board[79]== player and board[65] == player and board[51] == player and board[37] == player and board[23] == player) or \
            (board[65]== player and board[51] == player and board[37] == player and board[23] == player and board[9] == player) or \
            (board[106]== player and board[92] == player and board[78] == player and board[64] == player and board[50] == player) or \
            (board[92]== player and board[78] == player and board[64] == player and board[50] == player and board[36] == player) or \
            (board[78]== player and board[64] == player and board[50] == player and board[36] == player and board[22] == player) or \
            (board[64]== player and board[50] == player and board[36] == player and board[22] == player and board[8] == player) or \
            (board[91]== player and board[77] == player and board[63] == player and board[49] == player and board[35] == player) or \
            (board[77]== player and board[63] == player and board[49] == player and board[35] == player and board[21] == player) or \
            (board[63]== player and board[49] == player and board[35] == player and board[21] == player and board[7] == player) or \
            (board[76]== player and board[62] == player and board[48] == player and board[34] == player and board[20] == player) or \
            (board[62]== player and board[48] == player and board[34] == player and board[20] == player and board[6] == player) or \
            (board[61]== player and board[47] == player and board[33] == player and board[19] == player and board[5] == player):
            return True
        else: 
            return False         

    def is_board_full(board):
        if ' ' in board:
            return False
        else:
            return True

    while True:
        print_board()
        #Player X Input
        time.sleep(0.5)
        x_choice = int(raw_input(u'\n\t\t     Mời Người Chơi ( X ) Chọn Vị Trí Từ 1 -> 225 >> '))

        #Check space
        if board[x_choice] == ' ':
            board[x_choice] = 'X'
        else:
            print u'\n\t\t     Vị Trí Này Không Còn Trống , Lượt Người Chơi ( O ) Chọn !'
            time.sleep(1)
        #Check X win
        if is_winner(board, 'X'):
            
            print_board()
            print u'\n\t\t     Người Chơi ( X ) Thắng ! '
            break
    
        #Check hoa
        if is_board_full(board):
            print u'\n\t\t     Trận Đấu Hòa !'
            break
        
        #Player O Input
        print_board()
        time.sleep(0.5)
        o_choice = int(raw_input(u'\n\t\t     Mời Người Chơi ( O ) Chọn Vị Trí Từ 1 -> 225 >> '))

        #Check space
        if board[o_choice] == ' ':
            board[o_choice] = 'O'
        else:
            print u'\n\t\t     Vị Trí Này Không Còn Trống , Lượt Người Chơi ( X ) Chọn !'
            time.sleep(1)
        #Check X win
        if is_winner(board, 'O'):
            
            print_board()
            print u'\n\t\t     Người Chơi ( O ) Thắng ! '
            break
    
        #Check hoa
        if is_board_full(board):
            print u'\n\t\t     Trận Đấu Hòa !'
            break        

while True:
    menu()
    time.sleep(2)
    choice =  int(raw_input(u'\n\t\t\t\t\t\t\t     Mời Bạn Chọn Chế Độ Chơi >> '))
    if choice == 1:
        player_computer()
    elif choice == 2:
        player_player()
    time.sleep(1.5)
    if raw_input(u'\n\t\t     Bạn Có Muốn Tiếp Tục Chơi Không ( c >> Có / k >> Không ) >> ') != 'c':
        print u'\n\t\t     Tạm Biệt !'
        break


       
