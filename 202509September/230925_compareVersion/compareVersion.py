class Solution(object):
    def compareVersion(self, version1, version2):

        version1 = [int(i) for i in version1.split(".")]
        version2 = [int(i) for i in version2.split(".")]
        
        sizeVersion1 = len(version1)
        sizeVersion2 = len(version2)
        if sizeVersion1 < sizeVersion2: 
            currSizeVersion2=(sizeVersion2-sizeVersion1) 
            version1 += [0]*currSizeVersion2
        else: 
            currSizeVersion2=(sizeVersion1 - sizeVersion2)
            version2 += [0]*currSizeVersion2
        
        compareVersions=(version1 > version2) - (version1 < version2)
            
        return compareVersions
        
