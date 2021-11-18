# Sinusoida dan Fasor

## Pendahuluan
Arus bolak-balik (ac) lebih efisien dan ekonomis untuk transmisi jarak jauh.
Kita akan memulai analisis rangkaian dimana sumber tegangan atau arusnya bervariasi terhadap waktu.
Pada Bab ini secara khusus kita mengkaji eksitasi bervariasi waktu secara sinusoidal, atau eksitasi oleh suatu sinusoida.

## Sinusoida

<div class="alert alert-info"><strong>Definisi</strong>:
Sinusoid adalah sinyal yang berbentuk fungsi sinus atau kosinus.
</div>    

Arus sinusoidal biasanya dikenal sebagai *arus bolak-balik (ac)*.
Arus ini berbalik secara berkala dan memiliki nilai positif dan negatif secara bergantian.
Rangkaian yang dieksitasi oleh sumber arus atau tegangan sinusoidal disebut *rangkaian ac*.

Pertimbangkan tegangan sinusoidal
$$ v(t) = V_m \sin \omega t $$
dimana

$V_m =$ amplitudo sinusoida     
$\omega =$ frekuensi sudut dalam radian/s    
$\omega t =$ argumen dari sinusoida

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data untuk plot
t = np.arange(0.0, 4.5*np.pi, 0.01)
s = np.sin(1 * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='waktu (s)', ylabel='tegangan (mV)',
       title='Plot')
ax.grid()

# fig.savefig("test.png")
plt.show()

$$ \omega T = 2 \pi \quad \Rightarrow \quad T = \frac{2 \pi}{\omega} $$

Fakta bahwa $v(t)$ berulang setiap $T$ detik ditunjukkan dengan mengganti $t$ dengan $t + T$. Kita dapatkan

$$v(t + T) = V_m \sin \omega (t + T)$$

$$ v(t + T ) = V_m \sin \omega \left(t + \frac{2 \pi}{\omega} \right) $$

$$ v(t + T) = V_m \sin (\omega t + 2 \pi) $$

Maka:
$$ v(t + T) = v(t) $$

yang berarti bahwa $v$ memiliki nilai yang sama pada $t + T$ seperti pada $t$, dan $v(t)$ dikatakan periodik.

<div class="alert alert-info"><strong>Definisi</strong>:
Fungsi periodik adalah fungsi yang memenuhi $f(t) = f(t + nT)$, untuk semua $t$ dan untuk semua bilangan bulat $n$.
</div>

Seperti disebutkan, periode T dari fungsi periodik adalah waktu satu siklus lengkap atau jumlah detik per siklus.
Kebalikan dari kuantitas ini adalah jumlah siklus per detik, yang dikenal sebagai frekuensi siklik f dari sinusoidal.
Dengan demikian,

$$ f = \frac{1}{T} $$

jelas bahwa
$$ \omega = 2 \pi f $$

Dimana $\omega$ dalam radian per detik (rad/s), $f$ dalam (Hz).

Mari kita perhatikan ekspresi yang lebih umum untuk sinusoida,

$$ v(t) = V_m \sin (\omega t + \phi) $$

di mana $(\omega t + \phi)$ argumen dan $\phi$ fase.
Baik argumen maupun fase dapat dalam radian atau derajat.
Mari kita kaji dua sinusoida

$$ v_1(t) = V_m \sin \omega t \qquad \qquad v_2(t) = V_m \sin (\omega t + \phi) $$

t = np.arange(0.0, 4.5*np.pi, 0.01)
phi = 2
v1 = np.sin(t)
v2 = np.sin(t + phi)
fig, ax = plt.subplots()
ax.plot(t, v1 , label='v1')
ax.plot(t, v2 , label='v2')

ax.set(xlabel='waktu (s)', ylabel='tegangan (mV)',
       title='Plot')
ax.grid()

plt.legend()
plt.show()

Sinusoid dapat dinyatakan dalam bentuk sinus atau cosinus.
Ketika membandingkan dua sinusoidal, akan bijaksana untuk menyatakan keduanya sebagai sinus atau cosinus dengan amplitudo positif.
Ini dicapai dengan menggunakan identitas trigonometri berikut:

$$\begin{array}{l}
\sin (A \pm B) = \sin A \cos B \pm \cos A \sin B \\
\cos (A \pm B) = \cos A \cos B \mp \sin A \sin B
\end{array}$$

Dengan identitas ini, mudah untuk menunjukkan bahwa

