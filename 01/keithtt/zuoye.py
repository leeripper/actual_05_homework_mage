1、打印乘法口诀
提示：尝试print(‘kk’)与print(‘kk’, end=‘’)的区别

2、猜数游戏
随机生成一个0到100的数字，提示用户在控制台上输入一个数字
当用户输入数字小于生成的随机数，则打印猜小了
当用户输入数字大于生成的随机数，则打印猜大了
当用户输入数字等于生成的随机数，则打印猜对了，结束程序
用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序

提示：生成随机数的方法
import random
rand_num=random.randint(0,100)
