from sympy import *

## ELEMENTOS >> 5#
# GDL >> 4#

# VARIABLES COMUNES A LOS 5 ELEMENTOS

E, G = symbols('E G')
E = 2 * 10 ** 6
G = 8 * 10 ** 5
# DEFINIENDO VARIABLES PARA TODOS LOS ELEMENTOS#
A, L, I, k, bri, brd, ang, c1, c2, c3, c4, c5, c6 = symbols(
    'A L I k bri brd ang c1 c2 c3 c4 c5 c6')

# DETERMINANDO VARIABLES DE C/D ELEMENTO#

# ELEMENTO 1#
# VARIABLES#
A = .3 * .5  # AREA DE LA SECCION TRANSVERSAL
L = 3  # LONGITUD DEL ELEMENTO
I = .3 ** 3 * .5 / 12  # MOMENTO DE INERCIA
k = 1.2  # FACTOR DE FORMA
bri = bri  # BRAZO RIGIDO IZQUIERDO >>MATRIZ H
brd = bri  # BRAZO RIGIGO DERECHO >> MATRIZ H
ang = pi / 2  # ANGULO >> MATRIZ B

Ar = A / k  # AREA DE CORTE
a = 12 * E * I / (L ** 2 * Ar * G)

# MATRIZ B#
B1 = Matrix([[cos(ang), -sin(ang), 0, 0, 0, 0], [sin(ang), cos(ang), 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
             [0, 0, 0, cos(ang), -sin(ang), 0], [0, 0, 0, sin(ang), cos(ang), 0], [0, 0, 0, 0, 0, 1]])

# MATRIZ H#
H1 = Matrix([[1, 0, 0, 0, 0, 0, ], [0, 1, bri, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, -brd],
             [0, 0, 0, 0, 0, 1]])

# MATRIZ DE RIGIDEZ EN SMA LOCAL >> CONSIDERANDO DEFORMACIONES X FLEXION Y CORTE#
k1 = Matrix([[E * A / L, 0, 0, -E * A / L, 0, 0],
             [0, 12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              -12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a))],
             [-E * A / L, 0, 0, E * A / L, 0, 0],
             [0, -12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a))]])

# TRANSFORMACION DE LA MATRIZ DE RIGIDEZ EN SMA GBL#
K1 = B1 * k1 * B1.T

# ELEMENTO 2#
# VARIABLES#
A = .3 * .5  # AREA DE LA SECCION TRANSVERSAL
L = 3  # LONGITUD DEL ELEMENTO
I = .3 ** 3 * .5 / 12  # MOMENTO DE INERCIA
k = 1.2  # FACTOR DE FORMA
bri = bri  # BRAZO RIGIDO IZQUIERDO >>MATRIZ H
brd = brd  # BRAZO RIGIGO DERECHO >> MATRIZ H
ang = pi / 2  # ANGULO >> MATRIZ B

Ar = A / k  # AREA DE CORTE
a = 12 * E * I / (L ** 2 * Ar * G)

# MATRIZ B#
B2 = Matrix([[cos(ang), -sin(ang), 0, 0, 0, 0], [sin(ang), cos(ang), 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
             [0, 0, 0, cos(ang), -sin(ang), 0], [0, 0, 0, sin(ang), cos(ang), 0], [0, 0, 0, 0, 0, 1]])

# MATRIZ H#
H2 = Matrix([[1, 0, 0, 0, 0, 0, ], [0, 1, bri, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, -brd],
             [0, 0, 0, 0, 0, 1]])

# MATRIZ DE RIGIDEZ EN SMA LOCAL >> CONSIDERANDO DEFORMACIONES X FLEXION Y CORTE#
k2 = Matrix([[E * A / L, 0, 0, -E * A / L, 0, 0],
             [0, 12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              -12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a))],
             [-E * A / L, 0, 0, E * A / L, 0, 0],
             [0, -12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a))]])

# TRANSFORMACION DE LA MATRIZ DE RIGIDEZ EN SMA GBL#
K2 = B2 * k2 * B2.T

