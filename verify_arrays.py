import sys

# Increase integer string conversion limit for Googol-scale numbers
sys.set_int_max_str_digits(10000)

print("/// MATUSZEWSKI ARRAYS: PYTHON VERIFICATION PROTOCOL ///")
print("Loading data sets...\n")

# --- DEFINITIONS (Identical to Web/JS Logic) ---

# 1. EXA-SCALE (2^64)
s3 = 2**64
o3 = 10**10
exa_grid = [
    [(8*s3)+o3, (1*s3)+o3, (6*s3)+o3],
    [(3*s3)+o3, (5*s3)+o3, (7*s3)+o3],
    [(4*s3)+o3, (9*s3)+o3, (2*s3)+o3]
]

# 2. PLANCK-COSMIC (10^62)
s4 = 10**62
o4 = 314159265358979323846264338327950288419716939937510
planck_grid = [
    [(16*s4)+o4, (3*s4)+o4, (2*s4)+o4, (13*s4)+o4],
    [(5*s4)+o4, (10*s4)+o4, (11*s4)+o4, (8*s4)+o4],
    [(9*s4)+o4, (6*s4)+o4, (7*s4)+o4, (12*s4)+o4],
    [(4*s4)+o4, (15*s4)+o4, (14*s4)+o4, (1*s4)+o4]
]

# 3. GOOGOL-SCALE (10^100)
s5 = 10**100
googol_grid = [
    [11*s5, 24*s5, 7*s5, 20*s5, 3*s5],
    [4*s5, 12*s5, 25*s5, 8*s5, 16*s5],
    [17*s5, 5*s5, 13*s5, 21*s5, 9*s5],
    [10*s5, 18*s5, 1*s5, 14*s5, 22*s5],
    [23*s5, 6*s5, 19*s5, 2*s5, 15*s5]
]

def verify_grid(name, grid):
    print(f"--- VERIFYING: {name} ---")
    n = len(grid)
    target = sum(grid[0])
    is_valid = True
    
    # Rows
    for i in range(n):
        s = sum(grid[i])
        if s != target:
            print(f"[FAIL] Row {i} sum mismatch")
            is_valid = False
            
    # Cols
    for j in range(n):
        s = sum(grid[i][j] for i in range(n))
        if s != target:
            print(f"[FAIL] Col {j} sum mismatch")
            is_valid = False
            
    # Diag 1
    d1 = sum(grid[i][i] for i in range(n))
    if d1 != target:
        print(f"[FAIL] Main Diag mismatch")
        is_valid = False

    # Diag 2
    d2 = sum(grid[i][n-1-i] for i in range(n))
    if d2 != target:
        print(f"[FAIL] Anti Diag mismatch")
        is_valid = False
        
    if is_valid:
        print(f"[PASS] All vectors sum to constant.")
        print(f"CONSTANT (First 15 digits): {str(target)[:15]}...")
        print(f"Log10 Magnitude: ~10^{len(str(target))-1}")
    else:
        print("[CRITICAL FAILURE] Grid is not magic.")
    print("\n")

verify_grid("Exa-Scale (2^64)", exa_grid)
verify_grid("Planck-Cosmic (10^62)", planck_grid)
verify_grid("Googol-Prime (10^100)", googol_grid)
