# crypted-messages

# Blackbox API Reverse Engineering

## Endpoint Summary

### POST /data
- Input: string
- Output: Base64-encoded version of the input string
- Reasoning: Reverse engineering showed that the blackbox API returns an output that matches the Base64 encoding of the input. For example, input `"hello123"` returns `"aGVsbG8xMjM="`, which is the Base64 representation. Therefore, the mock version uses Python's `base64.b64encode()` to replicate this behavior.

---

### GET /time
- Output: Integer counter decreasing by 1 every second
- Reasoning: This is not a Unix timestamp or wall-clock time. The value is a large integer (e.g., `8160000+`) that steadily decreases by 1 every second. It behaves like an internal tick counter. Analysis revealed that it resets daily, starting from a fixed value (e.g., `8160000`) at **midnight**. The mock implementation subtracts seconds since midnight from this fixed number to emulate the countdown behavior.


### POST /fizzbuzz
- Returns false for all types of lists. But, input is required in JSON list form only. Else, it gives error. Always returns false, for all types of lists.

### POST /zap
- Removes digits from the input string

### POST /alpha
- Returns true if input starts with an alphabet

### POST /glitch
- If input length is odd → reverse it
- If even → return jumbled version
