import subprocess


def guardar_histograma(video, sortida):
    # Comanda per guardar l'histograma com a vídeo amb FFmpeg
    cmd = ['ffmpeg', '-i', video, '-vf', 'histogram', sortida]
    
    # Executar la comanda
    subprocess.run(cmd)

def mostrar_histograma_personalitzat(video, sortida):
    # Comanda per mostrar i guardar l'histograma amb la cadena de filtres personalitzada
    cmd = ['ffplay', video, '-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay', '-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay', '-vf', f'scale=1280:720,setsar=1,format=yuv420p -y {sortida}']
    
    # Executar la comanda
    subprocess.run(cmd)


