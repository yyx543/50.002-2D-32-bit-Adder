print('BC1.1\n')
for i in range(0,32):
    print('XB{0} := ODD(b{0},OP0);'.format(i))
    if i==0:
        print('nS{0} := ODD(A{0},XB{0},OP0);'.format(i))
        print('nC{0} := OR(AND(A{0},XB{0}),AND(OP0,A{0}),AND(OP0,XB{0}));'.format(i))
    else:
        print('nS{0} := ODD(A{0},XB{0},nC{1});'.format(i,i-1))
        print('nC{0} := OR(AND(A{0},XB{0}),AND(nC{1},A{0}),AND(nC{1},XB{0}));'.format(i,i-1))
    print('')

for i in range(0,16):
    print('nS0c{0} := OR(nS{0},nS{1}));'.format(i,i+16))
for i in range(0,8):
    print('nS1c{0} := OR(nS0c{0},nS0c{1}));'.format(i,i+8))
for i in range(0,4):
    print('nS2c{0} := OR(nS1c{0},nS1c{1}));'.format(i,i+4))
for i in range(0,2):
    print('nS3c{0} := OR(nS2c{0},nS2c{1}));'.format(i,i+2))
print('nZ := NOT(OR(nS3c0,nS3c1));')

print('')
#Check Addition or Subtraction
print('xC0 := NOT(OP0);')
print('')

#Generate G, P and Sprint('\n')
for i in range(0,32):
    print('xG0c{0} := NOT(AND(A{0},XB{0}));'.format(i))
    print('xP0c{0} := NOT(OR(A{0},XB{0}));'.format(i))
    print('S{0} := ODD(C0r{0},A{0},XB{0});'.format(i))
print('')

#Row1
for i in range(1,32,2):
    if i<31:
        print('G1c{0} := NOT(AND(xG0c{0},OR(xP0c{0},xG0c{1})));'.format(i,i-1))
        print('P1c{0} := NOT(OR(xP0c{0},xP0c{1}));'.format(i,i-1))
    print('C0r{1} := NOT(xC1r{0});'.format(i,i-1))
    print('C0r{0} := NOT(AND(xG0c{1},OR(xP0c{1},xC1r{0})));'.format(i,i-1))
print('')
#Row2
for i in range(3,32,4):
    if i<31:
        print('xG2c{0} := NOT(OR(G1c{0},AND(P1c{0},G1c{1})));'.format(i,i-2))
        print('xP2c{0} := NOT(AND(P1c{0},P1c{1}));'.format(i,i-2))
    print('xC1r{1} := NOT(C2r{0});'.format(i,i-2))
    print('xC1r{0} := NOT(OR(G1c{1},AND(P1c{1},C2r{0})));'.format(i,i-2))
print('')
#Row3
for i in range(7,32,8):
    if i<31:
        print('G3c{0} := NOT(AND(xG2c{0},OR(xP2c{0},xG2c{1})));'.format(i,i-4))
        print('P3c{0} := NOT(OR(xP2c{0},xP2c{1}));'.format(i,i-4))
    print('C2r{1} := NOT(xC3r{0});'.format(i,i-4))
    print('C2r{0} := NOT(AND(xG2c{1},OR(xP2c{1},xC3r{0})));'.format(i,i-4))
print('')
#Row4
for i in range(15,32,16):
    if i<31:
        print('xG4c{0} := NOT(OR(G3c{0},AND(P3c{0},G3c{1})));'.format(i,i-8))
        print('xP4c{0} := NOT(AND(P3c{0},P3c{1}));'.format(i,i-8))
    print('xC3r{1} := NOT(C4r{0});'.format(i,i-8))
    print('xC3r{0} := NOT(OR(G3c{1},AND(P3c{1},C4r{0})));'.format(i,i-8))
print('')
#Row5
print('C4r15 := NOT(xC0);')
print('C4r31 := NOT(AND(xG4c15,(OR(xP4c15,xC0))));')
print('')

#Generating z
for i in range(0,16):
    print('S0c{0} := NOT(OR(S{0},S{1}));'.format(i,i+16))
for i in range(0,8):
    print('S1c{0} := NOT(AND(S0c{0},S0c{1}));'.format(i,i+8))
for i in range(0,4):
    print('S2c{0} := NOT(OR(S1c{0},S1c{1}));'.format(i,i+4))
for i in range(0,2):
    print('S3c{0} := NOT(OR(S2c{0},S2c{1}));'.format(i,i+2))
print('Z := NOT(AND(S3c0,S3c1));')
print('\n')

print('SAT := ODD(Z,nZ);')
print('ASSIGN SAT;')

#Generating v
#print('V := NOT(AND((NOT(NOT(OR(S31,(NOT(AND(A31,XB31))))))),(NOT(AND(S31,(NOT(OR(A31,XB31))))))));')
#print('\n')

#to verify that the bits from the two circuits are the same by CEC
#print('N := S31;')