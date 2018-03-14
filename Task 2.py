class_list = open('class.txt', 'r+')
count = 0
ball_sum =[]
print('The list of students who passed a test less than 3:\n')
for test_list in class_list:
    controll = test_list.split(' ')
    ball_sum.append(int(controll[2]))
    count += 1
    if int(controll[2]) < 3:
        print(' '.join(controll))
sum = sum(ball_sum)
print('\nAverage sum for test in class - ', float("{0:.2f}".format(sum / count)))