import cv2

def redimensionar_foto( path, output, factor ):
    var = cv2.imread(path)
    var = cv2.cvtColor(var, cv2.COLOR_BGR2GRAY)
    height, width = var.shape
    res = cv2.resize(var, (factor, factor), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(output, res)
    
def resizeVideo( inp, factor ):
    var = inp
    height, width = var.shape
    inp = cv2.resize(var, None, fx=(1/factor), fy=(1/factor), interpolation = cv2.INTER_CUBIC)
    
redimensionar_foto("C:\\Users\\bigse\\Limpiador\\Fotos\\Positives\\9_9.jpg", 'C:\\Users\\bigse\\Limpiador\\Fotos\\Positives\\sample1.jpg', 50)