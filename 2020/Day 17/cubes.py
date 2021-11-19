import time
import itertools

def main(): 
    with open('test.txt') as openfileobject:
        xyPlane = []
        for line in openfileobject:
            xyPlane.append("."+line.strip()+".")
        xyPlane = ['.'*len(xyPlane[0])] + xyPlane + ['.'*len(xyPlane[0])]
        #print(xyPlane)
    dummy = ['.'*len(xyPlane[0])]*len(xyPlane)
    #print(dummy)
    zAxis = [dummy, xyPlane, dummy]
    

    # x, y, z
    buurman = [[-1,0,1], [1,0,-1], [-1,0,1]]
    buurman = list(itertools.product(*buurman))
    
    for counter in range(0,4):
        actives = 0
        middle = len(zAxis)//2
        start = middle- len(zAxis)+1
        #print(f"M: {middle} S: {start}")
        copy = []
        for zc, z in enumerate(zAxis):
            zPlane = []
            for yc, y in enumerate(z):
                newLine = ['.']
                for xc, x in enumerate(y):
                    #check for all possible 'buurmannen'
                    som = 0
                    for x1,y1,z1 in buurman:
                        
                        try:
                            som += zAxis[zc+z1][yc+y1][xc+x1] == "#"
                        except:
                            pass
                    som -= x=='#'
                    if x == '.': #inactive
                        if som == 3:
                            new = '#'
                        else:
                            new = '.'
                    else: #active
                        if som == 2 or som == 3:
                            new = '#'
                        else:
                            new = '.'
                    newLine.append(new)
                actives += newLine.count('#')
                zPlane.append(newLine)
                newLine.append('.')
            dummy = ['.']*len(newLine)
            zPlane.append(dummy)
           
            copy.append(zPlane)

            
        
        dummy = [[['.']*len(newLine)]*len(zPlane)]
        for pc, plane in enumerate(copy, start):
    
            print(f"Z= {pc}  {len(copy)+start}")

            
            for regel in plane:
                print("\t"+"".join(regel))
        zAxis = dummy + copy.copy() + dummy

        

        print(len(zAxis))
        print("=="*30)
        print(actives)
        
        
    #part2Answer = result
    #print(f"Part 2 is : {part2Answer} {(time.time()-start)*1000:.2f}ms") 
    
main()

