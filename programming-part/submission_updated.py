#!/usr/bin/env python
# coding: utf-8

# In[43]:


#closest pair of points
import sys
import math
import copy

distance_dict={}
        
def print_points(points):
    for p in points:
        print(p.x,p.y)

#Formula for finding distance between two points in 2-D plane
def find_distance(point1, point2):
    x_difference = point1.x - point2.x #distance between two point with respect to x
    x_difference = pow(x_difference,2) 
    
    y_difference = point1.y - point2.y #distance between two point with respect to y
    y_difference = pow(y_difference,2) 
    
    xy_add = x_difference + y_difference
    distance_between_two_points = math.sqrt(xy_add) #Applied distance calculation formula
    
    #Storing distance as a key and points as value for extraction closest point in the end
    distance_dict[str(round(distance_between_two_points,6))] = '('+str(point1.x)+','+str(point1.y)+') ('+str(point2.x)+','+str(point2.y)+')'
    
    return distance_between_two_points

def find_points_closest_to_strip(arr_st, min_distance):
    strip_size=len(arr_st)
    
    #pick all points one by one and its successor and run loop until their difference is less than minimum
    #distance. However, it is proven that this will always run 6 to 7 times, not more than that.
    for first in range(strip_size):
        second = first + 1
        first_condition = second < strip_size
        try:
            second_condition = (arr_st[second].y - arr_st[first].y) < min_distance
            while first_condition and second_condition:
                min_distance = find_distance(arr_st[first], arr_st[second])
                second += 1
                first_condition = second < strip_size
                second_condition = (arr_st[second].y - arr_st[first].y) < min_distance
        except:
            print("nooo")
 
    return min_distance

# Brute force will be used when only 2,3 points are remaining after recursive call, in that case, it will not
# be so computationaly expensive
def algo_bf(points, points_len):
    min_distance = float('inf')
    for first in range(points_len):
        for second in range(first + 1, points_len):
            temp_dist = find_distance(points[first], points[second])
            if temp_dist < min_distance:
                min_distance = temp_dist
 
    return min_distance

def closest_points(px, py, plen):
    #As recursive functions works good for larger points but if there are very less points then it is better
    #to use brute force instead of recursive approach
    if plen <= 3:
        bf_result = algo_bf(px, plen)
        return bf_result
    
    #Divide the array into halves
    mid = plen // 2
    mid_p = px[mid]
    pleft = px[:mid]
    pright = px[mid:]
    
    #After dividing array into halves, we will find the smallest distance on both sides of array. dleft for
    #left array and dright for right array.
    dleft = closest_points(pleft, py, mid)
    dright = closest_points(pright, py, plen - mid)
    
    #Now we will find smaller distance out of left and right array.
    dis = min(dleft,dright)
    
    #Now, one case is remaining which is of those points which are other side of array but closer to each
    #other, for this we will find points which have distance to mid less than above calculated 'dis'. Only
    #in this way those points will be closest otherwise 'dis' will be smallest distance.
    strip_px=[]
    strip_py=[]
    both_lr=pleft+pright
    
    for i in range(plen):
        lr_mid_diff = abs(both_lr[i].x - mid_p.x)
        if lr_mid_diff < dis:
            strip_px.append(both_lr[i])
            
        y_mid_diff = abs(py[i].x - mid_p.x)
        if y_mid_diff < dis:
            strip_py.append(py[i])
          
    #sort the sorted points array, with respect to x, now with respect to y
    strip_px.sort(key = lambda point: point.y) #It helps in finding smallest distance
    
    #closest points to strip with respect to x
    p_strip_x = find_points_closest_to_strip(strip_px, dis)
    min_px = min(dis,p_strip_x)
    
    #closest points to strip with respect to y
    p_strip_y = find_points_closest_to_strip(strip_py, dis)
    min_py = min(dis,p_strip_y)
    
    #find minimum of points (from x and y perspective)
    final_points = min(min_px,min_py)
    
    return final_points

#point class to define points as single object with x and y coordinates as class variables
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def find_closest_points(points):
    p_len = len(points)
    #points_x has sorted points with respect to x
    points_x=points
    points_x.sort(key = lambda p: p.x)

    #we are using deep copy so that x sorted points cannot be changed
    points_y = copy.deepcopy(points)
    
    #points_y has sorted points with respect to y
    points_y.sort(key = lambda p: p.y)
    
    #find smallest distance recursively
    c_points = closest_points(points_x, points_y, p_len)
    
    return c_points
   
if __name__ == '__main__':
    points_2d=[]
    file1=open(sys.argv[1],'r')
    lines = file1.readlines()
    for l in lines:
        l_coord=l.split()
        points_2d.append(Point(int(l_coord[0]),int(l_coord[1])))

    #total points
    print_points(points_2d)
    print('\n')
    #call closest points function
    smallest_distance=find_closest_points(points_2d)
    print("Closest points are: ",distance_dict[str(round(smallest_distance,6))])
    print("Distance between these points: ",smallest_distance)
    with open(sys.argv[2], 'a') as f:
        f.write("Closest points are: "+str(distance_dict[str(round(smallest_distance,6))])+'\n')
        f.write("Distance between these points: "+str(smallest_distance))

