class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans, prev = [folder[0]], ''.join((folder[0], '/'))

        for path in folder[1:]:
            if path.startswith(prev): continue

            ans.append(path)
            prev = ''.join((path, '/'))

        return ans