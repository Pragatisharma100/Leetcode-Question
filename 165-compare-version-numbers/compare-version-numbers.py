class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1=version1.split(".")
        ver2=version2.split(".")
        for i in range(min(len(ver1),len(ver2))):
            if int(ver1[i]) < int(ver2[i]):
                return -1
            elif int(ver1[i]) > int(ver2[i]):
                return 1
        if len(ver1) <len(ver2):
            for i in ver2[len(ver1):]:
                if int(i) > 0:
                    return -1
        if len(ver1) >len(ver2):
            for i in ver1[len(ver2):]:
                if int(i) > 0:
                    return 1
        return 0