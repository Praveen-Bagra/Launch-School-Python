strings = ['four', 'score', 'eleven', 'hello', 'one']

result = (string.capitalize()
          for string in strings
          if len(string) >= 5)

print(set(result))
