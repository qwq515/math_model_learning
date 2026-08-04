infor = 'hello,world' #字符串
Infor = 18            #int
into = 1.114          #浮点型
Into = ''
is_student = True     #布尔型 true or false 0 or 1
print(type(infor),type(Infor),type(is_student),type(into))           #type表示形式 注意了，正常情况下你不需要加单引号，加上等于说把它变成了str形
print(infor,Infor,into,Into,'蛊真人')

family = [1,'母亲','儿子']                     #列表，从0开始数数
family.append('女儿')                               #.append直接顺着加上一个元素
print(family[3])

for i in family:                        #循环语句
    print(i)
    print(type(i))                      #这里的i就没有定义，你看他的形式随元素的变化而变化

lists = [1,2,3,4,5]                     #为了更好的理解循环，看这个与下面的对比
for j in lists:
    num = 0
    num += j
print(num)

nums = 0
for k in lists:                         #事实上for循环应该来说就是在识别到退出之前不断地按顺序重复
    nums += k
print(nums)


length = 177
if length < 170:                        #其实这里类似区间
    print('矮子')
elif length < 190:                      #这里有个默认前提就是大于等于170，因为小于170的都进入if语句里了
    print('正常')
else:
    print("高个子")


commodity = {'name':'QQread','price':299,'time':2018}   #花括号是字典，方括号是列表，圆括号是元组，起那面的叫key，后面的映射到前面去
print(commodity['name'])                            #这里的[]只是表示一个查找，不表示，列表，实际上字典里面的是一个个的元组
print(commodity.keys())                             #以下三种是字典（dict）里面自带的内置方法（method），不需声明直接调用
print(commodity.values())
print(commodity.items())                            #事实上我们可以发现，items返回的是三个元素等于2的元组，其他的返回的也是迭代类型，方便遍历
    