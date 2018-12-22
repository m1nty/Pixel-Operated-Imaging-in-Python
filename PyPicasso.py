
import sys
#SYS READS COMMAND LINE ARGS

from PIL import Image
#PIL USED FOR IMAGE PROCESSING

import numpy as np
#NEED LINEAR ALGEBRA TOOLS

print("The following is going to be a masterpiece: \n\n\n\n\n\n")

asciichar = np.asarray(list(' .,:;*rs4A232hMHGS9B#%@'))
#THIS LIST CONTAINS ASCII FROM TO LOW TO HIGH WHITESPACE ITENSITY
 
if len(sys.argv) != 4: print("You need to input more arguments to script. In cmd looks like:\n\C:yourdirectory\yourcodesname.py imagename.jpeg scalingfac intensitycorrection"); sys.exit()
#CHECKS IF VALID PARAMETERS ARE GIVEN IN CMD


f, scale, intensity, width = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), 7/3.5
#ASSIGN PARAMETERS GIVEN TO VARIABLES
#'width' IS WIDTH CORRECTION SET TO 7/3.5 AS ESTIMATED STANDARD

picture = Image.open(f)

S = ( round(picture.size[0]*scale*width), round(picture.size[1]*scale) )
#IMAGE SCALING COLLECTED BY 'scale' AND 'width' TO ENLARGE BUT MAINTAIN CONSTANT ASPECT RATIO

picture = np.sum( np.asarray( picture.resize(S) ), axis=2)
picture -= picture.min()
#GIVEN IMAGE IS RESIZED
#SUMMATION OF RGB PER PIXEL TO GET MAX,MIN, THEN OVERALL INTENSITY: 0 = BLACK, 255 = WHITE

picture = (1.0 - picture/picture.max())**intensity*(asciichar.size-1)
#INTENSITIES ARE DIVIDED BY MAX TO OBTAIN VALUES IN RANGE {0,1}
#TO ASSIGN TO ASCIICHAR LIST, THE INDEX IS FOUND FROM SUBTRACTION FROM 1 TO ORDER FROM WHITEST TO DARKEST
#SCALED INTENSITIES ARE RAISED TO 'intensity' TO MODIFY THE INTENSITY DISTRIBUTION OF THE PIXELS ('intensity =1' IS ORIGINAL IMAGE INTENSITY)
#SCALED INTENSITIES ARE MULTIPLIED BY LARGEST 'asciichar' LIST VALUE TO THEN BE TRUNCATED TO AN INT VALUE TO EVALUATE TO AN INDEX IN THE LIST

print( "\n".join( ("".join(row) for row in asciichar[picture.astype(int)]) ) )
#THE IMAGE IS TRUNCATED TO TYPE INT TO SERVE AS THE ITERATION MAXIMUM FOR THE LOOP
#IMAGE MATRIX IS PASSED AS INDEX TO 'asciichar' SINCE NUMPY ALLOWS INDICES TO BE OF TYPE MATRIX (ESSENTIALLY A 2-D MATRIX)
#JOIN OPERATOR USED TO COMBINE EACH ROW, 'row', OF PIXEL MAP TO A SINGLE STRING FOR PRINTING AND TO PUT NEW LINE CHARACTERS IN BETWEEN
