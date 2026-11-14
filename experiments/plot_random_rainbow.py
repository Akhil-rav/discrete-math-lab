"""Plot saved exact probabilities; requires optional requirements-figures.txt.

Run: python -m experiments.plot_random_rainbow
Only this presentation layer converts rational values to floating point.
"""
import json
from fractions import Fraction
from pathlib import Path


def render():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    root=Path(__file__).resolve().parents[1]
    data=json.loads((root/'results/data/random_rainbow.json').read_text())
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                         'axes.spines.top':False,'axes.spines.right':False,
                         'svg.fonttype':'none','svg.hashsalt':'discrete-math-lab-random-rainbow'})
    fig,axes=plt.subplots(1,2,figsize=(11.8,4.5),layout='constrained')
    colors={'C8':'#B65E3B','2C4':'#28786E','cube':'#19354A'}
    names={'C8':'Cycle C8 (8 edges)','2C4':'Two squares (8 edges)','cube':'Cube (12 edges)'}
    for name in ('C8','2C4','cube'):
        rows=data['hosts'][name]['palettes']
        axes[0].plot([r['q'] for r in rows],
                     [float(Fraction(r['rainbow_probability'])) for r in rows],
                     color=colors[name],label=names[name],linewidth=2,marker='o',markersize=3)
    axes[0].set_title('Three hosts on eight vertices',loc='left',fontweight='bold')
    axes[0].legend(loc='lower right',frameon=False,fontsize=9)
    rows=data['hosts']['cube']['palettes']
    q=[r['q'] for r in rows]
    lower=[float(Fraction(r['second_moment_lower'])) for r in rows]
    upper=[float(Fraction(r['union_upper'])) for r in rows]
    axes[1].fill_between(q,lower,upper,color='#E7EEF2',label='Moment-bound interval')
    axes[1].plot(q,upper,color='#647F9B',linestyle='--',label='First-moment upper bound')
    axes[1].plot(q,lower,color='#B65E3B',linestyle=':',linewidth=2,label='Second-moment lower bound')
    axes[1].plot(q,[float(Fraction(r['rainbow_probability'])) for r in rows],
                 color='#19354A',linewidth=2,marker='o',markersize=3,label='Exact cube probability')
    axes[1].set_title('Cube: exact counts and moment bounds',loc='left',fontweight='bold')
    axes[1].legend(loc='lower right',frameon=False,fontsize=8.5)
    for ax in axes:
        ax.set(xlim=(1,24),ylim=(-0.015,1.035),xlabel='Available colors q',
               ylabel='Probability of a rainbow perfect matching')
        ax.set_xticks([1,4,8,12,16,20,24])
        ax.grid(axis='y',color='#E0E5EA',linewidth=0.7)
        ax.set_axisbelow(True)
    fig.suptitle('Independent uniform edge colors',fontsize=15,fontweight='bold',x=0.01,ha='left')
    output=root/'results/figures'
    output.mkdir(exist_ok=True)
    fig.savefig(output/'random_rainbow.svg',metadata={'Date':None})
    svg=output/'random_rainbow.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',
                   encoding='utf-8',newline='\n')
    fig.savefig(output/'random_rainbow.png',dpi=180)
    plt.close(fig)
    print('Rendered probability comparison with Matplotlib',matplotlib.__version__)


if __name__ == '__main__':
    render()
