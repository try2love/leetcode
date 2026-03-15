import sys
# strip去除开头结尾的空格，得到字符串
# split把字符串中依据空格进行切分得到list
# readline读取一行元素，遇到回车就终止，返回的是字符串
# readlines 读取多行元素，需要ctrl+d终止输入，返回List[str]
# data = sys.stdin.read().strip().split() # 返回一维列表
# data = sys.stdin.read().split() # 仍然返回一维列表，但是推荐strip
# data = sys.stdin.readline()
# data = sys.stdin.readlines()
# data = [[x.strip().split(",", " ") for x in data]]
# splitlines是一行输入为一个str，最后汇聚为一个list，元素数量等于行数
data = sys.stdin.read().strip().splitlines()

print(data, type(data), len(data))