# ELEMENTO 3#
# VARIABLES#
A = .3 * .5  # AREA DE LA SECCION TRANSVERSAL
L = 3  # LONGITUD DEL ELEMENTO
I = .3 ** 3 * .5 / 12  # MOMENTO DE INERCIA
k = 1.2  # FACTOR DE FORMA
bri = bri  # BRAZO RIGIDO IZQUIERDO >>MATRIZ H
brd = brd  # BRAZO RIGIGO DERECHO >> MATRIZ H
ang = pi / 2  # ANGULO >> MATRIZ B

Ar = A / k  # AREA DE CORTE
a = 12 * E * I / (L ** 2 * Ar * G)

# MATRIZ B#
B3 = Matrix([[cos(ang), -sin(ang), 0, 0, 0, 0], [sin(ang), cos(ang), 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
             [0, 0, 0, cos(ang), -sin(ang), 0], [0, 0, 0, sin(ang), cos(ang), 0], [0, 0, 0, 0, 0, 1]])

# MATRIZ H#
H3 = Matrix([[1, 0, 0, 0, 0, 0, ], [0, 1, bri, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, -brd],
             [0, 0, 0, 0, 0, 1]])

# MATRIZ DE RIGIDEZ EN SMA LOCAL >> CONSIDERANDO DEFORMACIONES X FLEXION Y CORTE#
k3 = Matrix([[E * A / L, 0, 0, -E * A / L, 0, 0],
             [0, 12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              -12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a))],
             [-E * A / L, 0, 0, E * A / L, 0, 0],
             [0, -12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a))]])

# TRANSFORMACION DE LA MATRIZ DE RIGIDEZ EN SMA GBL#
K3 = B3 * k3 * B3.T

# ELEMENTO 4#
# VARIABLES#
A = .3 * .5  # AREA DE LA SECCION TRANSVERSAL
L = 6  # LONGITUD DEL ELEMENTO
I = .3 * .5 ** 3 / 12  # MOMENTO DE INERCIA
k = 1.2  # FACTOR DE FORMA
bri = bri  # BRAZO RIGIDO IZQUIERDO >>MATRIZ H
brd = brd  # BRAZO RIGIGO DERECHO >> MATRIZ H
ang = 0  # ANGULO >> MATRIZ B

Ar = A / k  # AREA DE CORTE
a = 12 * E * I / (L ** 2 * Ar * G)

# MATRIZ B#
B4 = Matrix([[cos(ang), -sin(ang), 0, 0, 0, 0], [sin(ang), cos(ang), 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
             [0, 0, 0, cos(ang), -sin(ang), 0], [0, 0, 0, sin(ang), cos(ang), 0], [0, 0, 0, 0, 0, 1]])

# MATRIZ H#
H4 = Matrix([[1, 0, 0, 0, 0, 0, ], [0, 1, bri, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, -brd],
             [0, 0, 0, 0, 0, 1]])

# MATRIZ DE RIGIDEZ EN SMA LOCAL >> CONSIDERANDO DEFORMACIONES X FLEXION Y CORTE#
k4 = Matrix([[E * A / L, 0, 0, -E * A / L, 0, 0],
             [0, 12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              -12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a))],
             [-E * A / L, 0, 0, E * A / L, 0, 0],
             [0, -12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a))]])

# TRANSFORMACION DE LA MATRIZ DE RIGIDEZ EN SMA GBL#
K4 = B4 * k4 * B1.T

# ELEMENTO 5#
# VARIABLES#
A = .3 * .5  # AREA DE LA SECCION TRANSVERSAL
L = 6  # LONGITUD DEL ELEMENTO
I = .3 * .5 ** 3 / 12  # MOMENTO DE INERCIA
k = 1.2  # FACTOR DE FORMA
bri = bri  # BRAZO RIGIDO IZQUIERDO >>MATRIZ H
brd = brd  # BRAZO RIGIGO DERECHO >> MATRIZ H
ang = 0  # ANGULO >> MATRIZ B

Ar = A / k  # AREA DE CORTE
a = 12 * E * I / (L ** 2 * Ar * G)

