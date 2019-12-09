import turtle

turtle.Screen()
turtle.shape('turtle')
turtle.color('darkgreen')
turtle.speed('slowest')

# ===================
# 1: Largada

 turtle.forward(200)

# ===================
# 2: Dando a volta no abismo

# turtle.circle(100,180)

# ===================
# 3: Pulando pedras
'''
def turtle_jump(n=1):
	for i in range(1, n+1):
		turtle.right(90)
		turtle.circle(35, -180)
		turtle.right(90)
		turtle.forward(20)

turtle_jump(3)
'''

# ===================
# 4: Contornando o beco sem saída

#turtle.backward(50)
#turtle.right(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(200)

# ===================
# 5: Resolvendo o labirinto

'''
turtle.forward(20)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
'''

# Fim da corrida
turtle.done()
