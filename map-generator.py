import random
import numpy as np
from tempfile import TemporaryFile

def safe_get(l, idx_x, idx_y, default=0):
    """
    Jeśli index nie istnieje np "-1" to zwroc default
    """
    try:
        return l[idx_x][idx_y] or default
    except IndexError:
        return default

def generate(width, length, max_height, min_height, sea2land, max_height_delta):
    map_area = width*length
    sea_area = 0
    land_area = map_area
    
    our_map = [[None]*length]*width
    
    # get sea
    for x in range(width):
        if (sea_area/land_area) >= sea2land:
            break
        for y in range(length):
            # tu otrzymujemy poprzednie waartosci
            prev_vals = [safe_get(our_map, x-1,y-1), safe_get(our_map, x,y-1), safe_get(our_map, x-1,y)]
            max_prev_val = max(prev_vals)
            min_val = max_prev_val-max_height_delta
            sea_area += 1
            land_area -= 1
            our_map[x][y] = random.randint(max(min_val, min_height), min(-1, max_prev_val+max_height_delta))
            if sea_area/land_area >= sea2land:
                break
                
    #get_land
    for x in range(width):
        for y in range(length):
            if our_map[x][y] is None:                           
                prev_vals = [safe_get(our_map, x-1,y-1), safe_get(our_map, x,y-1), safe_get(our_map, x-1,y)]
                min_prev_val = min(prev_vals)
                max_prev_val = max(prev_vals)
                max_val = min_prev_val+max_height_delta
                our_map[x][y] = random.randint(max(0, min_prev_val-max_height_delta), min(max_val, max_height))
        
    return our_map

def save_npz(data, path):
    data = np.array(ooo)

    xs = []
    ys = []
    zs = []
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            xs.append(x)
            ys.append(y)
            zs.append(data[x][y])

#     outfile = TemporaryFile()
    np.savez(path, topo=np.array(zs), longitude=ys, latitude=xs)

raw = generate(20,20,20,-10,0.5,2)
save_npz(raw, "temp.npz")
