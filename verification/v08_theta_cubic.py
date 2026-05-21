#!/usr/bin/env python3
"""
Compute j-invariant from Jacobi theta constants using mpmath.
Verifies against known values: j(i) = 1728 and j(2i).
"""

import mpmath as mp

def j_invariant(tau, prec=50):
    """
    Compute the j-invariant for a given tau using theta constants.
    
    Uses the formula:
    j(tau) = 256 * (1 - theta_2^8 / theta_3^8)^3 / (theta_2^8 * theta_4^8 / theta_3^16)
    
    Parameters:
    tau : complex
        The modular parameter in the upper half-plane.
    prec : int
        Precision in decimal digits for mpmath.
    
    Returns:
    mp.mpf or mp.mpc
        The computed j-invariant value.
    """
    # Set working precision
    mp.mp.dps = prec
    
    # Compute theta constants using mpmath's jtheta
    # theta_2 = theta_2(0, q) where q = exp(i*pi*tau)
    # mp.jtheta(n, z, q) with n=2,3,4 gives theta_n(z, q)
    q = mp.e**(mp.pi * 1j * tau)
    theta2 = mp.jtheta(2, 0, q)
    theta3 = mp.jtheta(3, 0, q)
    theta4 = mp.jtheta(4, 0, q)
    
    # Compute powers of theta constants
    t2_8 = theta2**8
    t3_8 = theta3**8
    t4_8 = theta4**8
    
    # Compute j-invariant using the formula
    # j = 256 * (1 - t2^8/t3^8)^3 / (t2^8 * t4^8 / t3^16)
    numerator = 256 * (1 - t2_8 / t3_8)**3
    denominator = (t2_8 * t4_8) / (t3_8**2)  # t3^16 = (t3^8)^2
    
    j_val = numerator / denominator
    
    return j_val

def main():
    """
    Main function to compute j-invariant for tau=i and tau=2i,
    and verify against known values.
    """
    # Set precision for calculations
    precision = 50
    mp.mp.dps = precision
    
    print("=" * 60)
    print("j-invariant computation from Jacobi theta constants")
    print("=" * 60)
    
    # Test case 1: tau = i
    tau1 = 1j
    j_i = j_invariant(tau1, precision)
    expected_j_i = mp.mpf(1728)
    
    print(f"\n1. tau = i")
    print(f"   Computed j(i) = {j_i}")
    print(f"   Expected j(i) = {expected_j_i}")
    print(f"   Difference    = {abs(j_i - expected_j_i)}")
    
    # Check if close enough (within 10^-40)
    if abs(j_i - expected_j_i) < mp.mpf(10)**(-40):
        print("   ✓ Verification PASSED")
    else:
        print("   ✗ Verification FAILED")
    
    # Test case 2: tau = 2i
    tau2 = 2j
    j_2i = j_invariant(tau2, precision)
    
    # Known value: j(2i) = 287496 (exact integer)
    expected_j_2i = mp.mpf(287496)
    
    print(f"\n2. tau = 2i")
    print(f"   Computed j(2i) = {j_2i}")
    print(f"   Expected j(2i) = {expected_j_2i}")
    print(f"   Difference     = {abs(j_2i - expected_j_2i)}")
    
    if abs(j_2i - expected_j_2i) < mp.mpf(10)**(-40):
        print("   ✓ Verification PASSED")
    else:
        print("   ✗ Verification FAILED")
    
    # Additional verification: j-invariant is real for purely imaginary tau
    print(f"\n3. Reality check:")
    print(f"   Im(j(i))  = {mp.im(j_i)}")
    print(f"   Im(j(2i)) = {mp.im(j_2i)}")
    
    if abs(mp.im(j_i)) < mp.mpf(10)**(-40) and abs(mp.im(j_2i)) < mp.mpf(10)**(-40):
        print("   ✓ Both values are real (within numerical precision)")
    else:
        print("   ✗ Values have non-zero imaginary parts")
    
    print("\n" + "=" * 60)
    print("Computation complete.")
    print("=" * 60)

if __name__ == "__main__":
    main()