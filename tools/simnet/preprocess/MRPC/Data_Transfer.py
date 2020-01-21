# coding=utf8

'''
version: September 23, 2019 11:39 AM
Last revision: January 21, 2020 09:17 AM
  
Author : Chao-Hsuan Ke
'''

import csv
import codecs

# read csv
csvfile = 'train_utf8.csv'

# read txt
filePath = "C:\\Users\\barry.ke\\Desktop\\MSRParaphraseCorpus\\";  # file path
fileName = "msr_paraphrase_train.txt";  # file name
ftxt = open(filePath + fileName, 'r', encoding="utf-8")

# output csv
outputcsvfile = 'C:\\Users\\barry.ke\\Desktop\\output.csv'
f = open(outputcsvfile, "w", encoding="utf-8", newline='')
w = csv.writer(f)
quertId = -1
# questionId = 0

# csv to csv
# with codecs.open(csvfile, "r", encoding='utf-8') as csv:
#     for line in csv:
#         if line != "":
#             cols = line.split(",")
#             if(len(cols) > 5):
#                 questionId2 = questionId+1
#                 #print(quertId, cols[3])
#                 w.writerow([quertId, questionId, questionId2, cols[3], cols[4], cols[5]])
#                 quertId+=1
#                 questionId = questionId2
#                 questionId+=1
#
# csv.close()


# txt to csv
for line in ftxt:
    cols = line.split("	")
    if (len(cols) == 5):
        w.writerow([quertId, cols[1], cols[2], cols[3], cols[4], cols[0]])
        quertId += 1

ftxt.close()
