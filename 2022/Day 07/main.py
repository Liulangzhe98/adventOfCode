import json
from copy import deepcopy

template = {"dirs": [], "files": [], "size": 0}

def calc_size(file_struc, path_list=['/']):
    path = "/"+"/".join(path_list[1:])
    extra_size = 0
    for d in file_struc[path]['dirs']:
        extra_size += calc_size(file_struc, path_list+[d])
    file_struc[path]['size'] += extra_size
    return file_struc[path]['size'] 

def part_one(file_path, file_struc, max_f=100000):
    active_dir = []

    with open(file_path, 'r') as file:
        current_dict = None
        for e, line in enumerate(file.readlines(),1):
            line = line.strip()
            if line.startswith("$"):
                if line.startswith("$ ls"):
                    continue
                current_dict = line.split()[2]
                if current_dict == "..":
                    active_dir.pop()
                    continue 

                active_dir.append(current_dict)
                path = "/"+"/".join(active_dir[1:])
                file_struc[path] = deepcopy(template)
            
            else: # results of ls
                path = "/"+"/".join(active_dir[1:])
                if line.startswith("dir"):
                    file_struc[path]['dirs'].append(line.split()[1])
                else:
                    size, file = line.split()
                    file_struc[path]['files'].append(file)
                    file_struc[path]['size'] += int(size)
        calc_size(file_struc)
    return sum([v['size'] for _,v in file_struc.items() if v['size'] <= max_f])


def part_two(file_struc):
    TOTAL   = 70000000
    NEEDED  = 30000000
    space_f = NEEDED-(TOTAL-file_struc['/']['size'])
    return min([v['size'] for v in file_struc.values() if v['size'] >= space_f])

def main():
    file_struc = {}
    print(f"Solution 1T: {part_one('test.txt', file_struc)}")
    print(f"Solution 2T: {part_two(file_struc)}")
    print(f"Solution 1 : {part_one('input.txt', file_struc)}") 
    print(f"Solution 2 : {part_two(file_struc)}")
    
if __name__ == "__main__":
    main()
