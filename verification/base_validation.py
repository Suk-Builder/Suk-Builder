import json
import time
import abc
from decimal import Decimal, getcontext
from typing import Any, Dict, Optional

import numpy as np
import mpmath as mp
import sympy as sp


class BaseValidation(abc.ABC):
    """
    Abstract base class for validation frameworks.
    Provides timing, exception handling, and JSON export.
    """
    
    def __init__(self, name: str, precision: int = 50) -> None:
        """
        Initialize validation with name and decimal precision.
        
        Args:
            name: Identifier for the validation test
            precision: Number of decimal places for calculations
        """
        self.name = name
        self.precision = precision
        self.result: Optional[Dict[str, Any]] = None
        self.execution_time: Optional[float] = None
        self.error: Optional[str] = None
        
        # Set precision for mpmath and decimal
        mp.mp.dps = precision
        getcontext().prec = precision + 10  # Extra guard digits
    
    @abc.abstractmethod
    def run_validation(self) -> Dict[str, Any]:
        """
        Abstract method to perform the actual validation.
        Must return a dictionary with validation results.
        """
        pass
    
    def execute(self) -> None:
        """
        Execute validation with timing and exception handling.
        """
        start_time = time.perf_counter()
        try:
            self.result = self.run_validation()
            self.error = None
        except Exception as e:
            self.error = str(e)
            self.result = {"error": self.error}
        finally:
            self.execution_time = time.perf_counter() - start_time
    
    def save_result(self, filename: Optional[str] = None) -> str:
        """
        Export validation results to JSON file.
        
        Args:
            filename: Output filename (default: {name}_result.json)
        
        Returns:
            Path to saved JSON file
        """
        if filename is None:
            filename = f"{self.name.replace(' ', '_')}_result.json"
        
        output = {
            "name": self.name,
            "precision": self.precision,
            "execution_time_seconds": self.execution_time,
            "error": self.error,
            "result": self.result
        }
        
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2, default=str)
        
        return filename


class PiValidation(BaseValidation):
    """
    Validation that verifies pi to specified number of digits
    using multiple mathematical methods.
    """
    
    def run_validation(self) -> Dict[str, Any]:
        """
        Verify pi using mpmath high-precision calculation
        and compare with sympy's pi.
        """
        # Calculate pi using mpmath
        mp_pi = mp.pi
        
        # Get sympy pi as high-precision float
        sp_pi = float(sp.N(sp.pi, self.precision + 10))
        
        # Convert mpmath pi to string for digit comparison
        mp_pi_str = mp.nstr(mp_pi, self.precision + 2)
        sp_pi_str = f"{sp_pi:.{self.precision}f}"
        
        # Compare first 50 digits
        digits_match = mp_pi_str[:self.precision + 2] == sp_pi_str[:self.precision + 2]
        
        # Additional verification using numpy
        np_pi = np.pi
        numpy_error = abs(float(mp_pi) - np_pi)
        
        return {
            "mpmath_pi": mp_pi_str[:self.precision + 2],
            "sympy_pi": sp_pi_str[:self.precision + 2],
            "digits_match": digits_match,
            "numpy_absolute_error": float(numpy_error),
            "verified_digits": self.precision if digits_match else 0
        }


def main() -> None:
    """
    Demo function showing the validation framework usage.
    """
    print("=" * 60)
    print("ABSTRACT BASE VALIDATION FRAMEWORK DEMO")
    print("=" * 60)
    
    # Create and run pi validation
    validator = PiValidation(name="Pi 50-digit Verification", precision=50)
    
    print(f"\nRunning validation: {validator.name}")
    print(f"Precision: {validator.precision} digits")
    print("-" * 40)
    
    # Execute validation
    validator.execute()
    
    # Print results
    if validator.error:
        print(f"ERROR: {validator.error}")
    else:
        result = validator.result
        print(f"mpmath pi (first 52 chars): {result['mpmath_pi']}")
        print(f"sympy pi  (first 52 chars): {result['sympy_pi']}")
        print(f"Digits match: {result['digits_match']}")
        print(f"NumPy absolute error: {result['numpy_absolute_error']:.2e}")
        print(f"Verified digits: {result['verified_digits']}")
    
    print(f"\nExecution time: {validator.execution_time:.6f} seconds")
    
    # Export to JSON
    json_file = validator.save_result()
    print(f"Results saved to: {json_file}")
    
    # Demonstrate reading back
    print("\n" + "=" * 60)
    print("LOADED JSON RESULT:")
    print("=" * 60)
    with open(json_file, 'r') as f:
        loaded = json.load(f)
        print(json.dumps(loaded, indent=2, default=str))


if __name__ == "__main__":
    main()