import utils
import read_csv
import charts

#Algoritmo para graficar la poblacion por pais y mundial:
def run():
    data = read_csv.read_csv('data.csv')
    data = list(filter(lambda item:item['Continent'] == 'South America',data))
    
    countries = list(map(lambda x:x['Country/Territory'],data))
    percentages = list(map(lambda x:x['World Population Percentage'],data))
    charts.generate_pie_chart(countries,percentages)

    country = input('Type Country :') #Ingresar nombre de pais:
    print('Pais elegido:',country)

    result = utils.population_by_country(data,country)

    if len(result) > 0:
        country = result[0] # sobreescribe el pais ingresado por su contenido (diccionario)
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'],labels,values) # Importante: especificar el nombre del pais (country['Country'])


#-------Dualidad------
#Si es ejecutado desde la terminal, entonces ejecutar todo el modulo
# Si es ejecutado o invocado desde otro archivo, se omite esa ejecucion
if __name__ == '__main__':
   run()
