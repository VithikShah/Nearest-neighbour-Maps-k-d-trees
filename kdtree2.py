#------------------------MODULE TO IMPLEMENT KD-TREE------------------------------


#import math for math functions
import math

#counter function to count no. of recursive search queries
def cnt():
	cnt.count+=1

cnt.count=0

#function to calculate square distance between two points 'a' and 'b'
def square_distance(a, b):
	s = math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2)
	return s

#Defining a KDTree Node and it's attributes
class Node:
	def __init__(self,pt,ax,l,lt,rt):
		self.point=pt
		self.axis=ax
		self.label=l
		self.left=lt
		self.right=rt


class binaryheap:

	def __init__(self,ele=[]):
		self.elements=ele
		self.n=len(ele)
		self.buildheap()

	def buildheap(self):
		for i in range(self.n//2-1,-1,-1):
			self.heapify(i)

	def heapify(self,i):
		
		l=2*i+1
		r=2*i+2
		large=i

		if l<self.n and self.elements[large][2]<self.elements[l][2]:
		    large=l

		if r<self.n and self.elements[large][2]<self.elements[r][2]:
			large=r

		if large!=i:
			self.elements[large],self.elements[i]=self.elements[i],self.elements[large]
			self.heapify(large)

	def print(self):
		for i in range(self.n):
			print(self.elements[i]," , ",end='')
		print()

	def insert(self,x):
		
		self.elements.append(x)
		self.n+=1
		i=self.n-1

		while i>0 and self.elements[(i-1)//2][2]<self.elements[i][2]:
			self.elements[(i-1)//2],self.elements[i]=self.elements[i],self.elements[(i-1)//2]
			i=(i-1)//2


	def extractmax(self):
		
		self.elements[self.n-1],self.elements[0]=self.elements[0],self.elements[self.n-1]
		a=self.elements[self.n-1]
		self.elements.pop()
		self.n-=1
		self.heapify(0)
		return a

	def returnmax(self):
		return self.elements[0]
	


#Implementing KDTree 
class KDTree:

#Initialization using __init__	
	def __init__(self,objects=[]):
		
		#Building the Tree
		def build_tree(objects, axis=0):

			if not objects:
				return None

			#Sorting the coordinates to find the median
			objects.sort(key=lambda o: o[0][axis])    
			median_idx = len(objects) // 2
			median_point, median_label = objects[median_idx]

			#if axis=x, next_axis=y , vice versa
			next_axis = (axis + 1) % 2                 

			return Node(median_point, axis, median_label,
						build_tree(objects[:median_idx], next_axis),
						build_tree(objects[median_idx + 1:], next_axis))

		self.root = build_tree(list(objects))



	def nearest_neighbor(self,destination,t,n=0,r=None): 


		# state of search: best point found, its label,
		# lowest squared distance
		if t==1:
			bestheap=binaryheap()
		elif t==2:
			best=[]

		

		def recursive_search(here):
			
			if here is None:
				return

			global length
			#global counter update for every call
			cnt()                 
			point, axis, label, left, right = here.point,here.axis,here.label,here.left,here.right

			here_sd = square_distance(point, destination)
		
			# if t=1 find k nearest neighbours
			if t==1:
				if bestheap.n<n:
					bestheap.insert([point,label,here_sd])
				elif bestheap.returnmax()[2]>here_sd:
					bestheap.extractmax()
					bestheap.insert([point,label,here_sd])

		
			#If t=2 find neighbours within a radius of r units
			if t==2:
				if here_sd < r*r:
					best.append([point,label,here_sd])

			

			diff = destination[axis] - point[axis]
			close, away = (left, right) if diff <= 0 else (right, left)

			recursive_search(close)
			
			flag=0
			if t==1:
				for i in range(bestheap.n):
					if diff**2<bestheap.elements[i][2]:
						flag=1
			if t==2:
				if diff<r:
					flag=1
			
			if flag==1:
				recursive_search(away)

		recursive_search(self.root)
		
		if t==1:
			return bestheap
		elif t==2:
			return best 	

	#Method for returning the count of recursive search queries
	def returncounter(self):
		return cnt.count