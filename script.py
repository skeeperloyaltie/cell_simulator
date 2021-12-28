# import cellsim 
import cellsim
import os
import time

tissue = cellsim.Tissue(6,6,cellsim.Cell)

tissue = cellsim.Tissue(6,6,cellsim.Cell)

tissue = cellsim.Tissue(10,40,cellsim.Cell)
test_matrix = list()
for i in range(10):
    test_matrix.append([])
for j in range(40):
 	test_matrix[i].append(cellsim.Cell(False))

tissue.seed_from_matrix(test_matrix)
print("************************ Section one ************************")
print(tissue)

tissue = cellsim.Tissue(10,40,cellsim.Cell)
print("\n")
print("************************ Section Two ************************")
tissue.seed_from_file('test_tissue_01.txt', cellsim.Cell)
print(tissue)
print("\n")
print("************************ Section Three ************************")
tissue = cellsim.Tissue(10,40)
tissue.seed_random(0.5,cellsim.Cancer)
start = time.time()
for i in range(0,10):
	tissue.next_state()
	print(f"at: {time.time() - start}")
	print(tissue)
	time.sleep(0.1)
