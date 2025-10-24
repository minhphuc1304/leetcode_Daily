class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        st=set()
        def dfs(i,selected):
            if i==8:
                if not selected:
                    return
                s="".join(str(i)*i for i in selected)
                if len(s)<=7:
                    for i in set(permutations(s)):
                        st.add(int("".join(i)))
                else:
                    st.add(int("".join(sorted(s))))
                return
            dfs(i+1,selected)
            dfs(i+1,selected+[i])
        dfs(1,[])
        st=sorted(st)
        ix=bisect_right(st,n)
        return st[ix]