$$\begin{array}{rcl}
\sin (\omega t \pm 180^\circ) &=& - \sin \omega t \\
\cos (\omega t \pm 180^\circ) &=& - \cos \omega t \\
\sin (\omega t \pm 90^\circ) &=& \pm \cos \omega t \\
\cos (\omega t \pm 90^\circ) &=& \mp \sin \omega t
\end{array}$$

Dengan menggunakan hubungan ini, kita dapat mengubah sinusoidal dari bentuk sinus ke bentuk cosinus atau sebaliknya.

%reset -s -f

## Contoh
Tentukan amplitudo, fase, periode, dan frekuensi sinusoida

$$ v(t) = 12 \cos (50t + 10^\circ) $$

### Solusi
Amplitudo $V_m = 12 \, \mathrm{V}$    
Fasa es $\phi = 10^\circ$    
Frekuensi sudut $\omega = 50 \, \mathrm{rad/s}$.     
Periode 
$$T = \frac{2 \pi}{\omega} = \frac{2 \pi}{50} = 0,1257$$
Frekuensi
$$ f = \frac{1}{T} = 7,958 \, \mathrm{Hz} $$

import math

Vm = 12 # V
phi = 10 # derajat
omega = 50 # rad/s

T = 2*math.pi/omega
f = 1/T

print('T = %.4f'%T)
print('f = %.3f Hz'%f)

Diberikan sinusoida $5 \sin (4 \pi t - 60^\circ)$, hitung amplitudo, fasa, frekuensi sudut, periode dan frekuensi.

Amplitudo $V_m = 5$      
Fasa es $\phi =-60^\circ$     
Frekuensi sudut $\omega = 12,57$     
Periode
$$ T = \frac{2 \pi}{\omega} $$
Frekuensi
$$ f = \frac{1}{T} $$

Vm = 5 
phi = -60 # derajat

omega = math.pi*4 # rad/s
T = 2*math.pi/omega 
f = 1/T

print('omega = %1.2f rad/s'%omega)
print('T = %.2f s/rev'%T)
print('f = %.2f Hz'%f)

%reset -s -f

## Fasor
Sinusoid mudah diekspresikan dalam bentuk fasor, yang lebih mudah digunakan daripada fungsi sinus dan kosinus.

<div class="alert alert-info"><strong>Definisi</strong>:
Fasor adalah bilangan kompleks yang mewakili amplitudo dan fase sinusoida.
</div>

Suatu bilangan kompleks $z$ dapat ditulis dalam bentuk rectangular sebagai

$$ z = x + jy $$

dimana $j = \sqrt{-1}$; $x$ adalah bagian real $z$ dan $y$ adalah bagian imajiner dari $z$.

Bilangan kompleks $z$ juga dapat ditulis dalam polar atau bentuk eksponensial sebagai

$$ z = r \angle \phi = re^{j \phi} $$

dimana $r$ adalah magnitudo dari $z$ dan $\phi$ adalah fasa dari $z$.
Kita perhatikan bahwa $z$ dapat direpresentasikan dalam tiga cara:

$$\begin{array}{lcl} 
z = x + jy & & \text{Bentuk rectangular} \\
z = r \angle \phi & & \text{Bentuk polar} \\
z = re^{j \phi} & & \text{Bentuk eksponensial}
\end{array}$$

Diberikan $r$ dan $\phi$, kita dapat memperoleh $x$ dan $y$ sebagai 

$$ x = r \cos \phi \qquad \qquad y = r \sin \phi $$

Dengan demikian, $z$ dapat ditulis berupa

$$ z = x + jy = r \angle \phi = r( \cos \phi + j \sin \phi ) $$

* Penjumlahan dan pengurangan bilangan kompleks lebih baik dilakukan dalam bentuk rectangular.    
* Perkalian dan pembagian lebih baik dilakukan dalam bentuk polar.

Berikut ini beberapa operasi penting.

__Penjumlahan:__
$$ z_1 + z_2 = (x_1 + x_2) + j(y_1 + y_2) $$

__Pengurangan:__
$$ z_1 - z_2 = (x_1 - x_2) + j(y_1 - y_2) $$

__Perkalian:__
$$ z_1 z_2 = r_1 r_2 \; \angle (\phi_1 + \phi_2) $$

__Pembagian:__
$$ \frac{z_1}{z_2} = \frac{r_1}{r_2} \; \angle (\phi_1 - \phi_2) $$

