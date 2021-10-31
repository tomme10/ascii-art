import numpy as np
import cv2

brightness = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`\'. '

def valToAscii(val):
    try:
        return brightness[int((val/255)*len(brightness)-1)]
    except IndexError:
        print(val)
        return ' '

filename = 'gradient.jpg'
img = cv2.imread(filename)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(img.shape)

newImg = []
asciiImg = []
ppp = 1

exit = False

for i in range(0,len(img),ppp):
    newImg.append([])
    asciiImg.append([])
    for j in range(0,len(img[1]),ppp):
        values = []
        for x in range(ppp):
            for y in range(ppp):
                try:
                    values.append(img[i+x][j+y])
                except IndexError:
                    values.append(0)
		
        
        newImg[-1].append(sum(values)//len(values))
        asciiImg[-1].append(valToAscii(sum(values)/len(values)))

newImg = np.array(newImg,dtype=np.uint8)
print(newImg.shape)

#cv2.imwrite(f'{filename.split(".")[0]}-{ppp-1}-out.jpg',newImg)

with open(f'{filename.split(".")[0]}-{ppp-1}-out.txt','w+') as f:
    for line in [asciiImg[i] for i in range(0,len(asciiImg),2)]:
        f.write(''.join(line+['\n']))
