# Find a path avoiding obstacles using Vertical Cell Decomposition
# Author -- Shikhar Dev Gupta

import sys
from helpers.graph import *
from helpers.geometry import *;
import matplotlib.pyplot as plt

# Check for empty lines
file_handler = open("input_file","r");
raw_data = file_handler.read();
raw_data = raw_data.split("\n");

if(len(raw_data) <2):
	print("Incorrect format of the input file");
	exit;

def parse_input_line(line):
	temp2 = [];
	line = [i.strip() for i in line.split(",")];
	vertex = [];
	for index,i in enumerate(line):
		if(i[0] == "("):
			i = i[1:];
		if(i[len(i)-1] == ")"):
			i= i[:-1];
		vertex.append(int(i));
		if(index%2 != 0):
			temp2.append(vertex);
			vertex = [];
	return temp2;	

# Draw the obstacles and point the source and the destination----------------------------------------------
def draw_problem():
	bnd_x = [i.x for i in boundary];
	bnd_x.append(boundary[0].x);
	bnd_y = [i.y for i in boundary];
	bnd_y.append(boundary[0].y);
	poly_x = [];
	poly_y = []

	# Draw the boundary
	plt.plot(bnd_x, bnd_y);
	
	for index, i in enumerate(obstacles):
		poly_x.append([p[0] for p in i]);
		poly_y.append([p[1] for p in i]);
	
		plt.fill( poly_x[index], poly_y[index], color="#512DA8");
	
	plt.plot(source.x, source.y, marker="o");
	plt.plot(dest.x, dest.y, marker="o");
	plt.annotate('Source', xy=(source.x, source.y), xytext=(source.x+5, source.y-6) );
	plt.annotate('Destination', xy=(dest.x, dest.y), xytext=(dest.x-4, dest.y-10) );


# Extract vertices----------------------------------------------
temp = parse_input_line(raw_data[0]);
boundary = [point(i[0], i[1]) for i in temp];

# Extract source and dest
temp = parse_input_line(raw_data[len(raw_data)-1]);
source = point(temp[0][0], temp[0][1]);
dest = point(temp[1][0], temp[1][1]);

# Extract obstacles
obstacles = [];
for i in raw_data[1:len(raw_data)-1]:
	obstacles.append(parse_input_line(i) );

#sort by x-values
sorted_vertices = [];
for index,i in enumerate(obstacles):
	for j in i:
		j.append(index);
		sorted_vertices.append(j);
sorted_vertices.sort(key=lambda x: x[0]);

# Draw the problem
draw_problem();

new_sorted_vertices = [];

for i in sorted_vertices:
	temp = point(i[0], i[1], i[2]);
	new_sorted_vertices.append(temp);

new_obstacles = [];
for index, i in enumerate(obstacles):
	temp_obs = [];
	for j in i:
		temp = point(j[0], j[1], index);
		temp_obs.append(temp);
	new_obstacles.append(temp_obs);	


#-----------------------------------------------------------
# Find vertical lines
open_line_segments = [];

y_limit_lower = boundary[0].y;
y_limit_upper = boundary[2].y;

