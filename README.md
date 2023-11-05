# Sistemes de Codificació d'Àudio i Vídeo: Pràctica 3
**Instruccions per executar el fitxer**

Executeu el fitxer `P3-CarmeCorbi.py` especificant el número d'exercici com a argument. Per exemple, per executar l'Exercici 1, utilitzeu la següent comanda:
   ```python
   python3 P3-CarmeCorbi.py 1
   ```
Aquest fitxer és el principal. En aquesta pràctica, també s'han creat dos altres fitxers que són secundaris: ex4.py i ex6.py


## Exercici 1: Crear una classe Python per extreure macroblocs i vectors de moviment d'un vídeo amb FFMpeg
El propòsit d'aquest exercici té com a finalitat crear una classe que mitjançant la llibreria FFMpeg pugui extreure i visualizar la informació realitva als macroblocs i els vectors de moviment presents en un vídeo que ha sigut retallat. He creat una classe anomenada **VideoProcessor**, aquesta classe té un constructor **__init__** que rep els rutes dels fitxers de vídeo d'entrada i sortida i dues funcions **tallar_i_analitzar_video** i **analitzar_macroblocs_vectors_moviment**. 

La funció **tallar_i_analitzar_video** és la responsable de tallar el vídeo d'entrada, utilitza la comanda FFmpeg **ffmpeg -i "{self.video_entrada}" -ss 00:00:00 -t 00:00:09 -c:a copy {self.video_sortida}**, on -i self.video_entrada és la ruta del fitxer de vídeo d'entrada, -ss 00:00:00 especifica l'hora d'inici del tall, -t 00:00:09 indica la durada del tall (en el nostre cas, 9 segons) i -c:a copy fa una còpia del codec d'audio del vídeo original al vídeo de sortida. 

La funció **analitzar_macroblocs_vectors_moviment** té com a objectiu analitzar els macroblocs i vectors de movíment del vídeo d'entrada, utilitza la comanda FFmpeg **ffmpeg -flags2 +export_mvs -i {self.video_entrada} -vf codecview=mv=pf+bf+bb {self.video_sortida}** on -flags2 +export_mvs activa la exportació dels vectors de moviment en la sortida (aquestes vectors són dades que indiquen com es mouen les regions d'una image d'un frame a un altre en una seqüència de vídeo) , -i self.video_entrada indica la ruta del fitxer de vídeo d'entrada, -vf codecview= mv=pf+bf+bb utilitza un filtre de vídeo (vf) per mostrar els macroblocs i els vectors de moviment en el vídeo (codecview=mv=pf+bf+bb configura el filtre per postrar la informació dels macroblocs (pf), els vectors de moviment endavant (bf), i els vectors de moviment enrere (bb)). 

Dins de la funció **main** es verifica si es selecciona adequadament aquest exercici. Primer de tot, es defineix el vídeo d'entrada que en el meu cas és el BigBuckBunny i també es defineix el nom del vídeo de sortida **sortida_exercici_1.mp4** (és el vídeo retallat). Es crida a la funció **tallar_i_analitzar_video**. Seguidament, tornem a fer una crida a la classe i li passem com a vídeo d'entrada **sortida_exercici_1.mp4** i com nom del vídeo de sortida **sortida_exercici_1_2.mp4**. Per últim, cridem la funció **analitzar_macroblocs_vectors_moviment**. 

**Resultat de l'exercici 1:**
Podeu visualitzar els dos vídeos **sortida_exercici_1.mp4** i **sortida_exercici_1_2_mp4** adjunts en aquest repositori. La resposta per la terminal és la següent:

![](https://github.com/caarmeecoorbii/SCAV_P3/blob/main/exercici_1_2.png)

```python
# Executa l'exercici 1
python3 P3-CarmeCorbi.py 1
```