# MATRIZ B#
B5 = Matrix([[cos(ang), -sin(ang), 0, 0, 0, 0], [sin(ang), cos(ang), 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
             [0, 0, 0, cos(ang), -sin(ang), 0], [0, 0, 0, sin(ang), cos(ang), 0], [0, 0, 0, 0, 0, 1]])

# MATRIZ H#
H5 = Matrix([[1, 0, 0, 0, 0, 0, ], [0, 1, bri, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, -brd],
             [0, 0, 0, 0, 0, 1]])

# MATRIZ DE RIGIDEZ EN SMA LOCAL >> CONSIDERANDO DEFORMACIONES X FLEXION Y CORTE#
k5 = Matrix([[E * A / L, 0, 0, -E * A / L, 0, 0],
             [0, 12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              -12 * E * I / L ** 3 * (1 / (1 + a)), 6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a))],
             [-E * A / L, 0, 0, E * A / L, 0, 0],
             [0, -12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a)), 0,
              12 * E * I / L ** 3 * (1 / (1 + a)), -6 * E * I / L ** 2 * (1 / (1 + a))],
             [0, 6 * E * I / L ** 2 * (1 / (1 + a)), (2 - a) * E * I / L * (1 / (1 + a)), 0,
              -6 * E * I / L ** 2 * (1 / (1 + a)), (4 + a) * E * I / L * (1 / (1 + a))]])

# TRANSFORMACION DE LA MATRIZ DE RIGIDEZ EN SMA GBL#
K5 = B5 * k5 * B5.T

# PROBLEMA PRIMARIO#

# DEFINIENDO VARIABLES COMUNES#
w, L = symbols('w L')

# ELEMENTO 4#

L = 6
w = 3
E4i1j1 = w * L / 2
E4i2j1 = w * L ** 2 / 12
E4i3j1 = w * L / 2
E4i4j1 = -w * L ** 2 / 12

# ELEMENTO 5#

L = 6
w = 3
E5i1j1 = w * L / 2
E5i2j1 = w * L ** 2 / 12
E5i3j1 = w * L / 2
E5i4j1 = -w * L ** 2 / 12

# VECTOR DE CARGAS DE FIJACION EN SMA LOCAL#
r4 = Matrix([[0], [E4i1j1], [E4i2j1], [0], [E4i3j1], [E4i4j1]])
r5 = Matrix([[0], [E5i1j1], [E5i2j1], [0], [E5i3j1], [E5i4j1]])

# VECTOR DE CARGAS DE FIJACION EN SMA GBL
R4 = B4 * r4
R5 = B5 * r5

# APLICANDO LOS CODIGOS DE CONECTIVIDAD
MR4i1j1 = R4.extract([0], [0])  # 1
MR4i2j1 = R4.extract([1], [0])  # R
MR4i3j1 = R4.extract([2], [0])  # 2
MR4i4j1 = R4.extract([3], [0])  # 1
MR4i5j1 = R4.extract([4], [0])  # R
MR4i6j1 = R4.extract([5], [0])  # 3

MR5i1j1 = R5.extract([0], [0])  # 1
MR5i2j1 = R5.extract([1], [0])  # R
MR5i3j1 = R5.extract([2], [0])  # 3
MR5i4j1 = R5.extract([3], [0])  # 1
MR5i5j1 = R5.extract([4], [0])  # R
MR5i6j1 = R5.extract([5], [0])  # 4

# ENSAMBLAMOS EL VECTOR DE CARGAS DE FIJACION ANTERIOR >> RGBL
RGBL = Matrix([[MR4i1j1 + MR4i4j1 + MR5i1j1 + MR5i4j1],
              [MR4i3j1], [MR4i6j1 + MR5i3j1], [MR5i6j1]])

# PROBLEMA COMPLEMENTARIO#

# ENSAMBLAMOS LA MATRIZ DE RIGIDEZ GLOBAL#

# ELEMENTO 1#
# CODIGO DE CONECTIVIDAD >> R R R 1 R 2

c1 = 0
c2 = 0
c3 = 0
c4 = 1
c5 = 0
c6 = 2

if c1 == 0:
    K1.col_del(0)
    K1.row_del(0)
else:
    K1

if c2 == 0:
    if c1 == 0:
        K1.col_del(c2)
        K1.row_del(c2)
    else:
        K1.col_del(c1)
        K1.row_del(c1)
else:
    K1

if c3 == 0:
    if c2 == 0:
        if c1 == 0:
            K1.col_del(c3)
            K1.row_del(c3)
        else:
            K1.col_del(c1)
            K1.row_del(c1)
    else:
        K1.col_del(c2)
        K1.row_del(c2)
else:
    K1