__Inversi:__
$$ \frac{1}{z} = \frac{1}{r} \; \angle (- \phi) $$

__Akar kuadrat:__
$$ \sqrt{z} = \sqrt{r} \; \angle \frac{\phi}{2} $$

__Kompleks konjugat:__
$$ z^* = x - jy = r \angle (- \phi) = r e^{-j \phi} $$

Ide representasi fasor adalah berdasarkan identitas Euler.
Secara umum:

$$ e^{\pm j \phi} = \cos \phi \pm j \sin \phi $$

yang menunjukkan bahwa kita dapat menganggap $\cos \phi$ y $\sin \phi$ sebagai komponen real dan imajiner dari $e^{j \phi}$; kita dapat menuliskan

$$\begin{array}{l}
\cos \phi = \mathrm{Re} (e^{j \phi}) \\
\sin \phi = \mathrm{Im} (e^{j \phi})
\end{array}$$

## Contoh
Evaluasi bilangan kompleks berikut:
$$ (40 \angle 50^\circ + 20 \angle -30^\circ)^{1/2} $$

### Solusi
Menggunakan transformasi polar ke rectangular

$$ z = r \angle \phi \quad \rightarrow \quad
\left\{
\begin{array}{l}
x = r \cos \phi \\
y = r \sin \phi
\end{array}
\right.$$

__* Langkah-langkah:__

import math

phi1 = 50*(math.pi/180) # rad (konversi ke radian)
r1 = 40

x1 = r1*math.cos(phi1)
y1 = r1*math.sin(phi1)

print('z1 = %.2f + (%.2f)j'%(x1,y1))

phi2 = -30*(math.pi/180) # rad
r2 = 20

x2 = r2*math.cos(phi2)
y2 = r2*math.sin(phi2)

print('z2 = %.2f + (%.2f)j'%(x2,y2))

Hasil penjumlahannya:

x3 = x1 + x2
y3 = y1 + y2

print('z3 = %.2f + (%.2f)j'%(x3,y3))

Konversi $z_3$ ke koordinat polar

r3 = math.sqrt(x3**2 + y3**2)
phi3 = math.atan(y3/x3)

print('z3 = %.2f<%.2frad'%(r3,phi3))
print('z3 = %.2f<%.2f°'%(r3,phi3*180/math.pi))

Menghitung akar kuadrat dari ekspresi ini

r4 = math.sqrt(r3)
phi4 = phi3/2

print('z4 = %.2f<%.2frad'%(r4,phi4))
print('z4 = %.2f<%.2f°'%(r4,phi4*180/math.pi))

__* Menggunakan library cmath__

import cmath

r1 = 40 ; phi1 = 50*math.pi/180 
r2 = 20 ; phi2 = -30*math.pi/180
# Konversi ke koordinat rectangular
c1 = cmath.rect(r1,phi1)
c2 = cmath.rect(r2,phi2)

c3 = cmath.sqrt(c1 + c2)
c3p = cmath.polar(c3)

print('c1 = {:.2f}'.format(c1))
print('c2 = {:.2f}'.format(c2))

print('c3 = {:.2f}'.format(c3))

print('c3p = %.2f<%.2frad'%(c3p[0],c3p[1]))

%reset -s -f

## Contoh
$$ \frac{ (10 \angle -30^\circ) + (3 - 4j) }{ (2 + 4j) \, (3 - 5j)^*  } $$

### Solusi

1. Konversi $(10 \angle -30^\circ)$ ke rectangular
$$\begin{array}{l}
x = r \cos \phi \\
y = r \sin \phi
\end{array}$$

import math
import cmath

r1 = 10 ; phi1 = -30*(math.pi/180)

x1 = r1*math.cos(phi1)
y1 = r1*math.sin(phi1)

print('(%.2f %.2fj)'%(x1,y1))

2. Penjumlahan

c1 = complex(x1, y1)
c2 = complex(3, -4)
Num = c1 + c2
Num_pol = cmath.polar(Num)

print('Num = {:.2f}'.format(Num))
print('Num_pol = %.2f<%.2frad'%Num_pol)

c3 = complex(2,4)
c4 = 3-5j.conjugate()
Den = c3*c4
Den_pol = cmath.polar(Den)

print('Den = {:.2f}'.format(Den))
print('Den_pol = %.2f<%.2frad'%Den_pol)

Res = Num/Den
Res_pol = cmath.polar(Res)

print('Res = {:.2f}'.format(Res))
print('Res_pol = %.3f<%.2frad'%Res_pol)
print('%.2frad = %s°'%(Res_pol[1],round(Res_pol[1]*180/math.pi,2)))

%reset -s -f

## Latihan
Evaluasi bilangan kompleks berikut:
$$ [(5 + 2j)(-1 + 4j) - 5 \angle 60^\circ]^* $$

### Solusi

__Gunakan library cmath__

import math
import cmath

z1 = complex(5,2)
z2 = complex(-1,4)
z3 = cmath.rect(5,60*math.pi/180)

Hasil = (z1*z2 - z3).conjugate()

print('Hasil = {:.2f}'.format(Hasil))

__Ssolusi langkah demi langkah__
1. Konversi $(5 + 2j)$ ke koordinat polar

x1 = 5 
y1 = 2

r1 = math.sqrt(x1**2 + y1**2)
phi1 = math.atan(2/5)

z1 = complex(x1,y1)
z1p = (r1,phi1)

print('z1 = {:.2f}'.format(z1))
print('z1p = %.3f<%.3frad'%z1p)

2. Konversi $(-1 + 4j)$ ke koordinat polar

x2 = -1
y2 = 4

r2 = math.sqrt((-1)**2 + 4**2)
phi2 = math.pi + math.atan(4/-1)

z2 = complex(x2,y2)
z2p = (r2,phi2)

print('z2 = {:.2f}'.format(z2))
print('z2p = %.3f<%.2frad'%z2p)

3. Perkalian

r3 = z1p[0]*z2p[0]
phi3 = z1p[1] + z2p[1]

z3p = (r3,phi3)

print('z3p = %.3f<%.3frad'%z3p)

x3 = r3*math.cos(phi3)
y3 = r3*math.sin(phi3)

z3 = complex(x3,y3)

print('z3 = {:.2f}'.format(z3))

4. Konversi $5 \angle 60^\circ$ ke koordinat rektangular

r4 = 5
phi4 = 60*math.pi/180

z4p = (r4,phi4)

x4 = r4*math.cos(phi4)
y4 = r4*math.sin(phi4)

z4 = complex(x4,y4)

print('z4 = {:.2f}'.format(z4))

5. Pengurangan

z5 = z3 - z4

6. Konjugat

Res = z5.conjugate()

Hasil:

print('Res = {:.2f}'.format(Res))

%reset -s -f

## Latihan

$$ \frac{ (10 + 5j) + (3 \angle 40^\circ) }{ (-3 + 4j) } + (10 \angle 30^\circ) $$

import math
import cmath

__Menggunakan library cmath__

z1 = complex(10,5)
z2 = cmath.rect(3,40*math.pi/180)
z3 = complex(-3,4)
z4 = cmath.rect(10,30*math.pi/180)

Res = (z1 + z2)/z3 + z4

print('Res = {:.3f}'.format(Res))

__Solusi langkah demi langkah__

# Data:
x1 = 10 ; y1 = 5
r2 = 3
phi2 = 40*math.pi/180
x3 = -3 ; y3 = 4
r4 = 10
phi4 = 30*math.pi/180

$$\left.
\begin{array}{l}
r_2 = 3 \\
\phi_2 = 40^\circ
\end{array}
\right\} \quad \rightarrow \quad
\begin{array}{l}
x_2 = r_2 \cos \phi_2 \\
y_2 = r_2 \sin \phi_2
\end{array}$$

