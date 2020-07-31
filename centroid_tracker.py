from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

class CentroidTracker():
    def __init__(self, maxDisappeared=50):
        # object ID for next unique object
        self.nextObjectID = 0
        # keeps track of mapping object ID to centroid
        self.objects = OrderedDict()
        # keeps track of number of frames hidden
        self.disappeared = OrderedDict()

        # max number of hidden frames
        self.maxDisappeared = maxDisappeared

    def register(self, centroid):
        # register a new object
        self.objects[self.nextObjectID] = centroid
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1

    def deregister(self, objectID):
        # deregister an object
        del self.objects[objectID]
        del self.disappeared[objectID]

    """
    rects is a tuple in the format of -> (startX, startY, endX, endY)
    """
    def update(self, rects):
        # check for empty rects parameter
        if len(rects) == 0:
            # update list of disappeared objects
            for objectID in list(self.disappeared.keys()):
                self.disappeared[objectID] += 1

                # check for maxDisappeared
                if self.disappeared[objectID] > self.maxDisappeared:
                    self.deregister(objectID)

            # no centroids to update so early return
            return self.objects

        # array of input centroids for current frame
        inputCentroids = np.zeroes((len(rects), 2), dtype="int")

        # loop over rects
        for (i, (startX, startY, endX, endY)) in enumerate(rects):
            # derive centroid
            cX = int((startX + endX) / 2.0)
            cY = int((startY + endY) / 2.0)
            inputCentroids[i] = (cX, cY)

        # register centroids if untracked
        if len(self.objects) == 0:
            for i in range(0, len(inputCentroids)):
                self.register(inputCentroids[i])
        # update object coordinates
        else:
            # list of ids and cooresponding centroids
            objectIDs = list(self.objects.keys())
            objectCentroids = list(self.objects.values())

            # distance between each pair of centroids
            D = dsit.cdist(np.array(objectCentroids), inputCentroids)

            # sort so smallest row values is at the front of index list
            rows = D.min(axis=1).argsort()

            # sort so smallest column values is at the front of index list
            cols = D.argmin(axis=1)[rows]

            # determine if we need to update, register, or deregister an object
            usedRows = set()
            usedCols = set()

            for (row, col) in zip(rows, cols):
                # ignore if already examined
                if row in usedRows or col in usedCols:
                    continue

                # set centroid and reset disappeared counter
                objectID = objectIDs[row]
                self.objects[objectID] = inputCentroids[col]
                self.disappeard[objectID] = 0

                usedRows.add(row)
                usedCols.add(col)

            unusedRows = set(range(0, D.shape[0])).difference(usedRows)
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)

            # check for disappeared object
            if D.shape[0] >= D.shape[1]:
                for row in unusedRows:
                    objectID = objectIDs[row]
                    self.disappeared[objectID] += 1

                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deregister(objectID)
                    else:
                        for col in unusedCols:
                            self.register(inputCentroids[col])

        return self.objects













