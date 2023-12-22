import pydicom

ds = pydicom.dcmread('dicom_images\ID_0a0adf93f.dcm', force=True) # Utilizar force = True, para ler os metadados.

# Verificando todas as informações de metadados da imagem no formato DICOM
print(ds)

"""
Duas maneiras de acessar os metadados:

1º usando ds.*substituir_propriedade*

2º usando ds[0x*substituir_tag_sem_virgula*]

"""
# Verificando tipo de exame
print(ds.Modality)

# Verificando quantidade de pixel da imagem (Largura x Altura)
print(f'O tamanho da imagem é {ds.Rows} por {ds.Columns}')

# Encontrando o Espaçamento físico do pixel na largura e altura usando o 2º método
print(f'O distância física do pixel na lateral é {ds[0x00280030][0]} e na altura é {ds[0x00280030][1]}')