x2 = r2*math.cos(phi2)
y2 = r2*math.sin(phi2)

x_s1 = x1 + x2
y_s1 = y1 + y2

print('s1 = (%.3f,%.3f)'%(x_s1,y_s1))

$\begin{array}{l}
r_{s1} = \sqrt{x_{s1}^2 + y_{s1}^2} \\
\phi_{s1} = \arctan (y_{s1}/x_{s1})
\end{array}$

# Konversi ke polar
r_s1 = math.sqrt(x_s1**2 + y_s1**2)
phi_s1 = math.atan(y_s1/x_s1)

print('s1p = (%.3f,<%.3frad)'%(r_s1,phi_s1))

$$\left\{
\begin{array}{l}
r_3 = \sqrt{x_3^2 + y_3^2} \\
\displaystyle \phi_3 = \pi - \arctan \left| \frac{y_3}{x_3} \right|
\end{array}
\right.$$

r3 = math.sqrt(x3**2 + y3**2)
phi3 = math.pi - math.atan( y3 / abs(x3) )

print('c3p = (%.3f,%.3frad)'%(r3,phi3))

Pembagian dalam koordinat polar

$$\left\{
\begin{array}{l}
\displaystyle r_{f1} = \frac{r_{s1}}{r_3} \\
\phi_{f1} = \phi_{s1} - \phi_3
\end{array}
\right.$$

r_f1 = r_s1/r3
phi_f1 = phi_s1 - phi3

Konversi pecahan menjadi koordinat rectangular

$$\left\{
\begin{array}{l}
x_{f1} = r_{f1} \cos \phi_{f1} \\
y_{f1} = r_{f1} \sin \phi_{f1}
\end{array}
\right.$$

x_f1 = r_f1*math.cos(phi_f1)
y_f1 = r_f1*math.sin(phi_f1)

print('f1 = (%.3f,%.3f)'%(x_f1,y_f1))

Konversi ke koordinat rectangular $(10 \angle 30^\circ)$

$$\left\{
\begin{array}{l}
x_4 = r_4 \cos \phi_4 \\
y_4 = r_4 \sin \phi_4
\end{array}
\right.$$

x4 = r4*math.cos(phi4)
y4 = r4*math.sin(phi4)

print('c4 = (%.3f,%.3f)'%(x4,y4))

Penjumlahan dalam koordinat rectangular

x_res = x_f1 + x4
y_res = y_f1 + y4

# Print hasil
print('Hasil = (%.3f,%.3f)'%(x_res,y_res))

%reset -s -f

## Contoh
Transformasikan sinusoida menjadi fasor
$\begin{array}{ll}
a) & i = 6 \cos (50t - 40^\circ) \, \mathrm{A} \\
b) & v = -4 \sin (30t + 50^\circ) \, \mathrm{V}
\end{array}$

### Solusi
$a)$
$$ i = 6 \cos (50t - 40^\circ) \, \mathrm{A} $$

memiliki bentuk fasor $\vec{I} = (6, \angle -40^\circ) \, \mathrm{A}$

$b)$ karena $-\sin A = \cos (A + 90^\circ)$:

