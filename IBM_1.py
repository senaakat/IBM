
points=[(5,4),(7,2)]

def euclideanDistance(firstpoint,secondpoint):
        firstDistance= secondpoint[0]-firstpoint[0]
        secondDistance= secondpoint[1]-firstpoint[1]
        pointsBetweenDistance= (firstDistance**2 + secondDistance**2)**0.5
        print(f"Euclidean Distance between {firstpoint} and {secondpoint} is {pointsBetweenDistance}")
        return pointsBetweenDistance

euclideanDistance(points[0],points[1])