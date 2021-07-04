a, b = map(int, input().split())
result = 'No' if b / a > 6.0 or a > b else 'Yes'
print(result)