if c4 == 0:
    if c3 == 0:
        if c2 == 0:
            if c1 == 0:
                K1.col_del(c4)
                K1.row_del(c4)
            else:
                K1.col_del(c1)
                K1.row_del(c1)
        else:
            K1.col_del(c2)
            K1.row_del(c2)
    else:
        K1.col_del(c3)
        K1.row_del(c3)
else:
    K1

if c5 == 0:
    if c4 == 0:
        if c3 == 0:
            if c2 == 0:
                if c1 == 0:
                    K1.col_del(c5)
                    K1.row_del(c5)
                else:
                    K1.col_del(c1)
                    K1.row_del(c1)
            else:
                K1.col_del(c2)
                K1.row_del(c2)
        else:
            K1.col_del(c3)
            K1.row_del(c3)
    else:
        K1.col_del(c4)
        K1.row_del(c4)
else:
    K1

if c6 == 0:
    if c5 == 0:
        if c4 == 0:
            if c3 == 0:
                if c2 == 0:
                    if c1 == 0:
                        K1.col_del(c6)
                        K1.row_del(c6)
                    else:
                        K1.col_del(c1)
                        K1.row_del(c1)
                else:
                    K1.col_del(c2)
                    K1.row_del(c2)
            else:
                K1.col_del(c3)
                K1.row_del(c3)
        else:
            K1.col_del(c4)
            K1.row_del(c4)
    else:
        K1.col_del(c5)
        K1.row_del(c5)
else:
    K1

# ELEMENTO 2#
# CODIGO DE CONECTIVIDAD >> R R R 1 R 3

c1 = 0
c2 = 0
c3 = 0
c4 = 1
c5 = 0
c6 = 2

if c1 == 0:
    K2.col_del(0)
    K2.row_del(0)
else:
    K2

if c2 == 0:
    if c1 == 0:
        K2.col_del(c2)
        K2.row_del(c2)
    else:
        K2.col_del(c1)
        K2.row_del(c1)
else:
    K2

if c3 == 0:
    if c2 == 0:
        if c1 == 0:
            K2.col_del(c3)
            K2.row_del(c3)
        else:
            K2.col_del(c1)
            K2.row_del(c1)
    else:
        K2.col_del(c2)
        K2.row_del(c2)
else:
    K2

if c4 == 0:
    if c3 == 0:
        if c2 == 0:
            if c1 == 0:
                K2.col_del(c4)
                K2.row_del(c4)
            else:
                K2.col_del(c1)
                K2.row_del(c1)
        else:
            K2.col_del(c2)
            K2.row_del(c2)
    else:
        K2.col_del(c3)
        K2.row_del(c3)
else:
    K2

if c5 == 0:
    if c4 == 0:
        if c3 == 0:
            if c2 == 0:
                if c1 == 0:
                    K2.col_del(c5)
                    K2.row_del(c5)
                else:
                    K2.col_del(c1)
                    K2.row_del(c1)
            else:
                K2.col_del(c2)
                K2.row_del(c2)
        else:
            K2.col_del(c3)
            K2.row_del(c3)
    else:
        K2.col_del(c4)
        K2.row_del(c4)
else:
    K2

if c6 == 0:
    if c5 == 0:
        if c4 == 0:
            if c3 == 0:
                if c2 == 0:
                    if c1 == 0:
                        K2.col_del(c6)
                        K2.row_del(c6)
                    else:
                        K2.col_del(c1)
                        K2.row_del(c1)
                else:
                    K2.col_del(c2)
                    K2.row_del(c2)
            else:
                K2.col_del(c3)
                K2.row_del(c3)
        else:
            K2.col_del(c4)
            K2.row_del(c4)
    else:
        K2.col_del(c5)
        K2.row_del(c5)
else:
    K2

# ELEMENTO 3#
# CODIGO DE CONECTIVIDAD >> R R R 1 R 4

c1 = 0
c2 = 0
c3 = 0
c4 = 1
c5 = 0
c6 = 2

if c1 == 0:
    K3.col_del(0)
    K3.row_del(0)
else:
    K3

if c2 == 0:
    if c1 == 0:
        K3.col_del(c2)
        K3.row_del(c2)
    else:
        K3.col_del(c1)
        K3.row_del(c1)
else:
    K3

