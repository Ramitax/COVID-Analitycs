import csv
import os

class Covid:

# 1. Number of cases by province, separated by gender
# 3. Average age of those infected by province
# 4. Provinces with cases

    def __init__(self, archive):
        self.archive = archive
        self.data = {}
        # Format: self.data { province : [ male cases, female cases, unspecified cases, auxiliary ages ] }

    def read(self):
        with open(self.archive, 'r', encoding="utf-8") as archive:
            data = csv.DictReader(archive, delimiter=",")
            for line in data:
                if line['clasificacion_resumen'] == "Confirmado" and line['carga_provincia_nombre'] != 'SIN ESPECIFICAR':
                    if line['carga_provincia_nombre'] not in self.data:
                        self.data[line['carga_provincia_nombre']] = [0,0,0,0]
                    if line['sexo'] == 'M':
                        self.data[line['carga_provincia_nombre']][0] += 1
                    if line['sexo'] == 'F':
                        self.data[line['carga_provincia_nombre']][1] += 1
                    if line['sexo'] == 'NR':
                        self.data[line['carga_provincia_nombre']][2] += 1
                    if line['edad'] != '':
                        age = int(line['edad'])
                        self.data[line['carga_provincia_nombre']][3] += age

    def export(self):
        base = '''
        <!DOCTYPE html>
        <html lang="en">
    
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Covid</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
                integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
            </head>
    
            <body class="container">
                <h1 class="text-center mt-4">Covid - Argentina</h1>
                <hr>
                <h5 class="text-center font-weight-bold">Analitycs</h5>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th scope="col">Province</th>
                            <th scope="col">Cases</th>
                            <th scope="col">Male Cases</th>
                            <th scope="col">Female Cases</th>
                            <th scope="col">Unspecified Cases</th>
                            <th scope="col">Average Age</th>
                        </tr>
            </thead>
            <tbody>
    
            '''
        file = open("Covid19.html", "w", newline='\n', encoding="utf-8")
        with file:
            file.write(base)
            for province in self.data:
                cases = self.data[province][0] + self.data[province][1] + self.data[province][2]
                string_product = '<tr> <th scope="row">' + str(province) + '</th> <td>' + str(cases) + '</td>' \
                                 ' <td>' + str(self.data[province][0]) + '</td> <td>' + str(self.data[province][1]) + '</td>' \
                                 ' <td>' + str(self.data[province][2]) + '</td> <td>' + str(int(self.data[province][3] / cases)) + '</td> </tr>'
                file.write(string_product.replace('\x93', " ").strip())
            final_string = '''
                             </tbody>
                           </table>
                        </body>
                    </html>
                    '''
            file.write(final_string)
            file.close()

    def start(self):
        self.read()
        self.export()
        os.system(os.getcwd() + "/Covid19.html")