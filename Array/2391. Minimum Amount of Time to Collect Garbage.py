class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m_inx = 0
        p_inx=0
        g_inx=0
        garbagetime_ex_tt =0
        for i in range(1,len(travel)):
            travel[i] += travel[i-1]
        for i in range(len(garbage)):
            for j in range(len(garbage[i])):
                if garbage[i][j] == "M":
                    m_inx = i
                if garbage[i][j] == "G":
                    g_inx = i
                elif garbage[i][j] == "P":
                    p_inx = i
                garbagetime_ex_tt += 1
        garbagetime_ex_tt += travel[m_inx-1] if m_inx !=0 else 0
        garbagetime_ex_tt += travel[g_inx-1] if g_inx !=0 else 0
        garbagetime_ex_tt += travel[p_inx-1] if p_inx !=0 else 0
        print(travel[g_inx-1],travel[m_inx-1])
        return garbagetime_ex_tt