import sys
def patient_weight(x,y):
    patient_weight=[x,y]
    for item in patient_weight:
        print(item)

if __name__ == "__main__":
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    patient_weight(x, y)

    