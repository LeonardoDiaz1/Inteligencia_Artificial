import java.util.Arrays;
import java.util.Random;

public class AlgoritmoGenetico {
    private static final int TAMANO_POBLACION = 50;
    private static final int NUMERO_GENERACIONES = 100;
    private static final double PORCENTAJE_MUTACION = 0.1;
    private static final double PORCENTAJE_CRUCE = 0.8;

    private static final Random random = new Random();

    public static void main(String[] args) {
        double[] poblacion = generarPoblacionInicial(TAMANO_POBLACION);

        for (int generacion = 0; generacion < NUMERO_GENERACIONES; generacion++) {
            double[] aptitudes = evaluarPoblacion(poblacion);
            double[] seleccionados = seleccionarPoblacion(poblacion, aptitudes);
            double[] hijos = reproducirPoblacion(seleccionados);
            double[] mutados = mutarPoblacion(hijos);

            poblacion = mutados;

            double promedio = calcularPromedio(aptitudes);
            double maximo = calcularMaximo(aptitudes);

            double minimo = calcularMinimo(aptitudes);

            System.out.println("Generación: " + (generacion + 1));
            System.out.println("Mejor solución: " + maximo);
            System.out.println("Promedio: " + promedio);
            System.out.println("Peor solución: " + minimo);
            System.out.println("---------------------------------");
        }
    }

    private static double[] generarPoblacionInicial(int tamanoPoblacion) {
        double[] poblacion = new double[tamanoPoblacion];
        for (int i = 0; i < tamanoPoblacion; i++) {
            poblacion[i] = random.nextDouble() * 100; // Rango desolución entre 0 y 100
        }
        return poblacion;
    }

    private static double[] evaluarPoblacion(double[] poblacion) {
        double[] aptitudes = new double[poblacion.length];
        for (int i = 0; i < poblacion.length; i++) {
            aptitudes[i] = funcionObjetivo(poblacion[i]);
        }
        return aptitudes;
    }

    private static double funcionObjetivo(double x) {
        return x - 60 * x / 100 + 900 * x + 100;
    }

    private static double[] seleccionarPoblacion(double[] poblacion, double[] aptitudes) {
        double totalAptitudes = 0;
        double[] probabilidades = new double[poblacion.length];
        double[] seleccionados = new double[poblacion.length];

        for (double aptitud : aptitudes) {
            totalAptitudes += aptitud;
        }

        for (int i = 0; i < poblacion.length; i++) {
            probabilidades[i] = aptitudes[i] / totalAptitudes;
        }
        for (int i = 0; i < poblacion.length; i++) {
            double randomValue = random.nextDouble();
            double acumulado = 0;

            for (int j = 0; j < poblacion.length; j++) {
                acumulado += probabilidades[j];

                if (randomValue <= acumulado) {
                    seleccionados[i] = poblacion[j];
                    break;
                }
            }
        }
        return seleccionados;
    }

    private static double[] reproducirPoblacion(double[] poblacion) {
        double[] hijos = new double[poblacion.length];

        for (int i = 0; i < poblacion.length; i += 2) {
            double padre1 = poblacion[i];
            double padre2 = poblacion[i + 1];

            if (random.nextDouble() <= PORCENTAJE_CRUCE) {
                // Cruce de dos puntos (puedes utilizar otro tipo de cruces si deseas)
                int puntoCruce1 = random.nextInt(6); // 6 es el número de dígitos en la representación decimal de 100
                int puntoCruce2 = random.nextInt(6);

                if (puntoCruce2 < puntoCruce1) {
                    int temp = puntoCruce1;
                    puntoCruce1 = puntoCruce2;
                    puntoCruce2 = temp;
                }
                double hijo1 = (padre1 * Math.pow(10, puntoCruce1)
                        + padre2 * (Math.pow(10, puntoCruce2) - Math.pow(10, puntoCruce1))
                        + padre1 * (100 - Math.pow(10, puntoCruce2))) / 100;

                double hijo2 = (padre2 * Math.pow(10, puntoCruce1)
                        + padre1 * (Math.pow(10, puntoCruce2) - Math.pow(10, puntoCruce1))
                        + padre2 * (100 - Math.pow(10, puntoCruce2))) / 100;

                hijos[i] = hijo1;
                hijos[i + 1] = hijo2;
            } else {
                hijos[i] = padre1;
                hijos[i + 1] = padre2;
            }
        }
        return hijos;
    }

    private static double[] mutarPoblacion(double[] poblacion) {
        double[] mutados = Arrays.copyOf(poblacion, poblacion.length);

        for (int i = 0; i < poblacion.length; i++) {
            if (random.nextDouble() <= PORCENTAJE_MUTACION) {
                int digito = random.nextInt(6); // 6 es el número de dígitos en la representación decimal de 100
                double valorMutado = mutados[i] + Math.pow(10, digito) / 100;
                mutados[i] = Math.min(Math.max(valorMutado, 0), 100); // Asegura que el valor esté dentro del rango
                                                                      // permitido
            }
        }
        return mutados;
    }

    private static double calcularPromedio(double[] aptitudes) {
        double suma = 0;

        for (double aptitud : aptitudes) {
            suma += aptitud;
        }
        return suma / aptitudes.length;
    }

    private static double calcularMaximo(double[] aptitudes) {
        double maximo = Double.MIN_VALUE;

        for (double aptitud : aptitudes) {
            maximo = Math.max(maximo, aptitud);
        }
        return maximo;
    }

    private static double calcularMinimo(double[] aptitudes) {
        double minimo = Double.MAX_VALUE;

        for (double aptitud : aptitudes) {
            minimo = Math.min(minimo, aptitud);
        }
        return minimo;
    }
}