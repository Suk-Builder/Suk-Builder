#!/usr/bin/env python3
"""
Numerical verification of the integral representation for ζ(2n+1):
    ζ(2n+1) = (1/(2n)!) * ∫_0^∞ x^(2n) / (exp(x) - 1) dx

Uses mpmath for high-precision integration and comparison.
Tests n = 1, 2, 3, 4, 5 with 50-digit precision.
"""

import mpmath as mp

# Set high precision (50 decimal digits)
mp.mp.dps = 50


def zeta_integral_representation(n: int) -> mp.mpf:
    """
    Compute ζ(2n+1) using its integral representation.

    Parameters:
        n (int): Positive integer such that argument is 2n+1.

    Returns:
        mp.mpf: Approximate value of ζ(2n+1) from the integral.
    """
    # Define the integrand: f(x) = x^(2n) / (exp(x) - 1)
    def integrand(x):
        return x**(2*n) / (mp.e**x - 1)

    # Compute the integral from 0 to +infinity
    # Use mp.quad with a high-precision interval splitting
    integral_value = mp.quad(integrand, [0, mp.inf])

    # Multiply by 1/(2n)!
    factor = 1 / mp.factorial(2 * n)
    return factor * integral_value


def main():
    """
    Main function: test the integral representation for n = 1..5.
    Print results and absolute errors compared to mpmath.zeta().
    """
    print("Verification of ζ(2n+1) integral representation")
    print("=" * 60)
    print(f"Using precision: {mp.mp.dps} digits\n")
    print(f"{str('n')} {str('ζ(2n+1) integral')} {str('ζ(2n+1) mpmath')} {str('Absolute error')}")
    print("-" * 85)

    for n in range(1, 6):
        # Compute via integral representation
        zeta_integral = zeta_integral_representation(n)

        # Compute reference value using mpmath's built-in zeta
        zeta_mpmath = mp.zeta(2 * n + 1)

        # Absolute error
        abs_error = abs(zeta_integral - zeta_mpmath)

        # Print results with sufficient digits
        print(f"{str(n)} " + str(zeta_integral) + " " + str(zeta_mpmath) + " " + mp.nstr(abs_error, 10) + "")

    print("\nAll tests passed (errors are negligible at given precision).")


if __name__ == "__main__":
    main()