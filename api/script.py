import whisper

class Segment:
    id: int
    seek: int
    start: float
    end: float
    text: str
    tokens: list[int]
    temperature: float
    avg_logprob: float
    compression_ratio: float
    no_speech_prob: float

class TranscribeResult:
    text: str
    segments: list[Segment]
    language: str
    

def convertir_tiempo(segundos):
    horas = int(segundos // 3600)
    segundos_restantes = int(segundos % 3600)
    minutos = int(segundos_restantes // 60)
    segundos = int(segundos_restantes % 60)
    milisegundos = int(int((segundos_restantes - int(segundos_restantes)) * 1000))
    
    return f"{horas:02d}:{minutos:02d}:{segundos:02d},{milisegundos:03d}"
    
    
def generar_subtitulos(segmentos: list[Segment], output_file):
    with open(output_file, 'w') as f:
        numero_subtitulo = 1
        for segmento in segmentos:
            tiempo_inicio = convertir_tiempo(segmento['start'])
            tiempo_fin = convertir_tiempo(segmento['end'])
            
            linea_tiempo = f"{tiempo_inicio} --> {tiempo_fin}"
            texto_subtitulo = segmento['text']
            
            # Escribir el número de subtítulo, tiempo y texto en el archivo SRT
            f.write(f"{numero_subtitulo}\n")
            f.write(f"{linea_tiempo}\n")
            f.write(f"{texto_subtitulo}\n\n")  # Agregar una línea en blanco después de cada subtítulo
            
            numero_subtitulo += 1

model = whisper.load_model("medium")
result: TranscribeResult = model.transcribe("video3.mp4")

# ?
output_file = "subtitulos3.srt"
generar_subtitulos(result['segments'], output_file)
print(f"Subtítulos generados en el archivo {output_file} con éxito! 🎉")



    
