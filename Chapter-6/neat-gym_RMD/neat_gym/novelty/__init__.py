######################################################################################
'''Copyright (c) 2023, 2024 , Prof. Radhamadhab Dalai, ITER , Siksha O Aanusandhan University, 
Odisha, India
Author's email address :  radhamadhabdalai@soa.ac.in'''
###################################################################################
import numpy as np


class Novelty(object):
    

    def __init__(self, k, threshold, limit, ndims):
       

        self.k = k
        self.threshold = threshold
        self.limit = limit
        self.ndims = ndims

        # Archive implemented as a circular buffer
        self.archive = np.zeros((limit, ndims))
        self.count = 0

        # Default to naive kNN (no R*-tree)
        self.rtree_index = None

        # Create an Rtree Index for inserting the points
        try:
            from rtree import index
            p = index.Property()
            p.dimension = ndims
            self.rtree_index = index.Index(properties=p, interleaved=False)
        except Exception:
            pass

    def __str__(self):

        return ('Novelty k = %d  threshold = %f  limit = %d' %
                (self.k, self.threshold, self.limit))

    def __setstate__(self, state):
        '''
        Automagically called by pickle.load()
        '''

        self.k = state['k']
        self.threshold = state['threshold']
        self.limit = state['limit']
        self.ndims = state['ndims']
        self.archive = state['archive']
        self.rtree_index = state['rtree_index']

        # Reconstruct R*-tree index from archive
        if self.rtree_index is not None:
            for idx, pt in enumerate(self.archive):
                self.rtree_index.insert(idx, Novelty._expand_point(pt))

    def add(self, p):
        '''
        If the size of the archive is less than the limit, adds the point p.
        Otherwise, when the archive is full, checks whether sparseness of p is
        greater than the threshold. If so, adds p and removes oldest point in
        archive.
        @param p the point
        @return sparseness of point in archive
        '''

        # Compute sparseness of new point
        s = self._sparseness(p)

        # Below limit, fill archive and ignore actual sparseness
        if self.count < self.limit:

            self.archive[self.count] = np.array(p)

            # Insert new point in kNN.  With interleaved=False, the order of
            # input and output is: (xmin, xmax, ymin, ymax, zmin, zmax, # ...)
            if self.rtree_index is not None:
                self.rtree_index.insert(self.count, Novelty._expand_point(p))

            self.count += 1

        else:

            # If sparseness excedes threshold, ...
            if s > self.threshold:

                # Implement a circular buffer
                idx = self.count % self.limit

                # If R*-tree available
                if self.rtree_index is not None:

                    # Remove old point from kNN
                    p_old = Novelty._expand_point(self.archive[idx])
                    self.rtree_index.delete(idx, p_old)

                    # Insert new point in kNN.  With interleaved=False, the
                    # order of input and output is: (xmin, xmax, ymin, ymax,
                    # zmin, zmax, # ...)
                    self.rtree_index.insert(idx, Novelty._expand_point(p))

                # Store new point in archive
                self.archive[idx] = np.array(p)

                self.count += 1

        return s

    def _sparseness(self, p):
        '''
        Returns the sparseness of the given point p as defined by equation 1 on
        page 13 of Lehman & Stanley 2011. Recall that sparseness is a measure
        of how unique this point is relative to the archive of saved examples.
        '''

        nbrs = (self.rtree_index.nearest(Novelty._expand_point(p), self.k)
                if self.rtree_index is not None
                else np.argsort([Novelty._distance(p, q)
                                 for q in self.archive])[:self.k])

        nbrs = list(nbrs)

        dst = np.sqrt(np.sum(np.sum((self.archive[nbrs, :] - p)**2, axis=1)))

        return 1./self.k * dst

    @staticmethod
    def _distance(p1, p2):
        '''
        Returns the L2 distance between points p1 and p2 which are assumed to
        be lists or tuples of equal length.
        '''
        return np.sqrt(np.sum((np.array(p1)-np.array(p2))**2))

    @staticmethod
    def _expand_point(pt):
        return tuple(item for sublist
                     in [(x, x) for x in pt] for item in sublist)