$$ v = -4 \sin (30t + 50^\circ) \, \mathrm{V} = 4 \cos (30t + 50^\circ + 90^\circ) $$

$$ v = \cos (30t + 140^\circ) \, \mathrm{V} $$

Bentuk fasor dari $v$ adalah
$$ \vec{V} = (4, \angle 140^\circ \, \mathrm{V}) $$

## Latihan
Ekspresikan sinusoida berikut sebagai fasor:

$\begin{array}{ll}
a) & v = -7 \cos (2t + 40^\circ) \, \mathrm{V} \\
b) & i = 4 \sin (10t + 10^\circ) \, \mathrm{A}
\end{array}$

### Solusi
$a)$ Karena $- \cos A = \cos (A + 180^\circ)$:

$$ v = -7 \cos (2t + 40^\circ) \, \mathrm{V} = 7 \cos (2t + 40^\circ + 180^\circ) \, \mathrm{V} $$

$$ v = 7 \cos (2t + 220^\circ) \, \mathrm{V} $$

Bentuk fasor dari $v$ adalah: $ \vec{V} = (7, \angle 220^\circ) \, \mathrm{V} $

$b)$ Diketahui bahwa $\sin A = \cos (A - 90^\circ)$

$$ i = 4 \sin (10t + 10^\circ) \, \mathrm{A} = 4 \cos (10t + 10^\circ - 90^\circ) \, \mathrm{A} $$

$$ i = 4 \cos (10t - 80^\circ) \, \mathrm{A} $$

Bentuk fasor dari $\vec{I} = (4, \angle -80^\circ) \, \mathrm{A}$

## Contoh
Tentukan sinusoida yang direpresentasikan oleh fasor berikut:

$\begin{array}{ll}
a) & \vec{I} = -3 + 4j \, \mathrm{A} \\
b) & \vec{V} = j8e^{-j20} \, \mathrm{V}
\end{array}$

### Solusi
$a)$

import math
import cmath

I = complex(-3,4)
I_pol = cmath.polar(I)

r = I_pol[0]
phi_deg = I_pol[1]*180/math.pi

print('I_polar = (%.2f<%.3frad)'%I_pol)
print('I_polar = (%.2f<%.2f°)'%(r,phi_deg))

