#---------------------NEAREST NEIGHBOURS USING KD-TREES---------------------- 

#Imported modules and files
import math
import matplotlib.pyplot as plt #matplotlib for plotting graphs
import time
from kdtree2 import KDTree
from kdtree2 import binaryheap      #The KD-Tree class


#Passing the tree of particular place_type and finding neighbours

def find_places(tree,d,pts):

	x,y=[],[]
	x_all,y_all=[],[]

	for i in pts[0] :
		x_all.append(i[0][0])
		y_all.append(i[0][1])


	print("Do you want to find the closest ",pts[1],
		  "\n\t1) Enter the no. closest points",
		  "\n\t2) In a given radius")	
	t=int(input())

	start_time=time.time()
	
	#KNN (K- Nearest Neighbours)
	#-- when k is taken from user
	if t==1:
		l=int(input("Enter no. of closest points required : "))
		if len(pts[0])<l:
			print("\nOnly ",len(pts[0])," places exist.")
			l=len(pts[0])

		print("\n\n---- CLOSEST ",l," ",pts[1]," ----")

		#Calling nearest neighbour function	for a tree
		best=tree.nearest_neighbor(d,t,l)
	
		r=best.returnmax()[2]
		#Prinitng the results
		for _ in range(l):
			nextbest=best.extractmax()

			#Appeding x and y co-ordinates to two separate lists for plotting purposes
			x.append(nextbest[0][0])
			y.append(nextbest[0][1])

			#printing various attributes of closest point
			print("Closest point :",nextbest[0])
			print("Min_Distance  :",math.sqrt(nextbest[2]))
			print("Label of point:",nextbest[1])
			print("- - - - - - - - - - - - - - - ")

		print("\nCounter of recursive_search:",tree.returncounter())
		
		#Marking the neighbours on a graph		
		print("\n-------",time.time()-start_time,"-------")
		patch=plt.Circle((d[0],d[1]),radius=math.sqrt(r),color="#98ffff",alpha=0.2)
		ax=plt.gca()
		ax.add_patch(patch)
		plt.scatter(d[0], d[1], label="My Location", color= "black",marker= "^", s=140)
		plt.scatter(x_all, y_all, label= pts[1], color= pts[2],marker= "*", s=30) 
		plt.scatter(x,y,s=80,facecolors='none',edgecolors='b')  
		plt.legend() 
		plt.show() 
    
    #Getting neighbours within a radius 	
	if t==2:
		print(" ---- CLOSEST ",pts[1]," ----")
		
		r=float(input("\nEnter search radius :"))
		
		#Calling radius function	
		best=tree.nearest_neighbor(d,t,0,r)

		#Printing the results
		for i in range(len(best)):
			x.append(best[i][0][0])
			y.append(best[i][0][1])
			print("mindistance :",math.sqrt(best[i][2]))
			print("label:",best[i][1])
			print("closest point",best[i][0])
			print("- - - - - - - - - - - - - - - ")

		#Printing no. of times recursive_search() was called
		print("\nCounter of recursive_search:",tree.returncounter())

		#Total no. of points
		print("\nTotal no. of points within a distance of ",r," are ",len(best)," given above in decreasing order of distance")

		#Marking the places on a graph		
		patch=plt.Circle((d[0],d[1]),radius=r,color="#98ffff",alpha=0.2)
		ax=plt.gca()
		ax.add_patch(patch)
		plt.scatter(d[0], d[1], label="My Location", color= "black",marker= "^", s=140)
		plt.scatter(x_all, y_all, label= pts[1], color= pts[2],marker= "*", s=30) 
		plt.scatter(x,y,s=80,facecolors='none',edgecolors='b')  
		plt.axis('scaled')
		plt.legend() 
		plt.show() 

	

def plotgraph(*args):
	for arg in args:
		x=[]
		y=[]
		for i in arg[0] :
			x.append(i[0][0])
			y.append(i[0][1])

		plt.scatter(x, y, label= arg[1], color=arg[2], marker= "*", s=80) 
		  
	# x-axis label 
	plt.xlabel('x - axis') 
	# frequency label 
	plt.ylabel('y - axis') 
	# plot title 
	plt.title('CITY') 
	# showing legend 

#Extracting coordinates from the corresponding files
#Hotels
def hotels():
	
	points=[]
	c=0
	infile=open('hotels.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1

	return KDTree(points),points


#Schools
def schools():
	
	points=[]
	c=0
	infile=open('schools.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1

	return KDTree(points),points


#Police
def police():
	
	points=[]
	c=0
	infile=open('police.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1

	return KDTree(points),points

#Hospitals
def hospitals():
	
	points=[]
	c=0
	infile=open('hospitals.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1

	return KDTree(points),points

#Petrol Bunk
def petrol_bunk():
	
	points=[]
	c=0
	infile=open('petrol_bunk.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1

	return KDTree(points),points



def main():

	#Entering own location : 
	print("Enter your location ( x y ): ")
	d=list(map(float,input().split()))

	#defining python lists to store attributes of a type of place
	hotel_list   =[None,"hotels","green"]
	police_list  =[None,"police","yellow"]
	hospital_list=[None,"hospitals","red"]
	petrol_list  =[None,"petrol_bunk","cyan"]
	school_list  =[None,"schools","blue"]

	#making respective trees of differents places   
	police_tree , police_list[0]   = police()
	hotel_tree ,  hotel_list[0]    = hotels()
	school_tree , school_list[0]   = schools()
	petrol_tree , petrol_list[0]   = petrol_bunk()
	hospital_tree,hospital_list[0] = hospitals()

	#plotting graph
	plotgraph(police_list,hotel_list,school_list,petrol_list,hospital_list)

	# my location
	plt.scatter(d[0], d[1], label="My_Location", color="black", marker= "^", s=140)
	plt.legend() 

	# function to show the plot 
	plt.show() 
	#clear graph for future use
	plt.clf()


	print("Which closest place do you wanna find?",
		   "\n\t1.Police Station",
		   "\n\t2.Hotels",
		   "\n\t3.Schools",
		   "\n\t4.Petrol Bunk",
		   "\n\t5.Hospitals")
	choice=int(input())

	#Calling the corresponding find_places() method based on choice

	if choice==1:
		find_places(police_tree,d,police_list)
	elif choice==2:
		find_places(hotel_tree,d,hotel_list)
	elif choice==3:
		find_places(school_tree,d,school_list)
	elif choice==4:
		find_places(petrol_tree,d,petrol_list)
	elif choice==5:
		find_places(hospital_tree,d,hospital_list)
	else:
		print("Wrong choice!")



if __name__ == '__main__':
	main()
