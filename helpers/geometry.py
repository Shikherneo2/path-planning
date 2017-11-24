# Helpful geometry functions
# Author -- Shikhar Dev Gupta

from math import *
from random import *

# Define a point class 
class point:
	def __init__(self, x, y, obstacle = -1, test=-1):
		self.x = x;
		self.y = y;
		self.obstacle = obstacle;
		# Kind of a radioactive tracker! See where your point came from
		self.test = test;

	def __str__(self):	
		return ( "x = " + str(self.x) + ", y = " + str(self.y) + ", obs = " + str(self.obstacle) + " and test:"+str(self.test) );

	# Are the two points the same
	def equals(self, other):
		if( self.x == other.x and self.y == other.y):
			return True;
		else:
			return False;	

	# Return index of a point from a list of points
	def find_point(self, point_list):	
		for i in range(len(point_list)):
			if( self.x == point_list[i].x and self.y == point_list[i].y ):
				return i;
		return -1;		

	# Euclidean distance between two points
	def find_dist(self, pt2):
		return int( sqrt(pow((self.x - pt2.x),2) + pow(self.y-pt2.y, 2)) )	;		

	# Check if the point is inside an obstacle
	def inside_polygon(self, obstacles):
	    for polygon in obstacles:
		    x = self.x; y = self.y; 
		    points = [];
		    for i in polygon:
		    	points.append([i.x, i.y]);
		    n = len(points);
		    inside = False;
		    p1x, p1y = points[0];
		    for i in range(1, n + 1):
		        p2x, p2y = points[i % n];
		        if y > min(p1y, p2y):
		            if y <= max(p1y, p2y):
		                if x <= max(p1x, p2x):
		                    if p1y != p2y:
		                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x;
		                    if p1x == p2x or x <= xinters:
		                        inside = not inside;
		        p1x, p1y = p2x, p2y;
		    print points;
		    if(inside is True):
				return True;
	    return False;		

	# Find the point closest to a given point
	def find_closest_point(self, list_of_vertices):
		min_dist = 99999999; min_index = -1;
		for index, i in enumerate( list_of_vertices):
			dist = find_dist(self, i);
			if(dist<min_dist):
				min_dist = dist;
				min_index = index;
		return min_index;		


# General procedures---------------------------------------

# Pull a random point from a given range
def random_point(x_range, y_range):
	return point( randint(x_range[0], x_range[1]), randint(y_range[0], y_range[1]) );

# See if three points are counter-clockwise in direction
def counter_clockwise(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)


# Return true if line segments AB and CD intersect.
def intersect(A,B,C,D):
	# Check if any three points are co-linear 
	if( ( (A.x * (B.y - C.y) ) + (B.x * (C.y - A.y) ) + (C.x * (A.y - B.y) ) )== 0 ):
		return True;
	if( ( (A.x * (B.y - D.y) ) + (B.x * (D.y - A.y) ) + (D.x * (A.y - B.y) ) )== 0 ):
		return True;
	if( ( (A.x * (C.y - D.y) ) + (C.x * (D.y - A.y) ) + (D.x * (A.y - C.y) ) )== 0 ):
		return True;
	if( ( (B.x * (C.y - D.y) ) + (C.x * (D.y - B.y) ) + (D.x * (B.y - C.y) ) )== 0 ):
		return True;
		
	return counter_clockwise(A,C,D) != counter_clockwise(B,C,D) and counter_clockwise(A,B,C) != counter_clockwise(A,B,D);


# A generic line intersection function. Only returns -1 if lines are parallel
def line_intersection(segment1, segment2):
	line1 = [segment1[0].x, segment1[0].y], [segment1[1].x, segment1[1].y];
	line2 = [segment2[0].x, segment2[0].y], [segment2[1].x, segment2[1].y];
	
	x_diff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0]);
	y_diff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]);
	
	def determinant(a, b):
		return ( (a[0] * b[1]) - (a[1] * b[0]) );

	div = determinant(x_diff, y_diff);
	if div == 0:
		#parallel lines
		return -1;

	d = ( determinant(line1[0] , line1[1]) , determinant(line2[0], line2[1]));
	x = determinant(d, x_diff) / float(div);
	y = determinant(d, y_diff) / float(div);
	x = int(x + 0.5);
	y = int(y + 0.5);
	return point(x, y);


