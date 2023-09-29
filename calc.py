import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox
init_ra = 1
init_rb = 1

fa = np.linspace(0,1,1000)

def Fa(fa, ra, rb):
    return (ra*fa**2+fa*(1-fa))/(ra*fa**2+2*fa*(1-fa)+rb*(1-fa)**2)


fig, ax = plt.subplots(figsize=(8, 8))
line, = ax.plot(fa, Fa(fa, init_ra, init_rb), lw=2)
ax.plot(fa, fa, c='grey', linestyle='--')
ax.set_xlabel('fa')
ax.set_ylabel('Fa')

axra =   fig.add_axes([0.25, 0.06, 0.65, 0.02]) 
ra_slider = Slider(
    ax=axra,
    label='ra',
    valmin=0.1,
    valmax=5,
    valinit=init_ra,
)

axrb =  fig.add_axes([0.25, 0.02, 0.65, 0.02])
rb_slider = Slider(
    ax=axrb,
    label='rb',
    valmin=0.1,
    valmax=5,
    valinit=init_rb,
)

axra_text = fig.add_axes([0.1, 0.06, 0.1, 0.02])  
ra_text = TextBox(
    ax=axra_text,
    label='ra',
    initial=str(init_ra),
)
axrb_text = fig.add_axes([0.1, 0.02, 0.1, 0.02])  
rb_text = TextBox(
    ax=axrb_text,
    label='rb',
    initial=str(init_rb),
)

def update(val):
    line.set_ydata(Fa(fa, ra_slider.val, rb_slider.val))
    fig.canvas.draw_idle()

def update_from_text(val):
    ra_slider.set_val(float(ra_text.text))
    rb_slider.set_val(float(rb_text.text))
    update(None) 


ra_slider.on_changed(update)
rb_slider.on_changed(update)

ra_text.on_submit(update_from_text)
rb_text.on_submit(update_from_text)


plt.grid(True)
plt.show()