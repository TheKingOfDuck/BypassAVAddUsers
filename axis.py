import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 

 
lena = mpimg.imread('600-800.png') 
plt.imshow(lena) 
plt.axis('on') 
plt.xlim(0,800) 
plt.ylim(600,0) 
plt.show()