for pt in new_sorted_vertices:
	curr_line_segment = [ point(pt.x, y_limit_lower), point(pt.x, y_limit_upper) ]; 
	lower_obs_pt = curr_line_segment[0];
	upper_obs_pt = curr_line_segment[1];
	upper_gone = False;
	lower_gone = False;
	break_now = False;

	# Find intersection points with the vertical proposed lines. the intersection function returns false if segments are same, so no need to worry about same segment checking
	for index,obs in enumerate(new_obstacles):
		# Add the first point again for the last line segment of a polygon.
		
		obs.append( obs[0] );
		for vertex_index in range(len(obs)-1 ):
			res = segment_intersection( curr_line_segment[0], curr_line_segment[1], obs[vertex_index],  obs[vertex_index+1]);
			if (res!=-1):
				if ( index == pt.obstacle ):
					if pt.equals( res ) == False:
						if ( res.y > pt.y ):
							upper_gone = True;
						elif ( res.y < pt.y ):
							lower_gone = True;	
				else:	
					if pt.equals( res ) == False:
						if ( upper_gone is False ):
							if ( (res.y > pt.y) and res.y < (upper_obs_pt.y) ):
								upper_obs_pt = res;
						if ( lower_gone is False ):
							if ( (res.y < pt.y) and (res.y > lower_obs_pt.y) ):
								lower_obs_pt = res;
			if( upper_gone is True and lower_gone is True ):
				break_now = True;

		#No need to check for current point anymore...completely blocked
		if(break_now is True):
			break;		

	# Draw the vertical cell lines
	if(lower_gone is False):
		plt.plot( [lower_obs_pt.x, pt.x],  [lower_obs_pt.y, pt.y] );
		
	if(upper_gone is False):
		plt.plot( [pt.x, upper_obs_pt.x],  [pt.y, upper_obs_pt.y] );

	# Add to the global segment list
	if (lower_gone and upper_gone):
		open_line_segments.append([None, None]);
	elif (lower_gone):
		open_line_segments.append([None, upper_obs_pt]);
	elif (upper_gone):
		open_line_segments.append([lower_obs_pt, None]);
	else:
		open_line_segments.append([lower_obs_pt, upper_obs_pt]);


#------------------------------------------------------
# Find Polygon cells naiively. Will improve next. 
cells = [];

