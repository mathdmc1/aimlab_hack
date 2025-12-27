import cv2
import numpy as np

# Cargar imagen
img = cv2.imread("screenshot.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Blur para suavizar ruido
blur = cv2.GaussianBlur(gray, (5,5), 0)

# 2. Detectar bordes
edges = cv2.Canny(blur, 50, 150)

# 3. Buscar contornos
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # 4. Filtrar contornos muy pequeños
    if len(cnt) < 20:
        continue

    # 5. Ajustar una elipse al contorno
    try:
        ellipse = cv2.fitEllipse(cnt)
    except:
        continue

    (x,y), (a,b), angle = ellipse

    # 6. Filtro adicional: forma aproximadamente elíptica
    if a / b > 5:  # demasiado alargado = seguramente no es círculo 3D
        continue

    # Dibujar elipse
    cv2.ellipse(img, ellipse, (0,255,0), 2)

# Mostrar resultado
cv2.imshow("Elipses detectadas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