if c3 == 0:
    if c2 == 0:
        if c1 == 0:
            K3.col_del(c3)
            K3.row_del(c3)
        else:
            K3.col_del(c1)
            K3.row_del(c1)
    else:
        K3.col_del(c2)
        K3.row_del(c2)
else:
    K3

if c4 == 0:
    if c3 == 0:
        if c2 == 0:
            if c1 == 0:
                K3.col_del(c4)
                K3.row_del(c4)
            else:
                K3.col_del(c1)
                K3.row_del(c1)
        else:
            K3.col_del(c2)
            K3.row_del(c2)
    else:
        K3.col_del(c3)
        K3.row_del(c3)
else:
    K3

if c5 == 0:
    if c4 == 0:
        if c3 == 0:
            if c2 == 0:
                if c1 == 0:
                    K3.col_del(c5)
                    K3.row_del(c5)
                else:
                    K3.col_del(c1)
                    K3.row_del(c1)
            else:
                K3.col_del(c2)
                K3.row_del(c2)
        else:
            K3.col_del(c3)
            K3.row_del(c3)
    else:
        K3.col_del(c4)
        K3.row_del(c4)
else:
    K3

if c6 == 0:
    if c5 == 0:
        if c4 == 0:
            if c3 == 0:
                if c2 == 0:
                    if c1 == 0:
                        K3.col_del(c6)
                        K3.row_del(c6)
                    else:
                        K3.col_del(c1)
                        K3.row_del(c1)
                else:
                    K3.col_del(c2)
                    K3.row_del(c2)
            else:
                K3.col_del(c3)
                K3.row_del(c3)
        else:
            K3.col_del(c4)
            K3.row_del(c4)
    else:
        K3.col_del(c5)
        K3.row_del(c5)
else:
    K3

# ELEMENTO 4#
# CODIGO DE CONECTIVIDAD >> 1 R 2 1 R 3

c1 = 1
c2 = 0
c3 = 2
c4 = 3
c5 = 0
c6 = 4

if c1 == 0:
    K4.col_del(0)
    K4.row_del(0)
else:
    K4

if c2 == 0:
    if c1 == 0:
        K4.col_del(c2)
        K4.row_del(c2)
    else:
        K4.col_del(c1)
        K4.row_del(c1)
else:
    K4

if c3 == 0:
    if c2 == 0:
        if c1 == 0:
            K4.col_del(c3)
            K4.row_del(c3)
        else:
            K4.col_del(c1)
            K4.row_del(c1)
    else:
        K4.col_del(c2)
        K4.row_del(c2)
else:
    K4

if c4 == 0:
    if c3 == 0:
        if c2 == 0:
            if c1 == 0:
                K4.col_del(c4)
                K4.row_del(c4)
            else:
                K4.col_del(c1)
                K4.row_del(c1)
        else:
            K4.col_del(c2)
            K4.row_del(c2)
    else:
        K4.col_del(c3)
        K4.row_del(c3)
else:
    K4

if c5 == 0:
    if c4 == 0:
        if c3 == 0:
            if c2 == 0:
                if c1 == 0:
                    K4.col_del(c5)
                    K4.row_del(c5)
                else:
                    K4.col_del(c1)
                    K4.row_del(c1)
            else:
                K4.col_del(c2)
                K4.row_del(c2)
        else:
            K4.col_del(c3)
            K4.row_del(c3)
    else:
        K4.col_del(c4)
        K4.row_del(c4)
else:
    K4

if c6 == 0:
    if c5 == 0:
        if c4 == 0:
            if c3 == 0:
                if c2 == 0:
                    if c1 == 0:
                        K4.col_del(c6)
                        K4.row_del(c6)
                    else:
                        K4.col_del(c1)
                        K4.row_del(c1)
                else:
                    K4.col_del(c2)
                    K4.row_del(c2)
            else:
                K4.col_del(c3)
                K4.row_del(c3)
        else:
            K4.col_del(c4)
            K4.row_del(c4)
    else:
        K4.col_del(c5)
        K4.row_del(c5)
else:
    K4

# ELEMENTO 5#
# CODIGO DE CONECTIVIDAD >> 1 R 3 1 R 4

c1 = 1
c2 = 0
c3 = 2
c4 = 3
c5 = 0
c6 = 4