# Final Segment Intersection function
def segment_intersection(a, b, c, d):
	if( intersect(a, b, c, d) == True):
		return line_intersection([a, b], [c, d]);
	else:
		return -1;	

# Find centroid of list of vertices
def centroid(vertices):
	n = len(vertices);
	if( n==0 ):
		return -1;	
	sum_x = 0;
	sum_y = 0;
	for i in vertices:
		sum_x = sum_x + i.x;
		sum_y = sum_y + i.y;
	centr_x = int(0.5 + sum_x/float(n) );
	centr_y = int(0.5 + sum_y/float(n) );

	return point(centr_x, centr_y);	


# Find area of a polygon
def polygon_area(vertices, number_of_vertices):
	# Expects closed polygon

	n = number_of_vertices;
	if(n %2 !=0 ):
		vertices.append(vertices[0]);
	area = 0;
	for i in xrange(0, n, 2 ):
		area += vertices[i+1].x*(vertices[i+2].y-vertices[i].y) + vertices[i+1].y*(vertices[i].x-vertices[i+2].x);
	return int(area/2);


# Max point in a list of points
def point_max(lst, cmp2 = 1):
	#1 for x and 2 for y
	if(cmp2 == 1):
		max2 = -1; max2_ind = -1;
		tmp = [i.x for i in lst];
		for index,j in enumerate(tmp):
			if(j>max2):
				max2 = j;
				max2_ind = index;
	elif(cmp2 == 2):
		max2 = -1; max2_ind = -1;
		tmp = [i.y for i in lst];
		for index,j in enumerate(tmp):
			if(j>max2):
				max2 = j;
				max2_ind = index;
	return max2_ind;			


# Min point in a list of points
def point_min(lst, cmp2 = 1):
	#1 for x and 2 for y
	if(cmp2 == 1):
		min2 = 999999999; min2_ind = -1;
		tmp = [i.x for i in lst];
		for index,j in enumerate(tmp):
			if(j<min2):
				min2 = j;
				min2_ind = index;
	elif(cmp2 == 2):
		min2 = 999999999; min2_ind = -1;
		tmp = [i.y for i in lst];
		for index,j in enumerate(tmp):
			if(j<min2):
				min2 = j;
				min2_ind = index;
	return min2_ind;		

# Distance between two points
def find_dist(pt1, pt2):
	return int( sqrt(pow((pt1.x - pt2.x),2) + pow(pt1.y-pt2.y, 2)) )	;


# Check if the given segment is obstructed by given list of obstacles
# Returns True if segment is clear of obstructions
def check_obstruction(obstacles, segment):
	
	res = True; break_out = False;
	for obs in obstacles:
		# Add the last line to make closed polygon
		n = len(obs)-1;
		if ( obs[n].equals(obs[0]) is False):
			obs.append(obs[0]);
		for index in range(len(obs)-1):
			if (segment_intersection( segment[0], segment[1],  obs[index],  obs[index+1]) != -1):
				res = False;
				break_out = True;
				break;	
		if(break_out is True):
			break;
	return res;

# Find a point in some distance from the end of a line segment
def find_point_on_line(a, b, step):
	if(a.equals(b)):
		print "sdfsdfsdfsdf";
	v_vector_x = (b.x-a.x);
	v_vector_y = (b.y-a.y);
	vector_norm_x = v_vector_x/float( sqrt( pow(v_vector_x,2) + pow(v_vector_y,2)) );
	vector_norm_y = v_vector_y/float( sqrt( pow(v_vector_x,2) + pow(v_vector_y,2)) );

	result_x = b.x + (step*vector_norm_x);
	result_y = b.y + (step*vector_norm_y);

	return point( int(round(result_x) ), int(round(result_y) ) );


def step_from_to(p1,p2, step_size):
    if find_dist(p1,p2) < step_size:
        return p2;
    else:
        theta = atan2(p2.y-p1.y,p2.x-p1.x)
        return point(p1.x + step_size*cos(theta), p1.y + step_size*sin(theta) );	
