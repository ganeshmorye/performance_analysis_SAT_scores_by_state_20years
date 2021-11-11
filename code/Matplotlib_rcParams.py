# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (11.5,4.76)
# mpl.rcParams['figure.dpi'] = 1000
mpl.rcParams['figure.constrained_layout.use'] = True
mpl.rcParams['figure.constrained_layout.h_pad'] = 6./72.
mpl.rcParams['figure.constrained_layout.w_pad'] = 24./72.
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '-'
# mpl.rcParams['axes.facecolor'] = (0.914, 1.0, 1.0)
mpl.rcParams['axes.facecolor'] = '#FCF6F5FF'
# mpl.rcParams['figure.facecolor'] = (0.0, 0.0, 0.157)
# mpl.rcParams['figure.facecolor'] = '#990011FF'
mpl.rcParams['figure.facecolor'] = '#1d1e22'
mpl.rcParams['xtick.color'] = 'white'
mpl.rcParams['ytick.color'] = 'white'
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10
mpl.rcParams['ytick.left'] = True
mpl.rcParams['xtick.major.size'] = 6
mpl.rcParams['xtick.minor.size'] = 3
mpl.rcParams['ytick.major.size'] = 6
mpl.rcParams['ytick.minor.size'] = 3
mpl.rcParams['xtick.major.width'] = 1
mpl.rcParams['xtick.minor.width'] = 0.5
mpl.rcParams['ytick.major.width'] = 1
mpl.rcParams['ytick.minor.width'] = 0.5
mpl.rcParams['xtick.minor.visible'] =True
mpl.rcParams['ytick.minor.visible'] =False
mpl.rcParams['axes.grid'] = True
#mpl.rcParams['axes.grid.which'] = 'both'
#mpl.rcParams['grid.color'] = (0.85, 0.85, 0.85)

# plt.grid(b=True, which='major', color=(0.85, 0.85, 0.85), 
#           linestyle='-', alpha = 0.8, linewidth = 0.75)
# plt.grid(b=True, which='minor', color=(0.85, 0.85, 0.85, 0.5), 
#           linestyle='--', alpha = 0.8, linewidth = 0.25)

mpl.rcParams['axes.labelsize'] = 18
mpl.rcParams['axes.labelcolor'] = 'white'
#mpl.rcParams['axes.titlelocation'] = 'center'
mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['axes.xmargin'] = 0.05
#mpl.rcParams['axes.titlecolor'] = 'white'
mpl.rcParams['axes.titleweight'] = 'bold'
mpl.rc('axes', titlesize=24)
mpl.rcParams['text.color'] = 'white'
# Say, "the default sans-serif font is COMIC SANS"
mpl.rcParams['font.sans-serif'] = "Calibri"
# Then, "ALWAYS use sans-serif fonts"
mpl.rcParams['font.family'] = "sans-serif"

#mpl.rcParams['axes.spines.right'] = True

#box = axes.get_position()
#axes.set_position([0.05, 0.12, 0.9, box.height])

#box = axes.get_position()
#axes.set_position([box.x0, box.y0, box.width, box.height])

#legend_x = 1
#legend_y = 0.5
#plt.legend(["blue", "green"], loc='center left', bbox_to_anchor=(legend_x, legend_y))

#mpl.rcParams['figure.constrained_layout.use'] = True
#plt.tight_layout()