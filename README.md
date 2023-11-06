# Sistemes de Codificació d'Àudio i Vídeo: Pràctica 3
**Instruccions per executar el fitxer**

Executeu el fitxer `P3-CarmeCorbi.py` especificant el número d'exercici com a argument. Per exemple, per executar l'Exercici 1, utilitzeu la següent comanda:
   ```python
   python3 P3-CarmeCorbi.py 1
   ```
Aquest fitxer és el principal. En aquesta pràctica, també s'han creat dos altres fitxers que són secundaris: ex4.py i ex6.py


## Exercici 1: Crear una classe Python per extreure macroblocs i vectors de moviment d'un vídeo amb FFMpeg
El propòsit d'aquest exercici té com a finalitat crear una classe que mitjançant la llibreria FFMpeg pugui extreure i visualitzar la informació realitza als macroblocs i els vectors de moviment presents en un vídeo que ha sigut retallat. He creat una classe anomenada **VideoProcessor**, aquesta classe té un constructor **__init__** que rep les rutes dels fitxers de vídeo d'entrada i sortida i dues funcions **tallar_i_analitzar_video** i **analitzar_macroblocs_vectors_moviment**. 

La funció **tallar_i_analitzar_video** és la responsable de tallar el vídeo d'entrada, utilitza la comanda FFmpeg **ffmpeg -i "{self.video_entrada}" -ss 00:00:00 -t 00:00:09 -c:a copy {self.video_sortida}**, on -i self.video_entrada és la ruta del fitxer de vídeo d'entrada, -ss 00:00:00 especifica l'hora d'inici del tall, -t 00:00:09 indica la durada del tall (en el nostre cas, 9 segons) i -c:a copy fa una còpia del codec d'àudio del vídeo original al vídeo de sortida. 

La funció **analitzar_macroblocs_vectors_moviment** té com a objectiu analitzar els macroblocs i vectors de moviment del vídeo d'entrada, utilitza la comanda FFmpeg **ffmpeg -flags2 +export_mvs -i {self.video_entrada} -vf codecview=mv=pf+bf+bb {self.video_sortida}** on -flags2 +export_mvs activa l'exportació dels vectors de moviment en la sortida (aquests vectors són dades que indiquen com es mouen les regions d'una imatge d'un frame a un altre en una seqüència de vídeo) , -i self.video_entrada indica la ruta del fitxer de vídeo d'entrada, -vf codecview= mv=pf+bf+bb utilitza un filtre de vídeo (vf) per mostrar els macroblocs i els vectors de moviment en el vídeo (codecview=mv=pf+bf+bb configura el filtre per postrar la informació dels macroblocs (pf), els vectors de moviment endavant (bf), i els vectors de moviment enrere (bb)). 

Dins de la funció **main** es verifica si se selecciona adequadament aquest exercici. Primer de tot, es defineix el vídeo d'entrada que en el meu cas és el BigBuckBunny i també es defineix el nom del vídeo de sortida **sortida_exercici_1.mp4** (és el vídeo retallat). Es crida a la funció **tallar_i_analitzar_video**. Seguidament, tornem a fer una crida a la classe i li passem com a vídeo d'entrada **sortida_exercici_1.mp4** i com nom del vídeo de sortida **sortida_exercici_1_2.mp4**. Per últim, cridem la funció **analitzar_macroblocs_vectors_moviment**. 

**Resultat de l'exercici 1:**

Podeu visualitzar els dos vídeos **sortida_exercici_1.mp4** i **sortida_exercici_1_2_mp4** adjunts en aquest repositori. La resposta per la terminal és la següent:

