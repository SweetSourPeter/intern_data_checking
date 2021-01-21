import csv
import psutil
import os
import time
# info = psutil.virtual_memory()
# print(u'当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024) )
# print("------------------START------------------")
# # TIMER START
# start_time = time.time()
# with open ('user_test_1.csv', 'r', encoding= 'utf-8')as t1, open('user_test_2.csv', 'r', encoding= 'utf-8')as t2:
#     fileone = t1.readlines()
#     filetwo = t2.readlines()
#
# with open('update.csv', 'w') as outFile:
#     for line in filetwo:
#         # if （int(psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024) >= 200）
#         if (int(psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024) >= 200):
#             print('MEM LEAK!!!!!!!!')
#         # print((psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024) is float)
#         # print(int(psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024) >= 200)
#         if line not in fileone:
#             outFile.write(line)
#
# #
# # outFile = open('update.csv', 'w')
# # x = 0
# # for i in fileone:
# #     if i != filetwo[x]:
# #         outFile.write(filetwo[x])
# #     x += 1
# # print(x)
#
# outFile.close()
#
# # TIMER END
# end_time = time.time()
# print ("用时" + str((end_time - start_time)*1000) + '毫秒')
# # print("MEM used :  " + (end_time-start_time))
#
# print("------------------END------------------")

with open('Test_Date_1.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)

        for line in reader:
            print(line)
        # mydict = {rows[0]:rows[1] for rows in reader}


# def get_hash(key):
#     h=0
#     for char in key:
#         h += ord(char)
#     return h%1000
# print(get_hash('+lyimin357@gmail.com'))
# Result
#