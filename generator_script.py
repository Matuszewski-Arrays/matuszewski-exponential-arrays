import csv

# PROJECT: THE MATUSZEWSKI EXPONENTIAL ARRAYS
# RESEARCHER: Etienne Matuszewski | DATE: Dec 17, 2025

def create_squares():
    # 1. Exa-Scale (2^64)
    base_3 = [[8,1,6],[3,5,7],[4,9,2]]
    s3, o3 = 2**64, 10**10
    sq3 = [[(x*s3)+o3 for x in r] for r in base_3]

    # 2. Planck-Cosmic (10^62)
    base_4 = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
    s4, o4 = 10**62, 314159265358979323846264338327950288419716939937510
    sq4 = [[(x*s4)+o4 for x in r] for r in base_4]

    # 3. Googol-Prime (10^100)
    base_5 = [[1,15,24,8,17],[23,7,16,5,14],[20,4,13,22,6],[12,21,10,19,3],[9,18,2,11,25]]
    s5 = 10**100
    sq5 = [[x*s5 for x in r] for r in base_5]

    return {"Exa_Scale": sq3, "Planck_Cosmic": sq4, "Googol_Prime": sq5}

if __name__ == "__main__":
    data = create_squares()
    for name, grid in data.items():
        magic_sum = sum(grid[0])
        print(f"Square: {name} | Magic Sum: {magic_sum}")