for index1 in range(len(open_line_segments) ):
	curr_segment = open_line_segments[index1];
	curr_vertex = new_sorted_vertices[index1];
	break_now = False;
	done = [False, False, True];
	if( curr_segment[0] is None ):
		done[0] = True; 
	if( curr_segment[1] is None ):
		done[1] = True;	
	if( curr_segment[1] is None and open_line_segments[index1][0] is None):
		done[2] = False;	

	for index2 in range(index1+1,  len(open_line_segments) ):
		next_segment = open_line_segments[index2];
		next_vertex = new_sorted_vertices[index2];			
		
		double_index1 = -2;
		double_index2 = -2;
		lines_to_check = [];
		trapezoids = [];
		double_check = False;

		if ( next_segment[0] is not None and next_segment[1] is not None ):
			double_check = True;

		if( done[0] is False ):
			if( double_check ):
				double_index1 = len(lines_to_check);
				lines_to_check.append( [centroid([curr_segment[0], curr_vertex]), centroid([next_segment[0], next_vertex]), 0]);
				lines_to_check.append( [centroid([curr_segment[0], curr_vertex]), centroid([next_segment[1], next_vertex]), 0]);
				trapezoids.append([ curr_segment[0], next_segment[0], next_vertex, curr_vertex ]);
				trapezoids.append([ curr_segment[0], next_vertex, next_segment[1], curr_vertex ]);
			elif ( next_segment[0] is not None ):
				lines_to_check.append( [centroid([curr_segment[0], curr_vertex]), centroid([next_segment[0], next_vertex]), 0]);
				trapezoids.append([ curr_segment[0], next_segment[0], next_vertex, curr_vertex ]);
			elif( next_segment[1] is not None ):
				lines_to_check.append( [centroid([curr_segment[0], curr_vertex]), centroid([next_segment[1], next_vertex]), 0]);
				trapezoids.append([ curr_segment[0], next_vertex, next_segment[1], curr_vertex ]);
			else:
				lines_to_check.append( [centroid([curr_segment[0], curr_vertex]), next_vertex, 0]);
				trapezoids.append([ curr_segment[0], next_vertex, curr_vertex ]);

		if( done[1] is False ):
			if( double_check ):
				double_index2 = len(lines_to_check);
				lines_to_check.append( [centroid([curr_segment[1], curr_vertex]), centroid([next_segment[0], next_vertex]), 1]);
				lines_to_check.append( [centroid([curr_segment[1], curr_vertex]), centroid([next_segment[1], next_vertex]), 1]);
				trapezoids.append([ curr_vertex, next_segment[0], next_vertex , point(curr_segment[1].x, curr_segment[1].y,curr_segment[1].obstacle, 34)]);
				trapezoids.append([ curr_vertex, next_vertex, next_segment[1], curr_segment[1] ]);
			elif ( next_segment[1] is not None ):
				lines_to_check.append( [centroid([curr_segment[1], curr_vertex]), centroid([next_segment[1], next_vertex]), 1]);
				trapezoids.append([ curr_vertex, next_vertex, next_segment[1], curr_segment[1] ]);
			elif( next_segment[0] is not None ):
				lines_to_check.append( [centroid([curr_segment[1], curr_vertex]), centroid([next_segment[0], next_vertex]), 1]);
				trapezoids.append([ curr_vertex, next_segment[0], next_vertex , curr_segment[1] ]);
			else:
				lines_to_check.append( [centroid([curr_segment[1], curr_vertex]), next_vertex, 1]);
				trapezoids.append([ curr_vertex, next_vertex, curr_segment[1] ]);
		
		if( done[2] is False ):
			if(double_check):
				double_index = len(lines_to_check);
				lines_to_check.append( [curr_vertex, centroid([next_segment[0], next_vertex]), 2]);
				trapezoids.append([ curr_vertex,next_segment[0], next_vertex ]);
				lines_to_check.append( [curr_vertex, centroid([next_segment[1], next_vertex]), 2]);
				trapezoids.append([ curr_vertex, next_vertex, next_segment[1] ]);
			elif ( next_segment[0] is not None ):
				lines_to_check.append( [curr_vertex, centroid([next_segment[0], next_vertex]), 2]);
				trapezoids.append([ curr_vertex,next_segment[0], next_vertex ]);
			elif( next_segment[1] is not None ):
				lines_to_check.append( [curr_vertex, centroid([next_segment[1], next_vertex]), 2]);
				trapezoids.append([ curr_vertex, next_vertex, next_segment[1] ]);
			# Will this ever occur though??
			else:
				lines_to_check.append( [curr_vertex, next_vertex, 2]);
				trapezoids.append([curr_vertex, next_vertex]);

		temp_to_remove = [];
		for index5,q in enumerate(lines_to_check): 
			ok = [True, True, True];
			for index3,obs in enumerate(new_obstacles):
				# Add the last line to make closed polygon
				obs.append( obs[0] );
				for index4 in range(len(obs)-1):
					if (segment_intersection( q[0], q[1],  obs[index4],  obs[index4+1]) != -1):
						ok[q[2]] = False;
						if(index5 not in temp_to_remove):
							temp_to_remove.append(index5);
						

			if (  ok[q[2]] is True ):
				done[q[2]] = True;

		for i in range(len(lines_to_check)):
			if i not in temp_to_remove:
				cells.append(trapezoids[i]);
		
		if( done[0] == True and done[1] == True and done[2] == True ):
			break;

to_draw =[];
for i in cells:
	i.append(i[0]);
	to_draw.append(i);


#-------------------------------------------------------
# Merge overlapping Polygons
quad_cells = [i for i in cells if len(i)>3];
tri_cells = [i for i in cells if len(i)==3];
others = [i for i in cells if len(i)<3];
quads_to_remove = [];
quads_to_add = [];

quads_to_remove = [];
quads_to_add = [];
for index_cell in range(len(quad_cells)):
	for index_cell2,cell in enumerate(quad_cells):
		if(index_cell != index_cell2):
			if(quad_cells[index_cell][0].x == cell[0].x and quad_cells[index_cell][1].x == cell[1].x):
					temp1 = list(quad_cells[index_cell]);
					temp1.append(temp1[0]);
					temp2 = list(cell);
					temp2.append(temp2[0]);
					area1 = polygon_area(temp1,4); area2 = polygon_area(temp2,4);
					new_quad=[];
					
					new_quad.append( point(temp1[0].x, min(temp1[0].y, temp2[0].y)) );
					new_quad.append( point(temp1[1].x, min(temp1[1].y, temp2[1].y)) );
					new_quad.append( point(temp1[1].x, max(temp1[2].y, temp2[2].y)) );
					new_quad.append( point(temp1[0].x, max(temp1[3].y, temp2[3].y)) );
					new_quad.append( point(temp1[0].x, min(temp1[0].y, temp2[0].y)) );
					area3 = polygon_area(new_quad, 4);
					if( area1 + area2 >= area3):
						#merge
						quads_to_remove.append(index_cell);
						quads_to_remove.append(index_cell2);
						
						quads_to_add.append(new_quad);

