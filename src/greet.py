
# Minimal Python demo: run `python src/greet.py Alice`
import sys
name = sys.argv[1] if len(sys.argv) > 1 else "Studio"
print(f"Hello, {name}!")
