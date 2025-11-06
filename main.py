% --- Proyecto Final --------------------------------------
% 1. Lectura de nube de puntos:
data = readmatrix('CilindroHueco.asc');
x = data(:,1);
y = data(:,2);
z = data(:,3);

figure
scatter3(x, y, z, 5, 'filled')
axis equal
xlabel('X'), ylabel('Y'), zlabel('Z')
title('Hollow Cylinder Point Cloud')

% 2. Selección de puntos para medición (vista superior)
figure
scatter(x, y, 5, 'filled')
axis equal
xlabel('X'), ylabel('Y')
title('Dibuja un polígono sobre los puntos deseados')

roi = drawpolygon;  % selección manual
in = inpolygon(x, y, roi.Position(:,1), roi.Position(:,2));

x_sel = x(in);
y_sel = y(in);
z_sel = z(in);

hold on
scatter(x_sel, y_sel, 20, 'r', 'filled')
hold off

% 3. Obtener el polinomio que describen los puntos seleccionados
% (asumimos que la relación es z = f(x), por ejemplo, corte lateral)

% Ordena los puntos por X para un ajuste más limpio
[x_sorted, idx] = sort(x_sel);
z_sorted = z_sel(idx);

% Ajuste polinómico
grado = 2; % puedes cambiar a 3, 4...
p = polyfit(x_sorted, z_sorted, grado);
z_fit = polyval(p, x_sorted);

% Visualiza el resultado
figure
plot3(x_sorted, y_sel(idx), z_sorted, 'o', 'DisplayName', 'Datos reales')
hold on
plot3(x_sorted, y_sel(idx), z_fit, '-', 'LineWidth', 1.5, 'DisplayName', 'Polinomio ajustado')
grid on
xlabel('X'), ylabel('Y'), zlabel('Z')
title(['Ajuste polinomial de grado ', num2str(grado)])
legend
axis equal
