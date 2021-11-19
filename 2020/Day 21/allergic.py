import re

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1.split(" ") if value in lst2.split(" ")] 
    return lst3 

def main():
    with open("test.txt", "r") as openobj:
        allerDict = {}
        ingredientList = []
        
        for line in openobj:
            line = line.strip()[:-1]
            ingredients, allergens = line.split(" (")
            for allergen in allergens[9:].split(", "):
                try:
                    allerDict[allergen] = allerDict[allergen] + [ingredients]
                except:
                    allerDict[allergen] = [ingredients]
            for ing in ingredients.split(" "):
                ingredientList.append(ing)
        print(allerDict)
        endResult = []
        #while len(endResult) < len(allerDict):
        for _ in range(2):
            print("="*50)
            for key in allerDict.keys():
                reduceList = []
                
                poss = allerDict[key]
                complete = " ".join(poss).split(" ")       
                #print(f"{key} : {poss}")
                print(f"{key} | {complete} ", end = "| ")
                count = [complete.count(x) for x in complete]
                if any(i >= 2 for i in count):
                    print("WE can reduce", end = " | ")
                    print(count)
                    test = [x for x in complete if complete.count(x) >= 2]
                    for item in test:
                        if not item in reduceList:
                            reduceList.append(item)
                else:
                    print("Only unique ones")
                    reduceList = poss
                print(reduceList)
                allerDict[key] = reduceList
                
                #if len(poss) > 1:
                    #for nr in range(0, len(poss)-1):
                        #result = list(set(intersection(poss[nr], poss[nr+1]))-set(endResult))
                        
                        #if len(result) == 1:
                            #print("Reducing")
                            #allerDict[key] = result
                            #endResult.append(result[0])
                    #print(f"{key} : {result}")
                #else:
                    #result = [value for value in poss[0].split(" ") if value not in endResult]
                    
                    #if len(result) == 1:
                        #allerDict[key] = result
                        #endResult.append(result[0])
            #print(endResult)
        print(allerDict)
        for value in allerDict.values():
            #print(value[0])
            ingredientList = list(filter(lambda x: x != value[0], ingredientList))
        #print(ingredientList)
        #print(len(ingredientList))
main()

