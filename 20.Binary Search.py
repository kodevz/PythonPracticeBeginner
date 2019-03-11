# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:09:05 2018

@author: Karthi UK
"""


def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if arr[mid] == x:
            print("Element is present at index {}".format(mid))
            return mid;
        
        elif  x > arr[mid]:
            binarySearch(arr, mid+1, r, x)
            
        else:
            return binarySearch(arr, l, mid - 1, x)
    else:
       return False

a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
snum = int(input("Put One Number: "))
result = binarySearch(a,0, len(a) -1 , snum)


