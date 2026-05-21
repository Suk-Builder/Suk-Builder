#!/usr/bin/env python3
"""Chudnovsky 1/pi series and coefficient entropy analysis."""
import mpmath as mp
mp.mp.dps = 50

def chudnovsky_term(k):
    num = mp.factorial(6*k) * (13591409 + 545140134*k)
    den = mp.factorial(3*k) * (mp.factorial(k)**3) * (640320**(3*k + mp.mpf('1.5')))
    return 12 * (-1)**k * num / den

def main():
    print("="*60)
    print("CHUDNOVSKY SERIES FOR 1/pi")
    print("="*60)
    for N in [50, 100, 200]:
        s = mp.nsum(lambda k: chudnovsky_term(k), [0, N])
        print("\nN=" + str(N) + " | partial 1/pi=" + mp.nstr(s, 25))
        print("         | true 1/pi   =" + mp.nstr(1/mp.pi, 25))
        print("         | error       =" + mp.nstr(abs(s - 1/mp.pi), 5))

    # Entropy analysis
    print("\n--- Coefficient Entropy ---")
    coeffs = [abs(chudnovsky_term(k)) for k in range(20)]
    total = sum(coeffs)
    probs = [c/total for c in coeffs]
    entropy = -sum(p * mp.log(p) for p in probs if p > 0)
    print("Entropy S(20) = " + mp.nstr(entropy, 10))
    print("Max entropy = " + mp.nstr(mp.log(20), 10))
    print("Normalized = " + mp.nstr(entropy/mp.log(20), 5))
    print("\nConclusion: Low normalized entropy indicates concentrated information.")
    print("This suggests the series has structured, non-random coefficients.")

if __name__ == "__main__":
    main()
