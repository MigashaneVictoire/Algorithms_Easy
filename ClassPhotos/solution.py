def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    for i in range(len(redShirtHeights)):
        if max(redShirtHeights) > max(blueShirtHeights):
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        else:
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
    return True
