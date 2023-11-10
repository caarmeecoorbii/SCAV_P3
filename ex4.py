import subprocess
import requests
import json
def descarregar_subtitols(url,nom_subtitols):
        resposta = requests.get(url)

        if resposta.status_code == 200:
            # Convertir la resposta format JSON i extraure "blob" i "rawLines"
            info = json.loads(resposta.text)
            info_subtitols = info["payload"]["blob"]["rawLines"]

            # Guardar el contingut a un arxiu local
            with open(nom_subtitols, "w", encoding="utf-8") as file:
                file.write("\n".join(info_subtitols))

 
def integrar_subtitols(video_entrada, subtitols, video_sortida):
    # Utilitza FFmpeg per integrar els subtítols en el vídeo
    comanda_integrar_subtitols = [
        "ffmpeg",
        "-i", video_entrada, #Específica el vídeo d'entrada
        "-vf", f"subtitles={subtitols}",  # Utilitza els subtítols descarregats
        video_sortida #Genera un vídeo amb els substítold incrustats
    ]
    subprocess.run(comanda_integrar_subtitols)

def main():
    nom_subtitols = "subtitols_video.srt" #Nom del fitxer de subtítols
    video_entrada = "messi.mp4"  # Canvia-ho pel nom del teu vídeo d'entrada
    video_sortida = "messi_amb_subtitols.mp4" # Nom del vídeo amb els subtítols incrustats
    url = "https://github.com/caarmeecoorbii/SCAV_P3/blob/main/subtitles_video.srt"
    # Pas 1: Descarrega els subtítols
    
    descarregar_subtitols(url,nom_subtitols)

    # Pas 2: Integra els subtítols en el vídeo
    #integrar_subtitols(video_entrada, nom_subtitols, video_sortida)

if __name__ == "__main__":
    main()
