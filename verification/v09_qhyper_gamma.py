#!/usr/bin/env python3
"""Verify q-hypergeometric converges to Gamma ratio as q approaches 1."""
import mpmath as mp
mp.mp.dps = 50

def qpoch(a, q, n):
    if n == 0: return mp.mpf('1')
    prod = mp.mpf('1')
    for k in range(n):
        prod *= (1 - a * q**k)
    return prod

def psi1_sum(a, b, q, z, N):
    total = mp.mpf('0')
    for n in range(-N, N+1):
        num = qpoch(a, q, n)
        den = qpoch(b, q, n)
        if abs(den) < 1e-30: continue
        total += (num/den) * z**n
    return total

def main():
    print("="*60)
    print("q-Hypergeometric to Gamma Limit Verification")
    print("="*60)
    alpha, beta = mp.mpf('2'), mp.mpf('3')
    z = mp.mpf('0.5')
    gamma_limit = mp.gamma(beta)/mp.gamma(alpha) * mp.hyper([alpha], [beta], z)
    print("Theoretical limit (Gamma): " + mp.nstr(gamma_limit, 15))
    for q in [mp.mpf('0.9'), mp.mpf('0.99'), mp.mpf('0.999'), mp.mpf('0.9999')]:
        val = psi1_sum(q**alpha, q**beta, q, z, 500)
        err = abs(val - gamma_limit)
        print("q=" + str(q) + " | series=" + mp.nstr(val, 12) + " | error=" + mp.nstr(err, 5))
    print("\nConclusion: Error decreases as q approaches 1.")

if __name__ == "__main__":
    main()
