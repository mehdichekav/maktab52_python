import sys
import argparse


def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg


print("The average is", cal_average(sys.argv[1:]))

if __name__ == '__main__':
    print(sys.argv)

parser = argparse.ArgumentParser(description='sort some integers.')

parser.add_argument('-f', '--float', metavar='FLOAT', type=float, action='store', default=2)
parser.add_argument('-g', '--grades', metavar='GRADES', const=sum, action='store', default='auto')
parser.add_argument('len', action='store_const', const=len)

args = parser.parse_args()
add = args.sum(args.cal_average)
length = args.len(args.cal_average)
average = add / length
print(average)
