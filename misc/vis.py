import matplotlib.pyplot as plt
import numpy
from mpl_toolkits.mplot3d import Axes3D

figure = plt.figure()
ax = Axes3D(figure)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.zaxis.set_ticks([])
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))


def plot_it(x, y, z, colour):
    ax.plot_wireframe(x, y, z, rstride=1, cstride=1, color=colour)


centersR = numpy.arange(-1, 2)
centerx, centery = numpy.meshgrid(centersR, centersR)

plot_it(centerx, centery, numpy.full_like(centery, 3), "black")
plot_it(centery, centerx, numpy.full_like(centery, -3), "yellow")
plot_it(centerx, numpy.full_like(centery, 3), centery, "orange")
plot_it(centery, numpy.full_like(centery, -3), centerx, "red")
plot_it(numpy.full_like(centery, -3), centery, centerx, "green")
plot_it(numpy.full_like(centery, 3), centerx, centery, "blue")

postiveR = numpy.arange(1, 4)
negativeR = numpy.arange(-1, -4, -1)

posx, posy = numpy.meshgrid(postiveR, postiveR)
negx, negy = numpy.meshgrid(negativeR, negativeR)

pos3 = numpy.full_like(negx, 3)
neg3 = numpy.full_like(negx, -3)

plot_it(negx, negy, pos3, "black")
plot_it(posx, posy, pos3, "black")
plot_it(posx, negy, pos3, "black")
plot_it(negx, posy, pos3, "black")

plot_it(negx, negy, neg3, "yellow")
plot_it(posx, posy, neg3, "yellow")
plot_it(posx, negy, neg3, "yellow")
plot_it(negx, posy, neg3, "yellow")

plot_it(negx, neg3, negy, "red")
plot_it(negx, neg3, posy, "red")
plot_it(posx, neg3, negy, "red")
plot_it(posx, neg3, posy, "red")

plot_it(negx, pos3, negy, "orange")
plot_it(negx, pos3, posy, "orange")
plot_it(posx, pos3, negy, "orange")
plot_it(posx, pos3, posy, "orange")

plot_it(pos3, negx, negy, "blue")
plot_it(pos3, negx, posy, "blue")
plot_it(pos3, posx, negy, "blue")
plot_it(pos3, posx, posy, "blue")

plot_it(neg3, negx, negy, "green")
plot_it(neg3, negx, posy, "green")
plot_it(neg3, posx, negy, "green")
plot_it(neg3, posx, posy, "green")

edgesP = numpy.arange(1, 4)
edgesN = numpy.arange(-1, -4, -1)

eposx, eposy = numpy.meshgrid(edgesP, edgesP)
enegx, enegy = numpy.meshgrid(edgesN, edgesN)


plot_it(centerx, neg3, eposy, "red")
plot_it(centerx, neg3, enegy, "red")
plot_it(enegx, neg3, centery, "red")
plot_it(eposx, neg3, centery, "red")

plot_it(centerx, pos3, eposy, "orange")
plot_it(centerx, pos3, enegy, "orange")
plot_it(enegx, pos3, centery, "orange")
plot_it(eposx, pos3, centery, "orange")

plot_it(centerx, eposy, pos3, "black")
plot_it(centerx, enegy, pos3, "black")
plot_it(eposx, centery, pos3, "black")
plot_it(enegx, centery, pos3, "black")

plot_it(centerx, eposy, neg3, "yellow")
plot_it(centerx, enegy, neg3, "yellow")
plot_it(eposx, centery, neg3, "yellow")
plot_it(enegx, centery, neg3, "yellow")

plot_it(pos3, centery, enegx, "yellow")
plot_it(pos3, centery, enegy, "yellow")

alpha_plotX, alpha_plotY = numpy.meshgrid(numpy.arange(-3, 4, 1), numpy.arange(-3, 4, 1))
neg32 = numpy.full_like(alpha_plotX, -3)
ax.plot_surface(alpha_plotX, neg32, alpha_plotY, alpha=0.2, color="black")




plt.show()
