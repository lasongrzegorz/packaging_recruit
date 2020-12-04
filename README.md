# Packing algorithm
This is a simple script for packing orders


## General info
Assumptions:
* Small pack can contain max 3 products
* Medium pack can contain max 6 products
* Large pack can contain max 9 products
* Maximum order size is 100

Algorithm is designed in two versions:
* Package - it follows the general rule to use maximum number of fully filled
 large packs and the remainder put into either small pack, medium pack or another
  large pack.
* ProductA - it follows similar rule as 'Package', with the exception of
 order between 10-18pcs, for which there are used either 2 medium packs (10
 -12pcs) or 2 large packs (13-18pcs)

Each algorithm can be used by picking a method 'calculate_packages_count
(order_size)' providing a integer between 0 and 100. If there is lower or
 higher value provided, an exception is raised 

There are unittest in tests.py for both algorithms.    
 