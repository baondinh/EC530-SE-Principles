# Assignment 1
- User of module are other developers
- Mission of module: If user gives input of two arrays of geo location, match each point in the first array to the closest one in the second array
- To find the distance between two GPS locations, use Haversine Formula for precise straight-line distance that accounts for Earth's curvature

LaTeX generated from ChatGPT:
Prompt: "Give me the LaTeX snippet for the Haversine Formula to calculate GPS coordinate distance. I am including this formula in a README.md file"

Haversine "a" term computes the central angle between points on a sphere using spherical trigonometry. 
$$
a = \sin^2\!\left(\frac{\Delta \phi}{2}\right)
+ \cos(\phi_1)\cos(\phi_2)
\sin^2\!\left(\frac{\Delta \lambda}{2}\right)
$$

Distance formula converts central angle into arc length along the Earth's surface.
$$
d = 2R \cdot \operatorname{atan2}\!\left(\sqrt{a}, \sqrt{1-a}\right)
$$

$$
\Delta \phi = \phi_2 - \phi_1,\quad
\Delta \lambda = \lambda_2 - \lambda_1
$$

$$
R = 6371\ \text{km} \quad \text{(or } 3959\ \text{miles)}
$$

Quick Euclidean approximations assume 111.19 km for one degree of latitude. These approximations are accurate for small distances under 20 km



Also follow GitHub Docs "Hello World" module to setup intial module
https://docs.github.com/en/get-started/start-your-journey/hello-world