quads_to_remove = list(set(quads_to_remove));
for index in sorted(quads_to_remove, reverse=True):
    del quad_cells[index];

for i in quads_to_add:
	quad_cells.append(i);

# Remove duplicates
to_remove = [];
for index1 in range(len(quad_cells)):
	for index2 in range(index1+1, len(quad_cells)):
		duplicate = True;
		for k,m in zip(quad_cells[index1], quad_cells[index2]):
			if k.equals(m) is False:
				duplicate = False;
				break;
		if(duplicate is True):
			if index2 not in to_remove:
				to_remove.append(index2);		

for index in sorted(to_remove, reverse=True):
    del quad_cells[index];

# One more pass to remove extra quads generated because of cross - segments
quads_to_remove = [];
for index1 in range(len(quad_cells)):
	for index2 in range(len(quad_cells)):
		if(index1 != index2 and quad_cells[index1][0].x == quad_cells[index2][0].x and quad_cells[index1][1].x == quad_cells[index2][1].x):
			
			if( (quad_cells[index1][0].y<= quad_cells[index2][0].y) and  (quad_cells[index1][1].y<= quad_cells[index2][1].y)
				and (quad_cells[index1][2].y>= quad_cells[index2][2].y) and (quad_cells[index1][3].y >= quad_cells[index2][3].y)):			
				quads_to_remove.append(index2);


quads_to_remove = list(set(quads_to_remove) );
for index in sorted(quads_to_remove, reverse=True):
    del quad_cells[index];


#------------------------------------------------------
# Add boundary lines
if( boundary[0].x != new_sorted_vertices[0].x):
	quad_cells.append([boundary[0], point(new_sorted_vertices[0].x, y_limit_lower), point(new_sorted_vertices[0].x, y_limit_upper), boundary[3]]);
if( boundary[1].x != new_sorted_vertices[len(new_sorted_vertices)-1].x):
	quad_cells.append([point(new_sorted_vertices[len(new_sorted_vertices)-1].x ,y_limit_lower), boundary[1], boundary[2], point(new_sorted_vertices[len(new_sorted_vertices)-1].x, y_limit_upper) ]);

#-------------------------------------------------------
# Plot final cells
to_draw = quad_cells+tri_cells+others;
for i in to_draw:
	x = [j.x for j in i];
	y = [j.y for j in i];
	plt.plot(x, y);

#----------------------------------------------------------------------
# Get the graph
graph_vertices = [];
graph_edges = [];

for index1 in range(len(quad_cells)):
	same_boundary = [];
	for index2 in range(len(quad_cells)):
		if(index1 != index2):
			if( (quad_cells[index1][1].x == quad_cells[index2][0].x ) and ((quad_cells[index1][2].y in [quad_cells[index2][0].y, quad_cells[index2][3].y]) or (quad_cells[index1][1].y in [quad_cells[index2][0].y, quad_cells[index2][3].y]) ) ):
				same_boundary.append(index2);

	temp = quad_cells[index1][0:4];
	centroid_vertex = centroid(temp);
	place = centroid_vertex.find_point(graph_vertices)
	if( place == -1):
		graph_vertices.append(centroid_vertex);

	if(len(same_boundary)==1):
		temp_edge_middle = centroid([quad_cells[index1][1], quad_cells[index1][2]]);
		graph_vertices.append(temp_edge_middle);
		n = len(graph_vertices)-1;
		if(place != -1):
			graph_edges.append([place, n]);
		else:
			graph_edges.append([n-1, n]);
		temp = quad_cells[same_boundary[0]][0:4];
		curr_centroid_vertex = centroid(temp);
		place2 = curr_centroid_vertex.find_point(graph_vertices);
		if( place2 == -1 ):
			graph_vertices.append(curr_centroid_vertex);
			graph_edges.append([n, n+1]);
		else:
			graph_edges.append([n, place2]);

	elif(len(same_boundary)>1):
		n = len(graph_vertices)-1;
		if(place != -1):
			use = place;
		else:
			use = n;	
		for index, i in enumerate(same_boundary):
			temp = quad_cells[i][0:4];
			curr_centroid_vertex = centroid(temp);
			temp_edge_middle = centroid([quad_cells[i][0], quad_cells[i][3]]);
			graph_vertices.append(temp_edge_middle);
			pl1 =len(graph_vertices)-1;
			hmmm= curr_centroid_vertex.find_point(graph_vertices);
			if (hmmm == -1):
				graph_vertices.append(curr_centroid_vertex);
				pl2 =len(graph_vertices)-1;
			else:
				pl2 = hmmm;	
			graph_edges.append([use, pl1]);
			graph_edges.append([pl1, pl2]);		


