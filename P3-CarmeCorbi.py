import sys
import subprocess
import json
from ex4 import descarregar_subtitols,integrar_subtitols
from ex6 import guardar_histograma, mostrar_histograma_personalitzat


#Exercici 1: Crear classe per extreure macroblocs i vectors de moviment
class VideoProcessor:
    #Constructor de la classe 
    def __init__(self, video_entrada, video_sortida):
        self.video_entrada = video_entrada #Assigna la ruta del fitxer de vídeo d'entrada a una variable d'instància
        self.video_sortida = video_sortida #Assigna la ruta del fitxer de vídeo de sortida a una variabke d'instància

    def tallar_i_analitzar_video(self):
        # Pas 1: Tallar el vídeo amb FFmpeg
        #Defineix la comanda FFmpeg per tallar el vídeo
        comanda_tallar = [
            "ffmpeg",   #Comanda FFmpeg
            "-i", self.video_entrada, #Ruta del fitxer de vídeo d'entrada
            "-ss", "00:00:00",  # Hora d'inici del tall
            "-t", "00:00:09",  # Durada del tall (9 segons)
             "-c:a", "copy", #Copia el codec d'àudio
            self.video_sortida #Ruta del fitxer de vídeo de sortida
        ]
        #Executa la comanda FFmpeg per tallar el vídeo
        subprocess.run(comanda_tallar)
    
    
    def analitzar_macroblocs_vectors_moviment(self):
        # Pas 2: Utilitzar FFmpeg per a analitzar macroblocs i vectors de moviment
        comanda_analisi = [
            "ffmpeg", #Comanda FFmpeg
            "-flags2", "+export_mvs", #Activa la exportació dels vectors de moviment
            "-i", self.video_entrada, #Ruta del fitxer de vídeo d'entrada
            "-vf", "codecview=mv=pf+bf+bb", #Filtre de vídeo per a mostrar els macroblocs i vectors de moviment
            self.video_sortida #Ruta del fitxer de vídeo de sortida
        ]
        #Executa la comanda FFmpeg per analizar macroblocs i vectors de moviment
        subprocess.run(comanda_analisi)



#Exercici 2: Crear un nou contenidor amb exportació de vídeo i àudio
def processar_video(video_entrada,video_sortida):
       # Pas 1: Tallar BBB en un vídeo de 50 segons
    tallar_command = [
        "ffmpeg",
        "-i", video_entrada,
        "-ss", "00:00:00",  # Hora d'inici (0 segons)
        "-t", "00:00:50",  # Durada (50 segons)
        "-c:a", "copy",
        "BigBuckBunny_50.mp4"
    ]
    subprocess.run(tallar_command)

    # Pas 2: Exportar l'àudio com a pista MP3 mono
    mp3_mono_command = [
        "ffmpeg",
        "-i", "BigBuckBunny_50.mp4",
        "-vn",  # Sense vídeo
        "-ac", "1",  # Àudio mono
        "-c:a", "libmp3lame",
        "BigBuckBunny_monotrack.mp3"
    ]
    subprocess.run(mp3_mono_command)

    # Pas 3: Exportar l'àudio com a MP3 estèreo amb un bitrate inferior
    mp3_estereo_command = [
        "ffmpeg",
        "-i", "BigBuckBunny_50.mp4",
        "-vn",  # Sense vídeo
        "-ac", "2",  # Àudio estèreo
        "-b:a", "64k",  # Bitrate inferior ja que el birate original es de 1424 kb/s
        "-c:a", "libmp3lame",
        "BigBuckBunny_stereo_bitratebaix.mp3"
    ]
    subprocess.run(mp3_estereo_command)

    # Pas 4: Exportar l'àudio amb el codec AAC
    aac_command = [
        "ffmpeg",
        "-i", "BigBuckBunny_50.mp4",
        "-vn",  # Sense vídeo
        "-c:a", "aac", #Establir códec de audio a AAC
        "BigBuckBunny_AAC.aac"
    ]
    subprocess.run(aac_command)

    # Pas 5: Empaquetar-ho tot en un .mp4 amb FFmpeg
    empaquetar_command = [
        "ffmpeg",
        "-i", "BigBuckBunny_50.mp4",
        "-i", "BigBuckBunny_monotrack.mp3",
        "-i", "BigBuckBunny_stereo_bitratebaix.mp3",
        "-i", "BigBuckBunny_AAC.aac",
        "-map", "0", "-map", "1", "-map", "2", "-map", "3",
        "-c:v", "copy",
        "-c:a", "copy",
        video_sortida
    ]
    subprocess.run(empaquetar_command)
       

