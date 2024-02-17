class Solution(object):
    def countPoints(self, points, queries):
        lst=[]
        for i in queries:
            cnt=0
            x1=i[0]
            y1=i[1]
            r=i[2]
            for j in points:
                if sqrt((x1-j[0])**2 + (y1-j[1])**2)<=r:
                    cnt+=1
            lst.append(cnt)
        return lst