# 01/10/2024 06:00	terça
# 04/10/2024 14:02	sexta
# 01/10/2024 06:00	terça
# 01/10/2024 06:00	terça
# 01/10/2024 06:00	terça
# 01/10/2024 06:00	terça

import datetime

data_hora_str = '01/10/2024 06:00'


### 1. **Converter `data_hora` para um objeto `datetime`:**
# Usando o módulo `datetime`, podemos converter a string para um objeto `datetime`.
data_hora = datetime.datetime.strptime(data_hora_str, '%d/%m/%Y %H:%M')


### 2. **Acessar partes individuais (ano, mês, dia, hora, minuto):**
ano = data_hora.year
mes = data_hora.month
dia = data_hora.day
hora = data_hora.hour
minuto = data_hora.minute
print(f"Ano: {ano}, Mês: {mes}, Dia: {dia}, Hora: {hora}, Minuto: {minuto}")

### 3. **Somar ou subtrair tempo (dias, horas, minutos):**
# **Somar 10 dias:**

nova_data_hora = data_hora + datetime.timedelta(days=10)
print(nova_data_hora)

# **Subtrair 2 horas:**
nova_data_hora = data_hora - datetime.timedelta(hours=2)
print(nova_data_hora)


### 4. **Calcular a diferença entre duas datas:**
outra_data_hora = datetime.datetime(2024, 10, 15, 8, 0)
diferenca = outra_data_hora - data_hora
print(f"Diferença: {diferenca.days} dias e {diferenca.seconds // 3600} horas")


### 5. **Formatar a data e hora em outro formato:**
# **Formato 'YYYY-MM-DD HH:MM:SS':**
formato_novo = data_hora.strftime('%Y-%m-%d %H:%M:%S')


# **Somente a data em 'DD/MM/YYYY':**
formato_data = data_hora.strftime('%d/%m/%Y')
print(formato_data)


### 6. **Comparar duas datas:**
data_futura = datetime.datetime(2024, 11, 1, 6, 0)
if data_hora < data_futura:
    print("A data original é anterior à data futura.")
else:
    print("A data original é posterior ou igual à data futura.")

### 7. **Obter o dia da semana:**
dia_semana = data_hora.strftime('%A')  # Nome do dia em inglês
print(f"Dia da semana: {dia_semana}")


### 8. **Verificar se é uma data passada ou futura:**
agora = datetime.datetime.now()
if data_hora < agora:
    print("Esta data já passou.")
else:
    print("Esta data está no futuro.")
