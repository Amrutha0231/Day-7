from difflib import Differ
from numpy import diff
myfile1 = input("Enter First File's name for compare : ")
myfile2 = input("Enter Second File's name for compare : ")

ch1 = myfile1.split(".")
ch2 = myfile2.split(".")

if ch1[1] == "txt" and ch2[1] == "txt":
    with open(myfile1) as file_1, open(myfile2) as file_2:
        differ = Differ()
        lines1 = file_1.readlines()
        lines2 = file_2.readlines()
        diff = list(differ.compare(lines1, lines2))

        differences_found = False
        i = 1

        for line in diff:
            if line.startswith('- ') or line.startswith('+ '):
                if not differences_found:
                    print("Differences found:")
                    differences_found = True
                prefix = "Line " + str(i) + ":"
                file1_line = lines1[i - 1].strip() if i <= len(lines1) else ""
                file2_line = lines2[i - 1].strip() if i <= len(lines2) else ""
                print(f"{prefix} \"{file1_line}\" vs \"{file2_line}\"")
            if not line.startswith('? '):
                i += 1

        if not differences_found:
            print("No differences found")
else:
    print("File format Error!")
