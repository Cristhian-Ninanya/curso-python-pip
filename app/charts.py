import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):

    fig, ax = plt.subplots()
    ax.bar(labels,values)
    ax.set_title(f'Pais {name}')
    plt.savefig(f'./imgs/{name}.png') #Almacena la imagen del pais seleccionado
    plt.close()

def generate_pie_chart(labels,values):
    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.set_title('Poblacion Mundial')
    ax.axis('equal')
    plt.savefig('./imgs/pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a','b','c','d','e']
    values = [10,90,20,80,50]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels,values)