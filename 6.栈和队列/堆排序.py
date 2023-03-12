#向下调整函数
def sift(li, low, high):
    '''

    :param li: 堆
    :param low: 堆顶，根节点
    :param high:堆底
    :return:
    '''
    #循环不变量是：i->j是当前需要调整的部分,j始终指向大孩子

    i = low
    j = 2 * i + 1 #根节点的左孩子
    while j <= high:
        #判断当前左右孩子谁大，j指针指向大孩子
        if (j + 1) <= high and li[j + 1] > li[j]:
            j = j + 1
        #如果满足大顶堆，直接return
        if li[i] >= li[j]:
            return li
        #不满足，向下调整
        else:
            li[i], li[j] = li[j], li[i]
            #移动指针，这样搜索保证是在以low为根节点的子树进行搜索
            i = j
            j = 2 * i + 1
    return li
#堆排序
def heapsort(li):


    # 1.构建大顶堆，农村包围城市
    #最后一个叶子节点
    for i in range((len(li) - 2) // 2, -1, -1):
        li = sift(li, i, len(li) - 1) #始终以整个列表的最后一个做high，high的作用是控制搜索范围在子树中

    # 2.每次交换首位，向下调整，出数堆顶
    #记录堆底
    j = len(li) - 1
    while j > 0:
        li[0], li[j] = li[j], li[0] #交换首尾
        j -= 1
        li = sift(li, 0, j)
    return li

li = [i for i in range(100)]
import random
random.shuffle(li)

result = heapsort(li)
print(result)

# li = [3,8,7,6,5,0,1,2]
# result = sift(li,low=0,high=len(li)-1)
# print(result)


