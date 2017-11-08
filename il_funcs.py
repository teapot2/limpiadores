import cv2

def redimensionar( path, output, factor ):
    var = cv2.imread(path)
    var = cv2.cvtColor(var, cv2.COLOR_BGR2GRAY)
    height, width = var.shape
    res = cv2.resize(var, None, fx=(1/factor), fy=(1/factor), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(output, res)