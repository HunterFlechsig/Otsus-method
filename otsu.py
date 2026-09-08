import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

def getImageAsArray(path: str):
    img = Image.open(path)
    return np.asarray(img.convert('L'))

def applyImageThreshold(img: np.ndarray, threshhold: int) -> np.ndarray:
    thresholded_img = np.zeros(img.shape)
    thresholded_img[img >= threshhold] = 1
    return thresholded_img

def computeOtsusCriteria(img: np.ndarray, threshold: int) -> int:
    if(threshold % 50 == 0 or threshold == 255):
        print("checking threshold", threshold)

    thresholded_img = applyImageThreshold(img, threshold)

    num_pixels = img.size
    num_pixels_1 = np.count_nonzero(thresholded_img)

    weight_1 = num_pixels_1 / num_pixels
    weight_0 = 1 - weight_1

    if weight_0 == 0 or weight_1 == 0:
        return np.inf

    val_1 = img[thresholded_img == 1]
    val_0 = img[thresholded_img == 0]

    var_1 = np.var(val_1) if len(val_1) > 0 else 0
    var_0 = np.var(val_0) if len(val_0) > 0 else 0

    return weight_0 * var_0 + weight_1 * var_1

def findBestThreshold(img: np.ndarray):
    th_range = range(int(np.max(img)) + 1)
    criterias = [computeOtsusCriteria(img, threshold) for threshold in th_range] 
    best_threshold = th_range[np.argmin(criterias)] #argmin returns index
    return best_threshold

def getOtsuImage(path: str):
    img = getImageAsArray(path)
    best_threshold = findBestThreshold(img)
    thresholded_img = applyImageThreshold(img, best_threshold)
    return thresholded_img

def showComparison(path: str):
    burger_regular = getImageAsArray(path)
    burger_otsu = getOtsuImage(path)

    plt.figure(figsize=(20,10))
    plt.subplot(1,2,1)
    plt.title("Original Image", fontsize = 20)
    plt.imshow(burger_regular, cmap="gray")
    plt.subplot(1,2,2)
    plt.title("Otsu Method Image", fontsize = 20)
    plt.imshow(burger_otsu, cmap="gray")
    plt.tight_layout()
    plt.show()

showComparison('burger.jpg')
showComparison('hero.jpg')
