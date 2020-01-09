import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io, base64
import pickle

def base64_visualization(id):
    #Code by David Nagy and Zhenya Warshavsky
    df = pd.read_pickle('./data/df_v2.pkl')
    X = df.drop(['id', 'songid', 'artist', 'track', 'key', 'mode', 'duration_ms', 'time_signature'], axis=1)
    labels = [name.capitalize() for name in X.columns]
    X_visual = pickle.load(open('./data/X_visual.pkl', 'rb'))

    key_notation = {0: 'C', 1: 'C-sharp', 2: 'D', 3: 'D-sharp',
                    4: 'E', 5: 'F', 6: 'F-sharp', 7: 'G', 8: 'G-sharp',
                    9: 'A', 10: 'B-flat', 11: 'B'}
    mode_notation = {0: 'Minor', 1: 'Major'}
    fig = plt.figure(facecolor='#171330', figsize=(5,5))
    ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True, facecolor='#EF019F')
    data = X_visual[id]
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / 9)
    radii = data
    p = []
    for i in range(9):
        p.append((theta[i], radii[i]))
    poly = plt.Polygon(p, ec="k", color='#780150')
    ax.add_patch(poly)
    ax.set_xticks(theta)
    ax.set_xticklabels(labels, rotation=45, color='white', fontweight='bold')
    ax.set_yticklabels([])
    ax.grid(b=False, axis='y')
    ax.grid(axis='x', color='#171330')
    key = key_notation[df.loc[id, 'key']]
    mode = mode_notation[df.loc[id, 'mode']]
    time_sig = int(df.loc[id, 'time_signature'])
    minutes = np.round(df.loc[id, 'duration_ms'] / 36000, 2)
    duration = str(minutes)[:-3] + ':' + str(minutes)[-2:]
    textstr = f"Pitch: {key} {mode};  Time Signature: {time_sig} / 4;  Duration: {duration} minutes"
    props = dict(boxstyle='round', facecolor='#780150', alpha=1)
    ax.text(40.05, 1.75, textstr, fontsize=14,
            verticalalignment='top', bbox=props, color='white')
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.read())
