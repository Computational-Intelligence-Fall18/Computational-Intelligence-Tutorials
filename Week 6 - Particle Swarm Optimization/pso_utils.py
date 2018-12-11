import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from IPython.display import HTML

def data_point_creator(x_bound, y_bound, func, prec=.1):
    x = np.arange(-5.12, 5.12, prec)
    y = np.arange(-5.12, 5.12, prec)
    x, y = np.meshgrid(x, y)
    z = np.array(list(map(func, x, y)))
    return x, y, z

def three_d_plot(x, y, z, p_type='surface', genetic_points=None, with_countour=False, elev=45):
    fig = plt.figure()
    ax = fig.gca(projection='3d')


    plot_dict = {
        'surface': ax.plot_surface,
        'wireframe': ax.plot_wireframe,
    }
    
    assert p_type in plot_dict.keys()
    
    def animate(i):
        x_gen = genetic_points[i, :, 0]
        y_gen = genetic_points[i, :, 1]
        z_gen = genetic_points[i, :, 2]
        ax.clear()
        ax.scatter(x_gen, y_gen, z_gen, c='black',s=30)
        plot_dict[p_type](x, y, z)
        ax.contour(x, y, z, zdir='z', offset=-2, cmap=cm.coolwarm)
        ax.set_title('Generation {}'.format(i))
        ax.set_xlabel('X')
        ax.set_xlim(-10, 10)
        ax.set_ylabel('Y')
        ax.set_ylim(-10, 10)
        ax.set_zlabel('Z')
        ax.set_zlim(-2.2, 100)
        ax.view_init(elev=elev)
        

        return ax
    
    plot_dict[p_type](x, y, z)
    
    if with_countour :
#         cset = ax.contour(x, y, z, zdir='z', offset=-25, cmap=cm.coolwarm)
#         cset = ax.contour(x, y, z, zdir='x', offset=-10, cmap=cm.coolwarm)
        cset = ax.contour(x, y, z, zdir='y', offset=10, cmap=cm.coolwarm)
        ax.set_xlabel('X')
        ax.set_xlim(-10, 10)
        ax.set_ylabel('Y')
        ax.set_ylim(-10, 10)
        ax.set_zlabel('Z')
        ax.set_zlim(-25, 25)
    if not(genetic_points is None) :
        anim = animation.FuncAnimation(fig, animate, frames=genetic_points.shape[0], interval=200)
        plt.close()
        # call our new function to display the animation
        return HTML(anim.to_jshtml())
    
def two_d_plot(x, y, z, genetic_points=None, with_countour=False, elev=45):
    fig = plt.figure()
    ax = fig.gca()
     
    def animate(i):
        x_gen = genetic_points[i, :, 0]
        y_gen = genetic_points[i, :, 1]
        ax.clear()
        ax.scatter(x_gen, y_gen, c='black',s=30)
        ax.contour(x, y, z, zdir='z', offset=-2, cmap=cm.coolwarm)
        ax.set_title('Generation {}'.format(i))
        ax.set_xlabel('X')
        ax.set_xlim(-10, 10)
        ax.set_ylabel('Y')
        ax.set_ylim(-10, 10)
        return ax
    
    
    if with_countour :
        cset = ax.contour(x, y, z, zdir='y', offset=10, cmap=cm.coolwarm)
        ax.set_xlabel('X')
        ax.set_xlim(-10, 10)
        ax.set_ylabel('Y')
        ax.set_ylim(-10, 10)
    if not(genetic_points is None) :
        anim = animation.FuncAnimation(fig, animate, frames=genetic_points.shape[0], interval=200)
        plt.close()
        # call our new function to display the animation
        return HTML(anim.to_jshtml())
    
de_jong_func = lambda x, y: x**2 + y**2
a_p_hyper_ellipsoid_func = lambda x, y: x**2 + 2*y**2
ros_valley_func = lambda x, y: 100*(y - x**2)**2 + (1 -x)**2
rastrigin_func = lambda x, y: 20 + np.floor(x**2 + 10*np.cos(2*np.pi*x)) + np.floor(y**2 + 10*np.cos(2*np.pi*y))
multi_rastrigin_func = lambda x: 10*len(x) + sum([np.floor(i**2 + 10*np.cos(2*np.pi*i)) for i in x])