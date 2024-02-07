from copy import copy
list_1to9=[1,2,3,4,5,6,7,8,9]

#在b層建一個新的1-9，然後pop掉取過的，C層再複製b取過的，建一個新的1-9，pop調取過的
#d層再複製c層取過的，建新的1-9.....以下同上。這樣就最後一行就不用再把取過的加回去了。

# 如果再稍稍修改，效率會再更好喔
for a in list_1to9:        # a從list_1to9取數字
	list_a=copy(list_1to9)   # list_a複製list_1to9
	list_a.remove(a)         # 將a選取的數字從list_a去除，留下可以繼續被選取的字給b
	for b in list_a:         # b從list_a取數字
		list_b=copy(list_a)  # list_b複製list_a
		list_b.remove(b)     # 將b選取的數字從list_b去除，留下可以繼續被選取的字給c
		for c in list_b:
			list_c=copy(list_b)
			list_c.remove(c)
			for d in list_c:
				list_d=copy(list_c)
				list_d.remove(d)
				for e in list_d:
					list_e=copy(list_d)
					list_e.remove(e)
					for f in list_e:
						list_f=copy(list_e)
						list_f.remove(f)
						for g in list_f:
							list_g=copy(list_f)
							list_g.remove(g)
							for h in list_g:
								list_h=copy(list_g)
								list_h.remove(h)
								for i in list_h:
                                    #這時候選取完所有的數字，並填入方程式進行驗證，如果為是，輸出結果；如果為否，則沿著迴圈h到迴圈a一一測試各種可能。
									if (a/(b*10.+c)+d/(e*10.+f)+g/(h*10.+i))==1: 
										print (a,b,c,d,e,f,g,h,i) 