![](https://github.com/caarmeecoorbii/SCAV_P3/blob/main/exercici_1_2.png)

Aquesta sortida proporciona detalls sobre com es codifica el vídeo, incloent informació sobre els tipus de frames, la qualitat de compressió, la grandària del fitxer i altres aspectes rellevants.

```python
# Executa l'exercici 1
python3 P3-CarmeCorbi.py 1
```

## Exercici 2: Crear un nou contenidor BBB amb exportació de vídeo i àudio utilitzant FFMpeg
El propòsit d'aquest exercici és demostrar com utilitzar FFmpeg per realitzar diverses operacions de processament de vídeo i àudio i com empaquetar-ho tot en un nou fitxer de vídeo .mp4 amb les especificacions demandes. He creat una funció nova anomenada **processar_video** per dur a terme tots els passos.

1. **Tallar el vídeo a 50 segons**: utilitzo la comanda FFMpeg **ffmpeg -i {video_entrada} -ss 00:00:00  -t 00:00:50 -c:a copy BigBuckBunny_50.mp4**. La mateixa comanda que el primer exercici.
2. **Exportar l'àudio com a pista MP3 mono**: utilitzo la comanda FFMpeg **ffmpeg -i {BigBuckBunny_50.mp4} -vn -ac 1 -c:a libmp3lame {BigBuckBunny_monotrack.mp3}** on -vn indica que no es vol processar el vídeo, -ac 1 indica que només s'utilitza una única pista d'audio i -c:a libmp3lame que es faci servir el códec MP3. L'àudio es guarda amb el nom **BigBuckBunny_monotrack.mp3**.
3. **Exporta l'àudio com a MP3 estèreo amb un bitrate inferior**: utilitzo la comanda  FFMpeg **ffmpeg -i {BigBuckBunny_50.mp4} -vn -ac 2 -b:a 64k -c:a libmp3lame {BigBuckBunny_stereo_bitratebaix.mp3}** on -ac 2 específica que es vol generar una pista d'àudio amb dos canals, és a dir, àudio estèreo, -b:a 64k indica el bitrate d'àudio que es vol utilitzar per a la sortida MP3 (el bitrate del vídeo original és de 1424 kb/s). L'àudio es guarda amb el nom **BigBuckBunny_stereo_bitratebaix-mp3**.
4. **Exportar l'àudio amb el codec AAC**: utilitzo la comanda FFMpeg **ffmpeg -i {BigBuckBunny_50.mp4} -vn -c:a aac {BigBuckBunny_AAC.aac}** on -c:a aac indica que es fa servir el còdec AAC. L'àudio es guarda amb el nom **BigBuckBunny_AAC.acc**.
5. **Empaquetar-ho tot en un .mp4**: utilitzo la comanda FFmpeg per combinar el vídeo tallat amb les tres pistes d'àudio extretes. La comanda és la següent: **ffmpeg -i {BigBuckBunny_50.mp4} -i {BigBuckBunny_monotrack.mp3} -i {BigBuckBunny_stereo_bitratebaix.mp3} -i {BigBuckBunny_AAC.aac} -map 0 -map 1 -map 2 -map 3 -c:v copy -c:a copy {video_sortida}** on -map 0 -map 1 -map 2 -map 3 especifiquen com mapejar els fluxos d'entrada als fluxos de sortida (mapeja el vídeo d'entrada i els tres fluxos d'àudio d'entrada (1,2,3) als fluxos de sortida corresponents), -c:v copy indica que el vídeo s'ha de copiar directament del fitxer d'entrada original sense cap canvi de codec i -c:a copy indica que els àudios que s'han de copiar directament dels fitxers d'entrada originals no s'han de canviar de codec.

Dins de la funció **main** es verifica si se selecciona adequadament aquest exercici. Primer de tot, es defineix el nom del vídeo de sortida i finalment, es crida a la funció **processar_video**. 

**Resultat de l'exercici 2:**
Els diferents arxius mp3 i mp4 estan adjuntats en aquest repositori.

```python
# Executa l'exercici 2
python3 P3-CarmeCorbi.py 2
```
## Exercici 3: Comptar les pistes en un contenidor MP4
```python
# Executa l'exercici 3
python3 P3-CarmeCorbi.py 3
```

## Exercici 4: Generació de Vídeo amb subtítols integrats
El propòsit d'aquest exercici és crear un script que descarregui subtítols, els integri en un vídeo i produeixi una versió del vídeo amb els substítols incrustats. Aquest nou script s'anomena **ex4.py**.  En aquest script, he creat tres funcions: descarregar_subtitols, integrar_subtitols i main. 

La funció **descarregar_subtitols** utilitza la comanda **youtube-dl** per descarregar els subtítols des de la URL específica i guardar-los en un fitxer amb el nom especificat **nom_subtitols**. Específicament, utilitza les opcions **--skip-download** per evitar descarregar el vídeo en si, **--write-sub** per demanar a **youtube-dl** que escrigui els subtítols en un fitxer i **--sub-lang** per especificar l'idioma dels subtítols (en aquest cas, en castellà). 

La funció **integrar_subtitols** utilitza la següent comanda FFMpeg **ffmpeg -i {video_entrada} -vf f"subtitles={subtitols} {video_sortida}** on -vf f"subtitles={subtitols} especifica el filtre de vídeo que s'aplicarà al vídeo. S'utilitza el filtre **subtitles** que permet incrustar els subtítols en el vídeo. 

La funció **main** conté les rutes als recursos de vídeo i subtítols, i es crida a les dues funcions per realitzar el procés de descàrrega i integració dels subtítols.

## Exercici 5: Fer servir l'script anterior en el script principal
Per executar aquest script, importem les dues primeres funcions mencionades en el fitxer **P3-CarmeCorbi.py**. Dins de la funció **main** es verifica si se selecciona adequadament aquest exercici. Primer de tot, es defineixen algunes variables com **url_subtitols**, **nom_subtitols**, **video_entrada** i **video_sortida**. Per últim, es criden les dues funcions **descarregar_subtitols** i **integrar_subtitols**. 

El vídeo resultant d'aquest exercici s'anomena **messi_amb_subtitols**.
```python
# Executa l'exercici 5
python3 P3-CarmeCorbi.py 5
```

## Exercici 6: Creació d'histogrames YUV en un nou contenidor de vídeo
El propòsit d'aquest exercici és utilitzar FFMpeg per extreure l'histograma YUV d'un vídeo i crear un nou vídeo que mostri l'histograma com una pista de vídeo. He creat un nou script anomenat **ex6.py**. En aquest script, he creat dues funcions **guardar_histograma** i **guardar_histograma_personalitzat**. 

La funció **guardar_histograma** té com a objectiu extreure l'histograma YUV d'un vídeo utilitzant una comanda FFMpeg i guardar-lo com a un nou vídeo amb l'histograma com a pista de vídeo. La comanda FFMpeg que faig servir és la següent **ffmpeg -i {video} -vf  histogram {sortida}** on -vf histograma aplica un filtre de vídeo per extreure l'histograma. 

La funció **mostrar_histograma_personalitzat** té com a objectiu mostrar el vídeo original amb l'histograma YUV corresponent incrustat. No he aconseguit realitzar-ho amb una comanda FFmpeg, però he utilitzat la comanda FFplay per poder-ho visualitzar. La comanda FFplay és la següent: **ffplay {video} -vf split=2[a][b] [b]histogram format=yuva444p[hh] [a][hh]overlay -vf split=2[a][b] [b]histogram format=yuva444p[hh] [a][hh]overlay -vf f'scale=1280:720 setsar=1 format=yuv420p -y {sortida}** on -vf "split=2[a][b];[b]histogram,format=yuva444p[hh];[a][hh]overlay,scale=1280:720,setsar=1,format=yuv420p" especifica una sèrie de filtres que s'apliquen el vídeo d'entrada (split=2[a][b] divideix el vídeo en dues parts, [b]histogram,format=yuva444p[hh] genera l'histograma a partir de la part b i ho formateixa cpm a yuva444p, [a][hh]overlay superposa l'historgama generat hh amb la part a del vídeo original i scale=1280:720,setsar=1,format=yuv420p redimensiona el vídeo, configura l'aspect ratio i el format de sortida). 

Per executar aquest script, importem les dues funcions mencionades en el fitxer **P3-CarmeCorbi.py**. Dins de la funció **main** es verifica si se selecciona adequadament aquest exercici. Primer de tot, definim les rutes dels vídeos d'entrada i sortida. Finalment, cridem a les dues funcions.

El resultat de la funció **guardar_histograma** és el vídeo adjuntat en el repositori anomenat **histograma.mp4**. 

El resultat de la funció **mostrar_histograma_personalitzat** obra una pestanya on es pot visualitzar el vídeo. Aquí teniu la captura d'un dels frames del vídeo:

![](https://github.com/caarmeecoorbii/SCAV_P3/blob/main/ex6.png)
```python
# Executa l'exercici 6
python3 P3-CarmeCorbi.py 6
```





