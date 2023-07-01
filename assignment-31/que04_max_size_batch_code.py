

# 4. Write a python script to find maximum size batch code from a dictionary where key-
# values in the dictionary are batch codes and data-values are size of the batch.


batch_dict = {i: len(i) for i in input(
    "Enter batch code (seperated by spaces):").split(" ")}

print(max(batch_dict.values()))