if c1 == 0:
    K5.col_del(0)
    K5.row_del(0)
else:
    K5

if c2 == 0:
    if c1 == 0:
        K5.col_del(c2)
        K5.row_del(c2)
    else:
        K5.col_del(c1)
        K5.row_del(c1)
else:
    K5

if c3 == 0:
    if c2 == 0:
        if c1 == 0:
            K5.col_del(c3)
            K5.row_del(c3)
        else:
            K5.col_del(c1)
            K5.row_del(c1)
    else:
        K5.col_del(c2)
        K5.row_del(c2)
else:
    K5

if c4 == 0:
    if c3 == 0:
        if c2 == 0:
            if c1 == 0:
                K5.col_del(c4)
                K5.row_del(c4)
            else:
                K5.col_del(c1)
                K5.row_del(c1)
        else:
            K5.col_del(c2)
            K5.row_del(c2)
    else:
        K5.col_del(c3)
        K5.row_del(c3)
else:
    K5

if c5 == 0:
    if c4 == 0:
        if c3 == 0:
            if c2 == 0:
                if c1 == 0:
                    K5.col_del(c5)
                    K5.row_del(c5)
                else:
                    K5.col_del(c1)
                    K5.row_del(c1)
            else:
                K5.col_del(c2)
                K5.row_del(c2)
        else:
            K5.col_del(c3)
            K5.row_del(c3)
    else:
        K5.col_del(c4)
        K5.row_del(c4)
else:
    K5

if c6 == 0:
    if c5 == 0:
        if c4 == 0:
            if c3 == 0:
                if c2 == 0:
                    if c1 == 0:
                        K5.col_del(c6)
                        K5.row_del(c6)
                    else:
                        K5.col_del(c1)
                        K5.row_del(c1)
                else:
                    K5.col_del(c2)
                    K5.row_del(c2)
            else:
                K5.col_del(c3)
                K5.row_del(c3)
        else:
            K5.col_del(c4)
            K5.row_del(c4)
    else:
        K5.col_del(c5)
        K5.row_del(c5)
else:
    K5

# EXTRAYENDO ELEMENTOS#
# ELEMENTO 1#
M1i1j1 = K1.extract([0], [0])  # 11
M1i1j2 = K1.extract([0], [1])  # 12
M1i2j1 = K1.extract([1], [0])  # 21
M1i2j2 = K1.extract([1], [1])  # 22
# ELEMENTO 2#
M2i1j1 = K2.extract([0], [0])  # 11
M2i1j2 = K2.extract([0], [1])  # 13
M2i2j1 = K2.extract([1], [0])  # 31
M2i2j2 = K2.extract([1], [1])  # 33
# ELEMENTO 3#
M3i1j1 = K3.extract([0], [0])  # 11
M3i1j2 = K3.extract([0], [1])  # 14
M3i2j1 = K3.extract([1], [0])  # 41
M3i2j2 = K3.extract([1], [1])  # 44
# ELEMENTO 4#
M4i1j1 = K4.extract([0], [0])  # 11
M4i1j2 = K4.extract([0], [1])  # 12
M4i1j3 = K4.extract([0], [2])  # 11
M4i1j4 = K4.extract([0], [3])  # 13

M4i2j1 = K4.extract([1], [0])  # 21
M4i2j2 = K4.extract([1], [1])  # 22
M4i2j3 = K4.extract([1], [2])  # 21
M4i2j4 = K4.extract([1], [3])  # 23

M4i3j1 = K4.extract([2], [0])  # 11
M4i3j2 = K4.extract([2], [1])  # 12
M4i3j3 = K4.extract([2], [2])  # 11
M4i3j4 = K4.extract([2], [3])  # 13

M4i4j1 = K4.extract([3], [0])  # 31
M4i4j2 = K4.extract([3], [1])  # 32
M4i4j3 = K4.extract([3], [2])  # 31
M4i4j4 = K4.extract([3], [3])  # 33
# ELEMENTO 5#
M5i1j1 = K5.extract([0], [0])  # 11
M5i1j2 = K5.extract([0], [1])  # 13
M5i1j3 = K5.extract([0], [2])  # 11
M5i1j4 = K5.extract([0], [3])  # 14

