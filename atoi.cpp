#include <climits>
#include <iostream>
#include <string>

int myAtoi(std::string s) {
  int result = 0;
  char sign = ' ';

  int i = 0;

  // Skip all leading white space
  while (i < s.length() && s[i] == ' ') {
    i++;
  }
  // Check for sign
  if (s[i] == '+' || s[i] == '-') {
    sign = s[i];
    i++;
  }

  // Conversion
  for (i; i < s.length(); i++) {
    char c = s[i];
    if (std::string("0123456789").find(c) != std::string::npos) {
      int digit = c - '0';

      if (result > (INT_MAX - digit) / 10) {
        if (sign == '-') {
          result = -INT_MAX - 1;
          return result;
        } else {
          result = INT_MAX; // Clamp to INT_MAX on overflow
          return result;
        }

      } else {
        result = result * 10 + digit;
      }
    } else {
      // Non Digit Character encountered
      break;
    }
  }

  if (sign == '-')
    result = result *= -1;
  return result;
}

int main() {
  std::cout << myAtoi("0-1") << std::endl;
  std::cout << myAtoi("  1 x 2 3  ") << std::endl;
  std::cout << myAtoi("  -123  ") << std::endl;
}