%reset -s -f

Transformasi ke domain waktu

$$ i(t) = 5 \cos (\omega t + 126,87^\circ) \, \mathrm{A} $$

$b)$ karena $j = 1 \angle 90^\circ$,

$$ \vec{V} = 8j \angle -20^\circ = (1 \angle 90^\circ)(8 \angle -20^\circ) $$

$$ = 8 \angle (90^\circ - 20^\circ) = 8 \angle 70^\circ \, \mathrm{V} $$

Transformasi ke domain waktu menghasilkan

$$ v(t) = 8 \cos (\omega t + 70^\circ) \, \mathrm{V} $$

## Latihan
Tentukan sinusoida yang direpresentasikan oleh fasor berikut:

$\begin{array}{ll}
a) & \vec{V} = -10 \angle 30^\circ \, \mathrm{V} \\
b) & \vec{I} = j(5 - j12) \, \mathrm{A}
\end{array}
$

### Solusi

$a)$
$$ \vec{V} = -10 \angle 30^\circ = 10 \angle (30^\circ + 180^\circ) $$

$$ = 10 \angle 210^\circ \, \mathrm{V} $$ 

Transformasi ke domain waktu menghasilkan

$$ v(t) = 10 \cos (\omega t + 210^\circ) \, \mathrm{V} $$

$b)$
$$ \vec{I} = j(5 - j12) \, \mathrm{A} = 12 + 5j \, \mathrm{A} $$

import math
import cmath

I = complex(12,5)
I_pol = cmath.polar(I)

r = I_pol[0]
phi = I_pol[1]

print('I_polar = (%.2f<%.3frad)'%(r,phi))
print('I_polar = (%.2f<%.2f°)'%(r,phi*180/math.pi))

$$ I(t) = 13 \cos(\omega t + 22,62^\circ) \, \mathrm{A} $$

%reset -s -f

## Contoh
Diberikan
$$\begin{array}{l}
i_1(t) = 4 \cos (\omega t + 30^\circ) \, \mathrm{A} \\
i_2(t) = 5 \sin (\omega t - 20^\circ) \, \mathrm{A}
\end{array}$$
tentukan jumlahnya.

### Solusi
Disini kegunaan penting fasor: untuk menjumlahkan sinusoid dengan frekuensi yang sama.
Arus $i_1(t)$ adalah dalam bentuk standar.
Bentuk fasornya adalah

$$ \vec{I}_1 = 4 \angle 30^\circ $$

Kita perlu mengekspresikan $i_2(t)$ dalam bentuk cosinus.
Aturan untuk mengubah sinus ke cosinus adalah dengan mengurangi $90^\circ$.
Dengan demikian,

$$ i_2 = 5 \cos (\omega t 20^\circ - 90^\circ) = 5 \cos (\omega t - 110^\circ) $$

dan bentuk fasornya adalah

$$ \vec{I}_2 = 5 \angle -110^\circ $$

Jika kita anggap $i = i_1 + i_2$, maka

$$ \vec{I} = \vec{I}_1 + \vec{I}_2 = 4 \angle 30^\circ + 5 \angle -110^\circ $$

import math
import cmath

r1 = 4 ; phi1 = 30*(math.pi/180)
r2 = 5 ; phi2 = -110*(math.pi/180)

I1 = cmath.rect(r1,phi1)
I2 = cmath.rect(r2,phi2)

print('I1 = {:.3f}'.format(I1))
print('I2 = {:.3f}'.format(I2))

I = I1 + I2

print('I = {:.3f}'.format(I))

I_polar = cmath.polar(I)

print('I_polar = (%.3f<%.3frad)'%I_polar)

r = I_polar[0]
phi = I_polar[1]*180/math.pi
print('I_polar = (%.3f<%.3f°)'%(r,phi))

Transformasi ke domain waktu, kita peroleh

$$ i(t) = 3,218 \cos (\omega t - 56,976^\circ) \, \mathrm{A} $$

%reset -s -f

## Latihan
Jika
$$\begin{array}{l}
v_1 = -10 \sin (\omega t + 30^\circ) \, \mathrm{V} \\
v_2 = 20 \cos(\omega t - 45^\circ) \, \mathrm{V}
\end{array}$$
tentukan $v = v_1 + v_2$.

### Solusi

import math, cmath

$$ v_1 = -10 \sin (\omega t + 30^\circ) \, \mathrm{V} = 10 \cos (\omega t + 30^\circ + 90^\circ) \, \mathrm{V}$$