M5i2j1 = K5.extract([1], [0])  # 31
M5i2j2 = K5.extract([1], [1])  # 33
M5i2j3 = K5.extract([1], [2])  # 31
M5i2j4 = K5.extract([1], [3])  # 34

M5i3j1 = K5.extract([2], [0])  # 11
M5i3j2 = K5.extract([2], [1])  # 13
M5i3j3 = K5.extract([2], [2])  # 11
M5i3j4 = K5.extract([2], [3])  # 14

M5i4j1 = K5.extract([3], [0])  # 41
M5i4j2 = K5.extract([3], [1])  # 43
M5i4j3 = K5.extract([3], [2])  # 41
M5i4j4 = K5.extract([3], [3])  # 44

# MATRIZ DE RIGIDEZ GLOBAL#

KGBL = Matrix([[M1i1j1 + M2i1j1 + M3i1j1 + M4i1j1 + M4i1j3 + M4i3j1 + M4i3j3 + M5i1j1 + M5i1j3 + M5i3j1 + M5i3j3,
                M1i1j2 + M4i1j2 + M4i3j2, M2i1j2 + M4i1j4 + M4i3j4 + M5i1j2 + M5i3j2, M3i1j2 + M5i1j4 + M5i3j4],
               [M1i2j1 + M4i2j1 + M4i2j3, M1i2j2 +
                   M4i2j2, M4i2j4, Matrix([[0]])],
               [M2i2j1 + M4i4j1 + M4i4j3 + M5i2j1 + M5i2j3,
                   M4i4j2, M2i2j2 + M4i4j4 + M5i2j2, M5i2j4],
               [M3i2j1 + M5i4j1 + M5i4j3, Matrix([[0]]), M5i4j2, M3i2j2 + M5i4j4]])

# DESPLAZAMIENTOS GLOBALES
CN = Matrix([[12], [0], [0], [0]])  # CARGAS SOBRE LOS NUDOS
R = RGBL + CN
Q = -R

DGBL = KGBL ** -1 * Q

DGBLi1j1 = DGBL.extract([0], [0])  # 1
DGBLi2j1 = DGBL.extract([1], [0])  # 2
DGBLi3j1 = DGBL.extract([2], [0])  # 3
DGBLi4j1 = DGBL.extract([3], [0])  # 4

# CONTINUACION DEL PROBLEMA COMPLEMENTARIO
# DETERMINACION DE CARGAS EN EXTREMO DE BARRA

# DESPLAZAMIENTOS LOCALES

# ELEMENTO 1#
# CODIGO DE CONECTIVIDAD >> R R R 1 R 2
d1gbl = Matrix([[0], [0], [0], [DGBLi1j1], [0], [DGBLi2j1]])
d1lcl = B1.T * d1gbl

# ELEMENTO 2#
# CODIGO DE CONECTIVIDAD >> R R R 1 R 3
d2gbl = Matrix([[0], [0], [0], [DGBLi1j1], [0], [DGBLi3j1]])
d2lcl = B1.T * d2gbl

# ELEMENTO 3#
# CODIGO DE CONECTIVIDAD >> R R R 1 R 4
d3gbl = Matrix([[0], [0], [0], [DGBLi1j1], [0], [DGBLi4j1]])
d3lcl = B1.T * d3gbl

# ELEMENTO 4#
# CODIGO DE CONECTIVIDAD >> 1 R 2 1 R 3
d4gbl = Matrix([[DGBLi1j1], [0], [DGBLi2j1], [DGBLi1j1], [0], [DGBLi3j1]])
d4lcl = B1.T * d4gbl

# ELEMENTO 5#
# CODIGO DE CONECTIVIDAD >> 1 R 3 1 R 4
d5gbl = Matrix([[DGBLi1j1], [0], [DGBLi3j1], [DGBLi1j1], [0], [DGBLi4j1]])
d5lcl = B1.T * d5gbl

# FUERZAS LOCALES

# ELEMENTO 1
q1 = (k1 * d1lcl).evalf(2)

# ELEMENTO 2
q2 = (k2 * d2lcl).evalf(2)

# ELEMENTO 3
q3 = (k3 * d3lcl).evalf(2)

# ELEMENTO 4
q4 = (k4 * d4lcl + r4).evalf(2)

# ELEMENTO 5
q5 = (k5 * d5lcl + r5).evalf(2)