#Exercici 3: Comptar i mostrar les pistes d'un contenidor MP4
def retornar_pistes_mp4(video_entrada):
    #Definir comanda que compta el número de pistes
    num_pistes = ["ffprobe",
                  video_entrada,
                  "-show_entries" ,"format=nb_streams",
                    "-v","0",
                     "-of", "compact=p=0:nk=1" ]
    subprocess.run(num_pistes)

def mostrar_pistes(video_entrada):
    # Definir la comanda per mostrar les pistes
    cmd = ["ffprobe", video_entrada, "-print_format", "json", "-show_streams"]

    # Executar la comanda i capturar la sortida
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

   
    
    # La sortida exitosa conté informació detallada sobre les pistes
    info_pistes = json.loads(result.stdout)
        
    # Imprimir informació sobre cada pista
    for i, pista in enumerate(info_pistes["streams"], start=1):
        print(f"Pista {i}:")
        print(f"  Tipus: {pista['codec_type']}")
        print(f"  Format: {pista.get('codec_name', 'Desconegut')}")
        print(f"  Resolució: {pista.get('width', 'Desconegut')}x{pista.get('height', 'Desconegut')}")
        print("")

    return info_pistes["streams"]
    
    
#Funció main
def main():
    if len(sys.argv) < 2:
        print("Ús: python P3-CarmeCorbi.py [exercici]")
        return
    
    exercici = sys.argv[1]
    video_entrada = '/home/ccorbi/BigBuckBunny.mp4'
    

    #Exercici 1
    if exercici == '1':
       # Crida a la classe VideoProcessor per processar el vídeo
        video_processor = VideoProcessor(video_entrada, 'sortida_exercici_1.mp4')
        video_processor.tallar_i_analitzar_video()
        video_processor2 = VideoProcessor('sortida_exercici_1.mp4', 'sortida_exercici_1_2.mp4')
        video_processor2.analitzar_macroblocs_vectors_moviment()
    #Exercici 2
    elif exercici == '2':
        video_sortida = 'sortida_exercici_2.mp4'
        processar_video(video_entrada,video_sortida)
       

    #Exercici 3 
    elif exercici == '3':
        mostrar_pistes('sortida_exercici_2.mp4')
        retornar_pistes_mp4('sortida_exercici_2.mp4')

        
    #Exercici 4 i 5
    elif exercici == '5':
       nom_subtitols = "subtitols_video.srt" #Nom del fitxer de subtítols que es genera
       video_entrada = "messi.mp4"  # Canvia-ho pel nom del teu vídeo d'entrada
       video_sortida = "messi_amb_subtitols.mp4" # Nom del vídeo amb els subtítols incrustats
       url = "https://github.com/caarmeecoorbii/SCAV_P3/blob/main/subtitles_video.srt"
        # Pas 1: Descarrega els subtítols
       descarregar_subtitols(url,nom_subtitols)
       # Pas 2: Integra els subtítols en el vídeo
       integrar_subtitols(video_entrada, nom_subtitols, video_sortida)

    #Exercici 6
    elif exercici == '6':
        video_sortida1 = 'histograma.mp4'
        video_sortida2 = 'histograma+video.mp4'
        guardar_histograma('sortida_exercici_1.mp4',video_sortida1)
        mostrar_histograma_personalitzat('sortida_exercici_1.mp4', video_sortida2)
   
       

   





          
    else:
        print("Exercici no vàlid. Proporcionar un número del 1 al 6")

if __name__ == "__main__":
    main()