$$ v_1 = 10 \cos (\omega t + 120^\circ) $$

Kemudian:
$$\begin{array}{l}
\vec{V}_1 = 10 \angle 120^\circ \\
\vec{V}_2 = 20 \angle -45^\circ
\end{array}$$

r1 = 10 ; phi1 = 120*(math.pi/180)
r2 = 20 ; phi2 = -45*(math.pi/180)

V1 = cmath.rect(r1,phi1)
V2 = cmath.rect(r2,phi2)

print('V1 = {:.3f}'.format(V1))
print('V2 = {:.3f}'.format(V2))

# Penjumlahan
V = V1 + V2

print('V = {:.3f}'.format(V))

V_polar = cmath.polar(V)

print('V_polar = (%.3f<%.3frad)'%V_polar)

r = V_polar[0] ; phi = V_polar[1]*180/math.pi
print('V_polar = (%.2f<%.2f°)'%(r,phi))

$$ \vec{V} = 10,66 (\omega t - 30,95^\circ) \, \mathrm{V} $$

%reset -s -f

## Contoh
Dengan menggunakan pendekatan fasor, tentukan arus $i(t)$ suatu rangkaian yang dideskripsikan oleh persamaan integral-diferensial

$$ 4i + 8 \int i \, dt - 3 \frac{di}{dt} = 50 \cos (2t + 75^\circ) $$

### Solusi
Kita transformasikan tiap istilah dari domain waktu ke domain fasor.
Dengan memperhatikan persamaan

$$\begin{array}{ccc}
\displaystyle \frac{dv}{dt} & \Leftrightarrow & j \omega \, \mathrm{V} \\
\text{(Domain waktu)} & & \text{(Domain fasor)}
\end{array}$$

Demikian pula, integral $v(t)$ ditransformasikan ke domain fasor sebagai $\mathrm{V}/j \omega$.

$$\begin{array}{ccc}
\displaystyle \int v \, dt & \Leftrightarrow & \displaystyle \frac{\mathrm{V}}{j \omega} \\
\text{(Domain waktu)} & & \text{(Domain fasor)}
\end{array}$$

diperoleh bentuk fasor dari persamaan tersebut di atas

$$ 4 I + \frac{8I}{j \omega} - 3j \omega I = 50 \angle 75^\circ $$

Namun $\omega = 2$, maka

$$ I (4 - 4j -6j) = 50 \angle 75^\circ $$

$$ I = \frac{50 \angle 75^\circ}{4 - 10j} $$

import math , cmath

z2 = cmath.polar(4-10j)
r2 = z2[0] ; phi2 = z2[1]*180/math.pi
print('z2 = (%.2f<%.2frad)'%z2)
print('z2 = (%.2f<%.2f°)'%(r2,phi2))

r1 = 50 ; phi1 = 75
r = r1/r2 ; phi = phi1 - phi2

print('I = (%.3f<%.2f°)A'%(r,phi))

Konversi ke domain waktu,

$$ i(t) = 4,642 \cos (2t + 143,2^\circ) \, \mathrm{A} $$

%reset -s -f

### Latihan
Tentukan tegangan $v(t)$ pada suatu rangkaian yang dideskripsikan oleh persamaan integral-diferensial

$$ 2 \frac{dv}{dt} + 5v + 10 \int v \, dt = 20 \cos (5t - 30^\circ) $$

menggunakan pendekatan fasor.

$$ 2 j \omega V + 5V + 10 \frac{V}{j \omega} = 20 \angle -30^\circ $$

Letakkan $\omega = 5$, maka

$$ V (10j + 5 - 2j) = 20 \angle -30^\circ $$

$$ V = \frac{20 \angle -30^\circ}{5 + 8j} $$

import math, cmath

z2 = cmath.polar(5 + 8j)
r1 = 20 ; phi1 = -30
r2 = z2[0] ; phi2 = z2[1]*(180/math.pi)
r = r1/r2 ; phi = phi1 - phi2

print('z2 = (%.2f<%.2f°)'%(r2,phi2))
print('V = (%.2f<%.1f°)'%(r,phi))

$$ V = \frac{20 \angle -30^\circ}{9,43 \angle 57,99^\circ} = 2,12 \angle -88^\circ $$

Kemudian:

$$ v(t) = 2,12 \cos (5t - 88^\circ) \, \mathrm{V} $$