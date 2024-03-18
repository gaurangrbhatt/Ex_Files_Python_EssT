#!/usr/bin/env python3
# Conditinal assignment example

hungry = False
x = 'Feed the bear now!' if hungry else 'Do not feed the bear!'

print(x)
print()

ageAbove18 = True
y = 'Allow entrance to A+ rating movie!' if ageAbove18 else 'Do not enter!'

print(y)


isTestPassed = False
result = 'You have passed the exam' if isTestPassed else 'Unfortunately you have failed the test'
print(result)