# Add source and dest to graph
# Find the smallest distance vertex on graph and see if its clear to traverse
# Source------------------------------
min_ind = -1; min = 9999999;
for index, i in enumerate(graph_vertices):
	if( check_obstruction(new_obstacles, [source, i]) is True ):
		dist = find_dist(i, source);
		if( dist < min):
			min = dist;
			min_ind = index;

graph_vertices.append(source);
m = len(graph_vertices)-1;
graph_edges.append([min_ind, m]);	

# Destination------------------------------------
min_ind = -1; min = 9999999;
for index, i in enumerate(graph_vertices):
	if( check_obstruction(new_obstacles, [dest, i]) is True ):
		dist = find_dist(i, dest);
		if( dist < min):
			min = dist;
			min_ind = index;

graph_vertices.append(dest);
m = len(graph_vertices)-1;
graph_edges.append([min_ind, m]);

# Convert graph in adjacency list format
graph = [];
for j in range(len(graph_vertices)):
	graph.append([]);
	for i in graph_edges:
		if(i[0]==j):
			graph[j].append(i[1]);
		elif(i[1]==j):
			graph[j].append(i[0]);	

path = bfs(graph, len(graph_vertices)-2, len(graph_vertices)-1);

if(path is None):
	print "No path found. Sorry";
	sys.exit();
else:
	print "Path found."	;

# Draw everything--------------
for index,i in enumerate(graph_vertices):
	plt.annotate(str(index), xy=(i.x, i.y), xytext=(i.x+2, i.y-2) );
	# plt.plot(i.x,i.y, marker="x");

for i in graph_edges:
	temp_x = [graph_vertices[i[0]].x, graph_vertices[i[1]].x];
	temp_y = [graph_vertices[i[0]].y, graph_vertices[i[1]].y];
	plt.plot(temp_x,temp_y);


# draw path
temp_x = [graph_vertices[i].x for i in path];
temp_y = [graph_vertices[i].y for i in path];
plt.plot(temp_x,temp_y, color="#0F0F0F", linewidth=2);	


#----------------------------------------------------
# output into a file
file_output = open("vertical_cell_output", "w" );
str_to_write = "";
for index in range(len(graph_vertices)):

	str_to_write = str_to_write + ", "+str(index)+":"+"("+ str(int(graph_vertices[index].x) )+  ", "+ str(int(graph_vertices[index].y) ) + ")";

str_to_write = str_to_write[1:];

total_write = str_to_write+"\n";
str_to_write="";
for i in graph:
	if (i == []):
		continue;
	str_to_write = str_to_write + ",(";
	for j in i:
		str_to_write = str_to_write + str(j) + ",";
	str_to_write = str_to_write[:-1];
	str_to_write = str_to_write + ")";

str_to_write = str_to_write[1:];

total_write = total_write+ str_to_write + "\n";

str_to_write = "";
str_to_write =','.join(str(x) for x in path);

total_write = total_write + str_to_write;

file_output.write(total_write);
print "Output written to file.. Drawing the result";

plt.show();
