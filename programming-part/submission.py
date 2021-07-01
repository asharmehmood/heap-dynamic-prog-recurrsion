#!/usr/bin/env python
# coding: utf-8

# In[43]:


#closest pair of points
import sys
import math
import copy

distance_dict={}
#point class to define points as single object with x and y coordinates as class variables
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def print_points(points):
    for p in points:
        print(p.x,p.y)

#Formula for finding distance between two points in 2-D plane
def find_distance(p1, p2):
    distance = math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))
    distance_dict[str(round(distance,6))]='('+str(p1.x)+','+str(p1.y)+') ('+str(p2.x)+','+str(p2.y)+')'
    return distance

def bruteForce_algo(points, n):
    min_distance = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            temp_dist = find_distance(points[i], points[j])
            if temp_dist < min_distance:
                min_distance = temp_dist
 
    return min_distance

def find_points_closest_to_strip(strip, d):
    strip_size=len(strip)
    # Initialize the minimum distance as d
    min_distance = d
    
    #pick all points one by one and its successor and run loop until their difference is less than minimum
    #distance. However, it is proven that this will always run 6 to 7 times, not more than that.
    for i in range(strip_size):
        j = i + 1
        while j < strip_size and (strip[j].y - strip[i].y) < min_distance:
            min_distance = find_distance(strip[i], strip[j])
            j += 1
 
    return min_distance

def closest_points(px, py, n):
    #As recursive functions works good for larger points but if there are very less points then it is better
    #to use brute force instead of recursive approach
    if n <= 3:
        bf_result = bruteForce_algo(px, n)
        return bf_result
    
    #Divide the array into halves
    mid = n // 2
    mid_p = px[mid]
    pleft = px[:mid]
    pright = px[mid:]
    
    #After dividing array into halves, we will find the smallest distance on both sides of array. dleft for
    #left array and dright for right array.
    dleft = closest_points(pleft, py, mid)
    dright = closest_points(pright, py, n - mid)
    
    #Now we will find smaller distance out of left and right array.
    dis = min(dleft,dright)
    
    #Now, one case is remaining which is of those points which are other side of array but closer to each
    #other, for this we will find points which have distance to mid less than above calculated 'dis'. Only
    #in this way those points will be closest otherwise 'dis' will be smallest distance.
    strip_px=[]
    strip_py=[]
    both_lr=pleft+pright
    
    for i in range(n):
        if abs(both_lr[i].x - mid_p.x) < dis:
            strip_px.append(both_lr[i])
        if abs(py[i].x - mid_p.x) < dis:
            strip_py.append(py[i])
            
    strip_px.sort(key = lambda point: point.y) #It helps in finding smallest distance
    min_px = min(dis, find_points_closest_to_strip(strip_px, dis))
    min_py = min(dis, find_points_closest_to_strip(strip_py, dis))
    
    return min(min_px,min_py)

def find_closest_points(points, p_len):
    #points_x has sorted points with respect to x
    points_x=points
    points_x.sort(key = lambda point: point.x)
#     print_points(points_x)
    points_y = copy.deepcopy(points)
    #points_y has sorted points with respect to y
    points_y.sort(key = lambda point: point.y)
#     print('\n')
#     print_points(points_y)
    
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
    #points in 2 dimenstional plane
#     points_2d = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]

    #total points
    points_len = len(points_2d)
    print_points(points_2d)
    print('\n')
    #call closest points function
    smallest_distance=find_closest_points(points_2d,points_len)
    print("Closest points are: ",distance_dict[str(round(smallest_distance,6))])
    print("Distance between these points: ",smallest_distance)
    with open(sys.argv[2], 'a') as f:
        f.write("Closest points are: "+str(distance_dict[str(round(smallest_distance,6))])+'\n')
        f.write("Distance between these points: "+str(smallest_distance))


# In[ ]:




