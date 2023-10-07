import os
import math
import pefile

def cal_etp(data): # Entropy formula
    entropy = 0
    if data:
        for x in range(256):
            p_x = float(data.count(x)) / len(data)
            if p_x > 0:
                entropy += - p_x * math.log2(p_x)
    return entropy


def cal_pe_etp(file_path):
    # Designing an exception handling module to determine if a pe file
    try:
        pe = pefile.PE(file_path)
    except Exception as e:
        print(f"Error: Unable to open the PE file - {e}")
        return

    section_entropy_values = [] # Store the information entropy value and effective length of each PE section

    for section in pe.sections: 
        section_data = section.get_data()
        valid_data = section_data.rstrip(b'\x00')

        if valid_data: # Determine if valid data is null
            section_entropy = cal_etp(valid_data)
            section_length = len(valid_data)
            section_entropy_values.append((section_entropy, section_length))

    if section_entropy_values:
        # CCalculate the weighted sum of the information entropy of each section Total length of valid data for all PE sections
        weighted_entropy_sum = sum(entropy * length for entropy, length in section_entropy_values)
        total_length = sum(length for _, length in section_entropy_values)

        # Checks if the total valid length is greater than zero. If yes, it means that at least one PE section contains valid data
        if total_length > 0:
            # Calculate the weighted average information entropy
            weighted_average_entropy = weighted_entropy_sum / total_length 
            print(f"Weighted Average Entropy: {weighted_average_entropy:.4f}")
        else:
            print("No valid sections found in the PE file.")
    else:
        print("No sections with non-null data found in the PE file.")

if __name__ == "__main__":
    pe_file_path = input("Enter the path to the PE file: ")
    if os.path.exists(pe_file_path):
        cal_pe_etp(pe_file_path)
    else:
        print("Error: The specified file does not exist.")
