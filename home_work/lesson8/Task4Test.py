import FakeField

A = FakeField.Vovel()
print A.aoao
try:
    print A.field
except AttributeError, msg:
    print "ERROR", msg

