test_data = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1]

def validate_sub_sequence(test_data, sequence):
	count = 0
	len_seq = len(sequence)
	for num in test_data:
		# Base case
		if count == len_seq:
			break
		# Checking the current interating number and count index of the sequence
		if num == sequence[count]:
			count +=1

	return len_seq == count 

print(validate_sub_sequence(test_data,sequence))