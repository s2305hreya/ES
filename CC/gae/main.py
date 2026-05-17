print 'Content-Type: text/html'
print ''
# print '<h1>Hello Google App Engine</h1>'

# print 'hello'


# for i in range(5):
#     print "Name: Sunandha<br>"
#     print "Seat Number: 101<br>"
#     print "Department: Computer Engineering<br><br>"

# ------------------------------ 1b --------------------

# a = 10
# b = 5

# print "<pre>"

# print "First Number =", a
# print "Second Number =", b
# print ""

# print "Addition =", a + b
# print "Subtraction =", a - b
# print "Multiplication =", a * b
# print "Division =", a / b

# print "</pre>"

# ------------------------------------- 2a --------------------------

# print "<pre>"

# for i in range(1, 11):
#     print "10 x", i, "=", 10 * i

# print "</pre>"


# ------------------------------------- 2b --------------------------


a = 0
b = 1

print "<pre>"
print "Fibonacci Series:"
print ""

for i in range(10):
    print a
    c = a + b
    a = b
    b = c

print "</pre>"