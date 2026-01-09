def rem(l, word):
    for item in l:
        
        l.remove(word)

        return l


l=["mohan","rohan","sohan","suraj"]
print(rem(l,"suraj"))