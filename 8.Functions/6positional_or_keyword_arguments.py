def calculate_marks(maths, eng, hindi, comp, history):
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"hindi = {hindi}")
    print(f"comp = {comp}")
    print(f"history = {history}")
    total_marks = maths + eng + hindi + comp + history
    print(f"Total marks scored = {total_marks}")

calculate_marks(hindi=55, eng=34, maths=88, comp=44, history=98)
calculate_marks( 44, 98,hindi=55, eng=34, maths=88) # TypeError: calculate_marks() got multiple values for argument 'eng'